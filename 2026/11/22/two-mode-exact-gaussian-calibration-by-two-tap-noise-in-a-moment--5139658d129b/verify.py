"""Exact-arithmetic reproducibility checks for two-tap noise calibration.

Run with Python 3: python verify.py. No external dependencies.
This finite checker supplements, but does not replace, the algebraic proof.
"""
from fractions import Fraction as F
from random import Random

def solve(A,b):
    n=len(b)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        q=next((j for j in range(k,n) if M[j][k]),None)
        assert q is not None
        M[k],M[q]=M[q],M[k]
        c=M[k][k]
        M[k]=[u/c for u in M[k]]
        for i in range(n):
            if i!=k:
                c=M[i][k]
                if c:M[i]=[x-c*y for x,y in zip(M[i],M[k])]
    return [row[-1] for row in M]

def variance_lyapunov(eta,t,alpha,sigma,theta0,theta1):
    a=(1+eta)*t;b=eta*t
    M=[[a,-b,sigma*theta1],[F(1),F(0),F(0)],[F(0),F(0),F(0)]]
    w=[sigma*theta0,F(0),F(1)]
    E=[];bb=[]
    for i in range(3):
        for j in range(3):
            E.append([int(i==k and j==l)-M[i][k]*M[j][l] for k in range(3) for l in range(3)])
            bb.append(w[i]*w[j])
    return solve(E,bb)[0]

def variance_formula(eta,t,alpha,sigma,theta0,theta1):
    a=(1+eta)*t;b=eta*t
    A=theta0**2+theta1**2
    return sigma**2*((1+b)*A+2*a*theta0*theta1)/((1-b)*((1+b)**2-a**2))

rng=Random(3017);n=0
for k in range(150):
    eta=F(rng.randint(0,9),rng.randint(10,20))
    t=F(rng.randint(1,9),10)
    alpha=F(rng.randint(1,5),rng.randint(6,11))
    sigma=F(rng.randint(1,4),rng.randint(1,5))
    u=F(rng.randint(-5,5),rng.randint(1,7))
    v=F(rng.randint(-5,5),rng.randint(1,7))
    if not (u or v):continue
    x=variance_lyapunov(eta,t,alpha,sigma,u,v)
    y=variance_formula(eta,t,alpha,sigma,u,v)
    assert x==y,(eta,t,u,v,x,y)
    n+=1
assert n>=140

for j in range(300):
    eta=F(rng.randint(1,19),20)
    a=F(rng.randint(1,40),100)
    b=F(rng.randint(41,99),100)
    if a>=b:continue
    q=eta*(1+2*eta)
    K=1+q*a*b
    H=1+eta-q*(a+b)
    r=H/K
    assert -1<r<1+2*eta
    T=F(rng.randint(1,99),100)
    D=lambda x:(1-eta*x)*(1+(1+2*eta)*x)
    exact=K+H*T
    assert exact-D(T)==q*(T-a)*(T-b)
    assert K+H*a==D(a)
    assert K+H*b==D(b)
    n+=5

# Concrete example: exact at two modes, strict underdispersion between them.
eta=F(1,2);t1=F(1,4);t2=F(2,3);alpha=F(1,2)
q=eta*(1+2*eta)
K=1+q*t1*t2
H=1+eta-q*(t1+t2)
assert (q,K,H)==(1,F(7,6),F(7,12))
assert H/K==eta # zero temporal correlation is admissible at these two modes
# Choose sigma^2=2*alpha/(1-eta)=2, theta0^2=(alpha/sigma^2)*K=7/24.
# Test directly at the level of stationary second moments, without approximating radicals.
D=lambda t:(1-eta*t)*(1+(1+2*eta)*t)
tm=(t1+t2)/2
assert tm==F(11,24)
assert (K+H*t1)/D(t1)==1
assert (K+H*t2)/D(t2)==1
assert (K+H*tm)/D(tm)==F(826,851)
assert q*(tm-t1)*(tm-t2)/D(tm)==-F(25,851)

# Zero momentum: equal two-tap coefficients give exact stationary variance at every mode.
eta=F(0);alpha=F(1,3);sigma=F(1)
# c0=c1=1/sqrt(6) are represented using A=1/3 and c0*c1=1/6.
A=F(1,3);B=F(1,3)
for t in [F(j,31) for j in range(1,31)]:
    assert sigma**2/alpha*(A+B*t)/(1+t)==1
    n+=1
print(f'PASS: {n} exact rational identities and Lyapunov covariance checks')
