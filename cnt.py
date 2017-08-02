from math import pi,cos,sin
width=2.44219
n=int(input('Enter number of hexagon'))
radius=2.44219*n/(2*pi)
totalat=4*n
angle=(2*pi)/n
theta1=0
num=0
Xco=[]
Yco=[]
Zco=[]
r=[]
l=[]
mm=[]
while num<n:
    x1=radius*cos(theta1)
    y1=radius*sin(theta1)
    theta2=theta1+(angle/2)
    x2=radius*cos(theta2)
    y2=radius*sin(theta2)
    theta1+=angle
    z1=1.41*(1+sin(pi/6))
    z2=1.41
    z3=0
    z4=-1.41*sin(pi/6)
    if num==0:
        rr=[2,5,8,3]
        ll=[totalat-2,1,4,totalat-1]
        r.extend(rr)
        l.extend(ll)
    elif num==(n-1):
        rr=[(totalat-2),1,4,(totalat-1)]
        ll=[(totalat-6),(totalat-3),totalat,(totalat-5)]
        r.extend(rr)
        l.extend(ll)
    else:
        zo=4*(num)+1
        rr=[(zo+1),(zo+4),(zo+7),(zo+2)]
        ll=[(zo-3),(zo),(zo+3),(zo-2)]
        r.extend(rr)
        l.extend(ll)
    Xco.append(round(x1,6))
    Xco.append(round(x2,6))
    Xco.append(round(x2,6))
    Xco.append(round(x1,6))
    Yco.append(round(y1,6))
    Yco.append(round(y2,6))
    Yco.append(round(y2,6))
    Yco.append(round(y1,6))
    Zco.append(round(z1,6))
    Zco.append(round(z2,6))
    Zco.append(round(z3,6))
    Zco.append(round(z4,6))
    num+=1
zx=0
for num in range(1,totalat+1):
    if num in range(1,totalat,4):
        mm.append(num+(4*n)-zx)
        zx+=2
    elif num in range(4,totalat+1,4):
        mm.append(' ')
    else:
        if num%2==0:
           mm.append(num+1)
        else:
            mm.append(num-1)
gen_x=[]
gen_y=[]
for num in range(0,len(Xco),4):
    gen_x.append(Xco[num])
    gen_x.append(Xco[num+1])
    gen_y.append(Yco[num])
    gen_y.append(Yco[num+1])
height=int(input('Enter height of CNT:'))
h=2
gen_x_even=gen_x.copy()
gen_y_even=gen_y.copy()
#gen_x_even.insert(0,gen_x_even[-1])
#del gen_x_even[-1]
#gen_y_even.insert(0,gen_y_even[-1])
#del gen_y_even[-1]
def h1(num,n):
    return (num+1+(n*2))
def h2(num,n):
    return (num+1-(n*2))
zxz=1
while h<=height:
    if h%2==1:
        Xco.extend(gen_x_even)
        Yco.extend(gen_y_even)
    else:
        Xco.extend(gen_x)
        Yco.extend(gen_y)
    start,stop=int(totalat),int((totalat+(n*2)))
    for num in range(start,stop):
        if h%2==0:
            if num%2==1:
                z=1.41*h+0.705*(h+1)
            else:
                z=2.115*h
        else:
            if num%2==0:
                z=1.41*h+0.705*(h+1)
            else:
                z=2.115*h
        Zco.append(z)
        if num!=(stop-1):
            rr=num+2
        else:
            rr=start+1
        r.append(rr)
        if num!=start:
            ll=num
        else:
            ll=stop
        l.append(ll)
        if h!=height and h!=2:
            if h%2==1:
                if num%2==0:
                    m=h1(num,n)
                else:
                    m=h2(num,n)
            else:
                if num%2==1:
                    m=h1(num,n)
                else:
                    m=h2(num,n)
        elif h==2:
            if num%2==1:
                m=h1(num,n)
            else:
                m=zxz
                zxz+=4
        else:
            if h%2==0:
                if num%2==1:
                    m=' '
                else:
                    m=h2(num,n)
            else:
                if num%2==0:
                    m=' '
                else:
                    m=h2(num,n)
        mm.append(m)
    totalat=stop
    h+=1
myfile=open('./cnt.xyz','w')
myfile.write('{}\t\n'.format(totalat))
for num in range(totalat):
    nu=num+1
    if mm[num]==' ':
        M=''
    else:
        M=mm[num]
    myfile.write('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t\n'.format(nu,'C',Xco[num],Yco[num],Zco[num],2,r[num],l[num],M))
myfile.close()
