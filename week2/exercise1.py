"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# this creates a list withcthose words 
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #  it initialised a list with those words

for word in some_words:
   print(word)#it print a word for some_word list 
#I think this will do simething in some_word list 

for x in some_words:
    print(x)#x is not define in the some_word list so can not print
#i think this will do nothing with some_word
print(some_words)#it print some_word
#so i think will define some_word list

if len(some_words) > 3:
    print('some_words contains more than 3 words')#it print some_word list more than 3 words
#i think it will print some_word list more then 3 word
def usefulFunction():
#i think will define usefulFunction
    
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())#it ask for print a list 
    #i think it will define 
usefulFunction()#it operation define the useFunction
