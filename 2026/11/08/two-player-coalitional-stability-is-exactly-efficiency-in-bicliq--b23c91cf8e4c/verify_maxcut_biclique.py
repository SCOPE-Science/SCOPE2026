"""Independent exhaustive checks of a biclique max-k-cut equilibrium theorem.

Run with Python 3: python verify_maxcut_biclique.py
Uses only the standard library. It checks complete labelled color profiles,
all unilateral deviations and all coalitions of size at most two.
"""
from itertools import product, combinations
from math import comb, factorial


def surj(n, k):
    return sum((-1)**j * comb(k, j) * (k-j)**n for j in range(k+1))


def predicted_counts(a, b, q):
    proper = sum(comb(q, r)*comb(q-r, s)*surj(a, r)*surj(b, s)
                 for r in range(1, min(q, a)+1)
                 for s in range(1, min(q-r, b)+1))
    central = (factorial(a)//factorial(a//q)**q) * (factorial(b)//factorial(b//q)**q) if a%q==0 and b%q==0 else 0
    return proper, central


def util(profile, v, a, b):
    if v < a:
        return sum(profile[v] != profile[j] for j in range(a, a+b))
    return sum(profile[v] != profile[j] for j in range(a))


def brute(a, b, q):
    counts = [0, 0]
    total_profiles = 0
    for profile in product(range(q), repeat=a+b):
        total_profiles += 1
        base = tuple(util(profile, v, a, b) for v in range(a+b))
        one_improves = False
        for v in range(a+b):
            for c in range(q):
                if c != profile[v]:
                    changed = list(profile)
                    changed[v] = c
                    if util(changed, v, a, b) > base[v]:
                        one_improves = True
                        break
            if one_improves:
                break
        x = [profile[:a].count(c) for c in range(q)]
        y = [profile[a:].count(c) for c in range(q)]
        proper = all(x[c]*y[c] == 0 for c in range(q))
        central = a%q == b%q == 0 and all(t == a//q for t in x) and all(t == b//q for t in y)
        assert (not one_improves) == (proper or central), (a, b, q, profile, 'Nash')
        welfare = sum(util(profile, v, a, b) for v in range(a+b))
        if proper:
            assert welfare == 2*a*b
        if central:
            assert welfare == 2*a*b*(q-1)//q
        if one_improves:
            continue
        counts[1 if central and not proper else 0] += 1
        two_improves = False
        for v, w in combinations(range(a+b), 2):
            for c in range(q):
                if c == profile[v]:
                    continue
                for d in range(q):
                    if d == profile[w]:
                        continue
                    changed = list(profile)
                    changed[v] = c
                    changed[w] = d
                    if util(changed, v, a, b)>base[v] and util(changed, w, a, b)>base[w]:
                        two_improves = True
                        break
                if two_improves:
                    break
            if two_improves:
                break
        assert (not two_improves) == proper, (a, b, q, profile, '2-strong')
        if central:
            for v, w in combinations(range(a+b), 2):
                profitable_joint_colors = []
                for c in range(q):
                    if c == profile[v]:
                        continue
                    for d in range(q):
                        if d == profile[w]:
                            continue
                        changed = list(profile)
                        changed[v], changed[w] = c, d
                        if util(changed, v, a, b) > base[v] and util(changed, w, a, b) > base[w]:
                            profitable_joint_colors.append((c, d))
                expected_changes = [(profile[w], profile[v])] if (v < a <= w and profile[v] != profile[w]) else []
                assert profitable_joint_colors == expected_changes, (a, b, q, profile, v, w)
            blocking_pairs = sum(profile[i]!=profile[j] for i in range(a) for j in range(a,a+b))
            assert blocking_pairs == a*b*(q-1)//q
            assert blocking_pairs == sum(
                ((lambda z: util(z, i, a, b) > base[i] and util(z, j, a, b) > base[j])(
                    profile[:i] + (profile[j],) + profile[i+1:j] + (profile[i],) + profile[j+1:]
                )) for i in range(a) for j in range(a,a+b))
    expected = predicted_counts(a,b,q)
    assert tuple(counts) == expected, (a,b,q,counts,expected)
    return total_profiles


def main():
    checked = 0
    instances = 0
    for q in (2,3,4):
        for a in range(1,5):
            for b in range(1,5):
                if a+b <= 7:
                    checked += brute(a,b,q)
                    instances += 1
    print('VERIFIED: instances=%d profiles=%d; Nash, 2-strong, counts, blocking pairs' % (instances,checked))


if __name__ == '__main__':
    main()
