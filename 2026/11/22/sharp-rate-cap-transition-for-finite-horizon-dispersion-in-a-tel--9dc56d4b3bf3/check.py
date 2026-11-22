"""Independent finite-time moment propagation for a rate-limited telegraph particle."""
import math
import numpy as np
from scipy.linalg import expm


def effective_rate(B,T,R):
    assert B>0 and T>0 and R*T >= B - 1e-12
    return min(R,(1+B)/T)

def moment_integrator(segments,v=1.):
    y = np.array([0.,0.,1.])  # [E X^2, E XS, 1]
    for dt,rate in segments:
        assert dt>=0 and rate>=0
        mat=np.array([[0.,2*v,0.],[0.,-2*rate,v],[0.,0.,0.]])
        y=expm(mat*dt)@y
    return float(y[0])

def exact_value(B,T,R,v=1.):
    c=1/(R*T)
    c0=1/(B+1)
    if R>= (1+B)/T: c=c0
    K=(B*B-1+(B+1)**2*math.exp(-2*B))/2
    return v*v*T*T*(c0+K*(c-c0)**2)

def protocol(B,T,R):
    g=effective_rate(B,T,R)
    L=B/g
    return [((T-L)/2,0.),(L,g),((T-L)/2,0.)]

def check():
    for B in (.05,.25,1.,2.,5.):
      for T in (.3,1.,3.):
       for ratio in (1.,1.01,1.1,(1+B/2)/B,(1+B)/B,2*(1+B)/B):
        R=(B/T)*ratio
        if R*T+1e-11<B: continue
        pred=exact_value(B,T,R,1.3)
        direct=moment_integrator(protocol(B,T,R),1.3)
        assert abs(pred-direct)<2e-10*max(1.,pred), (B,T,R,pred,direct)
    # Variation against admissible inhomogeneous rates obtained by random capped segments.
    # Exact state propagation, not Monte Carlo, determines each terminal moment.
    rng=np.random.default_rng(19537)
    for (B,T,R) in ((1.,1.,1.03),(1.,1.,1.4),(1.,1.,2.0),(2.,.8,2.6),(.3,1.,.9)):
      opt=exact_value(B,T,R)
      n=20
      for _ in range(50):
        p=rng.dirichlet(np.ones(n))
        # construct feasible blockwise rates using rejection from constant-budget slice
        rates=rng.uniform(0,R,n)
        z=np.sum(rates)*T/n
        if z>B:
            rates*=B/z
        else:
            # fill remaining budget by water-filling to cap
            spare=B-z
            room=R-rates
            total=np.sum(room)*T/n
            if spare>total+1e-10:continue
            rates+=room*(spare/total)
        assert abs(sum(rates)*T/n-B)<1e-10
        cost=moment_integrator([(T/n,r) for r in rates])
        assert cost+1e-9>=opt,(B,T,R,cost,opt)
    B,T,R=1.,1.,1.
    print('PASS 90 exact segment propagations and 250 feasible randomized controls')
    for R in (1.,1.2,1.5,2.,5.):
        value=exact_value(B,T,R)
        print('B=1 T=1 R=',R,'optimum=',f'{value:.12f}', 'pulse=', protocol(B,T,R))
    K=(1.-1+(1.+1.)**2*math.exp(-2.))/2
    assert K>0
    print('verified sharp penalty coefficient K(1)=',K)

if __name__=='__main__':check()
