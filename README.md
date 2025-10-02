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
4. **Configure MongoDB**
   - Obtain your MongoDB connection string from [MongoDB Atlas](https://www.mongodb.com/atlas) or your local MongoDB instance
   - Update the connection details in the configuration file (`app.py` or config file)

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your web browser and navigate to `http://127.0.0.1:5000`
## 💡 How to Use

1. **Start Scanning**: Point item barcodes at your webcam. The application will detect and highlight barcodes in real-time.
2. **View Bill**: Successfully scanned items automatically appear in your digital cart with updated totals.
3. **Checkout**: Click "Proceed to Pay" when finished scanning.
4. **UPI Payment**: Scan the generated QR code with any UPI-enabled app to complete payment.
5. **Save Receipt**: Download your bill as a CSV file for records.

## 📁 Project Structure

```
SelfCheckoutSystem/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── templates/            # HTML templates
├── static/              # CSS, JavaScript, assets
└── README.md            # Project documentation
```
