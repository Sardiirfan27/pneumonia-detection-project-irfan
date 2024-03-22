# home.py
import streamlit as st
import streamlit.components.v1 as components
# from PIL import Image   

def home_page():
    centered_title = """
    <h1 style="text-align: center;">Deteksi Pneumonia Menggunakan CNN</h1>

    <div style="text-align: center;">
        <img src="https://www.gavi.org/sites/default/files/vaccineswork/2022/Thumbnail/Pneumonia-picture-1_h2.jpg" alt="Pneumonia Image" width="400"/>
    </div>
    
   <p style="text-align: center;"><strong>Source:</strong> Global Burden of Disease, 2019. <a href="https://www.healthdata.org/gbd/2019">https://www.healthdata.org/gbd/2019</a></p>

    """
    st.markdown(centered_title, unsafe_allow_html=True)

   

    paragraph = """
    <p>Pneumonia komuniti atau community-acquired pneumonia (CAP) merupakan pneumonia yang didapat di masyarakat, di mana infeksi terjadi di luar fasilitas pelayanan kesehatan. 
    Pneumonia sendiri didefinisikan sebagai inflamasi parenkim paru yang disebabkan oleh infeksi mikroorganisme patogen, seperti bakteri, virus, jamur, dan parasit; serta pajanan bahan kimia ke parenkim paru.<a id='#ref1' href=#ref style ="color :#003f88;">[1]</a>
    </p>
    <p>
    Secara global, pneumonia adalah penyebab utama kematian pada anak di bawah usia lima tahun, dan penyebab kematian keempat di segala usia. Satu orang meninggal karena pneumonia setiap 13 detik dan mereka yang berisiko terbesar adalah anak-anak (<5 tahun) dan orang tua (70+ tahun). 
    Pada tahun 2019, 672.000 dari 2,5 juta kematian pneumonia terjadi di antara anak balita, dengan 70% dari kematian balita (470.400) terjadi di antara anak di bawah usia 12 bulan.<a id='#ref1' href='https://www.gavi.org/vaccineswork/every-death-counts-pneumonia-five-charts' style ="color :#003f88;">[2]</a>
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
