import streamlit as st
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def main():
    st.set_page_config("Pelacak Lokasi")

    st.markdown("<h1 style='text-align: center;'>Aplikasi Pelacak Lokasi</h1>", unsafe_allow_html=True)

    nomor = st.text_input("Masukan nomor hp:")


    if st.button("Lacak"):
        nomor = phonenumbers.parse(nomor)
        st.success(f"Lokasi = {timezone.time_zones_for_number(nomor)}")
        st.success(f"Kartu = {carrier.name_for_number(nomor, "en")}")
        st.success(f"Negara = {geocoder.description_for_number(nomor, "en")}")
        st.success(f"Valid mobile number = {phonenumbers.is_valid_number(nomor)}")
        st.success(f"Checking possibility of number = {phonenumbers.is_possible_number(nomor)}")

if __name__ == "__main__": main()
