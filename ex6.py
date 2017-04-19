# string x is declared
x = "There are %d types of people." %10
binary = "binary"#string binary is declared
do_not = "don't" #string do_not is declared
#line 6 is an example of string inside string
y = "Those who know %s and those who %s." %(binary,do_not)
#print string x and y
print x
print y
# two more example of string inside string
print "I said: %r." %x # %r is used for debugging as it displas the raw input 
print "I also said: '%s'." % y

hilarious = False
joke_evaluation="Isn't that joke so funny?! %r"
# another string inside string	
print joke_evaluation % hilarious
#two strings w and e	
w = "This is the left side of..."
e = "a string with a right side."
# + operator concatenates w and e	
print w + e


