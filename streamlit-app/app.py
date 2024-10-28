import streamlit as st
import requests
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# WebUI Local Server URL
webui_url = "http://127.0.0.1:7860/sdapi/v1/img2img"

def query_webui(img, prompt):
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_str = base64.b64encode(img_buffer.getvalue()).decode()
    payload = {
        "init_images": [img_str],
        "prompt": prompt,
        "steps": 50,
        "width": 512,
        "height": 512,
        "cfg_scale": 7.5,
        "denoising_strength": 0.75,
    }
    response = requests.post(webui_url, json=payload)
    return response.json()

def display_image(img, prmpt):
    plt.figure(figsize=(12,12))
    plt.imshow(np.array(img))
    plt.axis('off')
    plt.title(prmpt)
    st.pyplot(plt)

st.title("Interior Design using AI")

# Dropdowns for Area/Room and Style
room = st.selectbox("Select Area/Room", ['Bedroom', 'Drawing Room', 'Basement', 'Sitting Room', 'Washroom', 'Conference Room', 'Office'], key="room_selectbox")
style = st.selectbox("Select Style", ['Modern', 'Minimalist', 'Scandinavian', 'Industrial', 'Mid-Century Modern', 'Art Deco', 'Craftsman', 'Rustic', 'Shabby Chic', 'Bohemian'], key="style_selectbox")

# Input for custom prompt or default prompt
use_custom_prompt = st.checkbox("Use custom prompt")
if use_custom_prompt:
    prompt = st.text_input("Enter your custom prompt", "", key="custom_prompt_input")
else:
    prompt = f"A {style} {room}"

# File Upload and Camera Input
uploaded_file = st.file_uploader("Upload an image of the room", type=["png", "jpg", "jpeg"])
img_file_buffer = st.camera_input("Or take a picture of the room")

# When the user clicks "Generate Image"
if (uploaded_file or img_file_buffer) and st.button("Generate Image", key="generate_image_button"):
    with st.spinner('Generating image...'):
        if uploaded_file:
            img = Image.open(uploaded_file).convert("RGB")
        elif img_file_buffer:
            img = Image.open(img_file_buffer).convert("RGB")

        # Query the WebUI server with the image and prompt
        response = query_webui(img, prompt)

        # Parse the response to get the generated image
        generated_image_data = response['images'][0]
        generated_image = Image.open(BytesIO(base64.b64decode(generated_image_data)))

        # Display the generated image
        st.write(f"Generated Image for: {prompt}")
        display_image(generated_image, prompt)
