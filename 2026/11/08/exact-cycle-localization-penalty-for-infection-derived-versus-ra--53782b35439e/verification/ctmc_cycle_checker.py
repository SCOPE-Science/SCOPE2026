"""Exact-rational CTMC checks of cycle immunity localization formulas.
Run: python ctmc_cycle_checker.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb


def all_seed_means(n, beta, gamma):
    """Independent CTMC first-step recursion; result is count including immune vertices."""
    graph = tuple((1 << ((j - 1) % n)) | (1 << ((j + 1) % n)) for j in range(n))
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def solve(s, i):
        if not i:
            return Fraction(n - s.bit_count())
        events = []
        for j in range(n):
            bit = 1 << j
            if i & bit:
                events.append((gamma, s, i & ~bit))
            elif s & bit:
                k_infectious_neighbors = (graph[j] & i).bit_count()
                if k_infectious_neighbors:
                    events.append((beta*k_infectious_neighbors, s & ~bit, i | bit))
        total = sum(rate for rate, _, _ in events)
        return sum((Fraction(rate,total)*solve(ns,ni) for rate,ns,ni in events),Fraction())

    def mean_for_removed(removed):
        mask = sum(1 << j for j in removed)
        eligible = full & ~mask
        k = len(removed)
        L = n-k
        return (sum((solve(eligible & ~(1<<j),1<<j)-k for j in range(n)
                    if eligible & (1<<j)),Fraction())/L)
    return mean_for_removed


def formula(n, k, beta, gamma):
    p=Fraction(beta,beta+gamma)
    L=n-k
    adjacent=Fraction(1)+Fraction(2,L)*sum(((L-d)*p**d for d in range(1,L)),Fraction())
    random=Fraction(1)+Fraction(2,L)*sum((Fraction(n*comb(n-d-1,k),comb(n,k))*p**d
                                                 for d in range(1,L)),Fraction())
    gap=Fraction(2,L)*sum(((L-d-Fraction(n*comb(n-d-1,k),comb(n,k)))*p**d
                                   for d in range(1,L)),Fraction())
    return adjacent,random,gap


def run():
    checks=0
    for n in range(4,9):
        for beta,gamma in ((1,1),(2,3)):
            mean=all_seed_means(n,beta,gamma)
            for k in range(2,n-1):
                Econtig,Erandom,D=formula(n,k,beta,gamma)
                mean_contig=mean(tuple(range(k)))
                perms=combinations(range(n),k)
                average=sum((mean(s) for s in perms),Fraction())/comb(n,k)
                assert mean_contig==Econtig,(n,k,beta,gamma,'contig',mean_contig,Econtig)
                assert average==Erandom,(n,k,beta,gamma,'random',average,Erandom)
                assert mean_contig-average==D>0,(n,k,beta,gamma,'gap',D)
                assert sum((Fraction(2,n-k)*(n-k-d - Fraction(n*comb(n-d-1,k),comb(n,k)))
                            for d in range(1,n-k)), Fraction()) == Fraction((k-1)*(n-k-1),k+1)
                checks+=1
                print(f'n={n},k={k},beta={beta},gamma={gamma},E_adj={Econtig},E_rand={Erandom},gap={D}')
    assert checks == sum(2*(n-3) for n in range(4,9)) == 30
    print(f'PASS: {checks} independent exact CTMC comparisons, 30 saturated-endpoint identities.')

if __name__=='__main__':run()
