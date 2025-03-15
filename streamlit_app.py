import streamlit as st
from huggingface_hub import InferenceClient

# Streamlit page setup
st.set_page_config(page_title="Fic_Gemma3_27B", page_icon="🤗💬")
st.title("🤗💬 Fic_Gemma App")

st.markdown("""
Aplikasi obrolan AI ini menggunakan model Google Gemma-3-27B, sebuah model bahasa canggih yang dirancang untuk tugas percakapan yang kompleks.Aplikasi obrolan AI ieu ngagunakeun model Google Gemma-3-27B, model basa nu panganyarna dimaksudkeun pikeun tugas ngobrol nu kompleks.
""")

# Hugging Face API Key
API_KEY = st.secrets.get("HF_API_KEY") 
client = InferenceClient(api_key=API_KEY)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Apa Kabar Teman-teman! Ada yang bisa saya bantu? Sapa nuung ka kawan-kawan! Aya tipeu nu bisa diping pin sapadana?"}
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input("Ask your question:"):
    # Add user message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Prepare alternating conversation history
    # chat_messages = [
    #     {"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages
    # ]
    print("User Prompt:", prompt)
    # print("Chat Messages:", chat_messages)


    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                messages = [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

                completion = client.chat.completions.create(
                    model="google/gemma-3-27b-it", 
                    messages=messages, 
                    # messages=chat_messages, 
                    max_tokens=128000
                )

                response= completion.choices[0].message["content"]
                print(response)


            except Exception as e:
                response = f"An error occurred: {str(e)}"

            st.write(response)

    # Add assistant message to the session state
    st.session_state.messages.append({"role": "assistant", "content": response})
