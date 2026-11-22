"""Deterministic checks of a Gaussian-marginal Poisson-reset diffusion fourth-cumulant identity.

Requires numpy and scipy. The 1D computations use a polynomial Markov-generator
matrix exponential, not the claimed fourth-cumulant formula; the 2D tests
use the independently expanded no-event/event conditioning of four moments.
"""
import math
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov

count = 0

def close(x,y,tol=2e-10):
    global count
    count += 1
    assert np.allclose(x,y,rtol=tol,atol=tol), (x,y)

def gm(n,s):
    if n%2: return 0.0
    return math.prod(range(1,n,2)) * s**(n//2)

# Reset density g_s(x)[1-delta/r + delta*x*x/(r*s)] is positive
# and non-Gaussian for 0<delta<r; generator tested via exact moments.
for kappa, diff, r, s in [(1.2,.7,2.1,1.6), (1.9,.4,2.4,.85), (2.0,.7,3.0,1.1)]:
    delta=kappa-diff/s
    assert 0<delta<r
    qmom=lambda n: gm(n,s)*(1+n*delta/r)
    nmax=8
    gen=np.zeros((nmax+1,nmax+1))
    for n in range(1,nmax+1):
        gen[n,n]=-(kappa*n+r)
        gen[n,0]+=r*qmom(n)
        if n>=2:gen[n,n-2]+=diff*n*(n-1)
        close(-kappa*n*gm(n,s)+(diff*n*(n-1)*gm(n-2,s) if n>=2 else 0)+r*(qmom(n)-gm(n,s)),0)
    for lag in [.08,.3,.7,1.2,2.4]:
        trans=expm(lag*gen)
        cross12=sum(trans[1,j]*gm(1+j,s) for j in range(nmax+1))
        cross22=sum(trans[2,j]*gm(2+j,s) for j in range(nmax+1))
        now2=sum(trans[2,j]*gm(j,s) for j in range(nmax+1))
        close(now2,s)
        close(cross12,s*math.exp(-(kappa+r)*lag))
        cumul=cross22-s*s-2*cross12**2
        predicted=2*(math.exp(r*lag)-1)*cross12**2
        close(cumul,predicted)
        assert cumul>0
        count+=1

# A genuinely nonnormal coupled 2D diffusion with a nonGaussian reset law,
# Gaussian stationary law N(0,Sigma), and positive source density.
A=np.array([[1.3,.25],[-.15,1.1]],float)
Sigma=np.array([[1.0,.16],[.16,1.2]],float)
D=np.array([[.45,.03],[.03,.38]],float)
r=3.0
Q=(A@Sigma+Sigma@A.T)/2-D
assert min(np.linalg.eigvalsh(Q))>0
assert r>np.trace(np.linalg.solve(Sigma,Q))
assert np.linalg.det(Sigma)>0
for lag in [.08,.22,.51,.94]:
    p=math.exp(-r*lag)
    E=expm(-A*lag)
    V=solve_continuous_lyapunov(A,2*D)
    Qnoise=V-E@V@E.T
    B=Sigma@E.T
    S0=E@Sigma@E.T+Qnoise
    Sreset=(Sigma-p*S0)/(1-p)
    assert min(np.linalg.eigvalsh((Sreset+Sreset.T)/2))>=-1e-10
    C=p*B
    K=np.zeros((2,2,2,2))
    for i in range(2):
      for j in range(2):
       for k in range(2):
        for l in range(2):
         four=p*(Sigma[i,j]*S0[k,l]+B[i,k]*B[j,l]+B[i,l]*B[j,k])+(1-p)*Sigma[i,j]*Sreset[k,l]
         K[i,j,k,l]=four-Sigma[i,j]*Sigma[k,l]-C[i,k]*C[j,l]-C[i,l]*C[j,k]
         close(K[i,j,k,l],(math.exp(r*lag)-1)*(C[i,k]*C[j,l]+C[i,l]*C[j,k]))
    Inv=np.linalg.inv(C)
    T=sum(K[i,j,k,l]*Inv[k,i]*Inv[l,j] for i in range(2) for j in range(2) for k in range(2) for l in range(2))
    close(T,2*3*(math.exp(r*lag)-1))
    close(math.log1p(T/6)/lag,r)
print('PASS',count,'independent deterministic checks')
