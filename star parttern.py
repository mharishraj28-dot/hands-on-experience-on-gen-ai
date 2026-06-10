def py():
    f=open('padma.txt','a+')
    f.write('star pattern lat \n------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write(' inverse star  latpattern  \n------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('star pattern rat rev \n------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('star pattern rat rev\n------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
py()
