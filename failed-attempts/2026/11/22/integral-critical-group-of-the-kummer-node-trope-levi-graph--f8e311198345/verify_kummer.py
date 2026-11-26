"""Exact integral verification for the node-trope incidence graph of a Kummer quartic.
Requires only Python 3 standard library. All arithmetic is exact."""
from itertools import product
from collections import Counter

P = list(product(range(4), repeat=2))
N = [[int((P[i][0] == P[j][0]) != (P[i][1] == P[j][1]))
      for j in range(16)] for i in range(16)]
assert all(sum(row) == 6 for row in N)
assert all(sum(N[i][h]*N[j][h] for h in range(16)) == (6 if i == j else 2)
           for i in range(16) for j in range(16))
L = [[(6 if i == j else 0) -
      (N[i][j-16] if i < 16 <= j else
       N[j][i-16] if j < 16 <= i else 0)
      for j in range(32)] for i in range(32)]
assert all(sum(row) == 0 for row in L)

def reduced(sink):
    return [[L[i][j] for j in range(32) if j != sink]
            for i in range(32) if i != sink]

def bareiss_determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n-1):
        if a[k][k] == 0:
            l = next((l for l in range(k+1,n) if a[l][k]), None)
            assert l is not None
            a[k],a[l] = a[l],a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z = a[i][j]*pivot-a[i][k]*a[k][j]
                assert z % previous == 0
                a[i][j] = z//previous
        for i in range(k+1,n): a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]

def p_valuation(a,p,limit):
    if a == 0: return limit
    v=0
    while a%p == 0:
        a//=p;v+=1
    return v

def local_smith_valuations(matrix,p,precision):
    """Diagonalize using invertible row/column moves in Z/(p**precision).
    The full list is exact when every valuation is < precision."""
    modulus=p**precision
    a=[[v%modulus for v in row] for row in matrix]
    n=len(a)
    valuations=[]
    for k in range(n):
        v,i,j=min((p_valuation(a[r][c],p,precision),r,c)
                  for r in range(k,n) for c in range(k,n))
        assert v < precision, 'Increase precision'
        a[k],a[i]=a[i],a[k]
        for r in range(n): a[r][k],a[r][j]=a[r][j],a[r][k]
        pv=p**v
        pivot=a[k][k]
        assert pivot%pv == 0
        inverse=pow(pivot//pv,-1,modulus//pv)
        for r in range(k+1,n):
            assert a[r][k]%pv == 0
            m=((a[r][k]//pv)*inverse)%(modulus//pv)
            for c in range(k,n): a[r][c]=(a[r][c]-m*a[k][c])%modulus
            assert a[r][k] == 0
        for c in range(k+1,n):
            assert a[k][c]%pv == 0
            m=((a[k][c]//pv)*inverse)%(modulus//pv)
            for r in range(k,n): a[r][c]=(a[r][c]-m*a[r][k])%modulus
            assert a[k][c] == 0
        valuations.append(v)
    return Counter(valuations)

expected_two=Counter({0:12,1:4,2:1,4:4,5:10})
expected_three=Counter({0:30,1:1})
for sink in (0,13,16,31):
    k=reduced(sink)
    assert bareiss_determinant(k) == 3*(2**72)
    for prec in (8,12): assert local_smith_valuations(k,2,prec) == expected_two
    for prec in (4,8): assert local_smith_valuations(k,3,prec) == expected_three
    assert local_smith_valuations(k,5,3) == Counter({0:31})
print('KUMMER_BIPLANE_CRITICAL_GROUP_VERIFIED_OK')
