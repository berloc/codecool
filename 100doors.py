doors = [0]*101

def switch(x):
    global doors
    if doors[x] == 0:
        doors[x] = 1
    else:
        doors[x] = 0

for i in range (1,101):
    for j in range (1, 101):
        if j%i == 0:
            switch(j)
            j += 1
        else:
            j += 1
    i += 1

for y in range (1,101):
    if doors[y] == 1:
        print (y)
