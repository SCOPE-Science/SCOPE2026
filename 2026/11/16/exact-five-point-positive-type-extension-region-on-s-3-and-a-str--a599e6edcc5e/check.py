"""Direct finite-group and rational certificates for a five-point S3 positive-type extension theorem.

Run with Python 3 and numpy. Infinite/continuous statements rely on the proof, not sampling.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt
import numpy as np

G=[(k,e) for k in range(3) for e in (0,1)]
def mul(x,y): return ((x[0]+(-1 if x[1] else 1)*y[0])%3,(x[1]+y[1])%2)
def inv(x): return (((-1 if x[1]==0 else 1)*x[0])%3,x[1])
def quotient(x,y): return mul(inv(x),y)
e=(0,0);s=(0,1);t=(2,1);r=(1,0);ri=(2,0);h=(1,1)
assert mul(s,t)==r and mul(t,s)==ri
D={e,s,t,r,ri}
cliques=[C for k in range(1,7) for C in combinations(G,k) if all(quotient(a,b) in D for a in C for b in C)]
tri=[C for C in cliques if len(C)==3]
assert len(tri)==8 and max(map(len,cliques))==3
classes={}
for C in tri:
    vals=[]
    for x,y in combinations(C,2):
        d=quotient(x,y)
        vals.append('a' if d==s else 'b' if d==t else 'c')
    pattern=''.join(sorted(vals))
    classes[pattern]=classes.get(pattern,0)+1
assert classes=={'abc':6,'ccc':2},classes

# Rational witness; every local 3x3 determinant is nonnegative.
a=b=F(11,16);c=F(0)
def values(x):
    return F(1) if x==e else a if x==s else b if x==t else c if x in (r,ri) else None
assert 1 + 2*a*b*c-a*a-b*b-c*c==F(7,128)
for C in cliques:
    M=np.array([[float(values(quotient(x,y))) for y in C] for x in C])
    assert np.linalg.eigvalsh(M)[0]>-1e-12
# Exhaustive rational missing-coordinate contradiction at a=b=11/16,c=0.
# Character blocks demand x <= -(a+b)+(1+2c), and x >= (a+b-2(1-c))/2.
left_upper=-(a+b)+(1+2*c)
right_lower=(a+b-2*(1-c))/2
assert right_lower==F(-5,16) and left_upper==F(-3,8)
assert right_lower-left_upper==F(1,16)

S=np.array([[1.,0.],[0.,-1.]])
T=np.array([[-.5,sqrt(3)/2],[sqrt(3)/2,.5]])
U=-S-T
I=np.eye(2)
assert np.max(np.abs(S@T + T@S + I))<1e-14
rng=np.random.default_rng(8147)
checked=0
for _ in range(450):
    # random state weights and real standard representation density
    weights=rng.dirichlet([1.,1.,2.])
    x,y=rng.normal(size=2);x,y=(x,y)/(1+np.hypot(x,y))
    phi0=np.array([x, -.5*x+sqrt(3)*y/2, -.5*x-sqrt(3)*y/2])
    a,b,d=weights[0]-weights[1]+weights[2]*phi0
    c=weights[0]+weights[1]-.5*weights[2]
    assert abs((a+b+d)-3*(weights[0]-weights[1]))<1e-10
    # two scalar Fourier coefficients and standard block inequalities
    c1=1+2*c+(a+b+d)
    c2=1+2*c-(a+b+d)
    block=(1-c)*I+(a-d)*S+(b-d)*T
    assert c1>-1e-10 and c2>-1e-10 and np.linalg.eigvalsh(block)[0]>-1e-10
    lhs=max(abs(a+b)-2*(1+2*c)/3,0)**2+(a-b)**2/3
    rhs=(2*(1-c)/3)**2
    assert lhs<=rhs+1e-10
    # Fourier reconstruction: 6x6 positive semidefinite Cayley matrix
    vv={e:1.,s:a,t:b,r:c,ri:c,h:d}
    mat=np.array([[vv[quotient(X,Y)] for Y in G] for X in G])
    assert np.linalg.eigvalsh(mat)[0]>-1e-10
    checked+=1

# For random admissible abc local candidate, exact global region equivalence to missing-real-value interval.
for _ in range(650):
    c=rng.uniform(-.5,1.)
    a,b=rng.uniform(-1.,1.,size=2)
    p=2*(1-c)/3;q=(1+2*c)/3
    dist=max(abs(a+b)-2*q,0)
    global_ok=dist*dist+(a-b)**2/3<=p*p+1e-12
    rad=4*(1-c)**2-3*(a-b)**2
    if rad>=0:
        lo1=-(a+b)-(1+2*c);hi1=-(a+b)+(1+2*c)
        lo2=(a+b-sqrt(rad))/2;hi2=(a+b+sqrt(rad))/2
        interval_ok=max(lo1,lo2)<=min(hi1,hi2)+1e-12
    else: interval_ok=False
    assert global_ok==interval_ok,(a,b,c,global_ok,interval_ok)
    checked+=1

# gap formula and strictness across internal c
for c in [F(-2,5),F(0),F(1,2),F(99,100)]:
    difference=(1+c)/2-((2+c)/3)**2
    assert difference==(1-c)*(1+2*c)/18 and difference>0
print('PASS: 8 maximal cliques (6 abc, 2 ccc), exact rational local nonglobal witness, 1100 random state/interval validations, 4 strict-gap identities')
