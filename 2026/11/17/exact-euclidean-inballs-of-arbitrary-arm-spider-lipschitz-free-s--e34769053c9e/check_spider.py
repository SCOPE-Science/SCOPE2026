"""Exact arithmetic checks for the spider-transportation inball theorem.

Run: python check_spider.py
Only finite instances are enumerated; the general theorem has a separate proof.
"""
from fractions import Fraction
from itertools import product, combinations_with_replacement


def rank(rows):
    a = [[Fraction(t) for t in row] for row in rows]
    if not a:
        return 0
    p = 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(p, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[p], a[pivot] = a[pivot], a[p]
        z = a[p][j]
        a[p] = [t / z for t in a[p]]
        for k in range(len(a)):
            if k != p and a[k][j]:
                z = a[k][j]
                a[k] = [t-z*s for t, s in zip(a[k], a[p])]
        p += 1
        if p == len(a):
            break
    return p


def proposed(lengths):
    N = 1 + sum(lengths)
    ws = [L*(L+1)//2 for L in lengths]
    us = [L*(L+1)*(2*L+1)//6 for L in lengths]
    ss = list(product((-1, 1), repeat=len(lengths)))
    delta = min(abs(sum(x*w for x,w in zip(s,ws))) for s in ss)
    winning = [s for s in ss if abs(sum(x*w for x,w in zip(s,ws))) == delta]
    return N*sum(us)-delta**2, winning, len(lengths) and (N-1-rank(winning))


def enumerate_all(lengths):
    N = 1 + sum(lengths)
    max_scaled = -1
    max_profiles = []
    for eps in product((-1,1), repeat=N-1):
        vals = [0]
        off = 0
        full = []
        for L in lengths:
            y=0
            gradients=eps[off:off+L]
            for e in gradients:
                y += e
                vals.append(y)
            full.append(len(set(gradients))==1)
            off+=L
        scaled=N*sum(v*v for v in vals)-sum(vals)**2
        if scaled > max_scaled:
            max_scaled, max_profiles = scaled, [(vals,all(full))]
        elif scaled==max_scaled:
            max_profiles.append((vals,all(full)))
    if not all(full for _,full in max_profiles):
        raise AssertionError(f'non-monotone maximizer {lengths}')
    # Integer vectors N * (v - mean(v)) are proportional to polar normals.
    centered = [[N*v-sum(vals) for v in vals] for vals,_ in max_profiles]
    center_dim = (N-1) - rank(centered)
    return max_scaled, len(max_profiles), center_dim


def test_arm_variance():
    checks=0
    for L in range(1,10):
        W=L*(L+1)//2
        U=L*(L+1)*(2*L+1)//6
        for eps in product((-1,1),repeat=L):
            y=0; vals=[]
            for x in eps:
                y+=x;vals.append(y)
            S=sum(vals); Q=sum(x*x for x in vals)
            assert (L+1)*(U-Q) >= W*W-S*S
            if len(set(eps))>1:
                assert (L+1)*(U-Q)>W*W-S*S
            checks+=1
    print('ARM_PATH_VARIANCE_INTEGER_IDENTITY_PASS',checks)


def test_all_profiles():
    profiles=[]
    for q in range(3,6):
        for ls in combinations_with_replacement(range(1,6),q):
            if sum(ls) <= 11:
                profiles.append(ls)
    profiles += [(1,2,3,4),(1,1,2,3,4),(1,2,5),(3,3,3),(1,1,1,1,1,1,1)]
    seen=set(); total=0; count=0
    for ls in profiles:
        if ls in seen: continue
        seen.add(ls)
        expected, winning, dim=proposed(ls)
        got, t, d=enumerate_all(ls)
        assert (got,t,d)==(expected,len(winning),dim),(ls,(got,t,d),(expected,len(winning),dim))
        count+=1
        total+=2**sum(ls)
    print('SPIDER_ALL_SIGNED_EDGE_POTENTIALS_PASS', 'profiles='+str(count),'potentials='+str(total))


def test_partition_dp():
    from collections import defaultdict
    cases=0
    for q in range(3,10):
        for ls in combinations_with_replacement(range(1,7),q):
            if sum(ls)>20: continue
            ws=[L*(L+1)//2 for L in ls]
            dp={0:1}
            for w in ws:
                nd=defaultdict(int)
                for x,v in dp.items():
                    nd[x+w]+=v
                    nd[x-w]+=v
                dp=nd
            best=min(map(abs,dp))
            num=sum(m for x,m in dp.items() if abs(x)==best)
            pred,winning,_=proposed(ls)
            assert num==len(winning)
            cases+=1
    print('TRIANGULAR_PARTITION_COUNTS_PASS', 'profiles='+str(cases))


if __name__=='__main__':
    test_arm_variance()
    test_all_profiles()
    test_partition_dp()
    print('ARBITRARY_ARM_SPIDER_THEOREM_FINITE_CHECKS_PASS')
