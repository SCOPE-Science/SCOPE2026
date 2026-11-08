"""Exact checks for fixed-edge containment on finite cycle contact networks.
Run with Python >=3.9 using only the standard library.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for t in range(1,n-k+2):
            for rest in compositions(n-t,k-1):
                yield (t,)+rest


def tail_path_closed(l,h,p):
    if l<h:
        return Q(0)
    return p**(h-1)*(h+(l-h)*(h-(h-1)*p))


def expected_cluster_total(l,p):
    return Q(l)+2*sum((l-d)*p**d for d in range(1,l))


def direct_outbreak_numerator(lengths, h, p):
    # Each component is a path. Enumerate independent open bonds exactly.
    total=Q(0)
    for l in lengths:
        for mask in range(1<<(l-1)):
            opens=mask.bit_count()
            prob=p**opens*(1-p)**(l-1-opens)
            start=0
            for j in range(l-1):
                if not (mask>>j)&1:
                    size=j-start+1
                    if size>=h:
                        total+=size*prob
                    start=j+1
            size=l-start
            if size>=h:
                total+=size*prob
    return total


def direct_mean_numerator(lengths,p):
    total=Q(0)
    for l in lengths:
        for mask in range(1<<(l-1)):
            opens=mask.bit_count()
            prob=p**opens*(1-p)**(l-1-opens)
            groups=[]; size=1
            for j in range(l-1):
                if (mask>>j)&1:
                    size+=1
                else:
                    groups.append(size);size=1
            groups.append(size)
            total+=sum(r*r for r in groups)*prob
    return total


def check():
    checks=0
    for n in range(3,12):
        for k in range(2,n):
            caps=list(compositions(n,k))
            balanced=tuple(sorted([n//k+1]*(n%k)+[n//k]*(k-n%k)))
            concentrated=tuple(sorted([n-k+1]+[1]*(k-1)))
            for p in [Q(1,5),Q(1,2),Q(4,5)]:
                means=[sum(expected_cluster_total(l,p) for l in a) for a in caps]
                assert min(means)==sum(expected_cluster_total(l,p) for l in balanced)
                assert max(means)==sum(expected_cluster_total(l,p) for l in concentrated)
                for h in range(2,n+1):
                    tails=[sum(tail_path_closed(l,h,p) for l in a) for a in caps]
                    if n<=k*(h-1):
                        assert min(tails)==0
                    else:
                        optimal=tuple([n-(k-1)*(h-1)]+[h-1]*(k-1))
                        best=sum(tail_path_closed(l,h,p) for l in optimal)
                        assert min(tails)==best
                        assert all(t!=best or sorted(a)==sorted(optimal) for a,t in zip(caps,tails))
                    checks+=1
    brute_cases=0
    for n in range(3,9):
        for k in range(2,n):
            for lengths in compositions(n,k):
                for p in [Q(1,3),Q(3,4)]:
                    assert direct_mean_numerator(lengths,p)==sum(expected_cluster_total(l,p) for l in lengths)
                    for h in range(2,n+1):
                        assert direct_outbreak_numerator(lengths,h,p)==sum(tail_path_closed(l,h,p) for l in lengths)
                        brute_cases+=1
    for p in [Q(1,10),Q(1,2),Q(3,4),Q(9,10)]:
        t51=(9-4*p)*p*p
        t42=(6-2*p)*p*p
        t33=6*p*p
        assert t42 < t51 and t42<t33
        assert (t51>t33)==(p<Q(3,4)) if p!=Q(3,4) else t51==t33
    print('PASS: partition extremizers, mean, and tails for',checks,'parameter cases')
    print('PASS: independently enumerated',brute_cases,'fixed-size outbreak probabilities')
    print('PASS: six-vertex three-case phase transition at p=3/4')

if __name__ == '__main__':
    check()
