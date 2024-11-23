---

# QR Code Generator  

A simple Python project to generate QR codes from user-provided URLs. Customize your QR code's colors and save it with a name of your choice.  

## Features  
- Accepts a URL as input to generate a QR code.  
- Allows saving the QR code image with a custom file name.  
- Customizable QR code colors using the `qrcode` and `Pillow` libraries.  

---

## Requirements  
- Python 3.7 or later  

---

## Setup  

### Step 1: Clone the Repository  
```bash
git clone https://github.com/amogh9792/QR_code_generator.git
cd QR_code_generator
```

### Step 2: Create a Virtual Environment  
```bash
python -m venv venv_qr
```

### Step 3: Activate the Virtual Environment  
- **Windows:**  
  ```bash
  venv_qr\Scripts\activate
  ```  
- **macOS/Linux:**  
  ```bash
  source venv_qr/bin/activate
  ```

### Step 4: Install Dependencies  
```bash
pip install -r requirements.txt
```

---

## Usage  

1. Run the script:  
   ```bash
   python qr_code_generator.py
   ```  
2. Enter the URL when prompted.  
3. Specify the desired file name (without the extension). The QR code will be saved as `<file_name>.png` in the project directory.

---

## Libraries Used  
- [`qrcode`](https://github.com/lincolnloop/python-qrcode): For creating QR codes.  
- [`Pillow`](https://pillow.readthedocs.io/): For image customization.  

---

## Example  
Here's a demonstration:  
1. Input URL: `https://amoghpathak.tech`  
2. File name: `MyWebsite`  
3. Output: The QR code is saved as `MyWebsite.png` in the project directory.  

---

## License  
This project is licensed under the MIT License.  

---

## Contributions  
Feel free to fork the repository, create a new branch, and raise a pull request for improvements or new features.  

---

For additional details, visit the GitHub repository: [QR Code Generator](https://github.com/amogh9792/QR_code_generator.git)  

---
