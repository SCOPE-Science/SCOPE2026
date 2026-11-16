"""Independent exact and numerical checks for two-polar-cap spin-one design.
Run: python check.py. Requires Python 3, SymPy and SciPy.
"""
from math import sqrt,acos,pi,sin,cos
import random
import sympy as S
from scipy.integrate import quad
h,d=S.symbols('h d',real=True)
p,q=(h+d)/2,(h-d)/2
L0=3*p-3*p*p+p**3+q**3
L1=3*(p*p+q*q)-2*(p**3+q**3)
L2=p**3+3*q-3*q*q+q**3
assert S.simplify((L0-L2)-3*d*(1-h))==0
assert S.simplify((L1-L2)-S.Rational(3,4)*(1-h)*(3*d*d+2*d+h*h-2*h))==0
assert S.simplify(S.diff(L1,d)-3*(1-h)*d)==0
assert S.simplify(S.diff(L2,d)-S.Rational(3,2)*(h-1)*(1+d))==0
dstar=(S.sqrt(1+6*h-3*h*h)-1)/3
assert S.simplify((3*dstar*dstar+2*dstar+h*h-2*h).expand())==0
assert S.limit(dstar/h,h,0)==1
qstar=(h-dstar)/2
assert S.limit(qstar/h**2,h,0)==1
opt=S.factor(L1)
bal=S.simplify(opt.subs(d,0))
assert S.limit((opt.subs(d,dstar)/bal),h,0)==2
assert S.simplify(opt-bal-S.Rational(3,2)*(1-h)*d*d)==0
# Verify angular spin-1 density independently by numerical integration in theta:
# d^1_{m,-1} squared equals (cos(theta/2)^4,
#                        2 sin(theta/2)^2 cos(theta/2)^2,
#                        sin(theta/2)^4), m=-1,0,+1.
# Normalized measure (2l+1)/2 sin(theta) dtheta for l=1.
def eigen_analytic(p,q):
    return [3*p-3*p*p+p**3+q**3,3*(p*p+q*q)-2*(p**3+q**3),p**3+3*q-3*q*q+q**3]
def eigen_angular(p,q):
    north=acos(1-2*p)
    south=pi-acos(1-2*q)
    fs=[lambda theta:cos(theta/2)**4,
        lambda theta:2*sin(theta/2)**2*cos(theta/2)**2,
        lambda theta:sin(theta/2)**4]
    return [1.5*(quad(lambda theta:f(theta)*sin(theta),0,north,epsabs=1e-13)[0]
              +quad(lambda theta:f(theta)*sin(theta),south,pi,epsabs=1e-13)[0]) for f in fs]
rng=random.Random(43017)
for _ in range(150):
    hh=rng.uniform(.0001,.9999)
    pp=rng.uniform(0,hh);qq=hh-pp
    aa=eigen_analytic(pp,qq);bb=eigen_angular(pp,qq)
    assert max(abs(a-b) for a,b in zip(aa,bb))<4e-12
for i in range(1,200):
    hh=i/200
    ds=(sqrt(1+6*hh-3*hh*hh)-1)/3
    assert 0<ds<hh
    pp=(hh+ds)/2;qq=(hh-ds)/2
    vals=eigen_analytic(pp,qq)
    assert abs(vals[1]-vals[2])<1e-12
    assert vals[0]>vals[1]
    fopt=min(vals)
    fequal=min(eigen_analytic(hh/2,hh/2))
    assert fopt>fequal
    # Global optimum sampling: verified numerical necessary check, not the proof.
    for j in range(101):
        x=hh*j/100
        assert min(eigen_analytic(x,hh-x))<=fopt+1e-11
print('PASS: exact symbolic identities, 150 independent Wigner-angular quadratures, 199 design-parameter checks, 20099 grid comparisons')
print('Sample h=0.2:',eigen_analytic((.2+(sqrt(1+1.2-.12)-1)/3)/2,(.2-(sqrt(1+1.2-.12)-1)/3)/2))
