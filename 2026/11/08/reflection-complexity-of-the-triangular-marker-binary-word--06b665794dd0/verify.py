#!/usr/bin/env python3
"""Standalone arithmetic and finite factor-language checks for the stated theorem.

Run with: python3 verify.py
No external packages are required. Finite checks support, not replace, the proof.
"""


def predicted(n):
    m, s = divmod(n, 6)
    c = (1, 2, 2, 4, 5, 7)
    return 6 * m * m + 2 * (s + 1) * m + c[s]


def pair_prediction(n):
    one = n // 2
    two = 0
    for a in range(max(0, (n - 5) // 3 + 1)):
        two += (n - 5 - 3 * a) // 2 + 1
    return one, two


def factors(n):
    if not n:
        return {""}
    # A word containing every length-n factor: after the gap n, factors
    # with 0/1 ones are present; every factor with >=2 ones has inner gap <n.
    finite = "1" + "".join("0" * j + "1" for j in range(1, n + 5))
    return {finite[i:i+n] for i in range(len(finite) - n + 1)}


def run_checks():
    tests = 0
    for n in range(0, 121):
        fs = factors(n)
        classes = {min(w, w[::-1]) for w in fs}
        pairlist = [(w, w[::-1]) for w in fs if w < w[::-1] and w[::-1] in fs]
        p = (n + 1) ** 2 // 4 + 1 if n else 1
        assert len(fs) == p, (n, "factor complexity", len(fs), p)
        assert len(classes) == predicted(n), (n, "reflection", len(classes), predicted(n))
        assert len(pairlist) == len(fs) - len(classes), (n, "pair count")
        if n:
            one, two = pair_prediction(n)
            assert len(pairlist) == one + two, (n, "pair formula", len(pairlist), one, two)
            assert sum(1 for u, v in pairlist if u.count("1") == 1) == one
            assert sum(1 for u, v in pairlist if u.count("1") == 2) == two
            assert not any(u.count("1") >= 3 for u, v in pairlist)
        tests += 1
    for n in (150, 200, 250):
        fs = factors(n)
        classes = {min(w, w[::-1]) for w in fs}
        assert len(fs) == (n + 1) ** 2 // 4 + 1
        assert len(classes) == predicted(n)
        tests += 1
    print(f"PASS: {tests} exhaustive finite factor-language tests; n=0..120,150,200,250")


if __name__ == "__main__":
    run_checks()
