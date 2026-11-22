"""Reproducible exact-rational consistency checks for a three-site filtered diffusion step."""
from fractions import Fraction as F


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def invert(A):
    n = len(A)
    U = [list(A[i]) + identity(n)[i] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c,n) if U[r][c])
        U[c], U[p] = U[p], U[c]
        v = U[c][c]
        U[c] = [z/v for z in U[c]]
        for r in range(n):
            if r == c:
                continue
            v = U[r][c]
            U[r] = [U[r][j] - v * U[c][j] for j in range(2*n)]
    return [r[n:] for r in U]


def add(A, B, t=F(1)):
    return [[A[i][j]+t*B[i][j] for j in range(len(A[i]))] for i in range(len(A))]


def laplacian(a,b):
    return [[a,-a,F(0)],[-a,a+b,-b],[F(0),-b,b]]


def ein(a,b,x):
    L = laplacian(a,b)
    I = identity(3)
    J = invert(add(I,L,x))
    return add(I,matmul(matmul(J,L),J),-2*x)


def gauss(a,b,x):
    L=laplacian(a,b); I=identity(3); L2=matmul(L,L)
    numer=add(add(I,L,-x),L2,x*x/F(3))
    denom=add(add(I,L,x),L2,x*x/F(3))
    return matmul(numer,invert(denom))


def formulas(a,b,x):
    D=1+2*(a+b)*x+3*a*b*x*x
    return (2*a*x*(1+2*b*x+b*(2*b-a)*x*x)/D**2,
            2*b*x*(1+2*a*x+a*(2*a-b)*x*x)/D**2,
            4*a*b*x*x*(1+(a+b)*x)/D**2)


def run():
    tests=0
    conductances=[F(1,3),F(1,2),F(1),F(3,2),F(2),F(3),F(5),F(9)]
    times=[F(1,50),F(1,5),F(1,2),F(1),F(3,2),F(3),F(6),F(15)]
    for a in conductances:
        for b in conductances:
            for x in times:
                M=ein(a,b,x)
                f12,f23,f13=formulas(a,b,x)
                assert (M[0][1],M[1][2],M[0][2]) == (f12,f23,f13)
                tests+=3
                assert all(M[i][j]==M[j][i] for i in range(3) for j in range(3))
                tests+=1
                assert all(sum(row)==1 for row in M)
                tests+=1
                assert all(M[i][i]>=F(1,2) for i in range(3))
                tests+=1
                # Sign-based exact decision for this x: at most one strong-edge transition can be negative.
                expect12=(1+2*b*x+b*(2*b-a)*x*x>=0)
                expect23=(1+2*a*x+a*(2*a-b)*x*x>=0)
                assert (M[0][1]>=0)==expect12 and (M[1][2]>=0)==expect23 and M[0][2]>0
                tests+=1
    M=ein(F(3),F(1),F(3)); G=gauss(F(3),F(1),F(3))
    assert M[0][1]==F(-9,2809) and G[0][1]==F(18,1621)
    tests+=2
    print('VERIFY_OK',tests,'exact_rational_checks')

if __name__=='__main__': run()
