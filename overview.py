import streamlit as st
import pandas as pd

def show_overview():
    st.subheader("About")

    st.write("""
    FSVA merupakan peta tematik yang menggambarkan visualisasi geografis dari hasil analisa data indikator kerentanan terhadap kerawanan pangan. 
    FSVA disusun menggunakan sembilan indikator yang mewakili tiga aspek ketahanan pangan, yaitu ketersediaan, keterjangkauan dan pemanfaatan pangan.

    FSVA adalah sistem kewaspadaan yang memberikan rekomendasi kepada pembuat keputusan dalam 
    penyusunan kebijakan dan program intervensi baik di tingkat pusat dan daerah dengan melihat 
    indikator utama yang menjadi pemicu terjadinya kerentanan terhadap kerawanan pangan.  
    """)

    st.image("petafsva.png", caption="Peta Ketahanan & Kerentanan Pangan Indonesia", use_column_width=True)

    st.subheader("Why is it Importants?")

    st.write('''
    Ketersediaan pangan yang lebih kecil dibandingkan kebutuhannya dapat menciptakan ketidak-stabilan ekonomi. 
    Berbagai gejolak sosial dan politik dapat juga terjadi jika ketahanan pangan terganggu. 
    Kondisi pangan yang kritis ini bahkan dapat membahayakan stabilitas ekonomi dan stabilitas Nasional.
    ''')

    st.subheader("Problems")

    st.write('''
    Banyak daerah di Indonesia yang masih belum memiliki Indeks Ketahanan Pangan (IKP) atau Indeks Komposit 
    yang menjadi penentu pemerintah dalam membuat skala prioritas perhatian dalam upaya pemerintah menciptakan Indonesia Tahan Pangan.
    ''')

    st.subheader("Goals")

    st.write("""
    - Memberikan kemudahan kepada daerah-daerah yang tertinggal dalam penyediaan data

    - Menghilangkan kerumitan perhitungan

    - Waktu yang lebih cepat untuk memperoleh status ketahanan pangan

    - Proses mendapatkan saran yang tepat dan cepat menjadi lebih efisien

    Dengan aplikasi ini kami berharap mendukung pemerintah dalam menciptakan masyarakat 
    yang tahan pangan dimana hal tersebut juga memberi dampak positif bagi kemajuan dan keberlanjutan masyarakat.

    """)

    st.subheader("Workflow Modelling")
    st.image("2.png", caption="Workflow Modelling", use_column_width=True)

    st.write("#### **Pengumpulan Dataset**")
    st.write("""
    Dataset yang digunakan berasal dari web Badan Pangan Nasional (BPN) : 
    https://fsva.badanpangan.go.id
    """)

    df = pd.read_csv('FSVA 2022-1.csv')
    st.write(df)

    st.image("cutoff.png", caption="Cut Off Point Indeks Ketahanan Pangan", use_column_width=True)

    st.write("**Atribut feature pada dataset :**")
    st.write("""
    - NCPR\t\t: Rasio Konsumsi Normatif terhadap Ketersediaan Bersih per Kapita

    - Kemiskinan (%)\t: Persentase Penduduk Miskin

    - Pengeluaran Pangan (%)\t: Persentase Rumah Tangga dengan Pengeluaran Pangan > 65% Total Konsumsi

    - Tanpa Listrik (%)\t: Persentase Rumah Tangga tanpa Listrik

    - Tanpa Air Bersih (%)\t: Persentase Rumah Tangga tanpa Air Bersih

    - Lama Sekolah Perempuan (tahun)\t: Rata-rata Lama Sekolah (tahun) Perempuan berusia 15 tahun keatas

    - Rasio Tenaga Kesehatan\t: Rasio Penduduk per Tenaga Kesehatan terhadap Tingkat Kepadatan Penduduk

    - Angka Harapan Hidup (tahun)\t: Angka Harapan Hidup (tahun)

    - Stunting (%)\t\t: Persentase Balita dengan Tinggi Badan dibawah Standar (Stunting)
    """)

    st.write("**Atribut target pada dataset :**")
    st.write('''
    Komposit : Indikator yang menunjukkan tingkat ketahanan suatu wilayah terhadap masalah pangan.

    - Komposit 1 mengartikan bahwa "Sangat Rentan"

    - Komposit 2 mengartikan bahwa "Rentan"

    - Komposit 3 mengartikan bahwa "Agak Rentan"

    - Komposit 4 mengartikan bahwa "Agak Tahan"

    - Komposit 5 mengartikan bahwa "Tahan"

    - Komposit 6 mengartikan bahwa "Sangat Tahan"
    ''')

    st.write("#### **Preprocessing**")
    st.write("""
    Preprocessing yang dilakukan hanya menghapus kolom yang tidak digunakan pada saat modelling.

    Berikut ini adalah kolom-kolom yang dihapus : 

    - Wilayah

    - IKP

    - IKP Ranking
    """)

