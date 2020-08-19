def RGB(color):
	r = int(color[1:3],16)
	g = int(color[3:5],16)
	b = int(color[5:7],16)
	a = 255 
	if len(color) == 9:
		a = int(color[7:9],16)
	return r,g,b,a

def mapThis(current,min1,max1,min2,max2):
	x = min1
	max1 -= x
	current -= x
	x = min2
	max2 -= x
	out = (current / max1) * max2
	out += x + 1
	max2 += x
	if out < min2:
		out = min2
	elif out > max2:
		out = max2
	return out