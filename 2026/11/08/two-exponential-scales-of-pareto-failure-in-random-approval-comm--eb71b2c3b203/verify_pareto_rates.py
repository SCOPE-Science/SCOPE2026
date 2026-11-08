#!/usr/bin/env python3
"""Exact finite certificate for fair-coin approval-committee Pareto rates.

Run: python3 verify_pareto_rates.py
Requires only the Python 3 standard library.
"""
from itertools import combinations, product
from math import comb
from fractions import Fraction


def event_masks(m):
    """An event mask includes each of the 2**m approval rows satisfying #Y>=#X."""
    ans = {1: [], 2: []}
    for t in (1, 2):
        for x in combinations(range(m), t):
            for y in combinations([j for j in range(m) if j not in x], t):
                truth = 0
                for row in range(1 << m):
                    if sum((row >> a) & 1 for a in y) >= sum((row >> a) & 1 for a in x):
                        truth |= (1 << row)
                ans[t].append((x, y, truth))
    return ans


def verify_pair_intersections():
    # Eight named columns suffice for any two disjoint-pair events of orders <=2.
    a = event_masks(8)
    assert (len(a[1]), len(a[2])) == (56, 420)
    expected = {(1, 1): 160, (1, 2): 160, (2, 2): 152}
    for t, s in expected:
        maximum = -1
        for i, u in enumerate(a[t]):
            for j, v in enumerate(a[s]):
                if t == s and j <= i:
                    continue
                maximum = max(maximum, (u[2] & v[2]).bit_count())
        assert maximum == expected[(t, s)], (t, s, maximum)
        print('pair-intersection', t, s, maximum, '/256')


def committees(m, k):
    return list(combinations(range(m), k))


def direct_failure(profile, m, k):
    """Direct independent verification of Pareto dominated committee."""
    cs = committees(m, k)
    for u in cs:
        for v in cs:
            if u == v:
                continue
            vu = [sum((row >> j) & 1 for j in u) for row in profile]
            vv = [sum((row >> j) & 1 for j in v) for row in profile]
            if all(a <= b for a, b in zip(vu, vv)) and any(a < b for a, b in zip(vu, vv)):
                return True
    return False


def events_failure(profile, m, k):
    r = min(k, m-k)
    for t in range(1, r+1):
        for x in combinations(range(m), t):
            for y in combinations([j for j in range(m) if j not in x], t):
                differences = [sum((row >> a) & 1 for a in y) -
                               sum((row >> a) & 1 for a in x) for row in profile]
                if min(differences) >= 0 and max(differences) > 0:
                    return True
    return False


def rho(t):
    return Fraction(1, 2) + Fraction(comb(2*t, t), 2 * 4**t)


def probability_interval(m, k, n):
    r = min(k, m-k)
    n1 = m * (m-1)
    n2 = 6*comb(m, 4) if r >= 2 else 0
    other = sum(comb(m,t)*comb(m-t,t) for t in range(3, r+1))
    leading = n1 * rho(1)**n + n2 * rho(2)**n
    err = n1 * Fraction(1,2)**n + n2 * Fraction(3,8)**n + comb(n1+n2,2)*Fraction(5,8)**n + other*Fraction(21,32)**n
    return leading, err


def nonlocal_failure(profile, m, k):
    for x in range(m):
        for y in range(m):
            if x != y and all(((row >> y) & 1) >= ((row >> x) & 1) for row in profile):
                return False
    return direct_failure(profile, m, k)


def nonlocal_probability_interval(m, k, n):
    r = min(k, m-k)
    n1 = m * (m-1)
    n2 = 6 * comb(m, 4) if r >= 2 else 0
    other = sum(comb(m, t) * comb(m-t, t) for t in range(3, r+1))
    front = n2 * Fraction(11, 16)**n
    err = (n2 * Fraction(3,8)**n + comb(n2,2)*Fraction(19,32)**n
           + n1*n2*Fraction(5,8)**n + other*Fraction(21,32)**n)
    return front, err


def verify_profiles():
    cases = [(4,2,3), (4,1,3), (5,2,2), (5,3,2), (3,1,4)]
    for m,k,n in cases:
        failure_count=0
        nonlocal_count=0
        for profile in product(range(1<<m), repeat=n):
            a=direct_failure(profile,m,k)
            b=events_failure(profile,m,k)
            assert a==b,(m,k,n,profile,a,b)
            failure_count += a
            nonlocal_count += nonlocal_failure(profile, m, k)
        actual=Fraction(failure_count, 1<<(m*n))
        leading,err=probability_interval(m,k,n)
        assert abs(actual-leading) <= err, (m,k,n,actual,leading,err)
        local_front, local_error = nonlocal_probability_interval(m,k,n)
        assert abs(Fraction(nonlocal_count, 1<<(m*n))-local_front) <= local_error
        print('profile-census',m,k,n,'profiles',1<<(m*n),'fail',failure_count,
              'nonlocal',nonlocal_count,'prob',actual,'two-front',leading,'error_bound',err)


def verify_genuine_two_swap():
    # Candidate support sets across five voters are bit masks.
    support=(3,5,10,28)
    profile=tuple(sum(((support[j]>>i)&1)<<j for j in range(4)) for i in range(5))
    for i,j in combinations(range(4),2):
        assert (support[i] & support[j]) not in (support[i],support[j])
    x=(1,2); y=(0,3)
    u=[sum((row>>j)&1 for j in x) for row in profile]
    v=[sum((row>>j)&1 for j in y) for row in profile]
    assert (u,v)==([1,1,1,1,0],[1,1,1,1,1]), (u,v)
    assert direct_failure(profile,4,2)
    print('nonlocal-witness',support,profile,u,v)


def main():
    assert [rho(t) for t in (1,2,3)] == [Fraction(3,4),Fraction(11,16),Fraction(21,32)]
    for t in range(1,30):
        assert rho(t+1)<rho(t)
    verify_pair_intersections()
    verify_profiles()
    verify_genuine_two_swap()
    print('ALL EXACT CHECKS PASSED')


if __name__ == '__main__':
    main()
