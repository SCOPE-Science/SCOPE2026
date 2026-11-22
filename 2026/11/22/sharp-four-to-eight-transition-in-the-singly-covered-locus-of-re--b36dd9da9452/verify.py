"""Independent numerical and algebraic checks for the rectangular Thales covering.
Standard-library Python 3 only. Finite checks support but do not prove the theorem.
"""
import math
from fractions import Fraction

T0 = 2*math.sqrt(2)

def G(t,theta):
    return ((t*t+1)*theta/2 + (t*t-1)*math.sin(2*theta)/4
            -t*math.sin(theta)**2+1/math.tan(theta))

def formula(t):
    assert t>=1
    base=1.5-math.pi/8*(t+1/t)
    if t<=T0: return base
    a=(t-math.sqrt(t*t-8))/4
    b=(t+math.sqrt(t*t-8))/4
    return base+(G(t,math.atan(b))-G(t,math.atan(a)))/(2*t)

def simpson(f,a,b,n=30000):
    assert n%2==0
    h=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))
            +2*sum(f(a+i*h) for i in range(2,n,2)))*h/3

def direct_radial(t):
    cut=math.atan(1/t)
    def f(z):
        R=min(t/math.cos(z),1/math.sin(z)) if 0<z<math.pi/2 else (t if z==0 else 1)
        L=abs(t*math.cos(z)-math.sin(z))
        return max(0,R*R-L*L)
    return (simpson(f,0,cut,10000)+simpson(f,cut,math.pi/2,30000))/(2*t)

def direct_grid(t,n=800):
    hits=0
    for i in range(n):
        x=t*(i+.5)/n
        for j in range(n):
            y=(j+.5)/n
            r2=x*x+y*y
            c=sum(r2<=sx*t*x+sy*y for sx in (-1,1) for sy in (-1,1))
            hits+=(c==1)
    return hits/(n*n)

# Rational identity for polar integrand; no floating point used.
for t in (Fraction(1),Fraction(2),Fraction(3),Fraction(4),Fraction(11,2)):
    for u in (Fraction(1,3),Fraction(1),Fraction(3,2),Fraction(7,3)):
        left=((t-u)**2/(1+u*u)-(1+u*u)/(u*u))/(1+u*u)
        right=(t*u+1)*(t*u-2*u*u-1)/(u*u*(1+u*u)**2)
        assert left==right

for t in (1,1.4,2,2.7,T0,2.83,3,4,5,10):
    analytical=formula(t)
    radial=direct_radial(t)
    grid=direct_grid(t,600)
    assert abs(analytical-radial)<3e-8,(t,analytical,radial)
    assert abs(analytical-grid)<0.0025,(t,analytical,grid)
    print(f't={t:.9g}  area_fraction={analytical:.12f}  radial={radial:.12f}  Cartesian_grid={grid:.12f}')

# A strict interior forbidden angular interval opens precisely at t > sqrt(8).
for t in (1,2,2.8,T0,3,4,10):
    D=t*t-8
    if t<T0-1e-12: assert D<0
    elif t>T0+1e-12:
        a=(t-math.sqrt(D))/4;b=(t+math.sqrt(D))/4
        assert 1/t<a<b<t
        m=(a+b)/2
        assert 2*m*m-t*m+1<0
        assert 2*a*a-t*a+1<1e-12
        assert 2*b*b-t*b+1<1e-12

# Cusp correction in the supercritical regime.
c=2*2**.25/9
for ep in (.02,.005,.001):
    t=T0+ep
    base=1.5-math.pi/8*(t+1/t)
    ratio=(formula(t)-base)/ep**1.5
    assert abs(ratio-c)<.004,(ep,ratio,c)

print('PASS: rational identities, polar quadrature, Cartesian incidence, threshold, cusp checks')
