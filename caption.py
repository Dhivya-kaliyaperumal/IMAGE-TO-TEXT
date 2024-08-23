import requests
import streamlit as st 
import base64

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("Dark Blue Purple Gradient Abstract Backdrop M7-73 - 10'W_10'H(3_3m).jfif")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(file):
   data = file.read()
   response = requests.post(API_URL, headers=headers, data=data)
   return response.json()

#upload the file
uploaded_file = st.file_uploader("upload an image", type="jpg")

if uploaded_file is not None:
    if st.button("click"):
        output = query(uploaded_file)
        st.write(output)
	


