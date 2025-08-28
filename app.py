from flask import Flask, render_template, request, redirect, url_for
from pyzbar import pyzbar
import cv2
import csv
import time, datetime
from mongo_access import get_database
import qrcode
app = Flask(__name__)
cam = False
customerdb="Bill"
barcodeData=''
@app.route("/")
def index():
    return render_template("index.html", cam=cam)
@app.route("/start_scanning", methods=["POST"])
def start_scanning():
    global cam
    return redirect(url_for("scan_barcode"))

@app.route("/scan_barcode")
def scan_barcode():
    cap = cv2.VideoCapture(0)
    start = time.time()
    
    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)
        final = cv2.line(decoded_objects, (0, int(decoded_objects.shape[0] / 2)),
                         (decoded_objects.shape[1], int(decoded_objects.shape[0] / 2)), (0, 0, 255), 1, 1)
        cv2.imshow("frame", final)
        end = time.time()
        if cam:
            break
        if cv2.waitKey(1) == ord("q"):
            break
        elif (end - start) > 100:  # 100 sec timeout
            break
    cap.release()
    cv2.destroyAllWindows()
    return redirect(url_for("continue_scanning"))

@app.route("/continue_scanning", methods=["GET", "POST"])
def continue_scanning():
    global cam

    if request.method == "POST":
        choice = request.form["choice"]
        if choice == "y":
            cam = False
            return redirect(url_for("scan_barcode"))
        else:
            exportcsv(customerdb)
            cam = False
            return redirect(url_for("show_exported_csv"))

    scanned_item = get_scanned_item_details(barcodeData)
    print('scanned',barcodeData,scanned_item)  # You'll need to implement this function

    return render_template("continue_scanning.html", scanned_item=scanned_item)

def get_scanned_item_details(barcode_data):
    import pymongo
    from bson import ObjectId  # Import ObjectId from bson module

    # MongoDB connection information
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")  # Change this URL to your MongoDB server
    db_name = "Project"  # Replace with your database name
    inventory_collection_name = "Inventory"
    bill_collection_name="Bill"
    # Connect to the database and collection
    db = mongo_client[db_name]
    inventory_collection = db[inventory_collection_name]
    bill_collection = db[bill_collection_name]
    barcode_data=ObjectId(barcode_data)

    # Find the document in the inventory collection by barcode data (or item ID)
    item_inventory = inventory_collection.find_one({"_id": barcode_data})

    if item_inventory:
        bill_name= item_inventory.get("name","")
        item = bill_collection.find_one({"name":bill_name})

        if item:
            # If the item is found, return its details
            return {
                "name": item.get("name", ""),
                "quantity": item.get("quantity", 0),
                "price": item.get("price", 0)
            }
        else:
            # If the item is not found, return None
            return None


def decode(image):
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        update_db(data)
    return image

def update_db(data):
    collection = get_database()
    add_to_bill(data)
    global barcodeData
    barcodeData=data
    print("Update Success!")
    global cam
    cam=True
      
def update_or_create_item(name,price,weight, quantity,collection):
    # Search for an item by name
    global customerdb
    customerdb=collection
    existing_item = collection.find_one({"name": name})
    if existing_item:
        # If the item already exists, update its quantity,price
        new_weight = existing_item["weight"] + weight
        new_quantity = existing_item["quantity"] + quantity
        new_price = existing_item["price"] + price
        collection.update_one({"name": existing_item["name"]}, {"$set": {"quantity": new_quantity}})
        collection.update_one({"name": existing_item["name"]}, {"$set": {"price": new_price}})
        collection.update_one({"name": existing_item["name"]}, {"$set": {"weight": new_weight}})
        print(f"Updated item: {name}, New quantity: {new_quantity}")
    else:
        # If the item doesn't exist, create a new document
        item = {"name": name, "quantity": quantity , "price":price, "weight":weight}
        collection.insert_one(item)
        print(f"Created new item: {name}, quantity: {quantity}")



def add_to_bill(inventory_id_str):
    import pymongo
    from bson import ObjectId  # Import ObjectId from bson module

    # MongoDB connection information
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")  # Change this URL to your MongoDB server
    db_name = "Project"  # Replace with your database name
    inventory_collection_name = "Inventory"
    bill_collection_name = "Bill"

    # Connect to the database
    db = mongo_client[db_name]
    inventory_collection = db[inventory_collection_name]
    bill_collection = db[bill_collection_name]

    # Convert the inventory_id_str to ObjectId
    inventory_id = ObjectId(inventory_id_str)

    # Find the document in the inventory collection by ID
    inventory_item = inventory_collection.find_one({"_id": inventory_id})
    

    if inventory_item:
        # Check if there's sufficient quantity in the inventory
        if inventory_item.get("quantity", 0) > 0:
            inventory_collection.update_one(
                {"_id": inventory_id},
                {"$inc": {"quantity": -1}}
            )
            inventory_name= inventory_item.get("name",None)
            inventory_price = inventory_item.get("price",None)
            inventory_weight = inventory_item.get("weight",None)
            
            update_or_create_item(inventory_name,inventory_price, inventory_weight,1,db["Bill"])
            print("Item added to the bill successfully.")
        else:
            print("Item is out of stock.")
    else:
        print("Item not found in the inventory.")



def exportcsv(collection):
    csv_file = "exported_data.csv"

    # Retrieve data from the MongoDB collection
    data = list(collection.find({}, {"_id": 0}))

    # Calculate total price and total weight
    total_price = sum(float(row["price"]) for row in data)
    total_weight = sum(float(row["weight"]) for row in data)
    total_quantity = sum(int(row["quantity"]) for row in data)

    # Add the total row to the data
    total_row = {"name": "Total", "quantity": total_quantity, "price": total_price, "weight": total_weight}
    data.append(total_row)

    # Define the CSV header (column names) based on your data structure
    csv_header = ["name", "quantity", "price", "weight"]

    # Write data to the CSV file
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_header)
        writer.writeheader()
        for document in data:
            writer.writerow(document)

    collection.drop()
    print("Successfully Exported")

    


@app.route("/show_exported_csv")
def show_exported_csv():
    csv_file = "exported_data.csv"
    csv_content = []

    # Read CSV data
    with open(csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            csv_content.append(row)

   # Calculate the total amount, excluding the last row (Total)
    total_amount = sum(float(row["price"]) for row in csv_content[:-1])

    # Define the payment request details
    vpa = "fabiosebastian111@oksbi"  # Replace with the recipient's VPA
    amount = total_amount # Replace with the transaction amount
    message = "Payment for your order"  # Optional message

    # Construct the UPI URL for the payment request
    upi_url = f"upi://pay?pa={vpa}&am={amount}&pn=RecipientName&mc=123456&tid=CUST001&tr=12345678&tn={message}"
    # Generate a Google Pay QR code with the total amount
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(r"Flask\static\qr_code.png")

    return render_template("show_exported_csv.html", csv_content=csv_content, total_amount=total_amount,qrcode=qr_image)


if __name__ == "__main__":
    app.run(debug=True)