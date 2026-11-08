"""Reproduce algebraic and finite-matrix diagnostics for a biased four-cycle.
Requires Python >=3.10, sympy >=1.11, numpy >=1.22.
The mathematical proof of the global transition is given in RESULT.md.
"""
import math
import numpy as np
import sympy as S

k,u=S.symbols('k u', positive=True)
z=S.Symbol('z')
W=S.zeros(4)
for i,bond in enumerate((1,1,1,k)):
    j=(i+1)%4
    W[j,i]+=bond*u
    W[i,i]-=bond*u
    W[i,j]+=bond/u
    W[j,j]-=bond/u
pol=S.Poly(W.charpoly(z).as_expr(),z)
t=u+1/u
expected=S.expand(z*(z**3+(k+3)*t*z**2+(k+1)*(3*t*t-2)*z+(3*k+1)*t*(t*t-2)))
assert S.simplify(pol.as_expr()-expected)==0
print('EXACT: four-state generator characteristic polynomial verified')

c3,c2,c1,_=pol.all_coeffs()[1:]
# For the cubic inside the characteristic polynomial:
a,b,c=[S.factor(q) for q in (c3,c2,c1)]
disc=S.factor(a*a*b*b-4*b**3-4*a**3*c-27*c*c+18*a*b*c)
s=S.Symbol('s', nonnegative=True)
# t^2=4+s, so replace even powers of u with a polynomial identity.
A=(k+3)*S.Symbol('t')
B=(k+1)*(3*S.Symbol('t')**2-2)
C=(3*k+1)*S.Symbol('t')*(S.Symbol('t')**2-2)
Dt=S.expand(A*A*B*B-4*B**3-4*A**3*C-27*C*C+18*A*B*C)
tsym=S.Symbol('t')
Dy=S.Poly(Dt,tsym).all_coeffs()
assert all(i%2==0 or v==0 for i,v in enumerate(reversed(Dy)))
Y=S.Symbol('y')
Dp=sum(S.expand(Dt).coeff(tsym,2*j)*Y**j for j in range(4))
Ds=S.expand(Dp.subs(Y,4+s))
claimed=16*(k-1)**2*(k*k-2*k+2)-4*k*(11*k**3-18*k*k+11*k+12)*s-8*k*k*(3*k*k-10*k+15)*s*s-k*k*(3*k*k-14*k+27)*s**3
assert S.factor(Ds-claimed)==0
assert S.factor(disc-Dt.subs(tsym,t))==0
print('EXACT: discriminant and shifted cubic in s verified')

# Positive coefficients are elementary: the discriminants of their quadratic factors are negative.
assert 18**2-4*11*11<0
assert 10**2-4*3*15<0
assert 14**2-4*3*27<0
assert S.factor(claimed.subs(s,0))==16*(k-1)**2*(k*k-2*k+2)

# Weak and strong bond limits.
q=S.Symbol('q',positive=True)
assert S.limit(S.expand(claimed.subs(s,q*k**S.Rational(-2,3))),k,0,dir='+')==32-27*q**3
strong=S.factor(S.limit(claimed/k**4,k,S.oo))
assert S.factor(strong+(s+4)*(3*s*s+12*s-4))==0
print('EXACT: coefficient positivity witnesses and singular limits verified')


def dval(s,k):
    return 16*(k-1)**2*(k*k-2*k+2)-4*k*(11*k**3-18*k*k+11*k+12)*s-8*k*k*(3*k*k-10*k+15)*s*s-k*k*(3*k*k-14*k+27)*s**3

def threshold(k):
    if k==1: return 0.
    lo,hi=0.,1.
    while dval(hi,k)>0: hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if dval(mid,k)>0: lo=mid
        else: hi=mid
    root=(lo+hi)/2
    return 2*math.asinh(math.sqrt(root)/2)

def matrix(k,f):
    u=math.exp(f/2)
    ret=np.zeros((4,4))
    for i,bond in enumerate((1.,1.,1.,k)):
        j=(i+1)%4
        fw,bw=bond*u,bond/u
        ret[j,i]+=fw;ret[i,i]-=fw
        ret[i,j]+=bw;ret[j,j]-=bw
    return ret

n=0
for kval in (0.025,0.1,0.4,0.75,1.,1.1,2.,4.,10.,100.):
    fc=threshold(kval)
    for delta in (-0.45,-0.1,-0.02,0.02,0.1,0.45):
        f=fc+delta
        if f<0: continue
        roots=np.linalg.eigvals(matrix(kval,f))
        actual=bool(np.max(np.abs(np.imag(roots)))>1e-7)
        assert actual==(f>fc), (kval,f,fc,roots)
        n+=1
print('NUMERIC: %d independent four-by-four spectral classifications agree'%n)

for kval in (0.05,0.5,1,2,10,100):
    fc=threshold(kval)
    assert abs(dval(4*math.sinh(fc/2)**2,kval))<1e-6*max(1,kval**4)
print('NUMERIC: %d threshold substitutions verified'%6)
print('NUMERIC: large-bond threshold',threshold(1e6),'exact limit',math.log(3)/2)
print('VERIFIED')
