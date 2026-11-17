#!/usr/bin/env python3
"""Independent exact enumerator and formula checks for root/leaf covariance in weighted recursive trees."""
from fractions import Fraction
from itertools import product


def enumerate_tree(n, theta):
    """Sum over all independent parent choices with exact rational probabilities."""
    acc = [Fraction(0) for _ in range(4)]
    local = {i: Fraction(0) for i in range(3,n+1)}
    for parents in product(*(range(1,i) for i in range(2,n+1))):
        probability = Fraction(1)
        for i, parent in enumerate(parents, 2):
            probability *= (theta if parent == 1 else 1)/(theta+i-2)
        degree = sum(parent == 1 for parent in parents)
        chosen = set(parents)
        leaves = sum(i not in chosen for i in range(2,n+1))
        acc[0] += probability
        acc[1] += probability * degree
        acc[2] += probability * leaves
        acc[3] += probability * degree * leaves
        for i in local:
            if parents[i-2] == 1:
                local[i] += probability * leaves
    return acc, local


def formula(n, theta):
    return theta * (n-1)*(n-2)/(2*(theta+n-2)**2)


def verify():
    checks = 0
    parameters = [Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(7,3),Fraction(5),Fraction(17)]
    for n in range(2,9):
        for theta in parameters:
            (total, ed, el, edl), local=enumerate_tree(n,theta)
            assert total == 1, (n,theta,total)
            checks += 1
            expected_degree = sum((theta/(theta+i-2) for i in range(2,n+1)),Fraction(0))
            expected_leaves = (n-1)*(n-2+2*theta)/(2*(theta+n-2))
            assert ed == expected_degree, (n,theta,ed,expected_degree)
            checks += 1
            assert el == expected_leaves, (n,theta,el,expected_leaves)
            checks += 1
            actual = edl-ed*el
            assert actual == formula(n,theta),(n,theta,actual,formula(n,theta))
            checks += 1
            for i in range(3,n+1):
                root_prob = theta/(theta+i-2)
                profile = theta * (i-2)*(2*theta+i-3) / (2*(theta+n-2)*(theta+i-2)*(theta+i-3))
                assert local[i]-root_prob*el == profile,(n,theta,i,local[i]-root_prob*el,profile)
                checks += 1
    for n in range(3,150):
        m=Fraction(n-2)
        optimum=Fraction(n-1,8)
        assert formula(n,m)==optimum
        checks += 1
        for theta in [Fraction(1,100),Fraction(1),m/4,m/2,m*2,m*5,Fraction(10000)]:
            if theta != m:
                assert formula(n,theta) < optimum
                checks += 1
    print('PASS',checks,'independent exact assertions')

if __name__ == '__main__':
    verify()
