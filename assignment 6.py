def py():
    f=open('padma.txt','w+')
    f.write('ROW RAT \n --------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
py()

def py():
    #col-rat
    f=open('padma.txt','a+')
    f.write('col rat \n---------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.close()
py()

def py():
    #row-rat-up
    f=open('padma.txt','a+')
    f.write('row rat upper \n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
py()
def py():
    #col-rat-down
    f=open('padma.txt','a+')
    f.write('col rat upper \n------------------\n')
    
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(j+65)))
        f.write('\n')
py()  

def py():
    #col-rat-up
    f=open('padma.txt','a+')
    f.write('col rat lower \n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(j+97)))
        f.write('\n')
    f.close()
py()

def py():
    #row-rat-up
    f=open('padma.txt','a+')
    f.write('row rat lower \n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(i+96)))
        f.write('\n')
    f.close()
py()

def py():
    #rev-row-rat
    f=open('padma.txt','a+')
    f.write('inverse row rat \n------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
py()
def py():
    #rev-col-rat
    f=open('padma.txt','a+')
    f.write('inverse col rat \n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.close()
py()
def py():
    # rev-col-rat
    f=open('padma.txt','a+')
    f.write('inverse row rat \n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('row rat upper \n------------------\n')
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
    f.write('row rat upper \n------------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(chr(k+64)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('row rat upper \n------------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
py()
def py():
    f=open('padma.txt','a+')
    f.write('row rat upper \n------------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(chr(k+96)))
        f.write('\n')
    f.close()
py()



def py():
    f=open('padma.txt','a+')
    f.write('Rat \n----------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(chr(j+96)))
        f.write('\n')
    f.close()

py()

def pon():
    f=open('padma.txt','a+')
    f.write('row rat upper \n------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
pon()

def pon():
    f=open('padma.txt','a+')
    f.write('row rat upper \n------------------\n')
    for i in range(6,0,-1):
        for k in range(6,i,-1):
            f.write(' ')
        for j in range(0,i):
            f.write(str(j)+' ')
        f.write('\n')
    f.close()
pon()
