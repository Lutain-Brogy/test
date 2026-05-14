import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("My Firestore App")

if st.button("Get Data"):
    docs = db.collection("users").stream()
    for d in docs:
        st.write(d.to_dict())
