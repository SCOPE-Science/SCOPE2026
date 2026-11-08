#!/usr/bin/env python3
"""Reproducibility checks for the equal-consensus/missing-bridge HK construction.

The symbolic proof is in RESULT.md. This independent checker uses exact
rational arithmetic for the six-agent example and floating point only for
finite-size corroboration of the spectral construction.
"""
from fractions import Fraction as F
from math import floor, log


def step(x, c, gamma, delta):
    """Original synchronous adaptive-confidence HK rule on a path."""
    n = len(x)
    edges = [abs(x[i+1] - x[i]) < c[i] for i in range(n-1)]
    xx = []
    for i in range(n):
        neighbors = [x[i]]
        if i and edges[i-1]: neighbors.append(x[i-1])
        if i < n-1 and edges[i]: neighbors.append(x[i+1])
        xx.append(sum(neighbors) / len(neighbors))
    cc = [c[i] + gamma*(1-c[i]) if edges[i] else delta*c[i]
          for i in range(n-1)]
    return xx, cc, edges


def B_times(y):
    m = len(y)
    assert m >= 2
    out = []
    for i in range(m):
        if i == 0: out.append(y[i]/6 + y[i+1]/3)
        elif i == m-1: out.append(y[i-1]/3 + y[i]/6)
        else: out.append((y[i-1]+y[i]+y[i+1])/3)
    return out


def perron(n):
    m = n-1
    y = [1.0/m] * m
    for _ in range(25000):
        by = B_times(y)
        s = sum(by)
        ny = [z/s for z in by]
        if max(abs(a-b) for a,b in zip(ny,y)) < 1e-14:
            y = ny
            break
        y = ny
    lam = sum(B_times(y))
    assert max(abs(a-lam*b) for a,b in zip(B_times(y),y)) < 5e-12
    x = [0.0]
    for inc in y: x.append(x[-1]+inc)
    assert abs(x[-1]-1) < 1e-12
    return lam, x


def exact_example():
    # Repeated block (0,1/2,1); all five edges share c_0=3/4.
    for delta in [F(0), F(1,5), F(2,5), F(1,2)]:
        x = [F(0),F(1,2),F(1)] * 2
        c = [F(3,4)] * 5
        g = F(1,5)
        for t in range(60):
            assert x == [F(1,2)-F(1,2)**(t+1), F(1,2),
                         F(1,2)+F(1,2)**(t+1)] * 2
            assert c[2] == F(3,4) * delta**t
            assert all(abs(x[i+1]-x[i]) < c[i] for i in (0,1,3,4))
            assert abs(x[3]-x[2]) >= c[2]
            x, c, edges = step(x,c,g,delta)
            assert edges == [True,True,False,True,True]
    # With delta>1/2, first activation time has the strict threshold.
    for delta in [F(3,5),F(4,5),F(9,10)]:
        x = [F(0),F(1,2),F(1)]*2
        c = [F(3,4)]*5
        tstar = next(t for t in range(300) if F(1,2)**t < F(3,4)*delta**t)
        for t in range(tstar+1):
            assert (abs(x[3]-x[2]) < c[2]) == (t==tstar)
            if t<tstar:
                x,c,_ = step(x,c,F(1,5),delta)
    return 60*4+3


def general_cases():
    cases = 0
    for n in range(3,12):
        lam, x0 = perron(n)
        assert (n-2)/(n-1)-1e-11 <= lam < 1
        assert all(x0[i] < x0[i+1] for i in range(n-1))
        assert max(abs(x0[i]+x0[n-i-1]-1) for i in range(n)) < 1e-10
        gap = max(x0[i+1]-x0[i] for i in range(n-1))
        c0 = (1+gap)/2
        for delta in (0.0, max(0.0,lam-0.03), lam+0.6*(1-lam)):
            # Floating checks use a safety margin; equality is proved, not tested.
            x=x0+x0
            c=[c0]*(2*n-1)
            tstar = None
            if delta > lam:
                tstar = next(t for t in range(10000) if lam**t < c0*delta**t)
            last = 30 if tstar is None else tstar
            for t in range(last+1):
                gap_bridge = abs(x[n]-x[n-1]); predicted = lam**t
                assert abs(gap_bridge-predicted) < 1e-9
                assert abs(c[n-1]-c0*delta**t) < 1e-9
                assert all(abs(x[i+1]-x[i])<c[i]+1e-12 for i in list(range(n-1))+list(range(n,2*n-1)))
                if tstar is not None and t==tstar:
                    assert gap_bridge < c[n-1]
                    break
                # check bridge remains absent to this point
                assert gap_bridge >= c[n-1]-1e-12
                if t < last:
                    x,c,flags=step(x,c,0.4,delta)
                    assert not flags[n-1], (n,delta,t,lam,gap_bridge,c[n-1])
                cases+=1
    return cases

if __name__ == '__main__':
    exact=exact_example()
    many=general_cases()
    print('VERIFY_OK exact_cases='+str(exact)+' finite_spectral_steps='+str(many))
    for n in (3,4,5,8,12,20):
        lam,x=perron(n)
        print('n=%d lambda=%.12f lower=%.8f initial_maxgap=%.8f' % (n,lam,(n-2)/(n-1),max(x[i+1]-x[i] for i in range(n-1))))
