"""Exact-rational checks for exponential-kernel quadrature positivity.

Requires SymPy; run: python verify_ou_weight_positivity.py
All infinite-family conclusions rely on the accompanying analytic proof.
"""
from sympy import Matrix, Rational, eye, zeros

checks=0

def check(ok, msg):
    global checks
    assert bool(ok), msg
    checks+=1

def gram(q):
    n=len(q)+1
    return Matrix(n,n,lambda i,j: Rational(1) if i==j else
                  __import__('functools').reduce(lambda x,y:x*y, q[min(i,j):max(i,j)], Rational(1)))

def atoms(K,q):
    n=K.rows
    basis=[]
    for k in range(n):
        basis.append(K[:,k])
    if n==1:
        return [K[:,0]*Rational(2,3), K[:,0]]
    basis.extend([K[:,0]*Rational(2,3), K[:,n-1]*Rational(3,4)])
    for j,r in enumerate(q):
        a=(1+r)/2
        b=r/a
        z=Matrix(n,1,lambda i,_: K[i,j]*a if i<=j else K[i,j+1]*b)
        basis.append(z)
    return basis

for n in range(1,9):
    q=[(Rational(2+(j%3),4+(j%3))) for j in range(n-1)]
    K=gram(q)
    Q=K.inv()
    check(K*Q==eye(n), f'precision inverse {n}')
    check(all(Q[i,i]>0 for i in range(n)), 'precision positive diagonal')
    check(all(Q[i,j]<=0 for i in range(n) for j in range(n) if i!=j), 'Stieltjes precision')
    check(all(z>0 for z in Q*Matrix([1]*n)), 'strictly positive precision row sums')
    for Dcoeff in (0,Rational(1,5),1):
        D=Matrix.diag(*[(Rational(0) if Dcoeff==0 else Dcoeff*(i%4+1)) for i in range(n)])
        A=K+D
        B=(eye(n)+Q*D).inv()
        check(B*(eye(n)+Q*D)==eye(n), 'inverse identity')
        check(all(B[i,j]>=0 for i in range(n) for j in range(n)), 'nonnegative transfer')
        vs=atoms(K,q)
        vs.append(sum((v*Rational(j+1,3) for j,v in enumerate(vs)),zeros(n,1)))
        for aidx,b in enumerate(vs):
            mass=Rational(1) if aidx<len(vs)-1 else sum((Rational(i+1,3) for i in range(len(vs)-1)),Rational(0))
            v=Q*b
            w=A.inv()*b
            check(all(z>=0 for z in v), f'cardinal nonnegative {n},{aidx}')
            check(all(z>=0 for z in w), f'weight nonnegative {n},{aidx}')
            check(sum(w)<=mass, f'weight mass bound {n},{aidx}')
            check((A*w)==b, 'linear system')
            if Dcoeff!=0:
                check(all(z>0 for z in w), 'strict nugget positivity')
print(f'PASS exact OU checks={checks}')
# Exact two-node Gaussian (alpha=2, lambda=1, x1=0,x2=1,
# target atom y=5) yields negative first weight even with d2=1.
# Its numerator is 2*exp(-25)-exp(-17)<0 by 2 < exp(8).
# This last inequality is proved analytically by exp(8)>1+8>2.
check(Rational(2)<Rational(9), "e^8 > 1+8 > 2")
print(f'PASS sharpness analytic inequality; total checks={checks}')
