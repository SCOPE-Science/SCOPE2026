from fractions import Fraction as F
import math, random

def f(x,s,lam,alpha):
    x1=lam*x+alpha*s
    u=s+x1-x
    return x1, (u if abs(u)<=1 else 0)

def iterate_phys(r,beta,q):
    lam=-r;alpha=beta+r; mu=r/(1+r);nu=beta+mu;q1=1/(1+r)
    period=(q+1) * (1 if q%2==0 else 2)
    xs=[mu+(nu-mu)*F(k,37) for k in range(1,37)]
    tests=0
    for x0 in xs+[q1,nu]:
        if x0==mu: continue
        X=(x0,F(0));
        for t in range(1,period):
            X=f(*X,lam,alpha)
            assert X!=(x0,F(0)),(q,x0,t)
            tests+=1
        X=f(*X,lam,alpha)
        assert X==(x0,F(0)),(q,x0,X)
        tests+=1
    # corner mu is NOT periodic, but eventually enters (mu,nu]
    X=(mu,F(0)); X=f(*X,lam,alpha);X=f(*X,lam,alpha)
    assert X==(-r*nu,0)
    return tests

sum_tests=0
for q in range(3,13):
    r=F(1,2); beta=F(2**q-1,3)
    sum_tests+=iterate_phys(r,beta,q)
print('Exact Fraction prime period assertions',sum_tests)

rng=random.Random(20261103)
num=0
for k in range(10000):
    r=rng.uniform(.12,.92)
    beta=max(1.01,1/r-1+.05)*rng.uniform(1,5)
    mu=r/(1+r); nu=beta+mu; q1=1/(1+r)
    L=math.log(nu/mu); a=math.log(1/r)/L
    assert a < .5
    z=rng.uniform(.000001,.999999)
    x=mu*math.exp(L*z)
    rho=2 if z<a else 1
    X=(x,0.)
    for j in range(rho):X=f(*X,-r,beta+r)
    z1=(z-a)%1
    assert abs(X[0]+mu*math.exp(L*z1))<1e-7*nu,(k,r,beta,z,X,z1)
    assert X[1]==0
    num+=1
print('Float genuine map section assertions',num)

# Exact consistency of every segment of the proposed physical-time tower,
# including the right-closed threshold and the second-step reset.
branch_tests = 0
for q in range(3, 13):
    r = F(1,2)
    beta = F(2**q-1,3)
    lam = -r
    alpha = beta+r
    mu = r/(1+r)
    nu = beta+mu
    q1 = 1/(1+r)
    chi = beta*(1+r)+r
    for sign in (-1, 1):
        for j in range(1, 200):
            x = mu + (q1-mu)*F(j,199)
            X = (sign*x, F(0))
            M = f(*X, lam, alpha)
            assert M == (-sign*r*x, -sign*(1+r)*x)
            R = f(*M, lam, alpha)
            assert R == (-sign*chi*x, F(0))
            branch_tests += 2
        for j in range(1,200):
            x = q1+(nu-q1)*F(j,199)
            X = (sign*x, F(0))
            assert f(*X, lam, alpha) == (-sign*r*x, F(0))
            branch_tests += 1
print('Exact Fraction branch/tower assertions',branch_tests)

# Independent exact rational phase-circle conjugacy at every rational grid
# phase (including all half-open endpoints), not just return times.
conjugacy_tests=0
for q in range(3,13):
    r=F(1,2); beta=F(2**q-1,3); lam=-r;alpha=beta+r
    mu=F(1,3); a=F(1,q); Lam=1+a; Gamma=2*Lam
    def X(z):
        zz=z*q
        assert zz.denominator==1
        return mu*F(2)**int(zz)
    def H(t):
        assert 0<t<=Gamma
        if t<=1: return (X(t),F(0))
        if t<=Lam: return f(X(t-1),F(0),lam,alpha)
        if t<=Lam+1: return (-X(t-Lam),F(0))
        return f(-X(t-Lam-1),F(0),lam,alpha)
    for k in range(1,2*q+3):
        t=F(k,q)
        tt=(t+1)%Gamma
        if tt==0:tt=Gamma
        left=f(*H(t),lam,alpha)
        right=H(tt)
        assert left==right, (q,t,left,right)
        conjugacy_tests+=1
print('Exact physical one-step conjugacy phase assertions',conjugacy_tests)
