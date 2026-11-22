"""Independent exact combinatorial and polynomial checks of a binary universal-word census."""
from math import comb
from itertools import combinations


def formula(k):
    offset = k * (k - 1) // 2
    terms = {}
    def add(j, amount):
        terms[j] = terms.get(j, 0) + amount
    for r in range(k + 2):
        add(k * (k + 1) // 2 + r, comb(k + 1, r))
    for j in range(k):
        for r in range(k):
            add(offset + j + r, comb(k - 1, r))
            add(offset + 2 * k + 2 - j + r, comb(k - 1, r))
    for d in range(1, k):
        for r in range(k - 1):
            add(offset + k - d + 1 + r, (k - d) * comb(k - 2, r))
            add(offset + k + d + 2 + r, (k - d) * comb(k - 2, r))
    return {i: v for i, v in terms.items() if v}


def arches(w):
    i = answer = 0
    while i < len(w):
        j = i + 1
        while j < len(w) and w[j] == w[i]:
            j += 1
        if j == len(w):
            return answer
        i = j + 1
        answer += 1
    return answer


def census(k):
    n = 2 * k + 2
    out = {}
    for ones in combinations(range(n), k + 1):
        w = [0] * n
        for p in ones:
            w[p] = 1
        if arches(w) < k:
            continue
        zeros_before = count = 0
        for letter in w:
            if letter == 0:
                zeros_before += 1
            else:
                count += zeros_before
        out[count] = out.get(count, 0) + 1
    return out


if __name__ == "__main__":
    for k in range(1, 8):
        expected = formula(k)
        observed = census(k)
        assert observed == expected, (k, observed, expected)
        assert sum(expected.values()) == 2 ** (k - 2) * (k * k + 3 * k + 8)
        assert min(expected) == k * (k - 1) // 2
        assert max(expected) == (k + 1) ** 2 - min(expected)
        assert all(expected[e] == expected[(k + 1) ** 2 - e] for e in expected)
        print(f"k={k} balanced_words={comb(2*k+2,k+1)} universal={sum(observed.values())} support={min(observed)}..{max(observed)}")
    for k in range(2, 101):
        coeff = formula(k)
        c = (k + 1) ** 2 // 2
        lhs = coeff.get(c - 1, 0) - coeff.get(c, 0)
        if k % 2:
            m = (k - 1) // 2
            rhs_num = comb(2 * m, m) * (3 * m - 1)
        else:
            m = k // 2
            rhs_num = comb(2 * m, m) * 3 * (m - 1)
        assert 2 * (m + 1) * lhs == rhs_num, (k, lhs, rhs_num)
    print("VERIFY_OK arch_vs_polynomial_k1_to7=7 central_identity_k2_to100=99")
