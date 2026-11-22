#!/usr/bin/env python3
"""Exact-rational and integer certificate for three-sample Fourier stability at order 25."""
from fractions import Fraction as F
from math import factorial, gcd
from itertools import combinations

N=25
D=10**9
EPS=F(1,10**6)
K=40

def atan_trunc(q):
    return sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(K)),F(0))

pi_approx=16*atan_trunc(5)-4*atan_trunc(239)
pi_error=F(16,(2*K+1)*5**(2*K+1))+F(4,(2*K+1)*239**(2*K+1))
assert pi_error<F(1,10**50)
assert 3<pi_approx-pi_error and pi_approx+pi_error<F(22,7)
maxx=F(22,7)
T=20
# Alternating series remainders, valid since successive terms decrease from index T at |x| <=22/7.
assert maxx**(2*T)/factorial(2*T)<F(1,10**18)
assert maxx**(2*T+1)/factorial(2*T+1)<F(1,10**18)

def sinecosine(t):
    x=F(2*t,25)*pi_approx
    s=sum(((-1)**j*x**(2*j+1)/factorial(2*j+1) for j in range(T)),F(0))
    c=sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(T)),F(0))
    return s,c

def rnd(x):
    return (2*x.numerator+x.denominator)//(2*x.denominator) if x>=0 else -rnd(-x)

roots=[]
for j in range(N):
    t=j if j<=N//2 else N-j
    s,c=sinecosine(t)
    roots.append((rnd(D*c),rnd(D*(s if j<=N//2 else -s))))
assert roots[0]==(D,0)
# The true ζ^j differs from the rounded Gaussian integer divided by D by < 10^(-9).
# Proof: each component has error <=1/(2D) + 1e-18 + 2π-error,
# and sqrt(2) < 3/2 yields total error <1/D.
assert F(3,2)*(F(1,2*D)+F(1,10**18)+2*pi_error)<F(1,D)

def zsum(R,C,u,v):
    a=b=0
    for c in C:
        x,y=roots[((R[u]-R[v])*c)%N]
        a+=x; b+=y
    return a,b

def det3(H,C,shift):
    """Leading minors of H - shift I, integer H=D F F*"""
    d=3*D-shift
    z01=zsum(H,C,0,1)
    z02=zsum(H,C,0,2)
    z12=zsum(H,C,1,2)
    sq=lambda z:z[0]*z[0]+z[1]*z[1]
    A,B=z01; Cx,Dy=z12; E,Fy=z02
    prodreal=(A*Cx-B*Dy)*E+(A*Dy+B*Cx)*Fy
    return d, d*d-sq(z01), d**3-d*(sq(z01)+sq(z02)+sq(z12))+2*prodreal

def make_c_reps():
    seen=set();reps=[]
    for C in combinations(range(N),3):
        if C in seen:continue
        orbit={tuple(sorted(((c+t)%N for c in C))) for t in range(N)}
        seen|=orbit; reps.append((C,len(orbit)))
    assert len(reps)==92 and len(seen)==2300
    assert all(o==25 for C,o in reps)
    return [c for c,o in reps]

creps=make_c_reps()
ALLR=list(combinations(range(N),3))
seen=set();row_reps=[]
for R in ALLR:
    if R in seen: continue
    O={tuple(sorted(((a*r+b)%N for r in R))) for a in range(N) if gcd(a,N)==1 for b in range(N)}
    seen|=O
    row_reps.append((R,len(O),len({r%5 for r in R})==3))
assert len(seen)==2300
assert row_reps==[
    ((0,1,2),250,True),((0,1,3),500,True),((0,1,4),500,True),
    ((0,1,5),500,False),((0,1,10),500,False),((0,5,10),50,False)]
print('exact affine row orbit classification:',row_reps)

# For each universal row orbit, only 25 translated consecutive column triples are extremal.
# Candidate consecutive C0 and all 91 other translation classes are tested separately.
thresholds={2:F(1,1000),3:F(1,250),4:F(1,100)}
intervals={2:(F(44,100000),F(50,100000)),
           3:(F(17,10000),F(18,10000)),
           4:(F(39,10000),F(40,10000))}
for k in (2,3,4):
    R=(0,1,k)
    t=thresholds[k]
    sh=int(D*(t+EPS)); neg=int(D*(t-EPS))
    assert F(sh,D)==t+EPS and F(neg,D)==t-EPS
    reps_count=0; min1=min2=min3=None
    for C in creps:
        if C==(0,1,2):continue
        v=det3(R,C,sh)
        assert all(s>0 for s in v),('nonconsecutive not PD',k,C,v)
        min1=v[0] if min1 is None else min(min1,v[0])
        min2=v[1] if min2 is None else min(min2,v[1])
        min3=v[2] if min3 is None else min(min3,v[2])
        reps_count+=1
    assert reps_count==91
    w=det3(R,(0,1,2),neg)
    assert w[2]<0 and w[0]>0 and w[1]>0,('consecutive not negative det',k,w)
    lower,upper=intervals[k]
    q=det3(R,(0,1,2),int(D*(lower+EPS)))
    assert all(x>0 for x in q),('lower interval failed',k,q)
    u=det3(R,(0,1,2),int(D*(upper-EPS)))
    assert u[2]<0 and u[0]>0 and u[1]>0,('upper interval failed',k,u)
    print('k=',k,'nonconsecutive classes=',reps_count,
          'threshold=',str(t),'consecutive strictly below, all other classes strictly above',
          'worst bound interval=',(str(lower),str(upper)),
          'smallest certified nonconsecutive leading determinant=',min3)

# Explicit singular minor whenever at least two selected row indices coincide mod 5.
# At columns C=(0,5,10), the corresponding rows of the true Fourier restriction coincide.
print('PASS: 6 exhaustive affine row orbits; 92 exhaustive column-translation classes; exact rational root bounds; all required integer determinant signs')
