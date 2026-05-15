import streamlit as st

st.title("Firestore Rule Writer")

choice = st.selectbox(
    "What rule would you like to write?",
    ["Allow read", "Deny read" ,
     #"Allow Edit", 
     #"Authentication Rule"
    ]
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

    user_id = st.text_input("Please paste the user ID allowed to read")

    if user_id:
        st.code(f"""
rules_version = '2';
service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /your_collection/{{documentId}} {{
      allow read: if request.auth != null
                  && request.auth.uid == "{user_id}";
    }}

  }}
}}
""", language="javascript")
        
elif edit_choice == "Conditional data based read":
    st.write("Copy rule below")

    condition = st.text_input("Please paste the condition for reading (e.g. visibility == public)")

    if condition:
        st.code(f"""
rules_version = '2';
service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /your_collection/{{documentId}} {{
      allow read: if resource.data.{condition};
    }}

  }}
}}
""", language="javascript")

if edit_choice == "Selected documents read":
    st.write("Copy rule below")

    doc_list = st.text_input("Which documents would you like to choose to be read? (comma separated)")

    if doc_list:
        st.code(f"""
rules_version = '2';
service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /your_collection/{{documentId}} {{
      allow read: if documentId in {doc_list.split(",")};
    }}

  }}
}}
""", language="javascript")

elif choice == "Deny read":
    st.write("Copy rule below, but remember nobody (including you) will not be able to read it")

    st.code("""
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    match /your_collection/{documentId} {
      allow read: if false;
    }

  }
}
""", language="javascript")
# elif choice == "Allow Edit":
   # st.write("Generate edit rule")

# elif choice == "Authentication Rule":
#    st.write("Generate auth rule")
