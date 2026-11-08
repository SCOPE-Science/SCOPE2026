"""Reproduce algebraic and finite-dimensional checks for positivity of periodic heat steps.

Run: python verify.py. Standard library only. Exact-fraction checks are separate
from floating-point checks; the analytic statements are proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, cos, pi, isclose

count = 0

def check(statement, message):
    global count
    count += 1
    if not statement:
        raise AssertionError(message)

def torus_laplacian(d,n):
    vertices = list(product(range(n), repeat=d))
    index={x:i for i,x in enumerate(vertices)}
    N=len(vertices)
    a=[[F(0) for _ in range(N)] for __ in range(N)]
    for i,x in enumerate(vertices):
        a[i][i]=F(2*d)
        for axis in range(d):
            for direction in (-1,1):
                y=list(x); y[axis]=(y[axis]+direction)%n
                a[i][index[tuple(y)]]-=1
    return a

def invert(a):
    N=len(a)
    b=[list(a[i])+[F(i==j) for j in range(N)] for i in range(N)]
    for col in range(N):
        p=next((k for k in range(col,N) if b[k][col]),None)
        if p is None: raise ArithmeticError('singular matrix')
        b[col],b[p]=b[p],b[col]
        fac=b[col][col]
        b[col]=[x/fac for x in b[col]]
        for row in range(N):
            if row==col: continue
            fac=b[row][col]
            if fac: b[row]=[u-fac*v for u,v in zip(b[row],b[col])]
    return [r[N:] for r in b]

def rational_diag(d,n,c):
    lap=torus_laplacian(d,n)
    N=len(lap)
    mat=[[F(i==j)+c*lap[i][j]/2 for j in range(N)] for i in range(N)]
    R=invert(mat)
    C=[[2*R[i][j]-F(i==j) for j in range(N)] for i in range(N)]
    for i in range(N):
        check(sum(R[i])==1,('resolvent row sum',d,n,c,i))
        check(sum(C[i])==1,('C row sum',d,n,c,i))
        for j in range(N):
            if i!=j:
                check(R[i][j]>0 and C[i][j]>0,('offdiagonal',d,n,c,i,j))
            check(C[i][j]==2*R[i][j]-F(i==j),('C=2R-I',d,n,c,i,j))
    return R[0][0], C[0][0]

# Exact finite matrices and sign changes.
for d,n,cvalues in [
    (1,3,[F(1),F(2),F(3)]),
    (1,4,[F(1),F(3,2),F(7,4)]),
    (1,5,[F(1),F(3,2),F(7,4)]),
    (2,3,[F(1,2),F(3,5),F(5,8),F(1)]),
    (2,4,[F(1,2),F(3,5),F(1)]),
]:
    for c in cvalues:
        diag, cdiag=rational_diag(d,n,c)
        check((cdiag>=0)==(diag>=F(1,2)),('diagonal criterion',d,n,c))
        if (d,n)==(1,3): check((cdiag>0)==(c<F(2)),('n3 root',c))
        if (d,n)==(2,3): check((cdiag>0)==(7*c*c-c-2<0),('3x3 polynomial root',c))

# The 3-by-3 exact polynomial follows after clearing the positive denominators.
for c in [F(1,10),F(1,2),F(3,5),F(2,3),F(2)]:
    f=(1+4/(1+F(3,2)*c)+4/(1+3*c))/9
    g=-(7*c*c-c-2)/(2*(3*c+1)*(3*c+2))
    check(f-F(1,2)==g,('3x3 exact identity',c))

# A direct binomial finite Fourier formula at n=3, useful even at large dimension.
def F3(d,c):
    return sum(F(comb(d,k)*2**k,3**d)/(1+F(3,2)*c*k) for k in range(d+1))
for d in range(1,81):
    for c in (F(1,2*d),F(1,d),F(2,d)):
        v=F3(d,c)
        check(F(0)<v<=1,('range',d,c))
        check((v>F(1,2)) if c==F(1,d) else True,('strict Jensen lower bound',d,c))
    if d>1:
        check(F3(d,F(1,d-1))<F3(d-1,F(1,d-1)),('dimension strict monotonic',d))

# First two Y moments are exactly 1 and 3/2 on all n>=3.
for n in range(3,121):
    mean=sum(1-cos(2*pi*j/n) for j in range(n))/n
    second=sum((1-cos(2*pi*j/n))**2 for j in range(n))/n
    check(isclose(mean,1,abs_tol=5e-14),('first moment',n))
    check(isclose(second,1.5,abs_tol=5e-14),('second moment',n))

# Bessel-resolvent and elliptic-integral constants are established analytically;
# numerical lattice checks use independent spectral summation.
def spectral_diag(d,n,c):
    yy=[1-cos(2*pi*j/n) for j in range(n)]
    return sum(1/(1+c*sum(yy[j] for j in inds)) for inds in product(range(n),repeat=d))/n**d
for n in range(3,41):
    c=1.5
    f=spectral_diag(1,n,c)
    exact=F(1,2)*(1+F(1,3**n))/(1-F(1,3**n))
    check(isclose(f,float(exact),rel_tol=3e-12,abs_tol=3e-12),('1d exact resolvent',n))
    check(exact>F(1,2),('finite cycle improvement exact',n))
    if n<=22: check(f>0.5,('finite cycle improvement numerical',n))
    if 4<=n<=22:
        check(spectral_diag(1,n,1.55)<spectral_diag(1,n-1,1.55),('n monotonic',n))
for n in range(3,11):
    for c in [0.25,0.5,0.625,1.0]:
        check(spectral_diag(2,n,c)>0,('2d resolvent positive',n,c))
        if n>=4:
            check(spectral_diag(2,n,c)<spectral_diag(2,n-1,c),('2d n monotonic',n,c))

print('PASS:',count,'standalone deterministic checks')
