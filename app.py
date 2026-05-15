import streamlit as st

st.title("Firestore Rule Writer")

choice = st.selectbox(
    "What rule would you like to write?",
    ["Allow read", "Allow Edit", "Authentication Rule"]
)


if choice == "Allow read":
    edit_choice = st.selectbox(
        "On what terms?",
        [
            "Allow public read",
            "Only owner reads",
            "Specific role reads",
            "Conditional data based read",
            "Selected documents read"          
        ]
    )

if edit_choice == "Allow public read":
    st.write("Copy rule below")
    st.code("""
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /your_collection/{documentId} {
      allow read: if true;
    }
  }
}
""", language="javascript")


elif edit_choice == "Only owner reads":
    st.write("Copy rule below")
    st.code("""
match /your_collection/{userId} {
  allow read: if request.auth != null
              && request.auth.uid == userId;
}
""", language="javascript")
    
elif edit_choice == "Specific role reads":
    st.write("Copy rule below")

elif edit_choice == "Conditional data based read":
    st.write("Copy rule below")

    doc_name = st.text_input("Please paste the name of the selected document(s)")

    if doc_name:
        st.code(f"""
rules_version = '2';
service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /your_collection/{{documentId}} {{
      allow read: if documentId == "{doc_name}";
    }}

  }}
}}
""", language="javascript")


elif choice == "Allow Edit":
    st.write("Generate edit rule")

elif choice == "Authentication Rule":
    st.write("Generate auth rule")
