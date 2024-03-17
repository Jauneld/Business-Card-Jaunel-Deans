#Jaunel Deans 9/8 - 9/11
#Generate a QR Code for our Business Card (practice)
#save the QR code as an image 
import qrcode  #This importing the QR package
#address of data
site_url= "https://drive.google.com/file/d/1YtfJKa1ZegV9tub_Ec7vtg0OozR0gd7A/view?usp=sharing"

imgName = "BusinessCard" #variable for card(string)

#sets uo the QR Code parameters
qr = qrcode.QRCode(
  version = 1,
  error_correction = qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,
)

#QR Code funtionality
qr.add_data(site_url)
qr.make(fit=True)

#QR Code image settings
img = qr.make_image(fill_color = 'black',back_color = 'white',)
img.save(f"{imgName}.png")
print("QR Code generated successfully")