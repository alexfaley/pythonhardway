x = "There are %d types of people ."%10
binary = "binary"
do_not = "don't"
y = "These who know %s and those %s" % (binary, do_not)

print x
print y

print "I said : %r" % x
print "I also said : '%r'" % y

hilarious = False
joke_evalution = "Isn't that joke so funny?! %s"
print joke_evalution % hilarious

w = "This is the left %s side of..."
e = "a string with a right side."
print w % 'alex'+e
print "one %" + "s %s three" % "two"
