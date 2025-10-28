# Python 3.11/3.12 Setup on Instance (Ubuntu)

This guide provides step-by-step instructions for updating and installing Python 3.11 and 3.12 on an Ubuntu-based instance.

## Prerequisites
- An instance running Ubuntu
- User with sudo privileges

## Steps

### 1. Update System Packages
Run the following command to update the package lists and upgrade installed packages:
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Required Dependencies
Install necessary system dependencies:
```bash
sudo apt install -y software-properties-common
```

### 3. Add the Deadsnakes PPA Repository
```bash
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
```

### 4. Install Python 3.11, 3.12, and Required Modules
```bash
sudo apt install -y python3.11 python3.11-venv python3.11-dev
sudo apt install -y python3.12 python3.12-venv python3.12-dev
```

### 5. Change Python Environment
Set up alternatives for Python versions:
```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
sudo update-alternatives --config python3
```
Select the desired version from the interactive prompt.

### 6. Upgrade Pip
Ensure pip is installed and upgraded:
```bash
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip
```

### 7. Reboot the Instance
Reboot to apply changes:
```bash
sudo reboot
```

### 8. Verify Installation
Check installed versions of Python and pip:
```bash
pip3 --version
python3 --version
```

## Notes
- The `update-alternatives` command allows switching between Python versions easily.
- Ensure all dependencies are installed before running Python-based applications.

## Author 
Abhishek Rajput
