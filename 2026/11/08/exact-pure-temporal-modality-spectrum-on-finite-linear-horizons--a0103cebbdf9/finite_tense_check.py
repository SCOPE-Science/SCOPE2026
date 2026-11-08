"""Reproduce the exact finite strict-past/strict-future modal spectrum.

Usage: python finite_tense_check.py

Each relation row is a bit mask of reachable times. Composition is ordinary
Boolean relation composition. All tests use integer arithmetic only.
"""
from collections import deque


def compose(left, right, n):
    out = []
    for row in left:
        mask = 0
        for k in range(n):
            if row & (1 << k):
                mask |= right[k]
        out.append(mask)
    return tuple(out)


def generators(n):
    past = tuple((1 << i) - 1 for i in range(n))
    future = tuple(((1 << n) - 1) ^ ((1 << (i + 1)) - 1) for i in range(n))
    return past, future


def closure(n):
    past, future = generators(n)
    identity = tuple(1 << i for i in range(n))
    seen = {identity: "", past: "P", future: "F"}
    queue = deque(seen)
    while queue:
        relation = queue.popleft()
        for letter, generator in (("P", past), ("F", future)):
            successor = compose(relation, generator, n)
            if successor not in seen:
                seen[successor] = seen[relation] + letter
                queue.append(successor)
    return seen


def canonical_relations(n):
    past, future = generators(n)
    identity = tuple(1 << i for i in range(n))
    zero = tuple(0 for _ in range(n))
    relations = {identity, zero}
    # Nonrectangular pure powers: extreme powers are themselves rectangles.
    for generator in (past, future):
        power = identity
        for _ in range(1, n - 1):
            power = compose(power, generator, n)
            relations.add(power)
    # Four independent orientations and all nonempty proper prefix/suffix sizes.
    for kind_row in ("low", "high"):
        for kind_col in ("low", "high"):
            for a in range(1, n):
                rows = set(range(a)) if kind_row == "low" else set(range(n - a, n))
                for b in range(1, n):
                    cols = set(range(b)) if kind_col == "low" else set(range(n - b, n))
                    column_mask = sum(1 << j for j in cols)
                    relations.add(tuple(column_mask if i in rows else 0 for i in range(n)))
    return relations


def binary_modal_image(relation, valuation, n):
    # Meet over accessible times; empty meets evaluate to truth value 1.
    return tuple(int((valuation & row) == row) for row in relation)


def run():
    for n in range(2, 13):
        found = closure(n)
        canonical = canonical_relations(n)
        target = 2 * (n - 1) * (2 * n - 1)
        assert set(found) == canonical, (n, "classification failure")
        assert len(found) == target, (n, "count failure", len(found), target)
        # A direct 0/1-valued check shows that distinct relations induce
        # different meet operators. The theoretical proof handles all n.
        if n <= 6:
            signatures = {
                tuple(binary_modal_image(rel, val, n)
                      for val in range(1 << n))
                for rel in found
            }
            assert len(signatures) == target, (n, "operator collision")
        print(f"n={n}: {len(found)} relations; normal forms agree")
    print("PASS: finite semigroup, normal-form and binary-separation checks")


if __name__ == "__main__":
    run()
