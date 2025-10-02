# 🛒 Self-Checkout System

A comprehensive self-checkout kiosk software built with **Python**.  
This application simulates a real-world self-checkout experience by using a webcam to scan item barcodes, managing an inventory with **MongoDB**, generating a real-time bill, and facilitating payments through **UPI QR codes**.

---

## 🚀 Key Features

- **Barcode Scanning**: Uses OpenCV and Pyzbar to detect and decode barcodes in real-time via your computer's webcam.  
- **MongoDB Inventory**: Connects to a MongoDB database to instantly fetch product details (name, price) upon a successful scan.  
- **Dynamic Bill Generation**: Scanned items are added to a digital shopping cart, and the total amount is calculated on the fly.  
- **UPI Payment Integration**: Generates a unique QR code for UPI payment once the user is ready to check out.  
- **CSV Bill Export**: Allows users to save their final bill as a `.csv` file for record-keeping.  
- **Simple User Interface**: A clean and intuitive interface built with Flask to display the video feed, bill, and payment options.  

---

## 🛠 Technology Stack

- **Backend Framework**: Flask  
- **Computer Vision**: OpenCV (`opencv-python`)  
- **Barcode Decoding**: Pyzbar (`pyzbar`)  
- **Database**: MongoDB  
- **Python-MongoDB Connector**: PyMongo (`pymongo`)  
- **QR Code Generation**: QRcode (`qrcode[pil]`)  

---

## 📦 Installation

### Prerequisites
- Python 3.7+
- MongoDB Atlas account or local MongoDB instance
- Webcam connected to your computer

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/cybergirlanss/SelfCheckoutSystem.git
   cd SelfCheckoutSystem
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

