from PIL import Image,ImageDraw,ImageFont

a=Image.open(r"C:\Users\lenovo\Desktop\1.jpg")
dr=ImageDraw.Draw(a)
fnt=ImageFont.truetype('GIGI.ttf',50)
dr.text((20,75),"Damn You",font=fnt,fill='#ff7f50')
a.show()
a.save('d:/test.jpg')
