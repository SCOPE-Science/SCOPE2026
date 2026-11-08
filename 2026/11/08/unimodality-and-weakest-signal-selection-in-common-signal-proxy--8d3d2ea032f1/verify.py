"""Exact tests for the finite-state, one-expert delegation theorem.
Run: python3 verify.py
Only Python standard library is used.
"""
from fractions import Fraction as Q
from math import comb, log
from random import Random


def tail(m, p, k):
    return sum(Q(comb(m, j)) * p**j * (1 - p)**(m-j)
               for j in range(max(0, k), m+1))


def success(h, t, states):
    if t >= h:
        return sum(pi*r for pi, q, r in states)
    m = 2*h - t
    return sum(pi*(r*tail(m, q, h-t) + (1-r)*tail(m, q, h+1))
               for pi, q, r in states)


def exact_increment(h, t, states):
    assert 0 <= t < h
    return Q(comb(2*h-t-1, h))*sum(
        pi*(q*(1-q))**(h-t-1) *
        (r*(1-q)**(t+2) - (1-r)*q**(t+2))
        for pi, q, r in states)


def all_values(h, states):
    return [success(h,t,states) for t in range(h+1)]


def one_peak(xs):
    ds = [b-a for a,b in zip(xs,xs[1:])]
    return not any(ds[i] < 0 and any(d > 0 for d in ds[i+1:])
                   for i in range(len(ds)))


def main():
    rng=Random(20261105)
    tests=0
    for h in range(1,9):
        for z in range(160):
            weights=[rng.randint(1,9) for _ in range(3)]
            total=sum(weights)
            states=[]
            for weight in weights:
                q=Q(rng.randint(51,95),100)
                r=Q(rng.randint(1,99),100)
                states.append((Q(weight,total),q,r))
            vals=all_values(h,states)
            assert one_peak(vals), (h, states, vals)
            for t in range(h):
                assert vals[t+1]-vals[t]==exact_increment(h,t,states)
                tests+=1
    assert tests==5760

    # Sharp boundary without the nonexpert competence hypothesis.
    bad=[(Q(1,5),Q(1,20),Q(1,4)),
         (Q(4,5),Q(9,10),Q(19,20))]
    vals=all_values(2,bad)
    assert vals==[Q(6366953,8000000), Q(15911,20000), Q(81,100)]
    assert vals[0]>vals[1]<vals[2]

    # A state with prior only 1/1000 controls the optimum at large population.
    rare=[(Q(1,1000),Q(11,20),Q(9,10)),
          (Q(999,1000),Q(4,5),Q(9,10))]
    target= int(log(9)/log(Q(11,9))-1)
    assert target==9
    for h in [100,150,200]:
        d=[exact_increment(h,t,rare) for t in range(14)]
        assert all(x>0 for x in d[:9])
        assert all(x<0 for x in d[9:])
        print('rare-state optimum',h,'=',target)

    # Confirm homogenous single-state integer cutoff, including negative or zero gain.
    for q in [Q(51,100),Q(3,5),Q(4,5)]:
        for r in [Q(1,5),Q(3,5),Q(9,10),Q(99,100)]:
            alpha=log(float(r/(1-r)))/log(float(q/(1-q)))
            if abs(alpha-round(alpha))<1e-10:continue
            expected=max(0, int((alpha-1)//1))
            for h in [max(expected+5,10)]:
                d=[exact_increment(h,t,[(Q(1),q,r)]) for t in range(h)]
                actual=next((i for i,x in enumerate(d) if x<0),h)
                assert actual==expected,(q,r,expected,actual)
    print('PASS', tests, 'exact direct-increment comparisons; 1280 one-peak exact cases;',
          'three large-population rare-state checks;',
          'one exact counterexample and 12 scalar parameter pairs')

if __name__=='__main__': main()
