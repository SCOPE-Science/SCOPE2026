"""Independent exact-algebra and numerical checks for the S^3 kernel theorem.
Requires Python 3.10+, SymPy, NumPy, SciPy. Finite checks supplement, not replace, the analytic proof.
"""
import math
import sympy as s
from scipy.integrate import quad

x,t=s.symbols('x t', real=True)
D=lambda z: s.expand(z**4+2*(t-1)*z**2+(t+1)**2)
f=lambda z:z/D(z)
H=s.factor((f(x-2)+f(x+2))/(2*f(x)))
R=s.factor(1/H)
U=t**2+2*t*x**2-6*t+x**4+6*x**2-39
C=x**4+2*x**3-9*x**2-10*x+4
assert s.simplify(R-(1+24*(t+5-x**2)/U)) ==0
assert s.simplify(R-(t+(x-3)**2)*(t+(x+3)**2)/U)==0
assert s.simplify((R.subs(x,x+1)-R)-24*(2*x+1)*(C-(2*x**2+2*x+11)*t-3*t**2)/(U*U.subs(x,x+1)))==0
Y=s.symbols('Y',real=True)
V=Y**2+(2*t+6)*Y+t**2-6*t-39
assert s.simplify(s.together(s.diff((Y-t-5)/V,Y))*V**2 + (Y-(t+5))**2-4*(t+1)*(t+4))==0
assert s.expand(C.subs(x,x+3))==x**4+14*x**3+63*x**2+98*x+28
checks=5

def j(l,a):
    z=a*a
    return 2*a*(l+1)*(1-((-1)**l)*math.exp(-math.pi*a))/((z+l*l)*(z+(l+2)**2))

def p(l,a,b):
    if l==0:return j(0,a)+b*(j(2,a)-j(0,a))/2
    if l==1:return j(1,a)+b*j(3,a)/2
    return j(l,a)+b*(j(l-2,a)+j(l+2,a))/2

def threshold(a):
    z=a*a
    x_star=math.sqrt(z+5+2*math.sqrt((z+1)*(z+4)))
    xs=[max(3,math.floor(x_star)),max(3,math.ceil(x_star))]
    val=lambda n:((z+(n-3)**2)*(z+(n+3)**2))/(z*z+2*z*n*n-6*z+n**4+6*n*n-39)
    return min(val(n) for n in xs),set(xs)

for a in (.08,.4,.9,1,1.3,1.8,2.9,3.8,5.7,10,22,55):
    low,ids=threshold(a)
    brute=min((2*j(l,a)/(j(l-2,a)+j(l+2,a)),l+1) for l in range(2,1500))
    assert abs(brute[0]-low)<2.e-13,(a,brute,low)
    checks+=1
    ub=(a*a+16)/(8-a*a) if a*a<8 else math.inf
    for b in (-low, -low+1.e-6, 0., (ub if math.isfinite(ub) else 8.0)):
        for l in range(0,180):
            v=p(l,a,b)
            assert v > -1.e-11,(a,b,l,v)
        checks+=180
    for b,l in [(-low-0.01,brute[1]-1),((ub+0.01 if math.isfinite(ub) else -low-.01),(0 if math.isfinite(ub) else brute[1]-1))]:
        assert p(l,a,b)<0,(a,b,l)
        checks+=1
    # numerical integration of independent Gegenbauer/Chebyshev formula
    for l in (0,1,2,3,5,9,17):
        b=-low+0.1
        integ=quad(lambda th: math.exp(-a*th)*(1+b*math.cos(2*th))*math.sin(th)*math.sin((l+1)*th),0,math.pi,epsabs=1e-12)[0]
        assert abs(integ-p(l,a,b))<4.e-11,(a,l,integ,p(l,a,b))
        checks+=1
for n in range(3,36):
    B=2*n*n+2*n+11
    Cn=n**4+2*n**3-9*n*n-10*n+4
    tau=(-B+math.sqrt(B*B+12*Cn))/6
    assert tau>0
    for e in (-1e-3,1e-3):
        t0=tau+e
        if t0<=0:continue
        rr=lambda k: ((t0+(k-3)**2)*(t0+(k+3)**2))/(t0*t0+2*t0*k*k-6*t0+k**4+6*k*k-39)
        assert (rr(n+1)-rr(n))*e <0
        checks+=1
print('PASS',checks,'exact symbolic identities and supplementary numerical tests')
