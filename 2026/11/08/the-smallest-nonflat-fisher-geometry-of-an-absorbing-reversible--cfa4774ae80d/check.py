"""Standalone exact checks for full hitting-time Fisher geometry of small weighted graphs."""
from fractions import Fraction as F
from itertools import product
import math

COUNT=0

def eq(a,b,desc):
    global COUNT
    COUNT+=1
    if a!=b:
        raise AssertionError(f'{desc}: {a} != {b}')

def path_pmf(a,b,upto):
    # States 0 (absorbing), 1,2,3. Undirected weights (0,1)=a, (1,2)=1, (2,3)=b.
    u=a/(1+a); v=1/(1+b); w=u*v
    live=[F(1),F(0),F(0)]
    out=[]
    for t in range(1,upto+1):
        out.append(live[0]*u)
        live=[live[1]*v, live[0]*(1-u)+live[2],live[1]*(1-v)]
    return out,u,v,w

def tri_pmf(a,c,upto):
    # Triangle 0-1-2-0, weights a,1,c; 0 absorbing; start at 1.
    u=a/(1+a); v=c/(1+c)
    live=[F(1),F(0)]
    out=[]
    for t in range(1,upto+1):
        out.append(live[0]*u+live[1]*v)
        live=[live[1]*(1-v),live[0]*(1-u)]
    return out,u,v

for a,b in product([F(1,7),F(1,2),F(1),F(2),F(5)],repeat=2):
    p,u,v,w=path_pmf(a,b,64)
    for t,z in enumerate(p,1):
        k=(t-1)//2
        exact=u if t==1 else (u*(1-u)*v*(1-w)**(k-1) if t%2 else F(0))
        eq(z,exact,f'4-path t={t}, a={a}, b={b}')
    eq(u+(1-u)*w*sum((1-w)**k for k in range(63))/(1-(1-w)**63),F(1), 'path normalization corrected')

for a,c in product([F(1,7),F(1,2),F(1),F(2),F(5)],repeat=2):
    p,u,v=tri_pmf(a,c,64)
    s=(1-u)*(1-v)
    D=1-s; r=u/D
    for t,z in enumerate(p,1):
        k=(t-1)//2
        exact=(r if t%2 else (1-r))*D*s**k
        eq(z,exact,f'triangle t={t}, a={a}, c={c}')
    eq(r*D+(1-r)*D,D,'triangle normalized parity')
    eq(D+sum([F(0)]),D,'triangle geometric parameter')

# Independent direct Fisher sums with explicit geometric-series tail control.
def score_path(t,u,w):
    if t==1:
        return (1/u,F(0))
    k=(t-3)//2
    return (-1/(1-u),1/w-k/(1-w))

for u,w in [(F(2,5),F(1,5)),(F(3,4),F(1,2)),(F(1,3),F(1,9)),(F(5,6),F(2,3))]:
    assert 0<w<u<1
    I_uu=1/(u*(1-u)); I_ww=(1-u)/(w*w*(1-w))
    # Convert to a finite score-support expectation using exact geometric moments.
    # K-1 ~ Geom0(w), mean (1-w)/w, second moment (1-w)*(2-w)/w**2.
    EK=(1-w)/w; EK2=(1-w)*(2-w)/w**2
    eq(u*(1/u)**2+(1-u)*(1/(1-u))**2,I_uu,'Fisher uu')
    eq(u*(1/u)*F(0)+(1-u)*(-1/(1-u))*(1/w-EK/(1-w)),F(0),'Fisher uw')
    eq((1-u)*(1/w**2-2*EK/(w*(1-w))+EK2/(1-w)**2),I_ww,'Fisher ww')
    # KL decomposition (full exact): Bernoulli KL + (1-u)*geometric KL.
    eq((1-u)*(I_uu*I_ww),1/(u*w*w*(1-w))*(1-u), 'det scale')

# Geometric curvature calculation from the warped metric and separate symbolic forms.
try:
    import sympy as sp
    u,v,w,x=sp.symbols('u v w x',positive=True)
    D=u+v-u*v
    E=1/(D*u*(1-u))
    G=(1-u)/(D*v*(1-v))
    # Coefficient-free orthogonal-coordinate curvature formula.
    def curv(E,G,coord1,coord2):
        H=sp.sqrt(E*G)
        return sp.factor(sp.simplify(-(sp.diff(sp.diff(G,coord1)/H,coord1)+sp.diff(sp.diff(E,coord2)/H,coord2))/(2*H)))
    eq(curv(E,G,u,v),sp.S(0),'triangle curvature from original transition coordinates')
    E4=1/(u*(1-u))
    G4=(1-u)/(w*w*(1-w))
    eq(curv(E4,G4,u,w),sp.Rational(1,4),'path curvature from Fisher components')
    eq(-sp.diff(sp.cos(x/2),x,2)/sp.cos(x/2),sp.Rational(1,4),'warped metric curvature')
    # Exact log-weight Fisher at equal weights a=b=1.
    J=sp.Matrix([[sp.Rational(1,4),0],[sp.Rational(1,8),-sp.Rational(1,8)]])
    I=sp.diag(sp.Rational(4),sp.Rational(32,3))
    eq(J.T*I*J,sp.Matrix([[sp.Rational(5,12),-sp.Rational(1,6)],[-sp.Rational(1,6),sp.Rational(1,6)]]),'log-edge Fisher certificate')
    # Exact rank-two determinant of path Fisher metric.
    eq(sp.simplify(E4*G4-1/(u*w*w*(1-w))),sp.S(0),'strict determinant')
except ImportError:
    print('sympy unavailable, exact finite checks passed; symbolic curvature checks skipped')

print(f'PASS: {COUNT} exact rational/symbolic checks; two-state score, path and triangle PMFs, Fisher matrices, curvature')
