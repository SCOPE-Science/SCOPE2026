"""Exact checks for the Steiner--Pluecker incidence graph; Python 3, no dependencies."""
from itertools import combinations
from collections import Counter
from math import prod

PAIRS = list(combinations(range(6), 2))
TRIPLES = list(combinations(range(6), 3))
B = [[int(set(a).issubset(b)) for b in TRIPLES] for a in PAIRS]
N = [[int(i in a) for a in PAIRS] for i in range(6)]
assert (len(PAIRS), len(TRIPLES)) == (15, 20)
assert [sum(r) for r in B] == [4]*15
assert [sum(B[i][j] for i in range(15)) for j in range(20)] == [3]*20
assert all(sum(B[i][t]*B[j][t] for t in range(20)) ==
           2*(i==j) + sum(N[h][i]*N[h][j] for h in range(6))
           for i in range(15) for j in range(15))

L = [[0]*35 for _ in range(35)]
for i in range(15):
    for j in range(20):
        if B[i][j]:
            k = 15+j
            L[i][i] += 1; L[k][k] += 1
            L[i][k] -= 1; L[k][i] -= 1
assert all(sum(L[i][j] for j in range(35)) == 0 for i in range(35))

def bareiss_det(M):
    A = [row[:] for row in M]; n=len(A); prior=1; sign=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((r for r in range(k+1,n) if A[r][k]),None)
            if r is None: return 0
            A[k],A[r]=A[r],A[k];sign=-sign
        t=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                c=A[i][j]*t-A[i][k]*A[k][j]
                assert c%prior==0
                A[i][j]=c//prior
        for i in range(k+1,n): A[i][k]=0
        prior=t
    return sign*A[-1][-1]

def smith_p_valuations(M,p,K=9):
    """Exact elimination over Z/(p**K); returns each Smith exponent < K."""
    modulus=p**K; A=[[x%modulus for x in row] for row in M]; n=len(A)
    def valuation(x):
        if not x:return K
        v=0
        while x%p==0:v+=1;x//=p
        return v
    exponents=[]
    for k in range(n):
        v,i,j=min((valuation(A[i][j]),i,j)
                  for i in range(k,n) for j in range(k,n))
        assert v<K, (p,k,'increase precision')
        A[k],A[i]=A[i],A[k]
        for row in A: row[k],row[j]=row[j],row[k]
        pivot=A[k][k]; d=p**v; reduced_mod=p**(K-v)
        inverse=pow((pivot//d)%reduced_mod,-1,reduced_mod)
        for i in range(k+1,n):
            assert A[i][k]%d==0
            multiple=((A[i][k]//d)*inverse)%reduced_mod
            for j in range(k,n):
                A[i][j]=(A[i][j]-multiple*A[k][j])%modulus
            assert A[i][k]==0
        for j in range(k+1,n):
            assert A[k][j]%d==0
            multiple=((A[k][j]//d)*inverse)%reduced_mod
            for i in range(k,n):
                A[i][j]=(A[i][j]-multiple*A[i][k])%modulus
            assert A[k][j]==0
        exponents.append(v)
    return Counter(exponents)

expected={2:Counter({0:24,1:6,2:4}),
          3:Counter({0:28,1:2,2:4}),
          5:Counter({0:26,1:8})}
expected_diag=[1]*24+[2]*2+[10]*2+[30]*2+[180]*4
order=prod(expected_diag)
assert order==2**14*3**10*5**8
# The two rooted matrices delete vertices in opposite bipartition classes.
for deleted in (0,15):
    keep=[i for i in range(35) if i!=deleted]
    R=[[L[i][j] for j in keep] for i in keep]
    det=bareiss_det(R)
    assert det==order,('det',deleted,det,order)
    for p in (2,3,5):
        got=smith_p_valuations(R,p)
        assert got==expected[p],(deleted,p,got,expected[p])
print('STEINER_PLUCKER_INTEGRAL_CERTIFICATE_OK')
print('order = 2^14 3^10 5^8 =',order)
print('invariant factors = 2^2, 10^2, 30^2, 180^4')
