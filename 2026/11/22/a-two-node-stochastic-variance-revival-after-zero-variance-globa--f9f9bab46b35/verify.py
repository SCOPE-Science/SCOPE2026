"""Exact rational checks for global-Lanczos Hermite residual variance reversal.
Only standard-library Python is required. This script supplies finite verification;
the analytic proof in RESULT.md covers all dimensions and perturbations.
"""
from fractions import Fraction as F
from itertools import product

A=F(1); B=F(9,4); C=F(5,4); MU=F(3,2)

def matmul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))] for i in range(len(X))]

def tr(X): return sum(X[i][i] for i in range(len(X)))
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def add(X,Y): return [[X[i][j]+Y[i][j] for j in range(len(X))] for i in range(len(X))]
def scale(c,X): return [[c*x for x in row] for row in X]
def inverse(M):
    n=len(M); rows=[list(M[i])+eye(n)[i] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if rows[i][j])
        rows[j],rows[k]=rows[k],rows[j]
        p=rows[j][j]; rows[j]=[v/p for v in rows[j]]
        for i in range(n):
            if i!=j:
                s=rows[i][j]
                rows[i]=[v-s*w for v,w in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]

def base(n,t=F(0)):
    assert n>=3
    M=[[F(0) for j in range(n)] for i in range(n)]
    M[0][0]=M[1][1]=F(13,8)
    M[0][1]=M[1][0]=F(5,8)
    M[2][2]=C
    for i in range(3,n): M[i][i]=MU
    for i in range(1,n-1):
        M[i][i+1]=M[i+1][i]=t
    return M

def two_step_coeff(M):
    n=len(M); S1=tr(M); S2=tr(matmul(M,M)); S3=tr(matmul(matmul(M,M),M))
    mu=S1/n
    u=-(S3-mu*S2)/(S2-mu*S1)
    v=-(S2+u*S1)/n
    return mu,u,v

def hermite_resid(M,m):
    n=len(M); I=eye(n); inv=inverse(M)
    mu,u,v=two_step_coeff(M)
    if m==1:
        return add(add(inv,scale(-2/mu,I)),scale(1/(mu*mu),M))
    Q=add(add(matmul(M,M),scale(u,M)),scale(v,I))
    return scale(1/(v*v),matmul(matmul(Q,Q),inv))

def rad_variance(M):
    n=len(M)
    return 4*sum(M[i][j]**2 for i in range(n) for j in range(i+1,n))

def r1(x): return (x-MU)**2/(x*MU**2)
def poly2(n,x): return x*x-F(93,28)*x+F(153*n-49,56*n)
def r2(n,x): return poly2(n,x)**2/(x*poly2(n,F(0))**2)
def delta(n): return F(35*(3*n-7)*(33*n-49),9*(153*n-49)**2)

checks=0
for n in range(3,31):
    H=base(n)
    mu,u,v=two_step_coeff(H)
    assert (mu,u,v)==(MU,-F(93,28),F(153*n-49,56*n)); checks+=1
    M1=hermite_resid(H,1); M2=hermite_resid(H,2)
    assert tr(M1)==F(11,45);checks+=1
    assert tr(M2)==F(213*n-539,45*(153*n-49));checks+=1
    assert tr(M2)<tr(M1); checks+=1
    assert rad_variance(M1)==0;checks+=1
    assert M2[0][1]==-delta(n)/2;checks+=1
    assert rad_variance(M2)==delta(n)**2;checks+=1
    assert all(M1[i][j]==0 for i in range(n) for j in range(i+1,n));checks+=1
    assert all(M2[i][j]==0 for i in range(n) for j in range(i+1,n) if (i,j)!=(0,1));checks+=1
    assert M2[0][0]==(r2(n,A)+r2(n,B))/2;checks+=1
    assert M2[2][2]==r2(n,C);checks+=1
    assert all(M2[i][i]==r2(n,MU) for i in range(3,n));checks+=1
    if n<=8:
        for z in product([-1,1],repeat=n):
            def quad(M): return sum(F(z[i]*z[j])*M[i][j] for i in range(n) for j in range(n))
            assert quad(M1)==tr(M1);checks+=1
            assert quad(M2)-tr(M2)==-delta(n)*z[0]*z[1];checks+=1

# Irreducible SPD tridiagonal perturbation: ratios grow as t approaches zero.
ratios=[]
for n in [3,4,6,9]:
    vals=[]
    for den in [100,1000,10000]:
        H=base(n,F(1,den))
        M1=hermite_resid(H,1);M2=hermite_resid(H,2)
        v1=rad_variance(M1);v2=rad_variance(M2)
        assert v1>0 and v2>0;checks+=1
        vals.append(float(v2/v1))
    assert vals[0]<vals[1]<vals[2];checks+=1
    ratios.append((n,vals))

print(f'PASS {checks} exact-rational assertions (n=3..30; all 2^n signs for n=3..8).')
print('At n=3: mean Ritz step-1=',MU,'; step-2 polynomial=', poly2(3,F(0)), '-93/28, 1')
print('At n=3: deterministic errors=',F(11,45),F(2,369))
print('At n=3: Rademacher one-probe variance step-1=', F(0),'step-2=',delta(3)**2)
print('Perturbed irreducible tridiagonal step-2/step-1 variance ratios:')
for n,vals in ratios:print(n,[round(z,3) for z in vals])
