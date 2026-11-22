"""Standalone finite-state checks for contrarian copying on balanced multipartite graphs.
Only Python 3, numpy and scipy are required. Checks supplement an analytic proof.
"""
from fractions import Fraction
import itertools
import numpy as np
from scipy.linalg import expm

def chain(r,n,eps):
    N=r*n; states=list(itertools.product([-1,1],repeat=N)); ix={s:k for k,s in enumerate(states)}
    Q=np.zeros((2**N,2**N))
    for i,s in enumerate(states):
        for x in range(N):
            target=[y for y in range(N) if y//n!=x//n]
            for y in target:
                z=list(s); z[x]=-s[y]; j=ix[tuple(z)]
                if i!=j: Q[i,j]+=1./len(target)
            z=list(s); z[x]=-s[x]; j=ix[tuple(z)]
            Q[i,j]+=eps/2.
        Q[i,i]=-sum(Q[i])
    return np.asarray(states,float),Q

def exact(r,n,eps):
    den=1+n*(2*(r-2)+(3*r-4)*eps+(r-1)*eps**2)
    u=1/den; v=-(1+eps)/den
    lam=eps+(r-2)/(r-1)
    var=2*(r-1)*(1+eps)*(2+eps)/den
    return u,v,lam,var

def run():
    cases=[(2,2,.25),(2,2,1.),(3,2,.5),(3,2,1.5)]
    count=0
    for r,n,eps in cases:
        ss,Q=chain(r,n,eps)
        # stationary left null-vector normalized
        A=Q.T.copy(); A[-1,:]=1.
        b=np.zeros(len(ss));b[-1]=1.
        pi=np.linalg.solve(A,b)
        assert np.linalg.norm(pi@Q,ord=np.inf)<2e-13
        assert pi.min()>-1e-13
        u,v,lam,var=exact(r,n,eps)
        for i in range(r*n):
          assert abs(pi@ss[:,i])<1e-12
          for j in range(i+1,r*n):
            wanted=u if i//n==j//n else v
            got=pi@(ss[:,i]*ss[:,j])
            assert abs(got-wanted)<2e-11,(r,n,eps,i,j,got,wanted)
            count+=1
        contrast=ss[:,:n].mean(axis=1)-ss[:,n:2*n].mean(axis=1)
        assert abs(pi@(contrast**2)-var)<2e-11
        count+=1
        # Exact finite-state semigroup for two-time stationary covariance.
        for t in [0.125,0.5,1.]:
            propagated=expm(Q*t)@contrast
            got=pi@(contrast*propagated)
            wanted=var*np.exp(-lam*t)
            assert abs(got-wanted)<3e-11,(r,n,eps,t,got,wanted)
            count+=1
        # Generator eigenfunction proof by finite-state independent check
        assert np.max(abs(Q@contrast+lam*contrast))<2e-13
        count+=1
    print('FINITE_STATE_CHECKS_PASSED',count)
    from sympy import symbols, simplify, factor
    r,n,a=symbols('r n a', positive=True)
    D=1+n*(2*(r-2)+(3*r-4)*a+(r-1)*a*a)
    U=1/D;V=-(1+a)/D
    assert simplify((1+a)*U+V)==0
    assert simplify((1+a)*V+(1+(n-1)*U+(r-2)*n*V)/((r-1)*n))==0
    G=1+(n-1)*U-n*V
    assert simplify(2*G/n-2*(r-1)*(1+a)*(2+a)/D)==0
    print('SYMBOLIC_IDENTITIES_PASSED',3)

if __name__=='__main__':run()
