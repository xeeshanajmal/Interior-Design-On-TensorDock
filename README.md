# Interior Design on TensorDock with AI

This project enables users to generate interior design images based on room types and styles using an AI-powered Stable Diffusion model deployed on a TensorDock server.

## Features
- Generate images based on room type (e.g., Bedroom, Office) and style (e.g., Modern, Minimalist).
- Custom prompt option available.
- Built with Streamlit for the user interface and TensorDock for server hosting.

## Table of Contents
- [Installation](#installation)
- [Cloud Deployment](#cloud-deployment)
- [Setup](#setup)
- [Usage](#usage)
- [Running the Application](#running-the-application)
- [Credits](#credits)


## General Information
### Hosting
1. I am using TensorDock to deploy but you can choose AWS, GCP or any other reliable and cost-effective platform.
2. I am customizing my server and with  following Hardware and software specs:

  Storage: 100 GB
  vCPUs: 8 AMD EPYC 7551P vCPUs
  RAM: 16 GB RAM
  GPU:1x RTX A4000 16 GB
  Operating System:  TensorML 20.04 PyTorch







## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/xeeshanajmal/Interior-Design-On-TensorDock.git
    cd Interior-Design-On-TensorDock
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Cloud Deployment

To deploy this application on a TensorDock server and make it accessible via the internet, follow these steps:

### 1. System Update and Installation
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

### 2. Clone the Repository:
```bash
git clone https://github.com/xeeshanajmal/Interior-Design-On-TensorDock.git
cd Interior-Design-On-TensorDock
```

### 3. Create a Virtual Environment:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 4. Install Required Dependencies:
```bash
pip install streamlit Pillow matplotlib numpy requests
```

### 5. Running the Application:
Start the Streamlit app on port 8501:

```bash
cd streamlit-app
streamlit run app.py --server.port 8501
```


## Setup

### TensorDock Setup

1. Create an instance on TensorDock with the necessary GPU and storage configurations.
2. Connect to your instance using SSH and perform the above installation steps.

### WebUI and Streamlit Ports
- WebUI: Accessible on port 7860
- Streamlit: Accessible on port 8501

## Usage
Once everything is set up, you can start the app and begin generating AI-generated interior designs.

- Room Types: Bedroom, Office, Conference Room, etc.
- Styles: Modern, Minimalist, Scandinavian, etc.
- Custom Prompts: Option to override the dropdown-generated prompt.

### Example Prompts
- Generated Prompt: "A Modern Bedroom"
- Custom Prompt: "A futuristic bedroom with ambient lighting"

## Running the Application

### 1.Run the Streamlit App:

```bash
cd streamlit-app
streamlit run app.py --server.port 8501
```

### 2.Run the WebUI:

```bash
cd stable-diffusion-webui
./webui.sh --listen --port 7860
```

### 3.Access the Web Interface:

1. Open your browser and go to http://<your-server-ip>:8501 for the Streamlit app or http://<your-server-ip>:7860 for the WebUI.
2. Select the room type and style, or enter a custom prompt.
3. Click Generate Image to generate an image using the Stable Diffusion model.


## Sample Output


## Credits
- Stable Diffusion Model: StabilityAI's Stable Diffusion
- UI Framework: Streamlit
- Server Hosting: TensorDock
