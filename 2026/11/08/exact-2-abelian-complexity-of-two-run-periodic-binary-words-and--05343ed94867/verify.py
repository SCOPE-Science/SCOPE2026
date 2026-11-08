"""Finite checks of the stated two-run 2-Abelian complexity formula.

Requires Python 3, standard library only. The proof is mathematical and does not
rely on this finite experiment.
"""


def observed_signature(word):
    """Directly count all one-letter and overlapping two-letter factors."""
    return (
        sum(x == "0" for x in word),
        sum(x == "1" for x in word),
        sum(word[i:i + 2] == "00" for i in range(len(word) - 1)),
        sum(word[i:i + 2] == "01" for i in range(len(word) - 1)),
        sum(word[i:i + 2] == "10" for i in range(len(word) - 1)),
        sum(word[i:i + 2] == "11" for i in range(len(word) - 1)),
    )


def brute(a, b, n):
    period = "0" * a + "1" * b
    repeated = period * (n // (a + b) + 2)
    return len({observed_signature(repeated[s:s + n]) for s in range(a + b)})


def predicted(a, b, n):
    residue = (n - 1) % (a + b) + 1
    lower = max(1, residue - b)
    upper = min(a, residue - 1)
    t = max(0, upper - lower + 1)
    return (int(residue <= a) + int(residue <= b) + 2 * t
            + int(residue >= a + 2) + int(residue >= b + 2))


def main():
    profiles = 0
    for a in range(1, 15):
        for b in range(1, 15):
            period = a + b
            for n in range(1, 2 * period + 5):
                expected = predicted(a, b, n)
                actual = brute(a, b, n)
                assert expected == actual, (a, b, n, expected, actual)
                profiles += 1
            peak = max(predicted(a, b, n) for n in range(1, period + 1))
            assert peak == min(period, 2 * min(a, b) + 2), (a, b, peak)
            assert (peak == period) == (abs(a - b) <= 2), (a, b)
    assert profiles == 6664
    print("PASS: 6664 factor-length profiles and 196 peak/threshold configurations")


if __name__ == "__main__":
    main()
