from fractions import Fraction as F
from itertools import product

# Vectors are pairs in basis (e1,e2); only e1*e1=e2 is nonzero.
def mul(x,y):
    return (F(0), x[0]*y[0])

def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mat_vec(M,x): return (M[0][0]*x[0]+M[0][1]*x[1], M[1][0]*x[0]+M[1][1]*x[1])
def mat_mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def inv2(M):
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    assert det != 0
    return ((M[1][1]/det,-M[0][1]/det),(-M[1][0]/det,M[0][0]/det))

e1=(F(1),F(0)); e2=(F(0),F(1)); basis=(e1,e2)

def is_avg(M):
    for x in basis:
        for y in basis:
            Px=mat_vec(M,x); Py=mat_vec(M,y)
            lhs=mul(Px,Py)
            r1=mat_vec(M,mul(x,Py))
            r2=mat_vec(M,mul(Px,y))
            if lhs != r1 or lhs != r2:
                return False
    return True

def criterion(M):
    a,b=M[0]
    c,d=M[1]
    return b == 0 and (a == 0 or d == a)

vals=[F(i) for i in range(-2,3)]
count=0
for a,b,c,d in product(vals, repeat=4):
    M=((a,b),(c,d))
    assert is_avg(M) == criterion(M)
    count += is_avg(M)

# Candidate families.
for a,c,d in product(vals, repeat=3):
    assert is_avg(((a,F(0)),(c,a)))
    assert is_avg(((F(0),F(0)),(c,d)))

# Automorphisms and conjugation formulas.
xis=[F(-2),F(-1),F(1),F(2)]
for xi,nu,a,c,d in product(xis, vals, vals, vals, vals):
    Phi=((xi,F(0)),(nu,xi*xi))
    # product preservation on basis
    for x in basis:
        for y in basis:
            assert mat_vec(Phi,mul(x,y)) == mul(mat_vec(Phi,x),mat_vec(Phi,y))
    Pinv=inv2(Phi)
    P=((a,F(0)),(c,a))
    got=mat_mul(mat_mul(Phi,P),Pinv)
    exp=((a,F(0)),(xi*c,a))
    assert got == exp
    Q=((F(0),F(0)),(c,d))
    got=mat_mul(mat_mul(Phi,Q),Pinv)
    exp=((F(0),F(0)),(xi*c-d*nu/xi,d))
    assert got == exp

# Normalization checks on nonzero grid parameters.
for a,c in product(vals, vals):
    if c:
        xi=F(1,1)/c
        Phi=((xi,F(0)),(F(0),xi*xi))
        P=((a,F(0)),(c,a))
        assert mat_mul(mat_mul(Phi,P),inv2(Phi)) == ((a,F(0)),(F(1),a))
for c,d in product(vals, vals):
    if d:
        xi=F(1)
        nu=c/d
        Phi=((xi,F(0)),(nu,xi*xi))
        Q=((F(0),F(0)),(c,d))
        assert mat_mul(mat_mul(Phi,Q),inv2(Phi)) == ((F(0),F(0)),(F(0),d))

print('grid_averaging_count', count)
print('CHECK_OK')
