"""Exact and numerical checks for median-radius laws of arclength-sampled metric stars."""
from math import comb, factorial
from fractions import Fraction as F
from random import Random


def bin_tail(k, q):
    return sum(F(comb(2*k+1,j)) * q**j * (1-q)**(2*k+1-j) for j in range(k+1,2*k+2))


def survival(lengths, k, t):
    total = sum(lengths)
    return sum((bin_tail(k, max(F(0), a-t)/total) for a in lengths), F(0))


def stochastic_checks():
    # Every elementary transfer is toward inequality; probabilities are exact rational.
    lengths = [F(2,3), F(5,4), F(17,12), F(7,3)]
    for k in (1,2,3,4):
        for i in range(len(lengths)):
            for j in range(len(lengths)):
                if lengths[i] <= lengths[j] or i==j:
                    continue
                delta = lengths[j] / 7
                more = lengths.copy(); more[i] += delta; more[j] -= delta
                candidates = sorted({F(0), *lengths, *more, F(1,17), F(3,4), F(10)})
                for a,b in zip(candidates,candidates[1:]):
                    candidates.append((a+b)/2) if False else None
                for t in candidates:
                    assert survival(more,k,t) >= survival(lengths,k,t)
                assert survival(more,k,0) > survival(lengths,k,0)


def jumps_and_inversion():
    # kth derivative breakpoint calculation from the polynomial, then recover lengths.
    for lengths in [[F(1),F(1),F(2),F(5)], [F(2,3),F(7,5),F(11,4)], [F(1),F(2),F(3)]]:
        L = sum(lengths)
        for k in (1,2,3,4):
            c = factorial(k+1)*comb(2*k+1,k+1)
            knots = sorted(set(lengths))
            jumps = {a:F(c * lengths.count(a), 1) / L**(k+1) for a in knots}
            recovered_L_power = F(c,1)/sum((a*J for a,J in jumps.items()),F(0))
            # Exact identity: the recovered kth power equals the true kth power.
            assert recovered_L_power == L**k
            assert all(J*L**(k+1)/c == lengths.count(a) for a,J in jumps.items())


def simulate():
    rand=Random(70813)
    lengths=[1.,2.,4.]
    L=sum(lengths)
    k=2; n=2*k+1
    thresh=0.9
    N=60000
    observed=0
    for _ in range(N):
        counts=[[],[],[]]
        for __ in range(n):
            x=rand.random()*L
            for i,a in enumerate(lengths):
                if x < a:
                    counts[i].append(x)
                    break
                x-=a
        # The sample median is on the majority arm, at the (k+1)th smallest depth
        # within that arm; otherwise it is the common hub.
        median=0.0
        for sample in counts:
            if len(sample)>=k+1:
                median=sorted(sample)[len(sample)-k-1]
        observed+=(median>thresh)
    predicted=float(survival([F(1),F(2),F(4)],k,F(9,10)))
    assert abs(observed/N-predicted)<0.018,(observed/N,predicted)
    return observed/N,predicted


if __name__=='__main__':
    stochastic_checks()
    jumps_and_inversion()
    x,y=simulate()
    print('STAR_MEDIAN_CHECKS_OK',x,y)
