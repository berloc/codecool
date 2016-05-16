import sys

def hello():
    try:
        return ("Hello %s!" %(sys.argv[1]))
    except IndexError:
        return ("Hello World!")

print (hello())
