"""Exact finite checks for cherry count versus total external length in Kingman's coalescent.

The coalescent has independent exponential holding times of rate k(k-1)/2.
All arithmetic below uses stdlib Fraction. Run: python3 verify_coalescent_cherry_external.py
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations


def coalescent_dp(n):
    # State is number b of singleton lineages; values (prob, sum C, sum E, sum CE).
    # E is the conditional mean external-branch length, given the merger history.
    D = {n: (F(1), F(0), F(0), F(0))}
    for k in range(n, 1, -1):
        nxt = defaultdict(lambda: (F(0),) * 4)
        for b, (p, c, e, ce) in D.items():
            hold = F(2 * b, k * (k - 1))
            for removed, ways in ((2, b * (b - 1)),
                                   (1, 2 * b * (k - b)),
                                   (0, (k - b) * (k - b - 1))):
                if ways == 0:
                    continue
                q = F(ways, k * (k - 1))
                x = int(removed == 2)
                terms = (p, c + p*x, e + p*hold,
                         ce + hold*c + x*e + p*x*hold)
                old = nxt[b - removed]
                nxt[b - removed] = tuple(old[t] + q * terms[t] for t in range(4))
        D = nxt
    prob, ec, ee, ece = [sum(z[i] for z in D.values()) for i in range(4)]
    assert prob == 1
    return ec, ee, ece - ec * ee


def enumerated_histories(n):
    """Sum over every labeled pair-merger history; independent from singleton-count DP."""
    total_weight = F(1)
    sum_c = sum_e = sum_ce = F(0)
    visits = 0
    def rec(blocks, cherries, external_mean, probability):
        nonlocal total_weight, sum_c, sum_e, sum_ce, visits
        k = len(blocks)
        if k == 1:
            visits += 1
            sum_c += probability * cherries
            sum_e += probability * external_mean
            sum_ce += probability * cherries * external_mean
            return
        b = sum((x & (x-1)) == 0 for x in blocks)
        external_mean += F(2*b, k*(k-1))
        step = probability * F(2, k*(k-1))
        for i, j in combinations(range(k), 2):
            a, d = blocks[i], blocks[j]
            new_c = cherries + int((a & (a-1)) == 0 and (d & (d-1)) == 0)
            rem = tuple(blocks[t] for t in range(k) if t not in (i,j))
            rec(rem + (a|d,), new_c, external_mean, step)
    rec(tuple(1 << i for i in range(n)), 0, F(0), F(1))
    return visits, sum_c, sum_e, sum_ce - sum_c*sum_e


def prefix_cross_checks(n):
    """Compute Cov(C_final,B_k) independently from the combinatorial formula.

    Future expected cherries conditional on k surviving blocks and b untouched
    leaves is b(b-1)/[3(k-1)] for n>=3 (and b<2 at level k=2).
    """
    D = {n: (F(1), F(0))}
    for k in range(n, 1, -1):
        tot_p = tot_c = tot_b = tot_bc = F(0)
        for b, (p, cpast) in D.items():
            future = F(b*(b-1),3*(k-1))
            tot_p += p
            tot_b += p*b
            tot_c += cpast + p*future
            tot_bc += b*(cpast + p*future)
        got = tot_bc - tot_c*tot_b
        expected = -F(k*(k-1)*(n-k)*(n-k-1),3*(n-1)*(n-2)*(n-3))
        assert tot_p == 1 and got == expected, (n,k,got,expected)
        nxt = defaultdict(lambda:(F(0),F(0)))
        for b,(p,c) in D.items():
            for d,ways in ((2,b*(b-1)),(1,2*b*(k-b)),(0,(k-b)*(k-b-1))):
                if ways:
                    q=F(ways,k*(k-1)); op,oc=nxt[b-d]
                    nxt[b-d]=(op+q*p,oc+q*(c+(d==2)*p))
        D=nxt


def main():
    history_count=0
    for n in range(2,8):
        visits, c, e, cov = enumerated_histories(n)
        history_count += visits
        dc,de,dcov = coalescent_dp(n)
        assert (c,e,cov)==(dc,de,dcov), (n,cov,dcov)
        assert e==2 and c == (F(n,3) if n>=3 else F(1))
        assert cov == (F(-2,9) if n>=4 else F(0)), (n,cov)
    checked=0
    for n in range(4,61):
        prefix_cross_checks(n)
        c,e,cov=coalescent_dp(n)
        assert c==F(n,3) and e==2 and cov==F(-2,9),n
        checked+=n-1
    print('PASS: exhaustive distinct-label histories n=2..7:', history_count)
    print('PASS: exact dynamic covariance n=2..60 (including n=2,3 exceptions)')
    print('PASS: exact Cov(C,B_k) checks:', checked)

if __name__=='__main__': main()
