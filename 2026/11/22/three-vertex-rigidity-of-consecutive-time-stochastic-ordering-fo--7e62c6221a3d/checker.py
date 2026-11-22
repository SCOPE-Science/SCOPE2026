"""Exact finite tests for three-time signed-walk sampling rigidity."""
from fractions import Fraction as Q
from itertools import product

def law(edges, c, b):
    n=3
    d=[sum(abs(edges[i][j]) for j in range(n)) for i in range(n)]
    s=[sum(edges[i]) for i in range(n)]
    weights=[c*d[i]+b*s[i] for i in range(n)]
    assert min(weights)>0
    total=sum(weights)
    a=[w/total for w in weights]
    P=[[abs(edges[i][j])/d[i] for j in range(n)] for i in range(n)]
    dist=[a]
    for _ in range(2):
        dist.append([sum(dist[-1][i]*P[i][j] for i in range(n)) for j in range(n)])
    return d,s,dist

def ordered(s,p,q):
    return all(sum(p[i] for i in range(3) if s[i]>=z)<=sum(q[i] for i in range(3) if s[i]>=z) for z in set(s))

checks=0
for x,y in product(range(-5,6),repeat=2):
    if not x or not y: continue
    edges=[[Q(0),Q(x),Q(y)],[Q(x),Q(0),Q(0)],[Q(y),Q(0),Q(0)]]
    for c,b in [(Q(3),Q(0)),(Q(3),Q(1)),(Q(3),Q(-1)),(Q(5),Q(2))]:
        d,s,l=law(edges,c,b)
        assert l[0][0]==Q(1,2)
        assert l[1]==l[2]
        if b==0: assert ordered(s,l[0],l[1]) and ordered(s,l[1],l[2])
        checks+=3+(b==0)
# All signs are represented in the exact finite grid, including the mixed-sign stars.
for c,b in [(Q(3),Q(-2)),(Q(3),Q(-1)),(Q(3),Q(0)),(Q(3),Q(1)),(Q(3),Q(2))]:
    edges=[[Q(0),Q(1),Q(-1)],[Q(1),Q(0),Q(1)],[Q(-1),Q(1),Q(0)]]
    d,s,l=law(edges,c,b)
    high=[t[1] for t in l]
    assert high==[(c+b)/(3*c+b),c/(3*c+b),(2*c+b)/(2*(3*c+b))]
    assert (ordered(s,l[0],l[1]) and ordered(s,l[1],l[2]))==(b==0)
    checks+=3
print('PASS',checks,'exact rational assertions')
