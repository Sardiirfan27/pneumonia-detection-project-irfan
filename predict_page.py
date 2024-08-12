import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from tensorflow.keras.preprocessing import image as img

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="quantized_model4.tflite")
interpreter.allocate_tensors()

# Function to preprocess image without load_img
def load_and_preprocess_image(image):
    #img_inf = img.load_img(image, target_size=(224, 224))  # Sesuaikan target_size dengan ukuran yang digunakan saat pelatihan
    try:
        # # Memeriksa mode gambar dan konversi jika grayscale
        # if image.mode == "L":
        #     image = image.convert("RGB")

        # Resize gambar menjadi ukuran yang diinginkan (sesuaikan dengan ukuran yang digunakan saat pelatihan model)
        image = image.resize((224, 224))
        img_array = np.asarray(image) # Konversi gambar menjadi array numpy
        img_array = img_array / 255.0 # Normalisasi nilai piksel menjadi [0, 1]

        # Menambahkan dimensi batch (untuk memenuhi kebutuhan input model)
        img_array = np.expand_dims(img_array, axis=0)

        return img_array

    except Exception as e:
        print("Error:", str(e))
        return None

# Function to make prediction
def binary_predict_image(interpreter, image, threshold=0.5):
    # Load and preprocess image
    input_data = load_and_preprocess_image(image)

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

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
    st.title("Deteksi Pneumonia dengan CNN")
    row1 = st.columns(2)
    with row1[0]:
        option = st.radio("Pilih opsi:", ("Upload Gambar", "Masukkan URL Gambar"))
        if option == "Upload Gambar":
            uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])
            
            if uploaded_file is not None:
                #membaca gambar
                image = Image.open(uploaded_file)
            
                st.image(image, caption="Gambar yang diunggah", width=250)
                if st.button("Prediksi"):
                    predicted_class, confidence_category = binary_predict_image(interpreter, image)
                    st.success(f"Prediction Result: {predicted_class} (Confidence: {confidence_category})", icon='✅')
                    
                    if predicted_class == 'Pneumonia':
                        with row1[1]:
                            recommendation()
    
            

        elif option == "Masukkan URL Gambar":
            url = st.text_input("Masukkan URL gambar:")
            if url:
                try:
                    image = Image.open(BytesIO(requests.get(url).content))
                    st.image(image, caption="Gambar dari URL", width=250)
                    if st.button("Prediksi"):
                        predicted_class, confidence_category = binary_predict_image(interpreter, image)
                        st.success(f"Prediction Result: {predicted_class} (Confidence: {confidence_category})", icon='✅')
                        if predicted_class == 'Pneumonia':
                            with row1[1]:
                                recommendation()
                except Exception as e:
                    st.write("Error:", e)
        
        #berikan padding untuk memberikan ruang
        vert_space = '<div style="padding: 180px 5px;"></div>'
        st.markdown(vert_space, unsafe_allow_html=True)

def recommendation():   
    paragraph = """
        <h1> Anda Terindikasi Pneumonia </h1>
        <p> Berikut adalah daftar gejala pneumonia yang paling umum:
        </p>
        <ul>
            <li>Batuk.</li>
            <li>Sesak napas.</li>
            <li>Sakit dada.</li>
            <li>Demam.</li>
            <li>Panas dingin.</li>
            <li>Kelelahan dan nyeri otot.</li>
        </ul>
        
        <h1> Rekomendasi </h1>
        <ul>
            <li>Istirahat yang cukup</li>
            <li>Minum Banyak Cairan: Contoh cairan yang dapat Anda minum adalah air putih hangat, teh herbal, kaldu ayam, dan jus buah tanpa gula tambahan.</li>
            <li>Konsumsi Makanan Sehat: Pilihlah makanan seperti bayam dan brokoli, serta buah-buahan segar seperti jeruk, stroberi, dan kiwi yang mengandung banyak antioksidan.</li>
            <li>Untuk mengatasi sesak napas, Anda dapat menghirup uap air hangat.</li>
        </ul>

    """
    st.markdown(paragraph, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
