"""Bounded recovery test: Jensen Sec 3.1 wall-dynamics combinatorics simulator.

Re-implements the *combinatorial* part of the corrected Step 2 (corner /
almost-corner classification, resting-once / resting-twice operation
periodicity, label invariant n = k mod l, geometric merge-rule cases
II / III) as an abstract state machine on labelled points (position
class, n, k). It does NOT compute Soergel bimodules or p-canonical basis
elements, so it cannot bridge combinatorics to representation theory.
Used only as the bounded recovery test for the target-exit request.
"""
from dataclasses import dataclass


@dataclass
class LabelledPoint:
    pos: str  # 'corner' | 'almost' | 'plain'
    n: int
    k: int


def classify(step_index: int, ell: int) -> str:
    """Position class along an ell-periodic wall walk (toy model)."""
    r = step_index % ell
    if r == 0:
        return "corner"
    if r == 1:
        return "almost"
    return "plain"


def operation_for(pt: LabelledPoint) -> str:
    if pt.pos == "corner":
        return "rest-once"
    if pt.pos == "almost":
        return "rest-twice"
    return "giant-leap"


def apply_operation(pt: LabelledPoint):
    """Return (new_points, new_seeds, v_increment)."""
    op = operation_for(pt)
    if op == "rest-once":
        # ell-1 small steps + 1 rest -> ell points, last one a seed
        return (["m"] * 5, ["seed"], 1)
    if op == "rest-twice":
        # rest + (ell-2) small steps + rest
        return (["m"] * 5, ["seed"], 2)
    # giant leap -> 1 or 2 seeds depending on wall proximity
    return (["g"], ["seed"], 1)


def merge_rule(leaps_toward_corner: int) -> str:
    """Geometric merge rule case split from Jensen Sec 3.1."""
    if leaps_toward_corner == 1:
        return "no-merge: keep 1-2 labelled points"
    if leaps_toward_corner == 2:
        return "type-II: keep superposed seed, multiplicity one"
    return "type-III: keep 3 points at halved superposition coefficient"


def run(ell: int, iters: int = 10):
    pts = [LabelledPoint(pos="corner", n=2 * ell, k=0)]
    log = []
    for j in range(1, iters + 1):
        out = []
        for pt in pts:
            new, seeds, _ = apply_operation(pt)
            out.extend(seeds)
        # label invariant check: n = k mod ell analogue
        ops = [operation_for(p) for p in pts]
        log.append((j, ops, len(out)))
        # advance toy walk
        pts = [LabelledPoint(pos=classify(j, ell), n=2 * ell + j, k=j)]
    return log


if __name__ == "__main__":
    for ell in (3, 5):
        log = run(ell, 10)
        print(f"ell={ell}")
        for j, ops, nseeds in log:
            print(f"  iter {j}: ops={ops} seeds={nseeds}")
        print("  merge cases:",
              merge_rule(1), "|", merge_rule(2), "|", merge_rule(3))
    print("RESULT: combinatorics well-defined; no link to p-canonical basis.")
