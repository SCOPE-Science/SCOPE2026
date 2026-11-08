"""Independent finite checks for the prefix-dominance abelian-spectrum theorem.

Standard-library Python 3. No third-party code or external data required.
The infinite theorem is proved in RESULT.md; these tests cannot replace it.
"""
from itertools import product


def prefix_counts(block):
    out = [0]
    for char in block:
        out.append(out[-1] + (char == "1"))
    return out


def bounds(u, v, residue):
    b = len(u)
    assert b == len(v) and b >= 2
    c = u.count("1")
    assert c == v.count("1") and 0 < c < b
    pu, pv = prefix_counts(u), prefix_counts(v)
    assert all(a <= z for a, z in zip(pu, pv))
    lo = min(c * ((s + residue) // b) + pu[(s + residue) % b] - pv[s]
             for s in range(b))
    hi = max(c * ((s + residue) // b) + pv[(s + residue) % b] - pu[s]
             for s in range(b))
    return lo, hi


def morphic_prefix(u, v, needed):
    word = "0"
    while len(word) < needed:
        word = "".join(u if char == "0" else v for char in word)
    return word[:needed]


def actual_range(word, length):
    pref = prefix_counts(word)
    counts = {pref[i + length] - pref[i]
              for i in range(len(word) - length + 1)}
    return min(counts), max(counts), len(counts)


def test_explicit_family():
    checked = 0
    for p in range(1, 8):
        for q in range(1, 8):
            u, v = "0" * p + "1" * q, "1" * q + "0" * p
            b = p + q
            w = morphic_prefix(u, v, 6000)
            for residue in range(b):
                low, high = bounds(u, v, residue)
                if residue == 0:
                    assert high - low + 1 == 2 * min(p, q) + 1
                for m in range(1, 9):
                    n = b * m + residue
                    actual = actual_range(w, n)
                    expected = (q * m + low, q * m + high, high - low + 1)
                    assert actual == expected, (p, q, n, actual, expected)
                    checked += 1
    return checked


def test_all_small_prefix_dominant_pairs():
    pairs, lengths = 0, 0
    for b in range(2, 7):
        for tail in product("01", repeat=b - 1):
            u = "0" + "".join(tail)
            c = u.count("1")
            if c == 0 or c == b:
                continue
            pu = prefix_counts(u)
            for vchars in product("01", repeat=b):
                v = "".join(vchars)
                if u == v or v.count("1") != c:
                    continue
                if any(x > y for x, y in zip(pu, prefix_counts(v))):
                    continue
                w = morphic_prefix(u, v, 6000)
                # A finite-prefix period test is a sampling filter, NOT
                # a proof that the infinite fixed point is aperiodic.
                if any(all(w[i] == w[i + d] for i in range(4500))
                       for d in range(1, 80)):
                    continue
                pairs += 1
                for n in range(b, 8 * b + 1):
                    lo, hi = bounds(u, v, n % b)
                    m = n // b
                    actual = actual_range(w, n)
                    expected = (c * m + lo, c * m + hi, hi - lo + 1)
                    assert actual == expected, (u, v, n, actual, expected)
                    lengths += 1
    return pairs, lengths


def main():
    explicit_checks = test_explicit_family()
    pairs, arbitrary_checks = test_all_small_prefix_dominant_pairs()
    print("explicit_family_parameter_pairs:", 49)
    print("explicit_family_length_checks:", explicit_checks)
    print("other_prefix_dominant_sample_pairs:", pairs)
    print("other_prefix_dominant_length_checks:", arbitrary_checks)
    print("all_finite_tests: PASS")
    print("Note: finite tests do not certify aperiodicity or the infinite theorem.")


if __name__ == "__main__":
    main()
