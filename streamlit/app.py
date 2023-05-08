import streamlit as st
import redis
import torch
from aniemore.recognizers.text import TextRecognizer
from aniemore.models import HuggingFaceModel

# Connect to Redis
redis_host = st.secrets["REDIS_HOST"]
redis_port = st.secrets["REDIS_PORT"]
r = redis.Redis(host=redis_host, port=redis_port)

# Load the TextRecognizer model
model = HuggingFaceModel.Text.Bert_Tiny
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tr = TextRecognizer(model=model, device=device)

def recognize_text(text):
    label = tr.recognize(text, return_single_label=True)
    return label

# Define the Streamlit interface
def main():
    st.title("Emotion Recognition")
    
    # Retrieve the list of keys from Redis and reverse it to show the latest results first
    keys = r.keys()
    keys.reverse()
    
    # Create a new Streamlit tab to show the history
    if st.sidebar.button("History"):
        st.sidebar.markdown("# History")
        for key in keys:
            value = r.get(key)
            st.sidebar.markdown(f"- **Query:** {key.decode('utf-8')}")
            st.sidebar.markdown(f"  **Result:** {value.decode('utf-8')}")
    
    # Create the main interface
    text = st.text_input("Enter some text:")
    if st.button("Recognize"):
        label = recognize_text(text)
        st.write("The text is", label)
        r.set(text, label)

if __name__ == "__main__":
    main()