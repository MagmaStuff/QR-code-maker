#imports qrcode module
import qrcode

#link (any website link you wish to encode)
link = qrcode.make("https://github.com/MagmaStuff/")
#Data (text to be encoded)
data = "credit to magmastuff"

#Creates the QR code
img = qrcode.make(data)

img.save('epic_image.png') #you can create folders and save them in there too. For example: img.save('folder/image.png')








#thank you for reading my code. I hope you enjoy it.