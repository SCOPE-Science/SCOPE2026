"""Exact-rational checks for a two-round, infection-triggered warning model.

Requires only Python 3 standard library. These finite tests complement, not replace,
the analytic proof of the all-parameter theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose


def theoretical(k, residuals, p):
    m = len(residuals)
    return 1 + (k+1)*p + m*p*p - p**(k+2)*sum(1-r for r in residuals)


def enumerated(k, residuals, p):
    # Sum over ALL primary mediator and sentinel successes, then independent
    # terminal infections. No analytic covariance/moment formula is used.
    m = len(residuals)
    exp = F(0)
    for initial_bits in product((0, 1), repeat=k+1):
        n_success = sum(initial_bits)
        weight = p**n_success * (1-p)**(k+1-n_success)
        alert = all(initial_bits[1:])
        mediator = initial_bits[0]
        probabilities = [p * (r if alert else 1) if mediator else F(0)
                         for r in residuals]
        for terminal_bits in product((0, 1), repeat=m):
            conditional = F(1)
            for bit, t in zip(terminal_bits, probabilities):
                conditional *= t if bit else (1-t)
            exp += weight*conditional*(1+n_success+sum(terminal_bits))
    return exp


def derivative(k, residuals, p):
    m=len(residuals)
    h=sum(1-r for r in residuals)
    return (k+1)+2*m*p-(k+2)*h*p**(k+1)


def criterion(k, residuals):
    return derivative(k, residuals, F(1)) < 0


def run_checks():
    count=0
    for k in range(1,5):
        for m in range(1,5):
            configurations = [
                [F(0)]*m, [F(1)]*m,
                [F(i, m+1) for i in range(1, m+1)],
                [F((2*i+1)%5, 5) for i in range(m)],
                [F(1,2)]*m,
            ]
            for residuals in configurations:
                for p in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
                    assert enumerated(k,residuals,p)==theoretical(k,residuals,p)
                    count+=1
    # A finite grid checks derivative signs and unique reversal in parameter examples.
    for k in range(1,9):
        for m in range(1,13):
            for r in (F(0),F(1,8),F(1,3),F(1,2),F(2,3),F(1)):
                residuals=[r]*m
                values=[derivative(k,residuals,F(j,100)) for j in range(101)]
                negatives=[j for j,v in enumerate(values) if v<0]
                if criterion(k,residuals):
                    assert negatives and negatives[-1]==100
                    assert negatives==list(range(negatives[0],101))
                    assert values[0]>0
                else:
                    assert not negatives
                count+=len(values)
    # Minimality inside the specified family, not among arbitrary networks.
    witnesses=[]
    for n in range(3,10):
        for k in range(1,n-2):
            m=n-2-k
            if m>=1 and criterion(k,[F(0)]*m):
                witnesses.append((n,k,m))
    assert min(n for n,k,m in witnesses)==6
    assert {(k,m) for n,k,m in witnesses if n==6}=={(1,3),(2,2)}
    count+=2
    return count

if __name__=='__main__':
    print('EXACT_RATIONAL_ASSERTIONS',run_checks())
    print('WITNESSES k=1,m=3 and k=2,m=2 satisfy strict high-transmission reversal')
