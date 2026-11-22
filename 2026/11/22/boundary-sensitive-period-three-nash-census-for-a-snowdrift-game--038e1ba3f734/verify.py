"""Finite supplementary verification of a three-action network-game census.

The theorem for all graph orders follows from the accompanying analytic proof;
these computations verify finite examples and payoff convention only.
"""
from fractions import Fraction as Q
from itertools import product


def graph_neighbors(kind, n):
    if kind == "path":
        assert n >= 2
        return [tuple(j for j in (i - 1, i + 1) if 0 <= j < n)
                for i in range(n)]
    assert kind == "cycle" and n >= 3
    return [((i - 1) % n, (i + 1) % n) for i in range(n)]


def is_equilibrium(profile, neighbors, b, c, ci):
    for i, adjacent in enumerate(neighbors):
        d = len(adjacent)
        m = sum(profile[j] == "C" for j in adjacent)
        payoffs = {"C": d * (b - 2 * c) + m * c,
                   "D": m * b,
                   "I": d * (b - ci)}
        if payoffs[profile[i]] < max(payoffs.values()):
            return False
    return True


def predicted(kind, n, cooperative):
    expected = {"I" * n}
    if cooperative:
        if kind == "path" and n % 3 == 1:
            expected.add("D" + "CCD" * ((n - 1) // 3))
        if kind == "cycle" and n % 3 == 0:
            p = "CCD" * (n // 3)
            expected.update({p[i:] + p[:i] for i in range(3)})
    return expected


def check_all():
    # Across threshold sides, never on excluded equality surfaces.
    cases = [(Q(5, 2), Q(6, 5)),
             (Q(5, 2), Q(7, 4)),
             (Q(7, 2), Q(6, 5)),
             (Q(7, 2), Q(7, 4)),
             (Q(9, 2), Q(19, 10))]
    checked = 0
    for b, ci in cases:
        coop = b > 3 and ci > Q(3, 2)
        for kind in ("path", "cycle"):
            for n in range(2 if kind == "path" else 3, 11):
                neighbors = graph_neighbors(kind, n)
                actual = {"".join(x) for x in product("CDI", repeat=n)
                          if is_equilibrium(x, neighbors, b, Q(1), ci)}
                expect = predicted(kind, n, coop)
                assert actual == expect, (b, ci, kind, n, actual, expect)
                checked += 1
    assert predicted("cycle", 9999, True) == {
        ("CCD" * 3333)[i:] + ("CCD" * 3333)[:i] for i in range(3)
    } | {"I" * 9999}
    assert predicted("cycle", 10000, True) == {"I" * 10000}
    print(f"PASS: {checked} graph/parameter exhaustive profile comparisons; "
          "all parameters rational; exact payoff arithmetic.")


if __name__ == "__main__":
    check_all()
