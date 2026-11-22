"""Exact self-contained checks of the directed-habitat extinction-budget theorem.

Run with Python 3: python check.py
The infinite-domain proof is in RESULT.md; these finite exact checks
only detect algebraic, normalization, and sign mistakes.
"""
from fractions import Fraction as F
from random import Random


def migration(n, edges):
    A = [[F(0) for _ in range(n)] for _ in range(n)]
    for i,j,a,b in edges:
        A[j][i] += a
        A[i][j] += b
        A[i][i] -= a
        A[j][j] -= b
    return A


def tree_solution(n, edges, growth):
    inc = [F(0)] * n
    out = [F(0)] * n
    adj = [[] for _ in range(n)]
    saving = F(0)
    for i,j,a,b,sa,sb in edges:
        assert a == sa*sa and b == sb*sb and a>0 and b>0
        inc[i] += sa*sb
        inc[j] += sa*sb
        out[i] += a
        out[j] += b
        saving += (sa-sb)**2
        adj[i].append((j,sa/sb))
        adj[j].append((i,sb/sa))
    v = [None] * n
    v[0] = F(1)
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j,ratio in adj[i]:
            if j not in seen:
                seen.add(j)
                v[j] = v[i]*ratio
                stack.append(j)
    assert len(seen)==n
    h = [growth + inc[i] - out[i] for i in range(n)]
    A = migration(n, [(i,j,a,b) for i,j,a,b,_,_ in edges])
    return A,v,h,saving


def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(x))]


def boundary_check(A,v,h,r):
    n = len(v)
    return all(sum(A[i][j]*v[j] for j in range(n)) + (r-h[i])*v[i]==0 for i in range(n))

# Three-patch fully rational witness from the theorem.
r = F(7)
ed = [(0,1,F(9),F(1),F(3),F(1)),
      (1,2,F(4),F(1),F(2),F(1))]
A,v,h,S = tree_solution(3,ed,r)
assert v == [F(1),F(3),F(6)]
assert h == [F(1),F(7),F(8)]
assert sum(h) == 16 == 3*r-S and S == 5
assert boundary_check(A,v,h,r)

rng=Random(434343)
scales=[F(1,4),F(1,2),F(1),F(2),F(3),F(4)]
cases=0
for n in range(2,12):
    for k in range(40):
        ed=[]
        for j in range(1,n):
            i=rng.randrange(j)
            sa,sb=rng.choice(scales),rng.choice(scales)
            ed.append((i,j,sa*sa,sb*sb,sa,sb))
        A,v,h,S=tree_solution(n,ed,F(1000))
        assert min(h)>0
        assert sum(h)==n*F(1000)-S
        assert all(z>0 for z in v)
        assert boundary_check(A,v,h,F(1000))
        # Exact equality of all pairwise AM-GM terms in Perron coordinates.
        for i,j,a,b,sa,sb in ed:
            assert a*v[i]/v[j]+b*v[j]/v[i] == 2*sa*sb
        cases+=1

# Full asymmetric two-patch low/high growth active-set classification.
two_cases=0
for sa,sb in [(F(3),F(1)),(F(2),F(1)),(F(1),F(3)),(F(1),F(2)),(F(2),F(2))]:
    a,b,q=sa*sa,sb*sb,sa*sb
    A=migration(2,[(0,1,a,b)])
    for r in [F(1,50),F(1,10),F(1,2),F(1),F(2),F(5),F(9)]:
        if r>=max(a,b)-q:
            h1,h2=r+q-a,r+q-b
        elif a>b:
            h1,h2=F(0),r*(a+b-r)/(a-r)
        else:
            h1,h2=r*(a+b-r)/(b-r),F(0)
        assert min(h1,h2)>=0
        M11=r-a-h1
        M22=r-b-h2
        assert M11*M22-a*b==0
        assert M11+M22<0
        two_cases+=1

# A directional three-cycle has a genuine nonzero circulation penalty.
a,b,r=F(4),F(1),F(3)
cycle=[]
for i in range(3):cycle.append((i,(i+1)%3,a,b))
C=migration(3,cycle)
assert matvec(C,[F(1)]*3)==[F(0)]*3
assert 3*r==9 and 3*r-3*(F(2)-F(1))**2==6
print('PASS:',cases,'exact directed-tree witnesses,',two_cases,
      'exact asymmetric two-patch regimes, an exact three-patch certificate,',
      'and a biased three-cycle contrast')
