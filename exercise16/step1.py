from sys import argv

script, file_name = argv

print "We've going to arase %r." % file_name
print "if you dont't want that, hit CTRL-C(^)."
print "If you want that, hit RETURN."

raw_input("?")
print "OPennig file ..."
target = open(file_name, 'w')
#target.truncate()

print "Now I'm going to ask you for three lines"
line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")
print "I'm going write these to end file."
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it."
target.close()
