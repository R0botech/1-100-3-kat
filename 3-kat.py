
mavi ="\u001b[34;1m"
print(mavi + """
======================================================
1'den 100'e kadar olan sayilarin 3 katini ekrana yazma
======================================================""")

for deger in range(1,100):
	if (deger % 3 !=0):
		continue
	else:
		print (deger)
