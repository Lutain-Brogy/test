import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

# --- Firebase init from Streamlit secrets ---
if not firebase_admin._apps:
    firebase_config = json.loads(st.secrets["firebase"])
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- UI ---
st.title("My Firestore App")

if st.button("Get Data"):
    docs = db.collection("users").stream()
    for d in docs:
        st.write(d.to_dict())
        
