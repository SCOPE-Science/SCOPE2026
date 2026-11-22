#!/usr/bin/env python3
"""Direct diagram enumeration for convexly ordered equivalence relations.

No external dependencies. This is a finite diagnostic, not the general proof.
"""
from itertools import combinations
from math import comb, factorial

def compositions(n):
    if n == 0:
        yield ()
        return
    for k in range(1, n + 1):
        for cuts in combinations(range(1, n), k - 1):
            boundaries = (0,) + cuts + (n,)
            yield tuple(boundaries[i+1]-boundaries[i] for i in range(k))

def formula(n, k, r):
    assert (n == k == 0) or (1 <= k <= n)
    a = n - 1
    def ca(i):
        if n == 0:
            return (1, -1)[i] if i <= 1 else 0
        if a == 0:
            return 1 if i == 0 else 0
        return comb(a + i - 1, i)
    return factorial(r) * sum(ca(i) * (2 ** (r-i)) * comb(k+r-i, r-i)
                              for i in range(r+1))

def direct(n_composition, r):
    n = sum(n_composition)
    old_class = []
    for class_id, size in enumerate(n_composition):
        old_class += [class_id] * size
    s = n + r
    # Each increasing arrangement of r new anonymous points has r! labellings.
    types_in_sorted_order = 0
    for old_positions in combinations(range(s), n):
        for mask in range(1 << max(0, s-1)):
            # Each set bit is an E-class boundary between consecutive positions.
            class_index = [0]
            for pos in range(s-1):
                class_index.append(class_index[-1] + ((mask >> pos) & 1))
            old_new_classes = [class_index[pos] for pos in old_positions]
            if all((old_class[i] == old_class[j]) ==
                   (old_new_classes[i] == old_new_classes[j])
                   for i in range(n) for j in range(i+1, n)):
                types_in_sorted_order += 1
    return types_in_sorted_order * factorial(r)

def main():
    checks = 0
    for n in range(0, 7):
        for profile in compositions(n):
            k = len(profile)
            for r in range(0, 4):
                got = direct(profile, r)
                want = formula(n, k, r)
                assert got == want, (profile, r, got, want)
                checks += 1
            if n <= 4:
                got = direct(profile, 4)
                want = formula(n, k, 4)
                assert got == want, (profile, 4, got, want)
                checks += 1
    recoveries = 0
    for n in range(0, 101):
        for k in ([0] if n == 0 else range(1, n + 1)):
            t1, t2 = formula(n,k,1),formula(n,k,2)
            kr = (t2 - t1*t1 - t1 - 2)//2
            nr = t1 - 2*kr - 1
            assert (nr,kr) == (n,k)
            recoveries += 1
    assert formula(4,2,2) == 96
    assert sum((m+1)*(m+2) for m in (1,3)) == 26
    assert sum((m+1)*(m+2) for m in (2,2)) == 24
    print(f"PASS direct extension-diagram comparisons: {checks}")
    print(f"PASS inverse reconstructions: {recoveries}")
    print("PASS four-point collision: 96 total pair types; anchored channel 26 versus 24")
    print("FINITE TESTS SUPPORT BUT DO NOT REPLACE THE GENERAL PROOF")

if __name__ == "__main__":
    main()
