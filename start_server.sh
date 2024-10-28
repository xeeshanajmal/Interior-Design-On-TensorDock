#!/bin/bash

echo "Starting Automatic1111 WebUI..."
cd ~/stable-diffusion-webui
./webui.sh --listen --port 7860 &  # The "&" allows this command to run in the background

sleep 10  # Wait for 10 seconds to ensure the WebUI starts

echo "Starting Streamlit app..."
cd ~/streamlit-app
streamlit run app.py --server.port 8501 &  # The "&" allows this command to run in the background

echo "Both WebUI and Streamlit app are now running."
