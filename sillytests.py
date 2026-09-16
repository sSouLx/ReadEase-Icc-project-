import colorful as cf


string = 'primeiro teste colorindo strings'

for i in range(len(string)):
    if i%2 == 0:
        string[i] = cf.bold_white(string[i])
        

print(string)