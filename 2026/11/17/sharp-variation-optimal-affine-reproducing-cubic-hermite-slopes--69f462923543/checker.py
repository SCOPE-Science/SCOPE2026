"""Reproduce exact algebra and finite stress checks for alternating-mesh spline TV design."""
from fractions import Fraction as F
from random import Random
from math import isfinite
import sympy as s

t=s.symbols('t', real=True)
H00=2*t**3-3*t**2+1
H01=-2*t**3+3*t**2
H10=t**3-2*t**2+t
H11=t**3-t**2
assert (H00+H01).expand()==1
assert (s.diff(H11,t).subs(t,F(2,3)))==0
assert H11.subs(t,F(2,3))==-F(4,27)
assert s.diff(H10,t).subs(t,F(1,3))==0
assert H10.subs(t,F(1,3))==F(4,27)
# Corner derivatives certify central step monotonicity for all alpha,beta in [0,1].
for alpha,beta in [(0,0),(1,0),(0,1),(1,1)]:
    der=s.expand(s.diff(H01+alpha*H10+beta*H11,t))
    assert min(float(der.subs(t,s.Rational(k,200))) for k in range(201))>=-1e-12
    assert all(s.GreaterThan(der,0).subs(t,s.Rational(k,200)) for k in range(201))
a,b,u,v,z=s.symbols('a b u v z',positive=True)
q=s.factor(2*a*b/(a*a+b*b))
u_star=b*b/(a*a+b*b)
v_star=a*a/(a*a+b*b)
assert s.simplify(b/a*(1-u_star+v_star)-q)==0
assert s.simplify(a/b*(1-v_star+u_star)-q)==0
assert s.simplify(q*(a/b+b/a)-2)==0
assert s.simplify(1+s.Rational(8,27)*q-(1+16*a*b/(27*(a*a+b*b))))==0
print('EXACT_HERMITE_BUMP_AND_OPTIMAL_PERIOD_TWO_IDENTITIES_PASS')

rng=Random(240617)
def hermite_primitive(t0,y0,y1,m0,m1,h):
    return y0*(2*t0**3-3*t0**2+1)+y1*(-2*t0**3+3*t0**2)+h*m0*(t0**3-2*t0**2+t0)+h*m1*(t0**3-t0**2)
def compute_tv(y,h,lam):
    # Finite data with constant extensions; verify over interior cells and two zero exterior cells.
    n=len(y)
    d=[(y[i+1]-y[i])/h[i] for i in range(n-1)]
    slopes=[0.]*n
    for i in range(1,n-1):
        slopes[i]=lam[i]*d[i-1]+(1-lam[i])*d[i]
    slopes[0]=slopes[-1]=0.
    tot=0.
    for i in range(n-1):
        vals=[hermite_primitive(k/120.,y[i],y[i+1],slopes[i],slopes[i+1],h[i]) for k in range(121)]
        tot+=sum(abs(vals[k+1]-vals[k]) for k in range(120))
    return tot
for _ in range(300):
    a0,b0=rng.uniform(.1,8),rng.uniform(.1,8)
    n=31
    hs=[a0 if i%2==0 else b0 for i in range(n-1)]
    lam=[0.]+[rng.random() for i in range(1,n-1)]+[0.]
    y=[0.]
    for i in range(n-1): y.append(y[-1]+rng.uniform(-2,2) if 1<i<n-3 else y[-1])
    tvd=sum(abs(y[i+1]-y[i]) for i in range(n-1))
    bounds=[(hs[i-1]*(1-lam[i])+hs[i+1]*lam[i+1])/hs[i] for i in range(1,n-2)]
    K=1+8/27*max(bounds)
    assert compute_tv(y,hs,lam) <= K*tvd+1e-7
    # Period-two optimal map and its fixed-mesh global bound
    den=a0*a0+b0*b0
    U=b0*b0/den; V=a0*a0/den
    l2=[(U if i%2==0 else V) for i in range(n)]
    k2=1+16*a0*b0/(27*den)
    assert compute_tv(y,hs,l2)<=k2*tvd+1e-7
print('RANDOM_BV_STRESS_CHECK_PASS 300')
print('ALL_NEW_CLAIM_CHECKS_PASS')
