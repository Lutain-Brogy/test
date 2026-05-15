import streamlit as st

st.title("Firestore Rule Writer")

choice = st.selectbox(
    "What rule would you like to write?",
    ["Allow read", "Allow Edit", "Authentication Rule"]
)

user_input = st.text_input("Describe your rule (optional)")


import streamlit as st

choice = st.selectbox(
    "What rule would you like?",
    ["Allow read", "Allow Edit", "Authentication Rule"]
)

if choice == "Allow read":
    edit_choice = st.selectbox(
        "On what terms?",
        [
            "Allow public read",
            "After authentication",
            "Only owner reads",
            "Specific role reads",
            "Conditional data based"
        ]
    )

    if edit_choice == "Allow public read":
        st.write("Thanks")

elif choice == "Allow Edit":
    st.write("Generate edit rule")

elif choice == "Authentication Rule":
    st.write("Generate auth rule")
