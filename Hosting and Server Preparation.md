# General Information

### Hosting
Finding a good hosting solution for AI can be challenging. High-end platforms like **Google Cloud** offer extensive features but are costly. On the other hand, **Runpod** is budget-friendly but with less OS control. I opted for **TensorDock** for its balance of OS control and affordability.

### Operating System
We chose **Ubuntu 22.04 with PyTorch** due to its easy setup and compatibility with TensorDock.

---

## Preparation

1. **Create an Account on TensorDock** and set up your Organization.
2. Deposit at least $5 for server costs.
3. **Generate an SSH Key** for secure server access:
   ```bash
   ssh-keygen -f ~/.ssh/tensordiffusion -t rsa -b 4096
For Windows, save it under C:\Users\<Your-Name>\.ssh. Remember to use backslashes (\) for Windows paths.

4.Create a New Cloud GPU:

- Choose a GPU model based on your budget (e.g., A4000 for image generation).
- Recommended: 32GB RAM, 8 CPU vCores, and 150GB storage for performance.

5. Set Up SSH Key:

- Copy the public key (.pub) using cat on Linux or a text editor on Windows.
- Paste it in the provided field on TensorDock.
Configure Ports:

Set server ports: 7860 (WebUI), 8501 (Streamlit), and another for backup.
Deploy Server with Ubuntu 22.04 LTS.

Server Preparation
Create an SSH Connection File:

For Windows:
bat
Copy code
ssh -i C:\Users\<username>\.ssh\tensordiffusion -p <ssh-port> user@<server-ip>
Save it as a .bat file for quick access.
Connect to the Server and run the following commands:

bash
Copy code
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv python3-tk git wget google-perftools zip unzip
Set Up Firewall:

bash
Copy code
sudo ufw allow ssh
sudo ufw allow <port>
sudo ufw enable
Install System Monitoring Tools:

Btop:

bash
Copy code
git clone https://github.com/aristocratos/btop.git
cd btop
make
sudo make install
Dust:

bash
Copy code
sudo snap install dust
Use FileZilla for easier file management via SFTP. Configure as:

Protocol: SFTP
Host: Your server's IP
Port: SSH port
Logon Type: Key File (point to your private key)
User: user
