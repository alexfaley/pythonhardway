from sys import argv

script, filename = argv

txt = open(filename)
print "Here's your file%r:" % filename
print txt.read()

print "Type to file name again:"
file_name_again = raw_input('>')
txt_again = open(file_name_again)
print txt_again.read()
