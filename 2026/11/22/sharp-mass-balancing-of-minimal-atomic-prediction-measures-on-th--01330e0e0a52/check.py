"""Reproducible finite diagnostics for sparse optimal prediction designs.
No finite calculation replaces the analytic proof of all-degree claims.
"""
import cmath, math
import numpy as np


def phi(t, a, n):
    # Valid on 0<=t<=pi (and its odd or pi-periodic continuation).
    return (n+1)*t+2*math.atan2(a*math.sin(t), 1-a*math.cos(t))


def bisection(f, lo, hi, goal, iters=90):
    for _ in range(iters):
        mid=(lo+hi)/2
        if f(mid)<goal:lo=mid
        else:hi=mid
    return (lo+hi)/2


def closest_plus(a,n):
    return bisection(lambda t:phi(t,a,n),0,math.pi,math.pi)


def closest_minus(a,n):
    return bisection(lambda d: (n+1)*d-2*math.atan2(a*math.sin(d),1+a*math.cos(d)),0,math.pi,math.pi)


def node_data(a,n,eta):
    # Solves z^(n+1)-a z^n+eta*a z-eta=0
    coeff=np.zeros(n+2, dtype=complex);coeff[0]=1;coeff[1]-=a;coeff[-2]+=eta*a;coeff[-1]-=eta
    roots=np.roots(coeff)
    w=(1-a*a)/(1-a*a+n*np.abs(roots-a)**2)
    return roots,w


def nearest_angle(z):
    return abs(cmath.phase(z))


def test():
    checks=0
    for a in (0.2,0.5,0.85):
      for n in range(1,13):
        for phase in (0,0.27,0.9,1.8,math.pi,4.8):
          z,w=node_data(a,n,cmath.exp(1j*phase))
          assert max(abs(abs(t)-1) for t in z)<1e-6
          assert min(w)>0
          assert abs(sum(w)-1)<1e-6
          for k in range(1,n+1):
            assert abs(sum(w*z**k)-a**k)<1e-5
            checks+=1
          checks+=3
        theta=closest_plus(a,n)
        z,ww=node_data(a,n,-1)
        value=(1-a*a)/(1-a*a+n*(1+a*a-2*a*math.cos(theta)))
        assert abs(max(ww)-value)<1e-6
        checks+=1
        for phase in (0,0.7,1.9,4.1):
          z,w=node_data(a,n,cmath.exp(1j*phase))
          assert max(w)>=value-1e-7
          checks+=1
        d=closest_minus(a,n)
        phase_eta=(-1)**n
        z,w=node_data(a,n,phase_eta)
        value=(1-a*a)/(1-a*a+n*(1+a*a+2*a*math.cos(d)))
        assert abs(min(w)-value)<1e-6
        checks+=1
        for phase in (0.7,1.9,3.0,4.1):
          z,w=node_data(a,n,cmath.exp(1j*phase))
          assert min(w)<=value+1e-7
          checks+=1
    # Large-n asymptotic via stable scalar root equations, not polynomial roots
    for a in (0.2,0.5,0.85):
        c=(1+a)/(1-a)
        d=1/c
        for n in (1000,10000):
          th=closest_plus(a,n);de=closest_minus(a,n)
          wmax=(1-a*a)/(1-a*a+n*(1+a*a-2*a*math.cos(th)))
          wmin=(1-a*a)/(1-a*a+n*(1+a*a+2*a*math.cos(de)))
          assert abs(n*wmax-c)<0.3
          assert abs(n*wmin-d)<0.005
          checks+=2
    print(f"PASS: {checks} finite diagnostics; analytic global proofs are separate.")

if __name__=='__main__':test()
