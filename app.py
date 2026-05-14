import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# --- Firebase init from Streamlit secrets ---
if not firebase_admin._apps:
    cred = credentials.Certificate(st.secrets["firebase"])
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- UI ---
st.title("My Firestore App")

if st.button("Get Data"):
    docs = db.collection("users").stream()
    for d in docs:
        st.write(d.to_dict())
        
