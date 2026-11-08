#!/usr/bin/env python3
"""Exact finite checks for two-team bipartite-friend swap stability.
All payoffs are computed from labeled agents, not the theorem's inequalities.
"""
from itertools import combinations
from math import comb


def predicted(s, t, a, x):
    d = s - t
    if not (max(0, a-t) <= x <= min(a, s)):
        raise ValueError('Infeasible occupancy')
    strictly = a-1 <= 2*x <= a+d+1
    weakly = (a-1 <= 2*x <= a+1) if d == 0 else (a-1 < 2*x < a+d+1)
    def welfare(y):
        return 2*(y*(s-y)+(a-y)*(t-a+y))
    opt = max(welfare(y) for y in range(max(0,a-t), min(a,s)+1))
    transf = welfare(x) == opt
    return (strictly, weakly, transf, welfare(x))


def brute(s, t, a, side1):
    n = s+t
    group1 = set(side1)
    group = [0 if i in group1 else 1 for i in range(n)]
    def utility(i, assign):
        return sum(1 for j in range(n) if j != i and assign[i] == assign[j] and ((i < a) != (j < a)))
    old = [utility(i, group) for i in range(n)]
    strict = weak = transf = True
    for i in range(n):
        for j in range(i+1, n):
            if group[i] == group[j]:
                continue
            changed = group[:]
            changed[i], changed[j] = changed[j], changed[i]
            di = utility(i, changed)-old[i]
            dj = utility(j, changed)-old[j]
            if di > 0 and dj > 0:
                strict = False
            if (di > 0 and dj >= 0) or (dj > 0 and di >= 0):
                weak = False
            if di+dj > 0:
                transf = False
    return (strict, weak, transf, sum(old))


def main():
    cases = assignments = payoff_checks = 0
    examples = {}
    by_n = {}
    for n in range(2, 11):
        for s in range((n+1)//2, n):
            t = n-s
            for a in range(1, n):
                cases += 1
                count = [0, 0, 0]
                formula_count = [0, 0, 0]
                for x in range(max(0,a-t),min(a,s)+1):
                    result = predicted(s,t,a,x)
                    mult = comb(a,x)*comb(n-a,s-x)
                    for k in range(3):
                        formula_count[k] += mult*result[k]
                for members in combinations(range(n),s):
                    assignments += 1
                    x = sum(i<a for i in members)
                    observed=brute(s,t,a,members)
                    expected=predicted(s,t,a,x)
                    payoff_checks += 1
                    if observed != expected:
                        raise AssertionError((s,t,a,members,observed,expected))
                    for k in range(3):
                        count[k] += observed[k]
                assert count == formula_count, (n,s,t,a,count,formula_count)
                if count[0] > count[1]:
                    examples.setdefault('strict_not_weak',(n,s,t,a,count))
                if count[1] > count[2]:
                    examples.setdefault('weak_not_transferable',(n,s,t,a,count))
                by_n[n] = by_n.get(n,0)+1
    assert examples['strict_not_weak'][0] == 3
    assert examples['weak_not_transferable'][0] == 5
    print('PASS: %d parameter settings; %d complete labeled assignments; %d explicit payoff comparisons.'%(cases,assignments,payoff_checks))
    print('Sharp first gaps:',examples)
    print('Parameter settings by population:',by_n)
    for s,t,a in [(4,1,2),(2,1,1),(8,4,6),(3,3,3)]:
        print('sample',s,t,a, [(x,predicted(s,t,a,x)) for x in range(max(0,a-t),min(a,s)+1)])

if __name__ == '__main__':
    main()
