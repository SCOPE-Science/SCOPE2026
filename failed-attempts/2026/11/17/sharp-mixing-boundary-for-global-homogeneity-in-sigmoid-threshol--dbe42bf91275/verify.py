"""Reproducible finite checks for a sigmoid threshold-network theorem.

Python 3 standard library only. These are finite checks, not an infinite proof.
"""
import math
import random


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z)) if z >= 0 else math.exp(z) / (1.0 + math.exp(z))


def coefficient(W):
    return max(0.5 * sum(abs(a-b) for a,b in zip(ra,rb))
               for ra in W for rb in W)


def flow(x, W, beta, h):
    return [-xi + sigmoid(h + beta*sum(w*xj for w,xj in zip(row,x)))
            for xi,row in zip(x,W)]


def step(x,W,beta,h,dt):
    def add(y, k, scale):
        return [a + scale*b for a,b in zip(y,k)]
    k1=flow(x,W,beta,h)
    k2=flow(add(x,k1,dt/2),W,beta,h)
    k3=flow(add(x,k2,dt/2),W,beta,h)
    k4=flow(add(x,k3,dt),W,beta,h)
    return [a+dt*(b+2*c+2*d+e)/6 for a,b,c,d,e in zip(x,k1,k2,k3,k4)]


def antisymmetric_root(a):
    assert a > 4
    lo,hi=1e-12,.5
    for _ in range(100):
        m=(lo+hi)/2
        if 0.5*math.tanh(a*m/2)-m >0:lo=m
        else:hi=m
    return (lo+hi)/2


def main():
    rng=random.Random(20261108)
    pairs=0
    for N in [2,3,5,10]:
        for _ in range(15):
            W=[]
            for i in range(N):
                row=[rng.uniform(.001,2) for _ in range(N)]
                W.append([v/sum(row) for v in row])
            delta=coefficient(W)
            for _ in range(15):
                x=[rng.random() for i in range(N)]
                D=max(x)-min(x)
                wx=[sum(a*b for a,b in zip(row,x)) for row in W]
                assert max(wx)-min(wx) <= (delta+1e-12)*D
                pairs+=1
    W=[[.875,.125],[.125,.875]]
    delta=coefficient(W)
    assert abs(delta-.75)<1e-14
    beta=8
    t=antisymmetric_root(beta*delta)
    assert .4 < t < .5
    x=[.5+t,.5-t]
    assert max(map(abs, flow(x,W,beta,-4))) < 1e-14
    f=.25-t*t
    assert -1+beta*f < 0 and -1+beta*delta*f < 0
    # In the two-site example, all three strict scalar fixed points exist;
    # under strong enough mixing all orbits end at one such uniform state.
    M=3; gamma=.25
    W3=[[gamma*(i==j)+(1-gamma)/M for j in range(M)] for i in range(M)]
    assert abs(coefficient(W3)-gamma) < 1e-14
    for x0 in [[.05,.65,.9],[.1,.2,.3],[.6,.7,.8],[0,1,0]]:
        x=x0[:]
        for j in range(600): x=step(x,W3,8,-4,.1)
        assert max(x)-min(x)<1e-8
        assert abs(x[0]-sigmoid(-4+8*x[0])) < 1e-8
    # Critical anti-symmetric line at beta*delta=4: t*D(t)^2 -> 3/2.
    # Preserve the exactly invariant antisymmetric subspace: the full system
    # is unstable in its transverse homogeneous direction at these parameters.
    z=.2
    duration=10000
    dt=.2
    def zflow(v): return -v + .5*math.tanh(2*v)
    for j in range(round(duration/dt)):
        k1=zflow(z); k2=zflow(z+dt*k1/2)
        k3=zflow(z+dt*k2/2); k4=zflow(z+dt*k3)
        z+=dt*(k1+2*k2+2*k3+k4)/6
    estimate=duration*(2*z)**2
    assert abs(estimate-1.5)<.03, estimate
    print('VERIFY_OK dob_coefficient_samples=%d stable_heterogeneous_pairs=1' % pairs,
          'strong_mixing_convergence=4 critical_inverse_time=1',
          'critical_tD2=%.9f' % estimate)

if __name__=='__main__':main()
