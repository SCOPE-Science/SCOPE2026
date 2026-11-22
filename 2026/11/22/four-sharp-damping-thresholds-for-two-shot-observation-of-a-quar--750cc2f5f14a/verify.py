"""Reproduce exact polynomial checks and finite numerical confirmations.

This checks a proved two-observation Gramian theorem.  Finite tests are
supplemental; all-integer-lag optimality is derived analytically.
Run: python3 verify.py
"""
from fractions import Fraction as F
from math import sqrt, cos, sin, pi, isclose


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z

def sub(a,b):
    n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n)]

def at(a,x):
    y=0
    for c in reversed(a): y=y*x+c
    return y

def bisect(poly,lo,hi,n=100):
    lo=float(lo);hi=float(hi);v=at(poly,lo)
    assert v*at(poly,hi)<0
    for _ in range(n):
        m=(lo+hi)/2
        if at(poly,m)*v>0:lo=m
        else:hi=m
    return (lo+hi)/2

# Exact polynomial eliminations, including nonzero factor q in E and K.
qE=[F(1),-2,-2,2]
qK=[F(1),-2,-2,-2,1]
qA=[F(-1),2,1]
assert sub(mul([1,1,-2], [1,1,-2]),[1,0,1]) == mul([0,2],qE)
assert sub(mul([1,0,1],[1,0,1]),mul([0,2],[1,2,1])) == qK
assert sub(mul([0,2],[1,1]),[1,0,1]) == qA
qk=bisect(qK,F(34,100),F(35,100))
qe=bisect(qE,F(40,100),F(41,100))
qa=sqrt(2)-1
qd=.5
assert qk<qe<qa<qd
assert isclose(qk,((1+sqrt(5))-sqrt((1+sqrt(5))**2-4))/2,rel_tol=1e-12)


def metrics(q,j):
    # Gramian of observations at 0 and j, q=rho**2.
    t=q**j
    s2=sin(pi*j/4)**2
    tr=1+t
    det=t*s2
    if det<1e-13: return (0.,float('inf'),0.,float('inf'),tr)
    disc=sqrt(max(0.,tr**2-4*det))
    emin=(tr-disc)/2
    emax=(tr+disc)/2
    return emin, tr/det, det, emax/emin, tr

checks=0
for q in [.001,.03,.1,.2,.3,.34,.35,.39,.4,.41,.42,.45,.49,.51,.6,.8,.95,.999]:
    rows=[(j,metrics(q,j)) for j in range(1,65)]
    k=(2 if q>qk else 1)
    e=(2 if q>qe else 1)
    a=(2 if q>qa else 1)
    d=(2 if q>qd else 1)
    assert all(rows[k-1][1][3]<=v[3]+1e-8 for _,v in rows if v[3]!=float('inf'))
    assert all(rows[e-1][1][0]+1e-8>=v[0] for _,v in rows)
    assert all(rows[a-1][1][1]<=v[1]+1e-8 for _,v in rows)
    assert all(rows[d-1][1][2]+1e-8>=v[2] for _,v in rows)
    assert all(rows[0][1][4]>v[4] for _,v in rows[1:])
    checks+=65*5

# Direct matrix construction, using independently computed row directions.
for rho in [.17,.5,.7,.95]:
    q=rho*rho
    for s in range(0,7):
        for d in range(1,21):
            p=[]
            for j in [s,s+d]:
                z=rho**j
                p.append((z*cos(j*pi/4),-z*sin(j*pi/4)))
            a=p[0][0]**2+p[1][0]**2
            b=p[0][0]*p[0][1]+p[1][0]*p[1][1]
            c=p[0][1]**2+p[1][1]**2
            tr=a+c
            det=a*c-b*b
            target=q**(2*s+d)*(sin(d*pi/4)**2)
            assert abs(tr-q**s*(1+q**d))<1e-10
            assert abs(det-target)<1e-10
            checks+=2

print('VERIFICATION_OK')
print(f'thresholds: condition={qk:.15f}, E={qe:.15f}, A={qa:.15f}, D={qd:.15f}')
print('supplementary comparisons:',checks)
