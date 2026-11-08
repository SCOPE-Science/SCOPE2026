"""Exact rational geometry and transverse-multiplier bound for a four-arc oscillator."""
from fractions import Fraction as F
from math import pi, exp, atan2, hypot
P=[(1,0),(0,2),(-3,0),(0,-4)]
Q=[(1,2),(-4,3),(-5,-2),(2,-3)]
C=[]; R2=[]
def det(a,b,c,d):return a*d-b*c
for i in range(4):
    pts=[P[i],Q[i],P[(i+1)%4]]
    a,b=pts[0]; c,d=pts[1]; e,f=pts[2]
    u,v=2*(c-a),2*(d-b)
    w,z=2*(e-a),2*(f-b)
    h=F(c*c+d*d-a*a-b*b);j=F(e*e+f*f-a*a-b*b)
    D=det(u,v,w,z)
    cx=det(h,v,j,z)/D;cy=det(u,h,w,j)/D
    C.append((cx,cy));R2.append((F(a)-cx)**2+(F(b)-cy)**2)
assert C==[(F(1,2),F(1)),(-F(47,22),F(43,22)),(-F(33,14),-F(37,14)),(F(3,14),-F(27,14))]
assert R2==[F(5,4),F(1105,242),F(725,98),F(425,98)]
ratio=F(1);factors=[]
for i,(x,y) in enumerate(P):
    radius=hypot(x,y); ex=F(x,int(radius));ey=F(y,int(radius))
    new=F(int(radius))-C[i][0]*ex-C[i][1]*ey
    j=(i-1)%4
    old=F(int(radius))-C[j][0]*ex-C[j][1]*ey
    assert new>0 and old>0
    factors.append(new/old);ratio*=new/old
assert factors==[F(7,11),F(1,22),F(99,133),F(29,19)]
assert ratio==F(261,7942)
s=sum(R2)
assert s==F(416235,23716)
assert float(1/ratio)*exp(-4*pi*float(s)/1000)>24
angles=[]
for i in range(4):
    def th(point):return atan2(float(F(point[1])-C[i][1]),float(F(point[0])-C[i][0]))
    angle=(th(P[(i+1)%4])-th(P[i]))%(2*pi)
    assert 0<angle<2*pi
    angles.append(angle)
correct=float(1/ratio)*exp(-2*sum(float(R2[i])*angles[i] for i in range(4))/1000)
assert 26<correct<27
print('FOUR_ARC_CLOCKWISE_REPELLING_EXACT_GEOMETRY_OK; G='+str(ratio)+'; lower_bound='+str(float(1/ratio)*exp(-4*pi*float(s)/1000))+'; multiplier='+str(correct))
