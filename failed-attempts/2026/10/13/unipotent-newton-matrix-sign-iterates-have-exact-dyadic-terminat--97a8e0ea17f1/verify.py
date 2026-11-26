from fractions import Fraction as F

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def zero(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]

def shift(n,M):
    A=zero(n)
    for i in range(n-1):
        A[i][i+1]=M
    return A

def inv_unipotent(Z):
    n=len(Z)
    I=eye(n)
    out=[row[:] for row in I]
    P=[row[:] for row in Z]
    sign=F(-1)
    for _ in range(1,n):
        out=add(out,scale(sign,P))
        P=mm(P,Z)
        sign=-sign
    return out

def newton(X):
    n=len(X)
    Z=add(X,scale(F(-1),eye(n)))
    Xinv=inv_unipotent(Z)
    return scale(F(1,2),add(X,Xinv))

def mat_eq(A,B):
    return A==B

def first_nonzero_superdiag(Z):
    n=len(Z)
    for d in range(1,n):
        if any(Z[i][i+d] != 0 for i in range(n-d)):
            return d
    return None

for n in range(2,10):
    M=F(3)
    I=eye(n)
    N=shift(n,M)
    X=add(I,N)
    k=0
    while True:
        Z=add(X,scale(F(-1),I))
        if Z==zero(n):
            break
        assert first_nonzero_superdiag(Z)==2**k
        coeff=Z[0][2**k]
        assert coeff == F(1,2**(2**k-1))*M**(2**k)
        X=newton(X)
        k+=1
    expected=0
    p=1
    while p<n:
        p*=2
        expected+=1
    assert k==expected

# Exact minimal 3x3 witness.
n=3
M=F(10)
I=eye(n)
N=shift(n,M)
X0=add(I,N)
X1=newton(X0)
X2=newton(X1)
Z1=add(X1,scale(F(-1),I))
assert Z1 == [[F(0),F(0),F(50)],[F(0),F(0),F(0)],[F(0),F(0),F(0)]]
assert X2==I
# Initial Frobenius square = 2 M^2; first = M^4/4.
ratio_frob_sq=(M**4/F(4))/(F(2)*M**2)
assert ratio_frob_sq==F(25,2)

print("VERIFY_OK")
print("n3_spectral_ratio", F(5))
print("n3_frobenius_ratio_sq", ratio_frob_sq)
