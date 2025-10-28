# 🐍 Python Essentials

This README provides essential Python setup and dependency management instructions.

## 📚 Table of Contents

1. [Python Virtual Environment Setup](#1-python-virtual-environment-setup)
2. [Installing Packages and Managing a Wheelhouse](#2-installing-packages-and-managing-a-wheelhouse)


## 1. Python Virtual Environment Setup

This guide provides step-by-step instructions to create and activate a Python virtual environment using `virtualenv`.

### 🔧 Prerequisites

* **Python 3** must be installed on your system.
  → [Download Python](https://www.python.org/downloads/)
* **pip** (Python package manager) should be available.
  It usually comes with Python, but if not, install it manually.

---

### ⚙️ Steps to Create a Virtual Environment

#### 1. Install `virtualenv`

```bash
pip install virtualenv
```

#### 2. Create a Virtual Environment

```bash
virtualenv -p python3 env
```

This command creates a virtual environment named `env` using Python 3.

#### 3. Activate the Virtual Environment

* **On Linux/MacOS**:

  ```bash
  source env/bin/activate
  ```
* **On Windows**:

  ```bash
  env\Scripts\activate
  ```

When activated, your terminal prompt will typically show the environment name, for example:

```
(env) $
```

### 🚪 Deactivating the Virtual Environment

To exit or deactivate the environment:

```bash
deactivate
```

### 💡 Tip

Always activate your virtual environment **before installing packages** to keep dependencies isolated from your global Python installation.

## 2. Installing Packages and Managing a Wheelhouse

### 🐍 **Installing Packages**

After activating your virtual environment, install packages using `pip`:

```bash
pip install package_name
```

### 📜 **Freezing Installed Packages**

Generate a `requirements.txt` file that lists all installed packages and their versions:

```bash
pip freeze > requirements.txt
```

### 📦 **Installing from `requirements.txt`**

To reinstall all dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 💾 **Downloading Wheelhouse Files**

A *wheelhouse* is a local directory that stores pre-downloaded `.whl` files (Python wheels).
This allows you to reuse the same packages across multiple builds — useful for speeding up Docker image builds or offline installations.

Download all required packages into a `wheelhouse` folder:

```bash
pip download -r requirements.txt -d wheelhouse/
```

### 🚀 **Installing from Wheelhouse**

Install packages directly from the local wheelhouse (without accessing PyPI):

```bash
pip install --no-index --find-links=wheelhouse -r requirements.txt
```

### 🧠 **Tip**

Using a wheelhouse ensures **faster builds**, **repeatable installations**, and **offline compatibility** — especially useful for **Docker** or **CI/CD environments**.


## Author

 - Abhishek Rajput
 - Palak Rajput
