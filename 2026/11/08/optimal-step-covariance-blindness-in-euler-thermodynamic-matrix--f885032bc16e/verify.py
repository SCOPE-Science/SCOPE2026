"""Exact arithmetic checks for an Euler covariance inverse-fiber classification.

These checks accompany, but do not replace, the general spectral proof.
"""
from fractions import Fraction as F

def matadd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def matsub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def scale(s,A):
    return [[s*v for v in r] for r in A]
def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

def cov(A,h):
    I=eye(2)
    B=matsub(I,scale(h,A))
    return scale(2*h,inv2(matsub(I,matmul(B,B))))

def check_cov(A,h,C):
    I=eye(2)
    B=matsub(I,scale(h,A))
    assert matadd(matmul(matmul(B,C),B),scale(2*h,I))==C
    assert inv2(C)==matsub(A,scale(h/2,matmul(A,A)))

I=eye(2)
assert matmul(I,I)==I
checks=0
for m in range(0,30):
    v=[F(1),F(m)]
    d=sum(x*x for x in v)
    P=[[v[i]*v[j]/d for j in range(2)] for i in range(2)]
    assert matmul(P,P)==P
    A=matsub(scale(3,I),scale(2,P))  # eigenvalues 1 and 3
    h=F(1,2)
    C=cov(A,h)
    assert C==scale(F(4,3),I)
    check_cov(A,h,C)
    assert matmul(matsub(I,scale(h,A)),matsub(I,scale(h,A)))==scale(F(1,4),I)
    # Starting from the origin, all finite-time marginal covariances are scalar.
    Cn=scale(F(0),I)
    B=matsub(I,scale(h,A))
    for t in range(1,16):
        Cn=matadd(matmul(matmul(B,Cn),B),scale(2*h,I))
        assert Cn==scale(F(4,3)*(1-F(1,4)**t),I)
        checks+=1
    h1,h2=F(1,5),F(1,2)
    C1,C2=cov(A,h1),cov(A,h2)
    reconstructed=scale(F(1)/(h2-h1),matsub(scale(h2,inv2(C1)),scale(h1,inv2(C2))))
    assert reconstructed==A
    check_cov(A,h1,C1)
    checks+=8
# Scalar branch example: stable A=1,3 give the same covariance at h=1/2.
assert cov([[F(1),F(0)],[F(0),F(3)]],F(1,2))==scale(F(4,3),I)
assert cov([[F(3),F(0)],[F(0),F(1)]],F(1,2))==scale(F(4,3),I)
# Unique fiber C=2h I has the sole stable SPD preimage A=h^{-1} I.
h=F(1,3)
assert cov(scale(F(3),I),h)==scale(2*h,I)
print(f'VERIFY_OK {checks} exact rational identities and finite-time checks')
