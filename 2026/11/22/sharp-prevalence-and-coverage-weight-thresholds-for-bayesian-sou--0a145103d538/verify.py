#!/usr/bin/env python3
"""Exact-rational checks for the wastewater-junction source-classification theorem.

Standard library only. A finite enumeration cannot replace the analytical proof.
"""
from fractions import Fraction as F
from itertools import combinations


def score(n, p, chosen, weight):
    """Direct enumeration of all states and observation-conditioned Bayes decisions."""
    evidence = {}
    for state in range(1 << n):
        probability = p**state.bit_count() * (1-p)**(n-state.bit_count())
        observed = tuple((state >> i) & 1 for i in range(n) if chosen & (1 << i))
        if chosen & (1 << n):
            observed += (int(state != 0),)
        if observed not in evidence:
            evidence[observed] = [F(0), [F(0) for _ in range(n)]]
        evidence[observed][0] += probability
        for i in range(n):
            if state & (1 << i):
                evidence[observed][1][i] += probability
    correct = sum(sum(max(pos, mass-pos) for pos in positives)
                  for mass, positives in evidence.values())
    covered = sum(
        p**state.bit_count() * (1-p)**(n-state.bit_count())
        for state in range(1 << n)
        if (chosen & (1 << n) and state != 0) or (chosen & state)
    )
    return correct/n + weight*covered


def formula(n, p, k, root, weight):
    q = 1-p
    accuracy = 1-p + F(k, n)*p
    coverage = 1-q**k
    if root:
        accuracy += F(n-k, n)*q**k*max(F(0), 2*p-1+q**(n-k)) if k<n else F(0)
        coverage = 1-q**n
    return accuracy + weight*coverage


def submodular(values, n):
    """Every distinct-element submodularity inequality, exact arithmetic."""
    for start in range(1 << (n+1)):
        for a, b in combinations(range(n+1), 2):
            if not (start & (1 << a)) and not (start & (1 << b)):
                if values[start | (1 << a)] + values[start | (1 << b)] < (
                    values[start] + values[start | (1 << a) | (1 << b)]
                ):
                    return False
    return True


def cutoff(n, p):
    q = 1-p
    if n == 2:
        return max(F(0), (1-3*p)/2)
    assert n == 3 and p >= F(1,5)
    d0 = 3*p*max(F(0), -1+3*p-p*p)
    d1 = 2*p*p*q
    d2 = p*q*q
    return max(F(0), (d1-d0)/(3*p), (d2-d1)/(3*p*q))


def run():
    checks = 0
    prevalences = [F(1,100), F(1,10), F(1,6), F(1,5), F(21,100),
                   F(22,100), F(1,4), F(1,3), F(19,50), F(2,5),
                   F(9,20), F(23,50), F(49,100)]
    weights = [F(0), F(1,1000), F(1,20), F(1,10), F(1,5), F(1), F(100)]
    for n in range(1, 6):
        for p in prevalences:
            for weight in (F(0), F(1), F(9,7)):
                for chosen in range(1 << (n+1)):
                    k = (chosen & ((1 << n)-1)).bit_count()
                    root = bool(chosen & (1 << n))
                    assert score(n, p, chosen, weight) == formula(n,p,k,root,weight)
                    checks += 1
    for n in (2,3):
        for p in prevalences:
            for weight in weights:
                values = [score(n,p,chosen,weight) for chosen in range(1 << (n+1))]
                expected = (p >= F(1,5) and weight >= cutoff(n,p)) if n==3 else weight >= cutoff(n,p)
                assert submodular(values,n) == expected, (n,p,weight,expected)
                checks += 1
            if n==2 or p >= F(1,5):
                boundary=cutoff(n,p)
                for weight, expected in [(boundary,True), (boundary+F(1,10000),True)]:
                    values=[score(n,p,mask,weight) for mask in range(1 << (n+1))]
                    assert submodular(values,n)==expected
                    checks+=1
                if boundary>0:
                    values=[score(n,p,mask,boundary-F(1,100000)) for mask in range(1 << (n+1))]
                    assert not submodular(values,n)
                    checks+=1
    p=F(1,10); root=1 << 3
    for weight in [F(0),F(1,7),F(1),F(1000)]:
        v=lambda mask: score(3,p,mask,weight)
        failure=v(root)+v(root|3)-v(root|1)-v(root|2)
        assert failure==F(3,200),failure
        checks+=1
    print(f'PASS: {checks} exact-rational assertions; 3/200 gap; all sensor subsets on tested grids.')


if __name__=='__main__':
    run()
