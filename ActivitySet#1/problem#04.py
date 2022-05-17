
hrs = input("Enter Hours:")
h = float(hrs)
a = input("Enter the Rate:")
b = float(a)

if h > 40:
	print(40* b + (h-40)*1.5*b)
else:
   	print( h  * b)
