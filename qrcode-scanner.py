import os
import cv2
from pyzbar.pyzbar import decode

def scan_qr_codes(folder_path):
    with open("qrcode extracts.txt", "w") as f:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            image = cv2.imread(file_path)
            qr_codes = decode(image)
            for qr_code in qr_codes:
                qr_data = qr_code.data.decode("utf-8")

                f.write(f"{filename}: {qr_data}\n")
if __name__ == "__main__":
    qr_codes_folder = "QR Codes"
    scan_qr_codes(qr_codes_folder)
    print("QR codes scanned successfully. Links saved in 'qrcode extracts.txt'")