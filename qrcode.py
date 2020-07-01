import pyqrcode
from pyqrcode import QRCode

d=input("Enter the url for which you would want to create QR Code: ")
url=pyqrcode.create(d)
url.svg("myqr.svg", scale=8)
