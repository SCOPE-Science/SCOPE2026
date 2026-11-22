"""Exact rational arithmetic certificate for a quintic conjugate Gram matrix.

Run with Python 3: python check.py
No external dependencies. Arithmetic is in Q[z]/(1+z+...+z^10).
"""
from fractions import Fraction as F

P = 11
B = 10
# Each row is eleven times 1/((1-z^j)(1-z^(-j))), j = 1,...,5.
H = [
    [5,0,-4,-7,-9,-10,-10,-9,-7,-4],
    [15,0,10,1,6,3,3,6,1,10],
    [14,0,2,9,-1,5,5,-1,9,2],
    [12,0,-3,3,7,-2,-2,7,3,-3],
    [9,0,-5,-6,-3,4,4,-3,-6,-5],
]

def reduce_poly(a):
    a=list(a)
    if len(a)<B: a += [F(0)]*(B-len(a))
    for i in range(len(a)-1,B-1,-1):
        c=a[i]
        if c:
            for k in range(B): a[i-B+k]-=c
        a[i]=F(0)
    return a[:B]

def times(a,b):
    p=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):p[i+j]+=x*y
    return reduce_poly(p)

def trace_real(a):
    a=reduce_poly(a)
    return (10*a[0]-sum(a[1:]))/2

def determinant(a):
    a=[list(row) for row in a]
    n=len(a); out=F(1)
    for i in range(n):
        k=next(k for k in range(i,n) if a[k][i])
        if k!=i: a[i],a[k]=a[k],a[i];out=-out
        pivot=a[i][i];out*=pivot
        for j in range(i+1,n):
            c=a[j][i]/pivot
            for l in range(i+1,n): a[j][l]-=c*a[i][l]
            a[j][i]=F(0)
    return out

h=[[F(x,P) for x in row] for row in H]
for j,vec in enumerate(h,1):
    den=[F(0)]*12
    den[0]=F(2)
    den[j]-=1
    den[P-j]-=1
    assert times(den,vec)==[F(1)]+[F(0)]*9,(j,"inverse mismatch")
    assert trace_real(vec)==F(5),j

G=[[trace_real(times(hi,hj)) for hj in h] for hi in h]
expected=[
    [11,4,3,3,4],
    [4,11,3,4,3],
    [3,3,11,4,4],
    [3,4,4,11,3],
    [4,3,4,3,11],
]
assert G==expected,(G,expected)
assert determinant(G)==75625,determinant(G)
print('Five inverse identities: PASS')
print('Five real traces equal five: PASS')
print('Galois conjugate Gram matrix:')
for row in G:print(*row)
print('Determinant of Gram matrix:',determinant(G))
print('Conjugate evaluation matrix is nonsingular: PASS')
