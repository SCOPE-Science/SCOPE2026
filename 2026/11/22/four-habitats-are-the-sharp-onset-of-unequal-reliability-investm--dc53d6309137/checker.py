"""Independent numerical consistency checks for four-patch path allocation.

All claims of global optimality are established analytically in RESULT.md;
these finite checks only detect implementation and algebra mistakes.
Requires Python 3 standard library.
"""
import math
import random


def score(x):
    q = [-math.expm1(-t) for t in x]
    return q[0]+q[1]+q[2]+q[0]*q[1]+q[1]*q[2]+q[0]*q[1]*q[2]


def enumerate_score(x):
    q = [-math.expm1(-t) for t in x]
    total = 0.0
    for mask in range(8):
        pr = 1.0
        edges = []
        for j in range(3):
            on = (mask >> j) & 1
            pr *= q[j] if on else 1.0-q[j]
            edges.append(on)
        count = sum(all(edges[i:j]) for i in range(3) for j in range(i+1,4))
        total += pr*count
    return total


def H(u):
    return u*u*u*(3.0-u)/(2.0*(2.0-u))


def solution(B):
    R = math.exp(-B)
    lo, hi = math.sqrt(R), 1.0
    for i in range(120):
        mid = 0.5*(lo+hi)
        if H(mid) < R:
            lo = mid
        else:
            hi = mid
    u = 0.5*(lo+hi)
    a = -math.log(u)
    b = B-2*a
    return a,b,a,u


def run():
    rng = random.Random(20261119)
    nchecks = 0
    budgets = [1e-3, .01, .05, .1, .2, .5, 1,2,4,8,16,30,50]
    last_gap = -1
    for B in budgets:
        a,b,c,u=solution(B)
        assert a>0 and b>0 and abs(a+b+c-B)<1e-12
        nchecks+=1
        assert b>a and b-a<math.log(4/3)
        nchecks+=1
        assert abs(H(u)-math.exp(-B))<1e-13
        nchecks+=1
        gap=b-a
        assert gap>last_gap
        nchecks+=1
        last_gap=gap
        opt = score([a,b,c])
        assert abs(opt-enumerate_score([a,b,c]))<2e-13
        nchecks+=1
        for k in range(2500):
            x=B*rng.random()
            y=(B-x)*rng.random()
            z=B-x-y
            candidate=score([x,y,z])
            assert opt+max(1e-10,2e-12*B) >= candidate, (B,opt,candidate,x,y,z)
            nchecks+=1
    for B in [0.01, .1,1,5,20]:
        u=math.exp(-B/2)
        equal=(1-u)*2+(1-u)**2
        for k in range(1500):
            x=B*rng.random()
            val=(1-math.exp(-x))+(1-math.exp(-(B-x)))+(1-math.exp(-x))*(1-math.exp(-(B-x)))
            assert equal+1e-12>=val
            nchecks+=1
    for B in [1e-3,.01]:
        a,b,_,_=solution(B)
        assert abs(a/B-2/7)<0.01 and abs(b/B-3/7)<0.02
        nchecks+=1
    for B in [20,50]:
        a,b,_,_=solution(B)
        assert abs(a-(B-math.log(4/3))/3)<0.01
        assert abs(b-(B+2*math.log(4/3))/3)<0.02
        nchecks+=2
    print('PASS',nchecks,'supplementary assertions')

if __name__ == '__main__':
    run()
