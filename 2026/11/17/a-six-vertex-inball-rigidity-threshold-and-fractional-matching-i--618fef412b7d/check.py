"""Exact facet-distance and low-dimensional incenter checks for complete-graph tree polytopes."""
from fractions import Fraction
from itertools import combinations
from math import comb, sqrt

def distances_squared(n):
    m = comb(n,2)
    z = Fraction(4*(n-1), n*(n-2)*(n+1))
    d = [Fraction(2*(n-1)*(s-1)*(n-s), n*s*(n+s-1)) for s in range(2,n)]
    assert min(d) == d[-1]
    if n <= 5: assert d[-1] < z
    else: assert z < d[-1]
    return z, d

for n in range(4,1001):
    distances_squared(n)
print('exact facet-distance minima: n=4..1000')

# Numerical independent linear programming against all actual facet planes.
try:
    import numpy as np
    from scipy.optimize import linprog
    from itertools import combinations
    for n in range(4,8):
        E=list(combinations(range(n),2)); m=len(E); half=np.ones((m,))/m
        AA=[]; bb=[]
        for j in range(m):
            a=np.zeros(m); a[j]=-1
            AA.append(np.r_[a,sqrt(1-1/m)]); bb.append(0)
        for s in range(2,n):
            for S in combinations(range(n),s):
                ss=set(S); a=np.array([int(u in ss and v in ss) for u,v in E],dtype=float)
                AA.append(np.r_[a,sqrt(sum(a)*(1-sum(a)/m))]); bb.append(s-1)
        c=np.zeros(m+1); c[-1]=-1
        re=linprog(c,A_ub=np.array(AA),b_ub=np.array(bb),A_eq=np.array([[1]*m+[0]]),b_eq=[n-1],bounds=[(None,None)]*(m+1),method='highs')
        assert re.success,re.message
        theory=sqrt(float(min([distances_squared(n)[0],distances_squared(n)[1][-1]])))
        assert abs(re.x[-1]-theory)<1e-8,(n,re.x[-1],theory)
        print('independent LP: n',n,'radius',re.x[-1],'theory',theory)
except ImportError:
    print('SciPy not installed; exact checks above remain valid')

# The degree-one fractional perfect-matching polytope on K5 has 22 vertices:
# 10 triangle-plus-edge supports, and 12 undirected Hamiltonian 5-cycles.
import itertools
E5=list(combinations(range(5),2))
verts=[]
for T in combinations(range(5),3):
    rest=set(range(5))-set(T)
    y={e:Fraction(0) for e in E5}
    for e in combinations(T,2): y[e]=Fraction(1,2)
    y[tuple(sorted(rest))]=Fraction(1)
    verts.append(tuple(y[e] for e in E5))
for perm in itertools.permutations(range(1,5)):
    cyc=(0,)+perm
    edge_set={tuple(sorted([cyc[j],cyc[(j+1)%5]])) for j in range(5)}
    y=tuple(Fraction(1,2) if e in edge_set else Fraction(0) for e in E5)
    verts.append(y)
verts=set(verts)
assert len(verts)==22,len(verts)
for y in verts:
    assert all(sum(y[k] for k,e in enumerate(E5) if i in e)==1 for i in range(5))
print('fractional K5 degree-one polytope: 22 distinct candidate vertices')

# Independently verify all 22 candidate centers against ALL facet inequalities,
# and that no other class except s=4 can be tight universally.
from math import sqrt
n=5; m=10; r=sqrt(3/20); ell=3*sqrt(6)/20; kappa=(8-3*sqrt(6))/5
for y in verts:
    x=[ell+kappa*float(t) for t in y]
    assert abs(sum(x)-4)<1e-10
    for s in range(2,5):
        for S in combinations(range(5),s):
            q=comb(s,2)
            val=sum(x[j] for j,e in enumerate(E5) if set(e)<=set(S))
            slack=(s-1)-val
            assert slack >=r*sqrt(q*(1-q/m))-1e-10
            if s<4: assert slack>r*sqrt(q*(1-q/m))+1e-5
    assert min(x)>=ell-1e-10
print('all 22 K5 candidate vertices satisfy all Euclidean eroded inequalities')
