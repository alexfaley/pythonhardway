tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat  food
\t* Fishes
\t* Catship\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
n=1000
while n>0:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
	n=n-1
		