"""Reproducible diagnostics for a two-sensitivity pollen-carryover allocation model.

The mathematical proof is independent of these finite computations.
Python 3, standard library only.
"""
import itertools
import math
import random


def h(x, low, high):
    return math.exp(-low*x) - math.exp(-high*x)


def transition_root(c, low, high):
    """Bisect the positive nonzero root of h(x)=h(c*x)."""
    lo, hi = 1e-12, 1.0
    while h(c*hi, low, high) <= h(hi, low, high):
        hi *= 2.0
        if hi > 1e8:
            raise AssertionError('no root bracket')
    for _ in range(140):
        mid = (lo+hi)/2
        if h(c*mid,low,high) > h(mid,low,high):
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def value(high_positions, n, low, high, q, load):
    total = 0.0
    for j in range(n):
        sensitivity = high if j in high_positions else low
        deposit = (1-q)*load*q**j
        total += -math.expm1(-sensitivity*deposit)
    return total


def predicted_starts(n, r, low, high, q, load):
    root = transition_root(q**r,low,high)
    thresholds = [root/((1-q)*q**j) for j in range(n-r)]
    return 1 + sum(load>x for x in thresholds), thresholds


def run():
    checks = 0
    rng = random.Random(314159)
    for n in range(2,10):
        for r in range(1,n):
            for _ in range(13):
                low = rng.uniform(.2,2.1)
                high = low+rng.uniform(.1,3.2)
                q = rng.uniform(.22,.89)
                root = transition_root(q**r,low,high)
                assert abs(h(root,low,high)-h(q**r*root,low,high))<1e-12
                checks += 1
                for k in range(n-r+1):
                    _, thresholds = predicted_starts(n,r,low,high,q,1.0)
                    if k==0:
                        load=thresholds[0]*.5
                    elif k==n-r:
                        load=thresholds[-1]*1.5
                    else:
                        load=math.sqrt(thresholds[k-1]*thresholds[k])
                    start,_=predicted_starts(n,r,low,high,q,load)
                    assert start==k+1
                    best=-1.0
                    winners=[]
                    for combo in itertools.combinations(range(n),r):
                        score=value(set(combo),n,low,high,q,load)
                        if score>best+2e-13:
                            best=score;winners=[combo]
                        elif abs(score-best)<2e-13:
                            winners.append(combo)
                    expected=tuple(range(start-1,start-1+r))
                    assert winners==[expected], (n,r,k,winners,expected)
                    checks+=2
                for k,thresh in enumerate(thresholds):
                    left=value(set(range(k,k+r)),n,low,high,q,thresh)
                    right=value(set(range(k+1,k+1+r)),n,low,high,q,thresh)
                    assert abs(left-right)<5e-12
                    checks += 1
    phi=(1+5**.5)/2
    low,high,q,n,r=1.0,2.0,2**-.5,6,2
    root=transition_root(q**r,low,high)
    assert abs(root-2*math.log(phi))<1e-12
    checks+=1
    transitions=[root/((1-q)*q**j) for j in range(n-r)]
    for j,th in enumerate(transitions):
        if j: assert abs(th/transitions[j-1]-1/q)<1e-12
        checks+=1
    load=8.0
    start,_=predicted_starts(n,r,low,high,q,load)
    optimal=value(set(range(start-1,start-1+r)),n,low,high,q,load)
    naive=value({0,1},n,low,high,q,load)
    print('Assertions passed:',checks)
    print('Golden-ratio transition:',format(root,'.15f'))
    print('Example transition loads:',[round(t,9) for t in transitions])
    print('At load 8: optimal high-quality one-based positions:',list(range(start,start+r)))
    print('Optimal expected successes:',format(optimal,'.12f'))
    print('First-two-high expected successes:',format(naive,'.12f'))
    print('Difference:',format(optimal-naive,'.12f'))

if __name__=='__main__':
    run()
