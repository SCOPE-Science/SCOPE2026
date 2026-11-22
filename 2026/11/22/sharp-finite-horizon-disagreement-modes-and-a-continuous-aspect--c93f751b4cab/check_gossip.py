"""Independent exact full covariance comparison and finite-size checks.
Uses only Python's standard library; no external data, scripts, or files.
"""
from fractions import Fraction as F
from math import sqrt

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def data(p, q):
    d = [F(1,p),F(1,q),F(1,p)+F(1,q)]
    w = [1-F(1,p),1-F(1,q),F(1,p)+F(1,q)]
    M = [[(1-d[i] if i==j else F(0)) +d[i]*w[j]/4 for j in range(3)] for i in range(3)]
    return M

def update(M,v):
    return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]

def matmul(A,B):
    n=len(A);m=len(B[0]);inner=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(inner)) for j in range(m)] for i in range(n)]

def cov_update(X,p,q):
    n=p+q; out=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(p):
      for j in range(p,n):
        # Q=I-(e_i-e_j)(e_i-e_j)^T/2
        Q=[[F(int(a==b))-(F(int(a==i)-int(a==j))*F(int(b==i)-int(b==j))/2) for b in range(n)] for a in range(n)]
        QBQ=matmul(matmul(Q,X),Q)
        for a in range(n):
          for b in range(n):out[a][b]+=QBQ[a][b]/(p*q)
    return out

def spectral_projections(p,q):
    n=p+q
    A=[[F(int(i==j)-F(1,p)) if i<p and j<p else F(0) for j in range(n)] for i in range(n)]
    B=[[F(int(i==j)-F(1,q)) if i>=p and j>=p else F(0) for j in range(n)] for i in range(n)]
    # projection onto block-constant zero-mean contrast
    v=[F(1,p) if i<p else -F(1,q) for i in range(n)]
    norm=sum(x*x for x in v)
    C=[[v[i]*v[j]/norm for j in range(n)] for i in range(n)]
    return A,B,C

for p,q in [(2,2),(2,3),(2,5),(3,3),(3,4),(4,6)]:
    M=data(p,q); coeff=[F(1)]*3
    A,B,C=spectral_projections(p,q); n=p+q
    X=[[A[i][j]+B[i][j]+C[i][j] for j in range(n)] for i in range(n)]
    for k in range(0,9):
        Y=[[coeff[0]*A[i][j]+coeff[1]*B[i][j]+coeff[2]*C[i][j] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):check(X[i][j]==Y[i][j],f'mismatch {(p,q,k,i,j)}')
        if k>0:
            check(coeff[1]>=coeff[0]>coeff[2] if q>p else coeff[1]==coeff[0]>coeff[2],f'ordering {(p,q,k)} {coeff}')
            check(coeff[1] <= (1-F(1,2*q))**k, 'one-step spectral bound')
            if k>1:check(coeff[1] < (1-F(1,2*q))**k, 'strict gain')
        X=cov_update(X,p,q)
        coeff=update(M,coeff)

# Many independent exact reduced recurrence comparisons, including wider asymmetry.
for p in range(2,16):
 for q in range(p,20):
    v=[F(1)]*3;M=data(p,q);nu=1-F(1,2*q)
    for k in range(1,27):
        v=update(M,v)
        check(v[1]>=v[0] and v[0]>v[2] if p<q else v[1]==v[0] and v[0]>v[2], 'top eigenmode ordering')
        check(v[1]<=nu**k, 'standard contraction')
        if k>1:check(v[1]<nu**k,'strictly stronger than power bound')

# Formula for the proportional-growth speedup and its implicit relation.
for j in range(1,1001):
    r=F(j,1000)
    z=float(r)
    R=(3*(1+z)-sqrt(9*z*z-14*z+9))/(4*z)
    check(1-1e-12<=R<4/3+1e-12,'aspect-ratio limits')
    check(abs((3-2*z*R)*(3-2*R)-1)<3e-10,'implicit quadratic')

print('PASS', checks, 'exact/proportional-limit checks')

def perron(p,q):
    ds=[1/p,1/q,1/p+1/q]
    ws=[1-1/p,1-1/q,1/p+1/q]
    def f(x):
        return sum(d*w/(4*(x-1+d)) for d,w in zip(ds,ws))
    lo=1-1/q
    hi=1.0
    for _ in range(120):
        mid=(lo+hi)/2
        if f(mid)>1:lo=mid
        else:hi=mid
    return (lo+hi)/2

for p,q in [(2,1000),(3,2000),(5,3000),(10,5000),(40,1000),(100,1000),(250,1000),(500,1000),(1000,1000)]:
    rho=perron(p,q)
    observed=(-__import__('math').log(rho))/(-__import__('math').log(1-1/(2*q)))
    r=p/q
    predicted=(3*(1+r)-sqrt(9*r*r-14*r+9))/(4*r)
    check(abs(observed-predicted)<0.007,f'asymptotic rate check {p,q}, {observed}, {predicted}')

print('PASS',checks,'total checks including asymptotic spectral-root tests')
