"""Reproduce analytic finite-window survey formulas with Python 3 stdlib."""
import math
import random


def values(n, rate, window):
    if n < 0 or rate <= 0 or window < 0:
        raise ValueError('domain')
    x = math.exp(-rate * window)
    v = [0.0]
    for _ in range(n):
        v.append(math.exp(-x * (1.0 - v[-1])))
    return v


def optimal_gaps(n, rate, window):
    v = values(n, rate, window)
    x = math.exp(-rate * window)
    return [x * (1-v[n-i-1]) / rate for i in range(n)]


def single_window_overlap(start, length, rate):
    return math.exp(-rate*start) * (rate*start + 1 - math.exp(-rate*length))


def union_detection(gaps, window, rate):
    # Disjoint first-detection events; uses gaps before each active interval.
    t = 0.0
    total = 0.0
    for gap in gaps:
        total += math.exp(-rate*t) * single_window_overlap(gap, window, rate)
        t += gap + window
    return total


def quadrature_single(start, length, rate, steps=5000):
    # Distinct integration of arrival density against survival to window start.
    h = start / steps
    total = 0.0
    for j in range(steps):
        a = (j+0.5)*h
        total += rate*math.exp(-rate*a)*math.exp(-rate*(start-a))*h
    total += math.exp(-rate*start)-math.exp(-rate*(start+length))
    return total


def check():
    checks = 0
    rng = random.Random(70787)
    for rate in (0.2,0.7,1.0,3.0):
        for window in (0.0,0.03,0.2,0.7,2.0):
            for n in range(1,11):
                v = values(n, rate, window)
                gaps = optimal_gaps(n,rate,window)
                assert abs(union_detection(gaps,window,rate)-v[-1]) < 8e-13
                checks += 1
                assert all(gaps[i+1]>=gaps[i]-1e-15 for i in range(len(gaps)-1))
                checks += 1
                if n>=2:
                    assert v[-1]>=v[-2] and (v[-1]>v[-2] or v[-1]>1-1e-12)
                    checks += 1
                for _ in range(70):
                    random_gaps = [rng.random()*6/rate for i in range(n)]
                    observed=union_detection(random_gaps,window,rate)
                    assert observed <= v[-1]+1e-12
                    checks += 1
                for _ in range(5):
                    perturbed = gaps.copy()
                    i=rng.randrange(n)
                    perturbed[i] += 0.05*(1+rng.random())/rate
                    assert union_detection(perturbed,window,rate)<=v[-1]+1e-13
                    checks += 1
    for _ in range(1000):
        rate=10**rng.uniform(-1.3,1.1)
        s=rng.random()*3/rate
        w=rng.random()*3/rate
        assert abs(quadrature_single(s,w,rate)-single_window_overlap(s,w,rate))<1e-12
        checks += 1
    for x in (0.1,0.3,0.5,0.8,0.95):
        epsilon=1.0
        cc=[]
        for n in range(1,1000):
            epsilon=-math.expm1(-x*epsilon)
            if epsilon==0: break
            if x**n>1e-300:
                cc.append(epsilon/x**n)
        assert len(cc)>10
        assert 0<cc[-1]<cc[0]<1
        assert cc[-1]/cc[-10]>0.9999 if len(cc)>20 else True
        checks += 3
    # Snapshot limit is rigorously algebraic, not exponential.
    e=1.0
    for n in range(1,100001):
        e = -math.expm1(-e)
    assert abs(100000*e-2)<0.001
    checks+=1
    print('PASS', checks, 'checks')
    print('example: rate=1, window=0.5, n=4')
    print('gap list', [round(g,12) for g in optimal_gaps(4,1,0.5)])
    print('optimal probability',round(values(4,1,0.5)[-1],12))

if __name__=='__main__':
    check()
