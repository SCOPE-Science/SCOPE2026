"""Exact binary Grassmann inclusion-spectrum test and scalar threshold tests.

Run with Python 3 and NumPy. This test is finite corroboration, not a
replacement for the parameter-uniform Grassmann harmonic proof.
"""
import itertools
import math
import numpy as np

def qnum(m, q):
    return (q**m - 1) // (q - 1)

def qbin(n, k, q):
    if k < 0 or k > n: return 0
    num = math.prod(q**(n-i)-1 for i in range(k))
    den = math.prod(q**(k-i)-1 for i in range(k))
    return num // den

def subspaces(d):
    ans = set()
    for basis in itertools.combinations(range(1, 64), d):
        elems = {0}
        for v in basis:
            elems |= {x ^ v for x in tuple(elems)}
        if len(elems) == 1 << d:
            ans.add(tuple(sorted(elems - {0})))
    return sorted(ans)

points = subspaces(1)
planes = subspaces(2)
solids = subspaces(3)
assert (len(points), len(planes), len(solids)) == (63, 651, 1395)
pmap = {p[0]:i for i,p in enumerate(points)}
plmap = {tuple(p):i for i,p in enumerate(planes)}
W1=np.zeros((1395,63),dtype=np.int64)
W2=np.zeros((1395,651),dtype=np.int64)
for j,U in enumerate(solids):
    for pt in U: W1[j,pmap[pt]]=1
    for a,b in itertools.combinations(U,2):
        T=tuple(sorted((a,b,a^b)))
        W2[j,plmap[T]]=1
assert np.all(W1.sum(axis=1)==7)
assert np.all(W2.sum(axis=1)==7)
S1=W1.T@W1
S2=W2.T@W2
I1=np.eye(63,dtype=np.int64)
I2=np.eye(651,dtype=np.int64)
# Full characteristic-spectrum identities via exact integer matrix products.
assert np.count_nonzero((S1-1085*I1)@(S1-140*I1))==0
assert np.count_nonzero(((S2-105*I2)@(S2-42*I2))@(S2-12*I2))==0
assert np.trace(S1)==1085+62*140
assert np.trace(S2)==105+62*42+588*12
# The independent incidence computation supplies the expected nontrivial
# harmonic eigenvalues of the distance-three graph on 1395 vertices.
assert [105,42,12]==[qnum(3,2)*qnum(4,2),
                        2*qnum(2,2)*qnum(3,2), 4*qnum(2,2)]
assert [1085,140]==[qnum(3,2)*qbin(5,2,2), 4*qbin(4,2,2)]

def params(q,n):
    E=qnum(3,q);C=q*q*qnum(n-4,q)-E
    A=(q+1)*C+E;B=q*C+E-1
    assert C>0 and 3*B>2*A
    def m(t):return C-A*2**t+B*3**t
    lo,hi=0.,1.
    assert m(lo)<0<m(hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if m(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2, m(1.)
for q in (2,3,4,5):
    for n in (6,7,8,10,15):
        t,eig=params(q,n)
        assert 0<t<1 and eig>0
        if q==2 and n in (6,7,10): print('q=2 n=',n,'threshold',t)
print('GRASSMANN_RANK_THREE_NEGATIVE_TYPE_CHECKS_PASS')
