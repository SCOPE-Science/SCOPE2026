"""Reproduce the analytic quorum survival formula using independent finite-state CTMC uniformization.
Scientific content only; requires Python 3.9+ standard library.
"""
import math
from fractions import Fraction


def binomial_tail(n, k, u):
    return sum(math.comb(n, j)*u**j*(1-u)**(n-j) for j in range(k,n+1))


def exact_survival(n, k, e, g, t):
    return math.exp(-g*t)*binomial_tail(n,k,math.exp(-(e-g)*t))


def independent_uniformization(n,k,e,g,t):
    # Markov chain for the number of occupied patches; independent losses
    # m -> m-1 at rate m(e-g), global catastrophe m -> 0 at rate g.
    # Poisson uniformization with Q >= max total departure rate.
    q = n*(e-g)+g
    if q == 0: return 1.0
    probs=[0.0]*(n+1); probs[n]=1.0
    weight=math.exp(-q*t); total=0.0
    for j in range(600):
        total+=weight*sum(probs[k:])
        nxt=[0.0]*(n+1)
        nxt[0]+=probs[0]
        for m in range(1,n+1):
            hazard=m*(e-g)+g
            nxt[m]+=probs[m]*(1-hazard/q)
            nxt[m-1]+=probs[m]*m*(e-g)/q
            nxt[0]+=probs[m]*g/q
        probs=nxt
        weight*=q*t/(j+1)
        if weight < 2e-17 and j>q*t+40: break
    return total


def elasticity(n,k,u):
    b=binomial_tail(n,k,u)
    return k*math.comb(n,k)*u**k*(1-u)**(n-k)/b if k<n else float(n)


def checks():
    count=0
    for n in range(2,9):
        for k in range(1,n+1):
            for g in (0.0,0.125,0.4,0.7,1.0):
                for t in (0.05,0.2,0.75,1.5,3.0):
                    a=exact_survival(n,k,1.0,g,t)
                    b=independent_uniformization(n,k,1.0,g,t)
                    assert abs(a-b)<5e-11,(n,k,g,t,a,b)
                    count+=1
    # Every elasticity value decreases as exp(-st) decreases in t, for 1<=k<n.
    for n in range(3,12):
        for k in range(1,n):
            vals=[elasticity(n,k,u) for u in (0.001,0.02,0.2,0.45,0.7,0.9)]
            assert all(vals[i]>vals[i+1] for i in range(5)),(n,k,vals)
            count+=1
    # Verify finite-time crossing pattern for all intermediate quorum sizes.
    for n in range(3,10):
        for k in range(2,n):
            for g1,g2 in ((0,.1),(0,.4),(.2,.8),(.6,1.0)):
                def ratio(t):
                    s1=exact_survival(n,k,1,g1,t)
                    s2=exact_survival(n,k,1,g2,t)
                    return math.log(s2/s1)
                # at low t it is negative, at high t positive, modulo underflow
                assert ratio(.003)<0,(n,k,g1,g2)
                assert ratio(25)>0,(n,k,g1,g2)
                lo,hi=.003,25
                for _ in range(75):
                    mid=(lo+hi)/2
                    if ratio(mid)>0:hi=mid
                    else: lo=mid
                assert ratio(lo)<=1e-11 and ratio(hi)>=-1e-11
                count+=1
    # n=3,k=2 mean formula identity, derivative and sharp max.
    for j in range(101):
        x=j/100
        direct=3/(2-x)-2/(3-2*x)
        rational=(5-4*x)/((2-x)*(3-2*x))
        assert abs(direct-rational)<2e-15
        count+=1
    xstar=(5-math.sqrt(3))/4
    ymax=(5-4*xstar)/((2-xstar)*(3-2*xstar))
    assert abs(ymax-(8-4*math.sqrt(3)))<2e-14
    assert all(ymax> (5-4*x)/((2-x)*(3-2*x)) for x in (0, .5, .8, .9, 1))
    print(f'PASS: {count} independent finite-state/uniformization, elasticity, crossing and exact-mean tests')


if __name__=='__main__':
    checks()
