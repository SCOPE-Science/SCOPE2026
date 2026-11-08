"""Reproducible finite checks for the shifted five triangular-offset semigroup theorem.
Run with Python 3.10+; no external dependencies.
"""
import heapq
import json

COINS = (1, 3, 6, 10)
K_BY_RESIDUE = (
    (1, 2, 3, 5, 6),
    (1, 2, 3, 4, 6, 7),
    (1, 3, 4, 5, 7, 8),
    (1, 2, 4, 5, 6, 8, 9),
    (1, 2, 3, 5, 6, 7, 9, 10),
    (1, 3, 6, 8, 10),
    (1, 2, 9),
    (1, 2, 3, 10),
    (1, 3, 4),
    (1, 2, 4, 5),
)
TYPES = (7, 8, 8, 9, 10, 7, 5, 6, 5, 6)


def coin_lengths(n):
    dp = [0] + [10**9] * n
    for m in range(1, n+1):
        dp[m] = 1 + min(dp[m-b] for b in COINS if b <= m)
    return dp


def apery_dijkstra(a):
    generators = (a, a+1, a+3, a+6, a+10)
    ap = [10**18] * a
    ap[0] = 0
    queue = [(0, 0)]
    while queue:
        n, r = heapq.heappop(queue)
        if n != ap[r]:
            continue
        for g in generators:
            nr = (r+g) % a
            nn = n+g
            if nn < ap[nr]:
                ap[nr] = nn
                heapq.heappush(queue, (nn,nr))
    return ap


def pf_via_apery(ap, a):
    generators = (a, a+1, a+3, a+6, a+10)
    return sorted(w-a for w in ap if w > 0 and all(
        w-a+g >= ap[(w-a+g) % a] for g in generators
    ))


def predicted(a, dp):
    result = [2*a+5, 2*a+8]
    result.extend((a-k)+a*(dp[a-k]-1) for k in K_BY_RESIDUE[a%10])
    return sorted(result)


def main():
    lengths = coin_lengths(2400)
    unexpected = [n for n in range(2390) if lengths[n+10] != lengths[n]+1]
    assert unexpected == [2, 5, 8], unexpected
    checked = 0
    for a in range(18, 1001):
        ap = apery_dijkstra(a)
        assert ap == [r+a*lengths[r] for r in range(a)], ('apery', a)
        actual = pf_via_apery(ap,a)
        target = predicted(a,lengths)
        assert actual == target, ('pf', a, actual, target)
        assert len(actual) == TYPES[a%10], ('type',a)
        checked += 1
    # Independent direct integer-reachability checks, without Apéry or coin lengths.
    direct_cases = (17, 18, 19, 20, 29, 30, 31, 78, 109, 237)
    for a in direct_cases:
        generators = (a, a+1, a+3, a+6, a+10)
        ap = apery_dijkstra(a)
        bound = max(ap) + max(generators) + 1
        has = [False] * (bound+1)
        has[0] = True
        for n in range(1,bound+1):
            has[n] = any(n>=g and has[n-g] for g in generators)
        actual = sorted(n for n in range(bound-max(generators)) if not has[n] and all(has[n+g] for g in generators))
        assert actual == pf_via_apery(ap,a), ('direct_reachability', a)
    # The pre-threshold boundary is an exact counterexample, not evidence for the infinite proof.
    ap17=apery_dijkstra(17)
    assert pf_via_apery(ap17,17) == [33,39,42,48,49]
    assert pf_via_apery(ap17,17) != predicted(17,lengths)
    result = {'status':'PASS','tested_aperY_and_pf_values':checked,
              'a_min':18,'a_max':1000,'coin_lengths_through':2400,
              'coin_shift_exceptions_below_2390':unexpected,
              'types_by_a_mod_10':list(TYPES),'direct_reachability_cases':list(direct_cases),'boundary_a17_pf':[33,39,42,48,49]}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':')))

if __name__ == '__main__':
    main()
