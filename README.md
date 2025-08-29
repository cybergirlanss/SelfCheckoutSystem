# Self Checkout Software
A comprehensive self-checkout kiosk software built with Python. This application simulates a real-world self-checkout experience by using a webcam to scan item barcodes, managing an inventory with MongoDB, generating a real-time bill, and facilitating payments through UPI QR codes.

# Key Features

Barcode Scanning: Uses OpenCV and Pyzbar to detect and decode barcodes in real-time via your computer's webcam.

MongoDB Inventory: Connects to a MongoDB database to instantly fetch product details (name, price) upon a successful scan.

Dynamic Bill Generation: Scanned items are added to a digital shopping cart, and the total amount is calculated on the fly.

UPI Payment Integration: Generates a unique QR code for UPI payment once the user is ready to check out.

CSV Bill Export: Allows users to save their final bill as a .csv file for record-keeping.

Simple User Interface: A clean and intuitive interface built with Flask to display the video feed, bill, and payment options.

# Technology Stack
This project is built with a combination of powerful and open-source libraries:

Backend Framework: Flask

Computer Vision: OpenCV (opencv-python)

Barcode Decoding: Pyzbar (pyzbar)

Database: MongoDB

Python-MongoDB Connector: PyMongo (pymongo)

QR Code Generation: QRcode (qrcode[pil])

# Getting Started
Follow these instructions to set up and run the project on your local machine.

Prerequisites
Python 3

A MongoDB Atlas account or a local MongoDB server instance.

A webcam connected to your computer.

1. Clone the Repository
git clone [https://github.com/FabioSebastian/SelfCheckoutSoftware/]

2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

3. Install Dependencies
Install all the required libraries using the requirements.txt file.

pip install -r requirements.txt

pip install Flask opencv-python pyzbar pymongo "qrcode[pil]"

4. Configure MongoDB
Obtain your MongoDB connection string.

Open the app.py file (or your main configuration file).

5. Run the Application
Execute the main Python script to start the Flask server.

python app.py

Open your web browser and navigate to http://127.0.0.1:5000 to start using the self-checkout system.

# How To Use
Start Scanning: Point your items' barcodes at the webcam. The application will draw a box around a detected barcode.

View Bill: Once a barcode is successfully scanned and found in the database, the item will appear on the bill to the right, and the total will be updated.

Finalize & Pay: When you are done scanning, click the "Proceed to Pay" button.

UPI Payment: A unique UPI QR code will be displayed. You can scan this with any UPI-enabled app to simulate payment.

Save Bill: After payment, you'll have the option to download the bill as a CSV file.
