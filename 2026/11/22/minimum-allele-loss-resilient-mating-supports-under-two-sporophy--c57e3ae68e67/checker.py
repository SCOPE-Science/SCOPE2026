"""Standalone finite-case corroboration for an S-locus compatibility support theorem.

Run: python3 checker.py
Uses only the Python standard library. Exhaustive searches below are finite checks,
not substitutes for the all-alphabet-size proof in RESULT.md.
"""
from itertools import combinations

assertions = 0


def check(condition, detail=""):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(detail)


def can_pollinate(donor, recipient, scheme):
    check(scheme in ("DOMCOD", "COD"))
    if scheme == "COD":
        return set(donor).isdisjoint(recipient)
    return min(donor) not in recipient


def robust(cohort, k, scheme):
    if len(cohort) != len(set(cohort)):
        return False
    if set().union(*(set(edge) for edge in cohort)) != set(range(1, k + 1)):
        return False
    for lost in range(1, k + 1):
        remaining = [edge for edge in cohort if lost not in edge]
        if not any(can_pollinate(a, b, scheme) for a in remaining
                   for b in remaining if a != b):
            return False
    return True


def census(k, scheme):
    possibilities = list(combinations(range(1, k + 1), 2))
    winners = []
    minimum = None
    for size in range(1, len(possibilities) + 1):
        for choice in combinations(possibilities, size):
            yes = robust(choice, k, scheme)
            check(isinstance(yes, bool))
            if yes:
                if minimum is None:
                    minimum = size
                if size == minimum:
                    winners.append(choice)
        if minimum is not None:
            break
    return minimum, winners


expected = {
    (2, "DOMCOD"): (None, 0), (2, "COD"): (None, 0),
    (3, "DOMCOD"): (None, 0), (3, "COD"): (None, 0),
    (4, "DOMCOD"): (5, 3), (4, "COD"): (None, 0),
    (5, "DOMCOD"): (4, 38), (5, "COD"): (5, 12),
    (6, "DOMCOD"): (3, 15), (6, "COD"): (3, 15),
}
for (k, scheme), want in expected.items():
    minimum, optimizers = census(k, scheme)
    check((minimum, len(optimizers)) == want, f"{k} {scheme}: {(minimum, len(optimizers))} != {want}")
    print(f"exhaustive k={k} {scheme}: min={minimum}; optimum supports={len(optimizers)}")

k4_dom = {frozenset(x) for x in census(4, "DOMCOD")[1]}
mandatory = {(2, 3), (2, 4), (3, 4)}
asserted = {frozenset(mandatory | {a, b}) for a, b in combinations([(1, 2), (1, 3), (1, 4)], 2)}
check(k4_dom == asserted, "not all three smallest pollen-dominant architectures")

cod5 = census(5, "COD")[1]
for cohort in cod5:
    degrees = [sum(v in e for e in cohort) for v in range(1, 6)]
    check(degrees == [2] * 5, "codominant minimizer is not a five-cycle")

for k in range(7, 61):
    matching = [(i, i + 1) for i in range(1, k, 2)]
    if k % 2:
        matching.append((1, k))
    check(len(matching) == (k + 1) // 2, f"cover size error at {k}")
    for scheme in ("DOMCOD", "COD"):
        check(robust(tuple(matching), k, scheme), f"general construction failed at {k} {scheme}")
        if k > 3:
            check(len(matching) * 2 >= k)

print(f"PASS: {assertions} finite assertions; exact proof remains in RESULT.md")
