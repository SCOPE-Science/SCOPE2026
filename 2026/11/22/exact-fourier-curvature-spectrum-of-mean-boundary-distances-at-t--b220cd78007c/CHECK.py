"""Independent arithmetic checks for the published curvature-spectrum identity.
No external packages are required. Finite checks do not establish the all-mode theorem.
"""
from fractions import Fraction as F
from math import pi, sin, cos, hypot

def add(a,b):
    out=a+[F(0)]*max(0,len(b)-len(a))
    for i,c in enumerate(b):out[i]+=c
    return out

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]+=c*d
    return out

def upoly(n):
    if n==0:return [F(1)]
    a,b=[F(1)],[F(0),F(2)]
    for _ in range(2,n+1):
        c=add([F(0)]+[2*t for t in b],[-t for t in a]);a,b=b,c
    return b

def integ_square(poly):
    sq=mul(poly,poly)
    return sum((F(2)*t/F(i+1) if i%2==0 else F(0)) for i,t in enumerate(sq))

def H(m):return sum((F(1,2*j-1) for j in range(1,m+1)),F(0))

def J_closed(m):
    return (F(1,m*m-1)+2*H(m)/((m*m-1)**2)
            +F(1,2*(2*m+1)*(m+1)**2)-F(1,2*(2*m-1)*(m-1)**2))

def Q(m):return F(12,4*m*m-1)-J_closed(m)

for m in range(2,16):
    u=upoly(m);v=upoly(m-2)
    p=add([t/F(m+1) for t in u],[-t/F(m-1) for t in v])
    j=integ_square(p)/4
    assert j==J_closed(m),(m,j,J_closed(m))
    assert Q(m)>0
    assert 16*m**4-18*m**3-33*m*m+23>0
assert Q(2)==F(44,135)
assert Q(3)==F(4,21)

def value(m,eps,n=240):
    zs=[]; w=[]
    for j in range(n):
        t=2*pi*j/n
        z=complex(cos(t),sin(t))
        z+=eps/2*(complex(cos((m+1)*t),sin((m+1)*t))/(m+1)
                  +complex(cos((1-m)*t),sin((1-m)*t))/(1-m))
        zs.append(z);w.append(1+eps*cos(m*t))
    T=0.0
    for i in range(n):
        for j in range(n):
            T+=w[i]*w[j]*abs(zs[i]-zs[j])
    return T/n**2/(2*pi)

for m in (2,3,4,6):
    e=0.035
    # Geometric central difference eliminates base-grid quadrature errors.
    h=(value(m,e)+value(m,-e)-2*value(m,0))/(2*e**2)
    exact=-float(Q(m))/(4*pi*pi)
    assert abs(h-exact)<4e-5,(m,h,exact)
print('PASS: exact rational mode integrals 2..15; positivity; m=2,3; direct geometric quadrature')
