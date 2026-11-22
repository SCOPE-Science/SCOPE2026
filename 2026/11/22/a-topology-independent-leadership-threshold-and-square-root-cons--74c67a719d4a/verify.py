"""Supplementary checks for the two-community leadership threshold.

Usage: python verify.py (requires scipy and numpy). The manuscript proof,
not the finite checks here, proves the general theorem.
"""
from fractions import Fraction as F
import math
import numpy as np
from scipy.integrate import solve_ivp


def reduced(t, state, p, a, rho):
    x, y = state
    c = 2 * p
    return (-(c + (1-c)*y)*x + a*y,
            (rho-c*c)*x*x*y*(1-y))


def full(t, state, W, anchor, rho):
    n = len(anchor)
    x = np.asarray(state[:n]); y = np.asarray(state[n:])
    d = x - W@x
    return np.r_[-(1-y)*d-y*(x-anchor), y*(1-y)*(rho*x*x-d*d)]


def exact_checks():
    # Arbitrary topology and unequal cross-neighbor probabilities, but equal total cross mass.
    p=F(3,4); c=2*p; a=F(3,5); rho=F(1,1)
    W = [
      [1-p,F(0),p,F(0)],
      [F(0),1-p,F(0),p],
      [p/2,p/2,1-p,F(0)],
      [p/3,2*p/3,F(0),1-p],
    ]
    signs=[1,1,-1,-1]
    assert all(sum(row)==1 for row in W)
    assert all(sum(W[i][j]*signs[j] for j in range(4))==(1-2*p)*signs[i] for i in range(4))
    count=0
    for x in [F(1,10),F(2,5),F(3,5)]:
      for y in [F(1,9),F(2,5),F(5,7)]:
        xx=[signs[i]*x for i in range(4)]
        aa=[signs[i]*a for i in range(4)]
        dx,dy=reduced(0,(x,y),p,a,rho)
        for i in range(4):
          d=xx[i]-sum(W[i][j]*xx[j] for j in range(4))
          f=-(1-y)*d-y*(xx[i]-aa[i])
          g=y*(1-y)*(rho*xx[i]**2-d**2)
          assert f==signs[i]*dx and g==dy
          count+=2
    return count


def numerical_checks():
    rng=np.random.default_rng(431126)
    count=0
    for n in [3,4,7,12]:
      groups=np.array([1 if i%3 else -1 for i in range(n)])
      assert len(set(groups))==2
      for p in [0.15,0.4,0.7,1.0]:
        W=np.zeros((n,n))
        for i in range(n):
          for val, mass in ((groups[i],1-p),(-groups[i],p)):
            idx=np.flatnonzero(groups==val)
            ww=rng.dirichlet(np.ones(len(idx)))
            W[i,idx]=mass*ww
        assert np.allclose(W.sum(1),1)
        assert np.allclose(W @ groups,(1-2*p)*groups)
        a=0.67; h0=0.31
        for factor in [0.3,1.0,1.7]:
          rho=factor*(2*p)**2
          x0=np.r_[a*groups,np.full(n,h0)]
          fullsol=solve_ivp(full,(0,30),x0,args=(W,a*groups,rho),rtol=2e-11,atol=2e-12,dense_output=True)
          redsol=solve_ivp(reduced,(0,30),[a,h0],args=(p,a,rho),rtol=2e-11,atol=2e-12,dense_output=True)
          assert fullsol.success and redsol.success
          for t in [0,0.2,1,3,10,30]:
            f=fullsol.sol(t); r=redsol.sol(t)
            assert max(abs(f[:n]-groups*r[0]))<2e-8
            assert max(abs(f[n:]-r[1]))<2e-8
            count+=2*n
    return count


def long_time_checks():
    p=0.75; c=2*p; a=0.6; eta=0.4
    critical=c*c
    # The threshold is the precise sign-change of the leadership derivative.
    for rho in [critical-1.25,critical,critical+0.7]:
        sol=solve_ivp(reduced,(0,400),[a,eta],args=(p,a,rho),
                      method='DOP853',rtol=1e-11,atol=1e-13,dense_output=True)
        assert sol.success
        x,y=sol.y[:,-1]
        if rho<critical:
            assert y<0.2 and x<0.1
        elif rho==critical:
            target=a*eta/(c+(1-c)*eta)
            assert abs(y-eta)<5e-11 and abs(x-target)<5e-11
        else:
            assert abs(y-1)<1e-8 and abs(x-a)<1e-8
    rho=1.; kap=critical-rho
    sol=solve_ivp(reduced,(0,10000),[a,eta],args=(p,a,rho),
                  method='BDF',rtol=2e-10,atol=2e-12)
    assert sol.success
    x,y=sol.y[:,-1]
    assert abs(x*math.sqrt(2*kap*10000)-1)<0.015
    assert abs(y*(a/c)*math.sqrt(2*kap*10000)-1)<0.015
    return 8


if __name__=='__main__':
    a=exact_checks(); b=numerical_checks(); c=long_time_checks()
    print('PASS: exact identities',a,'numeric coordinate comparisons',b,
          'phase and long-time checks',c)
