import util

r = 97
g = 178
b = 171

hsi = util.rgb2hsi(r,g,b)

rgb = util.hsi2rgb(hsi[0],hsi[1],hsi[2])

print(hsi)
print(rgb)