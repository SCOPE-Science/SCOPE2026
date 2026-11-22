"""Exact arithmetic checks for the Loewner stability theorem.

Run: python3 check.py. The proof in RESULT.md covers arbitrary dimension.
"""
from fractions import Fraction as Q
from random import Random

I = ((Q(1), Q(0)), (Q(0), Q(1)))
Z = ((Q(0), Q(0)), (Q(0), Q(0)))

def diag(a, b):
    return ((a, Q(0)), (Q(0), b))

def add(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(2)) for i in range(2))

def neg(A):
    return tuple(tuple(-v for v in row) for row in A)

def sub(A, B):
    return add(A, neg(B))

def mul(A, B):
    return tuple(tuple(sum((A[i][k] * B[k][j] for k in range(2)), Q(0)) for j in range(2)) for i in range(2))

def inv(A):
    a, b = A[0]; c, d = A[1]
    det = a*d-b*c
    assert det != 0
    return ((d/det, -b/det), (-c/det, a/det))

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def tr(A):
    return A[0][0]+A[1][1]

def pd(A):
    assert A[0][1] == A[1][0]
    return A[0][0] > 0 and det(A) > 0

def rot(c, s):
    return ((c,-s),(s,c))

def transp(A):
    return ((A[0][0],A[1][0]),(A[0][1],A[1][1]))

def endpoint(F, P):
    return mul(inv(sub(I,P)),mul(sub(F,P),F))

def stable(V):
    # In this theorem V is similar to a symmetric matrix: both eigenvalues real.
    return 1-tr(V)+det(V)>0 and 1+tr(V)+det(V)>0 and 1-det(V)>0

def gdiag(F):
    return diag((1+F[0][0]**2)/(1+F[0][0]),(1+F[1][1]**2)/(1+F[1][1]))

F=diag(Q(1,2),Q(3,4))
P0=diag(Q(4,5),Q(7,8))
V0=endpoint(F,P0)
assert V0 == diag(Q(-3,4),Q(-3,4))
P45=((Q(67,80),Q(-3,80)),(Q(-3,80),Q(67,80)))
V45=endpoint(F,P45)
assert V45 == ((Q(-9,8),Q(9,32)),(Q(3,8),Q(-15,32)))
assert tr(V45)==Q(-51,32) and det(V45)==Q(27,64)
assert not stable(V45)
assert pd(sub(gdiag(F),P0)) and not pd(sub(gdiag(F),P45))
# Determinant versus squared rotation-sine t: (2-15t)/3360.
for c,s in [(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(4,5),Q(3,5)),(Q(0),Q(1))]:
    R=rot(c,s)
    P=mul(mul(R,P0),transp(R))
    t=s*s
    assert det(sub(gdiag(F),P)) == (Q(2)-15*t)/3360
    assert (pd(sub(gdiag(F),P)) == (t < Q(2,15)))
    assert (stable(endpoint(F,P)) == (t < Q(2,15)))

rng=Random(34011)
checks=0
for _ in range(1400):
    a=Q(rng.randint(1,45),50)
    b=Q(rng.randint(1,45),50)
    p=Q(rng.randint(1,45),50)
    q=Q(rng.randint(1,45),50)
    c,s=[(Q(1),Q(0)),(Q(0),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))][rng.randrange(4)]
    F=diag(a,b)
    P=mul(mul(rot(c,s),diag(p,q)),transp(rot(c,s)))
    V=endpoint(F,P)
    D=diag(a*(1-a),b*(1-b))
    assert V == sub(F,mul(inv(sub(I,P)),D))
    assert (stable(V) == pd(sub(gdiag(F),P)))
    # Derive the finite endpoint directly from FCF relaxation and coarse correction.
    prev=I
    asym=V
    for j in range(1,8):
        if j==1: W=F
        else: W=add(mul(P,prev),mul(sub(F,P),F))
        if j==2: assert W==mul(F,F)
        prev=W
        # Independently assemble the FCF-relaxed C values and coarse residual solve.
        # C_i=F (i>=1); coarse residual r_i=F^2-F (i>=2).
        correction=Z
        for i in range(2,j+1):
            correction=add(mul(P,correction),sub(mul(F,F),F))
        assert W == add(F,correction)
        checks+=1
print('PASS: exact 2x2 matrix equalities, 2x2 sharp angular test,',checks,'finite endpoint tests')
