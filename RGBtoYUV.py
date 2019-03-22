from PIL import Image

def  rgbtoyuv (R, G, B):
   r=R/255
   g=G/255
   b=B/255

   Y=(0.299*r)+(0.587*g)+(0.114*b) # Y value
   U=0.492*(b-Y)                   # U value
   V=0.877*(r-Y)                   # V value

   return int(Y*255),int(U*255),int(V*255)
resim=Image.open("yuv.jpg").convert("RGB")
resim_pix = resim.load()
w=resim.size[0]
hg=resim.size[1]
for i in range(w):
   for j in range(hg):
       r, g, b = resim.getpixel((i, j))
       y, u, v = rgbtoyuv(y, u, v)
       resim_pix[i,j] = (y, u, v)
resim.save("yuv_new.jpg")
resim.show()

