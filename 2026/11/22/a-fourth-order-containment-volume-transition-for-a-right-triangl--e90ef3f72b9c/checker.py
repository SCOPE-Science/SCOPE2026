"""Exact vertex stratification and independent scalar checks for a triangle-rectangle containment polytope.

The geometric input is T=conv((0,0),(1,0),(0,1)), Q=[0,R]x[0,1].
Transformation coordinates are (s,t,u,v): (x,y)->(sx-ty+u,tx+sy+v).
This program uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations

ZERO, ONE = F(0), F(1)
T = ((0,0),(1,0),(0,1))
# A*x <= b0 + R*b1.
rows=[]
for x,y in T:
    rows.extend((
        ((-x, y, -1, 0), 0, 0),
        (( x,-y,  1, 0), 0, 1),
        ((-y,-x,  0,-1), 0, 0),
        (( y, x,  0, 1), 1, 0),
    ))

def solve(mat, rhs):
    a=[[F(z) for z in r]+[F(rhs[i])] for i,r in enumerate(mat)]
    n=len(a)
    for c in range(n):
        pivot=next((i for i in range(c,n) if a[i][c]),None)
        if pivot is None: return None
        a[c],a[pivot]=a[pivot],a[c]
        d=a[c][c];a[c]=[z/d for z in a[c]]
        for i in range(n):
            if i!=c:
                d=a[i][c]
                if d:a[i]=[z-d*y for z,y in zip(a[i],a[c])]
    return tuple(a[i][-1] for i in range(n))

def feasible_interval(z0,z1):
    lo,hi=ONE,None
    for a,b0,b1 in rows:
        q=F(b0)-sum(F(x)*y for x,y in zip(a,z0))
        p=F(b1)-sum(F(x)*y for x,y in zip(a,z1))
        # q + p R >= 0
        if p>0:lo=max(lo,-q/p)
        elif p<0:
            cap=-q/p;hi=cap if hi is None else min(hi,cap)
        elif q<0:return None
    return (lo,hi) if hi is None or lo<=hi else None

candidates=[]
for subset in combinations(range(len(rows)),4):
    mat=[rows[i][0] for i in subset]
    z0=solve(mat,[rows[i][1] for i in subset])
    if z0 is None:continue
    z1=solve(mat,[rows[i][2] for i in subset])
    interval=feasible_interval(z0,z1)
    if interval is not None:candidates.append((z0,z1,*interval))

def vertices(R):
    R=F(R)
    return {tuple(a+R*b for a,b in zip(z0,z1)) for z0,z1,lo,hi in candidates
            if lo<=R and (hi is None or R<=hi)}

# Every 4D vertex has at least 4 independent active inequalities. Thus
# the enumeration below is exhaustive, including nonsimple vertices.
breaks={ONE}
for z0,z1,lo,hi in candidates:
    breaks.add(lo)
    if hi is not None:breaks.add(hi)
assert breaks=={ONE,F(2)}, ('Unexpected combinatorial breakpoint', breaks)
assert [len(vertices(x)) for x in (ONE,F(3,2),F(2),F(3))]==[12,20,16,18]
# Check distinct affine candidates on each entire interval, not numerical samples.
for left,right,expected in [(ONE,F(2),20),(F(2),None,18)]:
    active={(z0,z1) for z0,z1,lo,hi in candidates
            if lo<=left and (right is None and hi is None or right is not None and (hi is None or hi>=right))
            and (lo < right if right is not None else True)}
    # Boundary-only candidates are deliberately excluded.
    assert len(active)==expected, (left,right,len(active))

def J(A,B):
    A,B=F(A),F(B)
    if B<=A/2:return B**3*(4*A-3*B)/12
    if B<=A:return (A**4-8*A**3*B+24*A*A*B*B-16*A*B**3+4*B**4)/48
    return A**3*(8*B-3*A)/48

def volume(R):
    R=F(R)
    return 2*(J(R,ONE)+J(ONE,R))

def closed_form(R):
    R=F(R)
    if R<1:return R**4*closed_form(1/R)
    return R-F(5,8)+max(ZERO,F(2)-R)**4/24

# Each piece has degree <= 4, so five distinct rational identities on each
# of the four open aspect intervals prove each complete polynomial identity.
regimes = (
    (F(1,8),F(1,6),F(1,5),F(1,4),F(1,3)),
    (F(3,5),F(2,3),F(3,4),F(4,5),F(9,10)),
    (F(11,10),F(6,5),F(4,3),F(3,2),F(9,5)),
    (F(5,2),F(3),F(4),F(6),F(10)),
)
for regime in regimes:
    assert all(volume(R)==closed_form(R) for R in regime)
for R in (F(1,2),ONE,F(2)):
    assert volume(R)==closed_form(R)
print('PASS: all 495 candidate hyperplane quartets enumerated exactly.')
print('PASS: only aspect transitions R=1 and R=2 on R>=1.')
print('PASS: vertex counts 12,20,16,18 in the four regimes.')
print('PASS: exact degree-at-most-four volume polynomials certified by rational interpolation.')
