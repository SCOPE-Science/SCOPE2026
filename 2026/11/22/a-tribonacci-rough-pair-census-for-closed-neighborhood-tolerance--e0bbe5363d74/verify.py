"""Reproducible finite checks for path-tolerance rough-pair enumeration.

Python 3 standard library only.  Exhaustive checks corroborate but do not
replace the all-length seven-state transfer argument in RESULT.md.
"""
from collections import deque

STATES = ((0, 0), (0, 1), (1, 0), (1, 1))
START = frozenset(((0, 0), (1, 1)))
SYMBOLS = "0*1"


def rough_output(bits):
    n = len(bits)
    word = []
    for i in range(n):
        triple = (bits[max(i - 1, 0)], bits[i], bits[min(i + 1, n - 1)])
        word.append("0" if triple == (0, 0, 0) else "1" if triple == (1, 1, 1) else "*")
    return "".join(word)


def move(q, symbol):
    result = set()
    for a, b in q:
        for c in (0, 1):
            s = "0" if a == b == c == 0 else "1" if a == b == c == 1 else "*"
            if s == symbol:
                result.add((b, c))
    return frozenset(result)


def automaton():
    subsets = [START]
    names = {START: 0}
    for state in subsets:
        for symbol in SYMBOLS:
            nxt = move(state, symbol)
            if nxt not in names:
                names[nxt] = len(subsets)
                subsets.append(nxt)
    trans = [[names[move(s, sym)] for sym in SYMBOLS] for s in subsets]
    accept = [bool(s & START) for s in subsets]
    return subsets, trans, accept


def dfa_counts(upto):
    subsets, trans, accept = automaton()
    assert len(subsets) == 12
    assert sum(accept) == 8
    counts = [0] * len(subsets)
    counts[0] = 1
    out = [sum(counts[i] for i, ok in enumerate(accept) if ok)]
    for _ in range(upto):
        new = [0] * len(subsets)
        for i, count in enumerate(counts):
            for j in trans[i]:
                new[j] += count
        counts = new
        out.append(sum(counts[i] for i, ok in enumerate(accept) if ok))
    return out


def direct_count(n):
    observed = set()
    for mask in range(1 << n):
        b = tuple(mask >> i & 1 for i in range(n))
        # Independent computation: bitmask lower and upper over neighborhoods.
        lo = hi = 0
        for i in range(n):
            near = sum(1 << j for j in range(max(0, i - 1), min(n - 1, i + 1) + 1))
            if mask & near == near:
                lo |= 1 << i
            if mask & near:
                hi |= 1 << i
        observed.add((lo, hi))
        assert len(b) == n
    return len(observed)


def seven_state_counts(upto):
    # A,B,C,D,F,G,H in the quotient by bit-complement symmetry.
    transitions = ((1, 1, 2), (1, 3), (4,), (5,), (1, 1, 4), (1, 6), (1, 4))
    accept = (1, 1, 0, 0, 1, 1, 1)
    v = [1, 0, 0, 0, 0, 0, 0]
    result = []
    for _ in range(upto + 1):
        result.append(sum(x * ok for x, ok in zip(v, accept)))
        nv = [0] * 7
        for i, x in enumerate(v):
            for j in transitions[i]:
                nv[j] += x
        v = nv
    return result


def main():
    dfa = dfa_counts(35)
    assert dfa[:11] == [1, 2, 3, 7, 13, 23, 43, 79, 145, 267, 491]
    assert dfa == seven_state_counts(35)
    assert all(dfa[n] == dfa[n - 1] + dfa[n - 2] + dfa[n - 3] for n in range(5, 36))
    for n in range(1, 17):
        assert direct_count(n) == dfa[n], (n, direct_count(n), dfa[n])
    print("VERIFY_OK: 16 exhaustive direct subset enumerations, 36 DFA/quotient counts, 31 recurrence tests")


if __name__ == "__main__":
    main()
