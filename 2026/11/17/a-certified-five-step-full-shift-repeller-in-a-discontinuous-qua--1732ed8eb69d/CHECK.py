"""Exact rational covering-and-expansion certificate for a five-step quadratic map."""
from fractions import Fraction as Q

LEFT = Q(1, 3)
RIGHT = Q(2, 3)
J = (Q(527, 2500), Q(7, 25))
CASES = (
    ("A", (Q(527, 2500), Q(6, 25)), "LRLLR", Q(23, 10)),
    ("B", (Q(1221, 5000), Q(7, 25)), "LRLRL", Q(21, 10)),
)


def phi(ch, x):
    if ch == "L":
        return 2 * x - x * x
    if ch == "R":
        return x * x
    raise ValueError(ch)


def evaluate_case(name, initial, word, derivative_threshold):
    lo, hi = initial
    assert J[0] <= lo < hi <= J[1]
    lower_product = Q(1)
    states = []
    for step, ch in enumerate(word):
        states.append((ch, lo, hi))
        assert Q(0) < lo <= hi < RIGHT
        if ch == "L":
            assert hi < LEFT, (name, step, "left-branch failure")
            lower_product *= 2 * (1 - hi)
        else:
            assert lo > LEFT, (name, step, "middle-branch failure")
            lower_product *= 2 * lo
        lo, hi = phi(ch, lo), phi(ch, hi)
    assert lo < J[0] and hi > J[1], (name, "covering failure")
    assert lower_product > derivative_threshold > 2, (name, "expansion failure")
    return states, lo, hi, lower_product


def main():
    assert CASES[0][1][1] < CASES[1][1][0]
    for name, initial, word, threshold in CASES:
        states, lo, hi, d = evaluate_case(name, initial, word, threshold)
        print(name, word, "final_range", float(lo), float(hi),
              "derivative_lower", float(d), "covered", True)
        for ch, x, y in states:
            print("  ", ch, float(x), float(y))
    # Exact verification of the biological map representation on used branches.
    for x in (Q(1, 5), Q(1, 4), Q(2, 5), Q(1, 2)):
        p = Q(1) if x <= LEFT else Q(0)
        expected = 2 * x - x * x if p else x * x
        assert x * x + 2 * p * x * (1 - x) == expected
    print("TWO_DISCONTINUITY_QSO_HORSESHOE_OK exact_branches=2 period=5")


if __name__ == "__main__":
    main()
