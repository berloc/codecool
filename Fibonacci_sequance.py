a, b, c, d = 0, 1, 2, 0
print ("Fibonacci sequance:")
while c < 32:
    d = d + 1
    print d, a
    a, b, c = b, a + b, c + 1
