"""Exact rational checks for the two-dimensional critical-coupling shift family.

Standard library only. The mathematical argument in RESULT.md is valid for
continuous parameters; finite rational probes are supplementary.
"""
from fractions import Fraction as F

def product(A, B, n=3):
    C = {}
    for (i,j),u in A.items():
        for (k,l),v in B.items():
            if i+k<=n and j+l<=n:
                C[i+k,j+l]=C.get((i+k,j+l),F(0))+u*v
    return C

def scale(A,c):
    return {k:c*v for k,v in A.items()}

def add(A,B):
    C=dict(A)
    for k,v in B.items(): C[k]=C.get(k,F(0))+v
    return C

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def test(a,b):
    a,b=F(a),F(b)
    assert a>1 and abs(b)<a*a-1
    D=[[a*a-1,a*b],[a*b,a*a+b*b-1]]
    A=[[F(0),a],[F(0),F(0)]]
    At=[[A[j][i] for j in range(2)] for i in range(2)]
    D2=matmul(D,D); ADA=matmul(matmul(At,D),A)
    E=[[D[i][j]+D2[i][j]-ADA[i][j] for j in range(2)] for i in range(2)]
    assert det(D)==(a*a-1)**2-b*b>0
    assert det(E)==-a**6*b*b
    if b==0: assert E[0][0]>0 and E[0][1]==E[1][1]==0
    # Derive Taylor terms of R and P^-1 independently by formal multiplication.
    R={(1,1):a*a,(2,2):F(1),(3,3):F(1)}
    inv={(i,j): F(1,a**4)*(-b/a**2)**(i+j)
         for i in range(4) for j in range(4)}
    RR=product(R,R); RRR=product(RR,R)
    Q=add(add(R,scale(product(RR,inv),-1)),product(RRR,product(inv,inv)))
    H=[[Q.get((i,j),F(0)) for j in (2,3)] for i in (2,3)]
    assert H==[[0,b/a**2],[b/a**2,1-a**(-2)-b*b/a**4]],H
    assert det(H)==-b*b/a**4
    # First terms of nonnegative CNP coefficients when b=0.
    alpha=1-1/a**2; beta=(a*a-1)/a**4
    assert alpha>0 and beta>0 and alpha+beta==1-1/a**4<1
    fs=[F(0),1/a**2,F(0)]
    for k in range(3,20):
        fs.append(alpha*fs[-1]+beta*fs[-2])
        assert fs[-1]>0

N=0
for a in [F(5,4),F(3,2),F(2),F(7,3),F(4)]:
    for b in [F(0),F(1,128),F(-1,128),F(1,12),F(-1,12),F(1,4),F(-1,4),F(1,2),F(-1,2),F(3,4),F(-3,4)]:
        if abs(b)<a*a-1:
            test(a,b); N+=1
print('PASS: exact rational defect, slack, and two-variable Pick coefficients for',N,'admissible parameter pairs')
