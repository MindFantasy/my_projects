import cv2
from qrcode import make
from os import listdir
from pathlib import Path

class QR_handling:
    def __init__(self):
        self.amount = None
        self.png_list = []

    def start(self):
        print("\nThis is a program to generate and decode QR codes")
        self.code_or_decode()

    def code_or_decode(self):
        print("\nDo you want to generate the QR code or decoded it?")
        while True:
            decision = input("To proceed input \"code\" or \"decode\": ").strip().lower()
            if decision == "code":
                self.information_collection_coding()
                break
            elif decision == "decode":
                self.qr_decoding_files()
                break
            print("To proceed you need to imput \"code\" or \"decode\"")

    def information_collection_coding(self):
        while True:
            self.amount = input("How many codes needs to be generated? ").strip()
            if self.amount.isnumeric():
                break
            print("The input needs to be a number")

        print("\nDo you want to manually name the QR files?")
        while True:
            decision = input("To proceed input \"manually\" or \"automaticly\": ").strip().lower()
            if decision == "manually":
                self.qr_coding_detailed()
                break
            elif decision == "automaticly":
                self.qr_coding_basic()
                break
            print("To decine user needs to input only \"manually\" or \"automaticly\"")

    def qr_coding_basic(self):
        for i in range(1, int(self.amount) + 1):
            text = input("Input the text that needs to be incoded into QR code: ")
            image = make(text)
            image.save(f"ORcode number:{i}.png")
        print("Your QR codes were created")

    def qr_coding_detailed(self):
        for i in range(1, int(self.amount) + 1):
            file_name = input("\nInput name of the file with qrcode: ")
            text = input("Input the text that needs to be incoded into QR code: ")
            image = make(text)
            image.save(f"{file_name}.png")
        print("Your QR codes were created")

    def qr_decoding_files(self):
        file_list = listdir(Path.cwd())
        for file in file_list:
            if file.find("png") != -1:
                self.png_list.append(file)
        self.png_list.sort()
        self.qr_decoding()

    def qr_decoding(self):
        for file in self.png_list:
            image = cv2.imread(file)
            detect = cv2.QRCodeDetector()
            value, points, straight_qrcode = detect.detectAndDecode(image)
            print(f"\nFile name of QR code: {file} \nDecoded text: {value}")



first = QR_handling()
first.start()