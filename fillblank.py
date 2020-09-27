from PIL import Image
from tqdm import tqdm

#画像読み込み
im = Image.open("FilippineBig.png")

#RGBに変換
rgb_im = im.convert('RGB')

#画像サイズ取得
size = rgb_im.size
print(size[0],size[1])

#空イメージ
im2 = Image.new('RGB',size)

for x in tqdm(range(size[0])):
	for y in range(size[1]):
		#ピクセル取得
		r,g,b = rgb_im.getpixel((x,y))
		
		#ffffffなら125,125,125にする
		if(r==255 and g==255 and b==255):
			r = 125
			g = 125
			b = 125

		#set pixel
		im2.putpixel((x,y),(r,g,b))
	
#show
im2.save('FilippineBig.ppm')