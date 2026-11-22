"""Independent exact and numerical checks for the quadratic local primal-dual update law."""
from fractions import Fraction as F
import numpy as np


def exact_two_agent():
    count=0
    for tau in range(1, 17):
        for numer in range(1, 11):
            lam=F(numer, 12)
            W=[[F(1,2)*(1+lam),F(1,2)*(1-lam)],
               [F(1,2)*(1-lam),F(1,2)*(1+lam)]]
            c=[F(1),F(-1)]; x=[F(0),F(0)]; y=[F(0),F(0)]
            r=1-(1-lam)/tau
            for t in range(12):
                phi=x[:]
                for j in range(tau):
                    phi=[phi[i]-(phi[i]-c[i])-y[i]/tau for i in range(2)]
                xn=[sum(W[i][j]*phi[j] for j in range(2)) for i in range(2)]
                yn=[y[i]+phi[i]-xn[i] for i in range(2)]
                assert xn == [lam*r**t*ci for ci in c], (tau,numer,t,xn)
                assert yn == [tau*(1-r**(t+1))*ci for ci in c]
                x,y=xn,yn
                count+=2
    return count


def random_stochastic(n, rng):
    b=rng.uniform(0.1,1.0,(n,n)); b=(b+b.T)/2
    for _ in range(200):
        d=1/np.sqrt(b.sum(axis=1))
        b=(d[:,None]*b)*d[None,:]
    # normalizing may still leave tiny off; 200 iterations enough
    assert np.max(abs(b.sum(axis=1)-1))<2e-12
    return b


def numeric_checks():
    rng=np.random.default_rng(20261121); count=0; reports=[]
    for n in (2,3,4,6):
        for j in range(30):
            W=random_stochastic(n,rng)
            A=rng.uniform(0.6,2.5,n)
            alpha=float(rng.uniform(0.12,0.65)/A.max())
            T=1/(alpha*A)
            L=np.eye(n)-W
            B=np.sqrt(T)[:,None]*L*np.sqrt(T)[None,:]
            mu=np.linalg.eigvalsh(B)
            mu2=mu[1]
            Q=np.linalg.qr(np.column_stack([np.ones(n),np.eye(n)[:,:-1]]))[0][:,1:]
            # Q spans orthogonal complement of ones
            for tau in (30,100,300,900):
                h=(1-alpha*A)**tau
                k=(1-h)/(tau*alpha*A)
                top=np.hstack([W*h[None,:],-(W*k[None,:])@Q])
                bot=np.hstack([Q.T@(L*h[None,:]), np.eye(n-1)-Q.T@((L*k[None,:])@Q)])
                M=np.vstack([top,bot])
                eig=np.linalg.eigvals(M)
                rho=np.max(np.abs(eig))
                assert rho<1+1e-10
                delta=tau*(1-rho)
                if tau==900: 
                    assert abs(delta-mu2)<.12, (n,j,delta,mu2)
                    reports.append((n,round(mu2,7),round(delta,7)))
                count+=2
    return count,reports


def exact_saga_mean():
    """Enumerate every within-round sample path of a two-component SAGA table."""
    from itertools import product
    checks=0
    for tau in range(1,9):
        for alpha in (F(1),F(1,2),F(3,4)):
            for d in (F(1,4),F(1,2)):
                curv=[1+d,1-d]
                for x,c,y in ((F(0),F(1),F(0)),(F(2),F(-1),F(1,3)),(F(-2,3),F(1,3),F(-3,5))):
                    out=F(0);out2=F(0)
                    for js in product((0,1),repeat=tau):
                        phi=x; tab=[x,x]
                        for j in js:
                            grad=lambda u,i: curv[i]*(u-c)
                            mean_stored=(grad(tab[0],0)+grad(tab[1],1))/2
                            g=mean_stored+grad(phi,j)-grad(tab[j],j)
                            next_phi=phi-alpha*g-y/tau
                            tab[j]=next_phi
                            phi=next_phi
                        out+=phi;out2+=phi*phi
                    out/=2**tau;out2/=2**tau
                    h=(1-alpha)**tau
                    pred=h*x+(1-h)*c-(1-h)/(tau*alpha)*y
                    assert out==pred,(tau,alpha,d,x,c,y,out,pred)
                    if alpha==1 and tau==2 and x==0 and c==1 and y==0:
                        assert out2-out*out == (1+d*d)/4
                    checks+=1
    return checks

if __name__=='__main__':
    a=exact_two_agent()
    b, reports=numeric_checks()
    c=exact_saga_mean()
    print(f'PASS: {a} exact-rational two-agent trajectory assertions; {b} numerical spectral assertions; {c} exact two-component variance-reduced conditional mean cases')
    print('Example (nodes, mu2, tau(1-rho)):',reports[:5])
