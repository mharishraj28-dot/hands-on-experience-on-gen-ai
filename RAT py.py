def py():
    f=open('padma.txt','a+')
    f.write('rat inverserow \n---------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat  inverse col \n---------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat  inverseupper row \n---------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat  inverseupper col \n---------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(j+64)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat inverselower row \n---------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(i+96)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat lower col\n---------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(j+96)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat row\n---------------------\n')
    for i in range(1,6):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat col\n---------------------\n')
    for i in range(1,6):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat row up\n---------------------\n')
    for i in range(1,6):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat col up\n---------------------\n')
    for i in range(1,6):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(j+64)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat row down\n---------------------\n')
    for i in range(1,6):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(i+96)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('rat col dowm\n---------------------\n')
    for i in range(1,6):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(j+96)))
        f.write('\n')
    f.close()
py()
