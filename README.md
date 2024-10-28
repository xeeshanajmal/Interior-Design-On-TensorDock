# Interior Design On TensorDock

This repository contains the codebase for running an interior design application using **Stable Diffusion** and **Streamlit**. The project leverages **TENSORDOCK** servers to run the Automatic1111 WebUI and provides a custom Streamlit app interface to generate new room designs based on user-uploaded images.

## Project Structure

```bash
Interior-Design-On-TensorDock/

├── stable-diffusion-webui/ # Contains the Automatic1111 WebUI code
├── streamlit-app/ # Contains the Streamlit app code
│ └── app.py # Main Streamlit app script
└── start_server.sh # Shell script to start both WebUI and Streamlit
```

## Setup Instructions

### Prerequisites
- Ubuntu Server with GPU (Recommended: TensorDock)
- Python 3.x

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/xeeshanajmal/Interior-Design-On-TensorDock.git
   cd Interior-Design-On-TensorDock
   ```

2. **Install Dependencies**:

```bash

cd stable-diffusion-webui
bash install.sh # Follow the WebUI installation steps
```

3. **Start Server**:

```bash
./start_server.sh
```

## Streamlit App Features
- Upload an image or use camera input to capture a room.
- Select room type and style for the generated design.
- Generate an AI-designed image using Stable Diffusion.
