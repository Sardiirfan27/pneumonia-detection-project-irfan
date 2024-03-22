# home.py
import streamlit as st
import streamlit.components.v1 as components
# from PIL import Image   

def home_page():
    centered_title = """
    <h1 style="text-align: center;">Deteksi Pneumonia Menggunakan CNN</h1>
    """
    st.markdown(centered_title, unsafe_allow_html=True)

   

    paragraph = """
    <p>Pneumonia komuniti atau community-acquired pneumonia (CAP) merupakan pneumonia yang didapat di masyarakat, di mana infeksi terjadi di luar fasilitas pelayanan kesehatan. 
    Pneumonia sendiri didefinisikan sebagai inflamasi parenkim paru yang disebabkan oleh infeksi mikroorganisme patogen, seperti bakteri, virus, jamur, dan parasit; serta pajanan bahan kimia ke parenkim paru.<a id='#ref1' href=#ref style ="color :#003f88;">[1]</a>
    </p>

    """
    st.markdown(paragraph, unsafe_allow_html=True)

    markdown_text = """
    Pentingnya deteksi dini dan diagnosis yang cepat dalam kasus pneumonia menjadi fokus utama dalam pengembangan proyek ini. 
    Penerapan teknologi kecerdasan buatan, khususnya dalam analisis citra medis, dapat membantu mengidentifikasi tanda-tanda pneumonia lebih efisien dan akurat. 
    
    Penggunaan Convolutional Neural Networks (CNN) memainkan peran kunci dalam proyek prediksi penyakit pneumonia berbasis citra medis. CNN dirancang khusus untuk mengekstraksi pola dari data spasial, seperti citra, dan telah terbukti sangat efektif dalam tugas-tugas untuk pemodelan prediktif. 
    Oleh sebab itu pada proyek ini saya akan mencoba membuat proyek Prediksi Pneumonia dengan pemodalan CNN serta melakukan beberapa uji coba arsitektur CNN dan penerapan transfer learning untuk mendapatkan hasil yang bagus.

    """
    st.markdown(markdown_text)




if __name__ == "__main__":
    home_page()
