"""Independent exact sign-cell and numerical integration checks for triangular-prism central sections.

Run: python verify_prism.py. This is finite corroboration; the unrestricted proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import asin, cos, pi, sin, sqrt, isclose
from scipy.integrate import quad
from scipy.optimize import brentq

# An algebraic real is represented as p+q*sqrt(3), using exact rationals.
def alg(p=0, q=0):
    return F(p), F(q)

def sign(z):
    p, q = z
    if p == 0: return (q > 0) - (q < 0)
    if q == 0: return (p > 0) - (p < 0)
    if (p > 0) == (q > 0): return (p > 0) - (p < 0)
    diff = p*p - 3*q*q
    if diff == 0: return 0
    return (1 if p > 0 else -1) * (1 if diff > 0 else -1)

def sub(a, b): return a[0]-b[0], a[1]-b[1]
def negative(a): return -a[0], -a[1]
def absalg(a): return a if sign(a)>0 else negative(a)

def count_cut(a, b, c, H):
    # Dot products with the six actual vertices, multiplied by 2*sqrt(3).
    z=[alg(2*a, 0), alg(-a,b), alg(-a,-b)]
    lift=alg(0,F(H)*c)
    top=[sign((v[0]+lift[0],v[1]+lift[1])) for v in z]
    bottom=[sign(sub(v,lift)) for v in z]
    if 0 in top+bottom: return None, None
    edges=[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]
    s=top+bottom
    actual=sum(s[i]!=s[j] for i,j in edges)
    # Independent classification by horizontal dot values and vertical threshold.
    v=sorted((absalg(e) for e in z),key=lambda t:float(t[0])+float(t[1])*sqrt(3))
    threshold=absalg(lift)
    comparison1=sign(sub(threshold,v[0]))
    comparison2=sign(sub(threshold,v[1]))
    comparison3=sign(sub(threshold,v[2]))
    if 0 in (comparison1,comparison2,comparison3): return None, None
    predicted=4 if comparison1<0 else 5 if comparison2<0 else 4 if comparison3<0 else 3
    return actual, predicted

def formulas(H):
    q=2/sqrt(4+3*H*H)
    A=asin(q/2)
    B=asin(sqrt(3)*q/2)
    C=asin(q)
    p3=1-6*A/pi
    p5=6*(2*B-A-C)/pi
    return p3, 1-p3-p5, p5

def sphere_angular_integrals(H):
    R=1/sqrt(3)
    def T(m):return 2*R*m/sqrt(H*H+4*R*R*m*m)
    p3=1-(6/pi)*quad(lambda th:T(cos(th)),0,pi/6,epsabs=2e-13)[0]
    p5=(6/pi)*quad(lambda th:T(cos(th-pi/3))-T(cos(th+pi/3)),0,pi/6,epsabs=2e-13)[0]
    return p3,1-p3-p5,p5

def root_eq(q):
    return sqrt(3)/sqrt(1-3*q*q/4)-.5/sqrt(1-q*q/4)-1/sqrt(1-q*q)

checks=0
for H in (F(1,3),F(1,2),F(1),F(3,2),F(2),F(3)):
    counts={3:0,4:0,5:0}
    for a in range(-7,8):
      for b in range(-7,8):
        for c in range(-7,8):
          if a==b==c==0:continue
          actual,pred=count_cut(a,b,c,H)
          if actual is None:continue
          assert actual==pred,(H,a,b,c,actual,pred)
          assert actual in counts
          counts[actual]+=1
          checks+=2
    assert all(counts[k]>0 for k in counts), (H,counts)
    checks+=1

for H in (.001,.09,.25,.5,.6136881767448,.8,1,1.7,3,10,100):
    p=formulas(H); q=sphere_angular_integrals(H)
    for j in range(3):
        assert abs(p[j]-q[j])<3e-12, (H,p,q)
        assert 0<=p[j]<=1
        checks+=2
    assert abs(sum(p)-1)<2e-15
    checks+=1

qstar=brentq(root_eq,.001,.999)
hstar=sqrt((4/qstar**2-4)/3)
assert .6136<hstar<.6138
assert .3851<formulas(hstar)[2]<.3852
checks+=2
for h in (.03,.1,.3,.5,.614,1,1.5,3,10,100):
    if h<hstar:
        assert formulas(h)[2]<formulas(hstar)[2]
    else:
        assert formulas(h)[2]<formulas(hstar)[2]
    checks+=1
print('PASS:',checks,'exact sign-cell / quadrature / extremizer checks; h*=',format(hstar,'.14f'))
