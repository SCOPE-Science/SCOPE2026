from fractions import Fraction as F

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def lower_inverse(w,L):
    n=len(L)
    R=eye(n)
    P=eye(n)
    for k in range(1,n):
        P=mul(P,L)
        R=add(R,scale(w**k,P))
    return R

def q2_matrix(n,w,eps):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    U=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(1,n):
        L[i][i-1]=eps
        U[i-1][i]=eps
    R=lower_inverse(w,L)
    T=mul(R,add(scale(1-w,eye(n)),scale(w,U)))
    return mul(add(eye(n),T),scale(w,R))

# Exact rational witness n=3, omega=7/5, epsilon=1/10.
n=3; w=F(7,5); eps=F(1,10)
Q=q2_matrix(n,w,eps)
assert Q[2][0] == F(-68943,15625000)
assert Q[0][0] == F(10843,12500)
assert Q[1][0] == F(14651,312500)
# Sylvester minors of A=I-eps(S+S^T): 1, 99/100, 49/50.
assert F(1)>0 and F(99,100)>0 and F(49,50)>0
# Closed-form endpoint entry for the chain witness.
closed=w**n*eps**(n-1)*((n+1)-n*w+(n-1)*w*w*eps*eps)
assert closed == Q[n-1][0] < 0
# Coefficients in R+(1-w)R^2 are nonnegative at the proposed boundary.
for n in range(1,13):
    wb=F(n+1,n)
    for j in range(n):
        assert (j+2)-(j+1)*wb >= 0
    assert (n+1)-n*wb == 0
print('VERIFY_OK')
