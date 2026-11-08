"""Direct numerical and exact-rational checks for critical aerosol SIS mean-field theorem."""
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp
from numpy.linalg import eigvalsh,eigvals

def example():
    n=3; A=np.ones((n,n))-np.eye(n); B=np.ones((n,1)); bd=F(1,4); be=F(1,6); sg=F(1); ga=F(1); de=F(1)
    # Critical symmetry: (bd*(n-1) + be*sg*n/de)/ga =1.
    assert bd*2+be*sg*3/de==ga
    ux=[F(1)]*3; th=[F(3)]
    W=sum(a*a for a in ux)+(be*sg/de**2)*sum(t*t for t in th)
    numerator=ga*sum(a**3 for a in ux)+(be*sg**2/de**2)*sum(t**3 for t in th)
    K=numerator/W
    assert W==F(9,2) and K==F(5,3)
    assert F(1)/K==F(3,5) and F(3)/K==F(9,5)
    # Direct quadratic identity from full nonlinear vector field (arctan has zero second derivative at origin).
    x=F(1); y=F(3)
    exposure=bd*2*x+be*y
    assert ga*x==exposure
    assert sg*3*x==de*y
    assert -3*(F(2,9)*x*exposure) - F(1,9)*(sg*3*x*y) ==-K # left PF weighted Q2
    # Verify cubic remainder of arctan to 0 from the true field.
    def rhs(t,z):
        a,b=z
        return [(0.5*a+b/6)*(1-a)-a, np.arctan(3*a)*(1-b)-b]
    for tmax in (1e3, 1e4, 1e5):
        s=solve_ivp(rhs,[0,tmax],[0.4,0.3],method='DOP853',rtol=1e-9,atol=1e-11)
        assert s.success
        observed=np.array(s.y[:,-1])*tmax
        reference=np.array([3/5,9/5]);print('t',tmax,'scaled',observed, 'reference',reference)
        assert max(abs(observed-reference)) < (120.0/tmax)**0.65

def random_hetero():
    rng=np.random.default_rng(241702)
    for it in range(30):
        n=4; m=2
        A=np.zeros((n,n));
        # Connected path
        for i in range(n-1): A[i,i+1]=A[i+1,i]=1
        B=np.array([[1,0],[1,1],[1,1],[0,1]],float)
        bd=rng.uniform(.03,.12); sigma=rng.uniform(.3,1.5); delta=rng.uniform(.4,1.8); beta=rng.uniform(.07,.32)
        M=bd*A+beta*sigma/delta*(B@B.T)
        gamma=np.max(eigvalsh(M))
        vals,vecs=np.linalg.eigh(M)
        u=vecs[:,-1];u=abs(u)
        T=B.T@u;W=u@u+beta*sigma/delta**2*(T@T)
        K=(gamma*sum(u**3)+beta*sigma**2/delta**2*sum(T**3))/W
        v=np.concatenate((u,sigma/delta*T));w=np.concatenate((u,beta/delta*T))/W
        L=np.block([[bd*A-gamma*np.eye(n),beta*B],[sigma*B.T,-delta*np.eye(m)]])
        assert max(abs(L@v))<1e-10
        assert max(abs(w@L))<1e-10
        assert abs(w@v-1)<1e-10
        assert abs(max(eigvals(L).real))<1e-10
        x,y=v[:n],v[n:]
        Q2=np.concatenate((x*(bd*A@x+beta*B@y),sigma*(B.T@x)*y))
        assert abs(w@Q2-K)<1e-10
        assert K>0
    print('30 heterogeneous random topology/parameter algebraic checks passed')

if __name__=='__main__':
    example();random_hetero();print('ALL CHECKS PASS')
