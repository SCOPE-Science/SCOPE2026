"""Exact checks for odd-cycle two-class stochastic trace probing.
Run: python check.py (Python >=3.9; standard library only).
These finite tests supplement, but do not replace, the proof.
"""
from fractions import Fraction
from itertools import product


def normalized_weights(n, r):
    return [Fraction(0)] + [(r**d + r**(n-d))**2 for d in range(1, n)]


def variance_normalized(spins, weights):
    n = len(spins)
    return 4 * sum((weights[j-i] for i in range(n) for j in range(i+1, n)
                    if spins[i] == spins[j]), Fraction(0))


def claimed_minimum(n, weights):
    m = (n-1)//2
    return 2*sum(((n+(-1)**d*(n-2*d))*weights[d] for d in range(1,m+1)), Fraction(0))


def claimed_gap(n, weights):
    if n == 5:
        return 8*(weights[1]-weights[2])
    return 8*(weights[1]-2*weights[2]+weights[3])


def windows(spins,k):
    n=len(spins)
    return sum(sum(spins[(i+j)%n] for j in range(k))**2 for i in range(n))


def test():
    cases = 0
    partitions = 0
    recurrences = 0
    for n in [5,7,9,11,13]:
        m=(n-1)//2
        optimal=tuple((-1)**i for i in range(n))
        almost=list(optimal)
        almost[2]*=-1
        almost[3]*=-1
        assert sum(optimal)**2==sum(almost)**2==1
        assert sum(optimal[i]==optimal[(i+1)%n] for i in range(n))==1
        assert sum(almost[i]==almost[(i+1)%n] for i in range(n))==3
        assert windows(almost,2)==windows(optimal,2)+8
        for k in range(3,m+1):
            assert windows(almost,k)==windows(optimal,k)
        for r in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
            weights=normalized_weights(n,r)
            best=claimed_minimum(n,weights)
            gap=claimed_gap(n,weights)
            assert variance_normalized(optimal,weights)==best
            assert variance_normalized(almost,weights)==best+gap
            assert gap>0
            for bits in product((-1,1), repeat=n-1):
                s=(1,)+bits
                value=variance_normalized(s,weights)
                assert value >= best
                matches=sum(s[i]==s[(i+1)%n] for i in range(n))
                if matches==1:
                    assert value==best
                else:
                    assert value>=best+gap
                partitions+=1
            cases+=1
            # Green kernel recurrence, B_{ij} = c*(r^d+r^(n-d)).
            c=1/((1/r-r)*(1-r**n))
            G=[c*(r**d+r**(n-d)) for d in range(n)]
            mu=r+1/r-2
            for d in range(n):
                assert (mu+2)*G[d]-G[(d+1)%n]-G[(d-1)%n]==(1 if d==0 else 0)
                recurrences+=1
    print(f'PASS: {cases} exact parameter cases, {partitions} exact spin tests, '
          f'{recurrences} Green recurrence tests; sharp nonoptimal variance gap.')


if __name__=='__main__':
    test()
