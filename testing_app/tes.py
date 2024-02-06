import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing import image as img

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="quantized_model4.tflite")
interpreter.allocate_tensors()

input_shape=(224,224,3)  # Dimensi input gambar yang diharapkan oleh model

def load_and_preprocess_image(image_path):
    img_inf = img.load_img(image_path, target_size=(input_shape[0], input_shape[1]))  # Sesuaikan target_size dengan ukuran yang digunakan saat pelatihan
    img_array = img.img_to_array(img_inf)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalisasi nilai piksel menjadi [0, 1]
    return img_array

def binary_predict_image(interpreter, image, threshold=0.5):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Load and preprocess image
    input_data = load_and_preprocess_image(image)

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Perform inference
    interpreter.invoke()

    # Get output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Adjust confidence
    confidence = output_data[0][0]
    if 0.35 <= confidence <= 0.5 or 0.5 < confidence <= 0.65:
        confidence_category = 'Potentially Misclassified'
    elif 0.20 <= confidence < 0.35 or 0.65 < confidence <= 0.80:
        confidence_category = 'Fairly Confident'
    else:
        confidence_category = 'Very Confident'

    # Determine predicted class label based on threshold
    predicted_class_label = 'Pneumonia' if output_data[0][0] > threshold else 'Normal'

    return predicted_class_label, confidence_category

def main():
    # Streamlit app
    st.title("Pneumonia Detection with TensorFlow Lite Model")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Predict"):
            predicted_class, confidence_category = binary_predict_image(interpreter, uploaded_file)
            st.write("Prediction Result:")
            st.write(f"Class: {predicted_class}")
            st.write(f"Confidence: {confidence_category}")

if __name__ == "__main__":
    main()
