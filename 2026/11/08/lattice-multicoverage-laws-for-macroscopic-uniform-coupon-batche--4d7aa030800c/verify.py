"""Exact finite checks for uniform subset-drawing occupancy laws."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def full_distribution(n,d,c,t):
    draws = list(combinations(range(n),d))
    p = Fraction(1,len(draws))
    state = {tuple([0]*n):Fraction(1)}
    for _ in range(t):
        new=defaultdict(Fraction)
        for counts,weight in state.items():
            for group in draws:
                nxt=list(counts)
                for i in group:
                    if nxt[i]<c: nxt[i]+=1
                new[tuple(nxt)]+=weight*p
        state=new
    return state


def fixed_r_survival(n,d,c,t,r):
    # Independent exact reduction to r tagged coupons, via subset pattern weights.
    weights=defaultdict(int)
    for group in combinations(range(n),d):
        weights[tuple(i for i in range(r) if i in group)] += 1
    n_draws=comb(n,d)
    state={tuple([0]*r):Fraction(1)}
    for _ in range(t):
        new=defaultdict(Fraction)
        for counts,weight in state.items():
            for group,mult in weights.items():
                nxt=list(counts)
                for i in group:
                    if nxt[i]<c: nxt[i]+=1
                new[tuple(nxt)] += weight*Fraction(mult,n_draws)
        state=new
    return sum((v for counts,v in state.items() if max(counts)<c),Fraction(0))


def run():
    assertions=0
    for n in range(4,8):
        for d in range(1,n):
            for c in range(1,4):
                for t in range(0,6):
                    dist=full_distribution(n,d,c,t)
                    total=sum(dist.values(),Fraction(0))
                    assert total==1
                    assertions+=1
                    moment=[Fraction(0)]*4
                    success=Fraction(0)
                    for counts,weight in dist.items():
                        u=sum(v<c for v in counts)
                        if u==0:success+=weight
                        for r in range(1,4):
                            moment[r]+=weight*(factorial(u)//factorial(u-r) if u>=r else 0)
                    for r in range(1,4):
                        exact = fixed_r_survival(n,d,c,t,r)
                        assert moment[r] == factorial(n)//factorial(n-r)*exact,(n,d,c,t,r)
                        assertions+=1
                    h=sum(Fraction(comb(t,j)*d**j*(n-d)**(t-j),n**t) for j in range(min(c-1,t)+1))
                    assert moment[1]==n*h
                    assertions+=1
                    assert moment[2]+moment[1]-moment[1]*moment[1] <= moment[1]
                    assertions+=1
                    assert Fraction(0) <= success <= Fraction(1)
                    assertions+=1
    print(f"Exact finite occupancy and negative-covariance assertions passed: {assertions}")


if __name__=='__main__': run()
