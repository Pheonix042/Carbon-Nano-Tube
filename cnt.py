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
        print(ll)
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
for num in range(1,totalat+1):
    if num in range(1,totalat,4):
        mm.append(' ')
    elif num in range(4,totalat,4):
        mm.append(' ')
    else:
        if num%2==0:
           mm.append(num+1)
        else:
            mm.append(num-1)
myfile=open('./cnt.xyz','w')
myfile.write('{}\t \n'.format(totalat))
for num in range(totalat):
    R=r[num]
    L=l[num]
    nu=num+1
    if mm[num]==' ':
        M=''
    else:
        M=mm[num]
    myfile.write('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t\n'.format(nu,'C',Xco[num],Yco[num],Zco[num],R,L,M))
    print(R,L,M)
myfile.close()
