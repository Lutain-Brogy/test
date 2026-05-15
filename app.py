import streamlit as st

st.title("Firestore Rule Writer")

choice = st.selectbox(
    "What rule would you like to write?",
    ["Allow Edit", "Allow Write", "Authentication Rule"]
)

user_input = st.text_input("Describe your rule (optional)")

if choice == "Allow Edit":
    st.write("Generate update rule")
    st.write("User input:", user_input)

elif choice == "Allow Write":
    st.write("Generate write rule")
    st.write("User input:", user_input)

elif choice == "Authentication Rule":
    st.write("Generate auth rule")
    st.write("User input:")
