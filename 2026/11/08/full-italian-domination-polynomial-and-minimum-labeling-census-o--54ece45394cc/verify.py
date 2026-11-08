#!/usr/bin/env python3
"""Finite reproducibility checks for Italian-domination enumerators of sunlet graphs."""
from itertools import product
from collections import Counter
from math import ceil


def weight_polynomial(n):
    """Transfer computation indexed by pairs of successive cycle-center labels."""
    assert n >= 3
    states = list(product(range(3), repeat=2))
    N = 4*n+1
    answer = [0]*N
    for start in states:
        current = {start: [1]+[0]*(N-1)}
        for _ in range(n):
            nxt = {}
            for (a,b), poly in current.items():
                for c in range(3):
                    dst=(b,c)
                    d=nxt.setdefault(dst,[0]*N)
                    if b==0:
                        opts=(2,1) if a+c>=1 else (2,)
                    elif b==1:
                        opts=(2,3)
                    else:
                        opts=(2,3,4)
                    for wt in opts:
                        for j, count in enumerate(poly[:N-wt]):
                            if count: d[j+wt] += count
            current=nxt
        for j, count in enumerate(current.get(start, [])):
            answer[j]+=count
    return answer


def direct_polynomial(n):
    """Whole-graph enumeration without local-state reductions."""
    ans=Counter()
    for labels in product(range(3),repeat=2*n):
        good=True
        for i in range(n):
            center, leaf=labels[i],labels[n+i]
            if leaf==0 and center<2:
                good=False; break
            if center==0 and leaf+labels[(i-1)%n]+labels[(i+1)%n]<2:
                good=False; break
        if good:
            ans[sum(labels)]+=1
    return ans


def predicted_optima(n):
    k=(n+2)//3
    if n%3==0: return 3*2**k
    if n%3==2: return n*2**k
    return n*(k+2)*2**(k-1)


def direct_minimum_count(n):
    """Enumerate all low-cost column types independently of the polynomial transfer."""
    types=((0,1),(0,2),(1,1),(2,0))
    best=10*n; count=0; b_count=0
    for sel in product(range(4),repeat=n):
        w=sum(sum(types[i]) for i in sel)
        if w>best: continue
        if any(types[sel[i]][0]==0 and
               types[sel[i]][1]+types[sel[(i-1)%n]][0]+types[sel[(i+1)%n]][0]<2
               for i in range(n)):
            continue
        if w<best:
            best=w; count=0; b_count=0
        count+=1
        b_count+=(1 in sel)
    return best,count,b_count


def main():
    for n in range(3,7):
        a=weight_polynomial(n)
        b=direct_polynomial(n)
        assert {j:v for j,v in enumerate(a) if v} == dict(b),(n,a,b)
        print('WHOLE_GRAPH_POLYNOMIAL_OK',n,'total',sum(a))
    for n in range(3,17):
        poly=weight_polynomial(n)
        lo=next(i for i,c in enumerate(poly) if c)
        assert lo == (4*n+2)//3,(n,lo)
        assert poly[lo] == predicted_optima(n),(n,poly[lo],predicted_optima(n))
        print('TRANSFER_MINIMUM_AND_COUNT_OK',n,lo,poly[lo])
    for n in range(3,10):
        lo,count,bs=direct_minimum_count(n)
        assert lo==(4*n+2)//3 and count==predicted_optima(n),(n,lo,count)
        expected_b=n*2**(((n+2)//3)-1) if n%3==1 else 0
        assert bs==expected_b,(n,bs,expected_b)
        print('INDEPENDENT_OPTIMAL_COLUMN_CENSUS_OK',n,count,bs)
    print('VERIFY_OK')

if __name__ == '__main__': main()
