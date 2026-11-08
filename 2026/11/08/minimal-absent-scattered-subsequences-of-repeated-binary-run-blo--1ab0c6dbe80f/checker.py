#!/usr/bin/env python3
"""Independent finite checks for minimal absent scattered subsequences.

Run: python checker.py
No third-party modules are required.
This is finite corroboration, not a substitute for the theorem's proof.
"""
from collections import defaultdict
from itertools import groupby, product


def all_subsequences(word):
    seen = {""}
    for ch in word:
        added = {x + ch for x in seen}
        seen.update(added)
    return seen


def explicit_minimal_absent(word):
    present = all_subsequences(word)
    candidates = {p + ch for p in present for ch in "01"}
    return {u for u in candidates - present if all(u[:j] + u[j+1:] in present for j in range(len(u)))}


def proposed_minimal_absent(u, a, b, r):
    if not u:
        return False
    runs = [(c, len(list(g))) for c, g in groupby(u)]
    block_usage = sum((size + (a if c == "0" else b) - 1) // (a if c == "0" else b)
                      for c, size in runs)
    discounts = sum(c == "0" and d == "1" for (c, _), (d, _) in zip(runs, runs[1:]))
    if block_usage - discounts != r + 1:
        return False
    for c, size in runs:
        if (size - 1) % (a if c == "0" else b):
            return False
    if len(runs) > 1 and (runs[0] == ("0", 1) or runs[-1] == ("1", 1)):
        return False
    for c, size in runs[1:-1]:
        if size == 1 and ((c == "1" and a == 1) or (c == "0" and b == 1)):
            return False
    return True


def expected_count(a, b, r):
    assert a > 0 and b > 0 and r > 0
    if a >= 2 and b >= 2:
        f0, f1 = 0, 1
        for _ in range(2*r+2):
            f0, f1 = f1, f0 + f1
        return f0
    if a == b == 1:
        values = [0, 3, 5, 9]
        while len(values) <= r:
            values.append(2*values[-1] - values[-2] + values[-3])
        return values[r]
    return 3 * (1 << (r-1))


def main():
    cases = total = verified_words = 0
    for a, b, r in product(range(1, 5), range(1, 5), range(1, 5)):
        w = ("0"*a + "1"*b)*r
        if len(w) > 20:
            continue
        found = explicit_minimal_absent(w)
        assert len(found) == expected_count(a,b,r), (a,b,r,"count",len(found),expected_count(a,b,r))
        for u in found:
            assert proposed_minimal_absent(u,a,b,r), (a,b,r,"missing",u)
        # Check all possible false positives by testing every nonempty word up to max MAS length.
        limit = max(map(len, found))
        for length in range(1, limit+1):
            for letters in product("01", repeat=length):
                u = "".join(letters)
                got = proposed_minimal_absent(u,a,b,r)
                assert got == (u in found), (a,b,r,"difference",u,got)
                verified_words += 1
        cases += 1
        total += len(found)
    print(f"PASS: {cases} parameter triples; {total} literal MAS; {verified_words} literal candidate comparisons")
    print("Counts by regime (r=1..10):")
    for a,b in ((1,1),(1,2),(2,2)):
        print(f"a={a},b={b}:", [expected_count(a,b,r) for r in range(1,11)])


if __name__ == "__main__":
    main()
