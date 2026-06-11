def hrt():
    hrt=[(1,2),(1,3),(1,5),(1,6),(2,1),(2,4),(2,7),(3,1),(3,7),(4,2),(4,6),(5,3),(5,5),(6,4)]
    for i in range(1,10):
        for j in range(1,10):
            if(i,j) in hrt:
                print('+',end= ' ')
            else:
                print('.',end= ' ')
        print()
hrt()

def py():
    print('oval ')
    circle=[(2,2),(2,3),(3,1),(3,4),(4,1),(4,4),(5,2),(5,3)]
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in circle:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()

def py():
    oval=[(2,3),(4,2),(4,4),(5,2),(5,4),(7,3)]
    print('oval')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in oval:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()

def py():
    circle=[(2,2),(2,3),(3,1),(3,4),(4,1),(4,4),(5,2),(5,3)]
    print('circle')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in circle:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()


def py():
    square=[(2,3),(2,4),(2,5),(3,3),(3,5),(4,3),(4,4),(4,5)]
    print('square')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in square:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()

def py():
    rec=[(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,7),(4,3),(4,4),(4,5),(4,6),(4,7)]
    print('rec')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in rec:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()

def py():
    tri=[(2,3),(3,2),(3,4),(4,1),(4,2),(4,3),(4,4),(4,5)]
    print('triangle')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in tri:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()

def py():
    semi=[(2,2),(2,3),(2,4),(3,1),(3,5),(4,1),(4,2),(4,3),(4,4),(4,5)]
    print('semicircle')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in semi:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()

def py():
    trap=[(3,3),(3,4),(3,5),(4,2),(4,6),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7)]
    print('trapezoid')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in trap:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()

def py():
    pentagon=[(1,4),(2,3),(2,5),(3,2),(3,6),(5,3),(5,4),(5,5)]
    print('pentagon')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in pentagon:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()

def py():
    star=[(2,4),(4,2),(4,3),(4,5),(4,6),(5,3),(5,5),(6,4),(7,3),(7,5)]
    print('star')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in star:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
py()
