"""Exact integer/rational checks for the four-mode Fourier fourth-moment theorem.
Run: python3 check.py (Python standard library only)."""
from fractions import Fraction
from itertools import product
import cmath

def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):z[i+j]+=v*w
    return z

def deriv(a):return [(i+1)*a[i+1] for i in range(len(a)-1)]
P=[3,0,12,4,3]
g=[-3,-3,3,1]
left=add(mul(deriv(P),[1,0,1]),[-4*v for v in mul([0,1],P)])
right=[-4*v for v in mul([0,1],g)]
assert left[:len(right)]==right and all(v==0 for v in left[len(right):]),(left,right)
lo,hi=Fraction(1261802,10**6),Fraction(1261803,10**6)
gf=lambda x:x**3+3*x**2-3*x-3
Mf=lambda x:(3*x**4+4*x**3+12*x*x+3)/(2*(1+x*x)**2)
assert gf(lo)<0<gf(hi)
assert Fraction(28,10)<Mf(lo)<Fraction(281,100)

def abs2(z):return z.real*z.real+z.imag*z.imag
count=0
for coeffs in product([-2,-1,0,1,2], repeat=4):
    if coeffs==(0,0,0,0):continue
    s=sum(x*x for x in coeffs)
    r=[sum(coeffs[j+k]*coeffs[j] for j in range(4-k)) for k in range(1,4)]
    conv=[sum(coeffs[i]*coeffs[k-i] for i in range(4) if 0<=k-i<4) for k in range(7)]
    assert sum(x*x for x in conv)==s*s+2*sum(x*x for x in r)
    a,b,c,d=map(abs,coeffs)
    A2=Fraction(a*a+d*d,2);B2=Fraction(b*b+c*c,2)
    assert (a*b+c*d)**2 <= (a*a+d*d)*(b*b+c*c)
    assert (a*c+b*d)**2 <= (a*a+d*d)*(b*b+c*c)
    assert 2*b*c <= b*b+c*c
    assert 2*a*d<=a*a+d*d
    count+=1
for N in [7,8,9,11,15]:
    v=[complex(.7, .2),complex(-.3,.6),complex(.1,-.7),complex(.2,.4)]
    conv=[sum(v[i]*v[k-i] for i in range(4) if 0<=k-i<4) for k in range(7)]
    exact=sum(abs2(x) for x in conv)
    sample=sum(abs2(sum(v[j]*cmath.exp(2j*cmath.pi*j*k/N) for j in range(4)))**2 for k in range(N))/N
    assert abs(exact-sample)<1e-8,(N,exact,sample)
print('VERIFY_OK derivative_polynomial=PASS root_rational_bracket=PASS integer_coeff_vectors=',count,'cyclic_quadrature_N=7,8,9,11,15 PASS')
