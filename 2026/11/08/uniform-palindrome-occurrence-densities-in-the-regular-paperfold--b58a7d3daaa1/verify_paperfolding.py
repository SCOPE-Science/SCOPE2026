"""Exact finite 2-adic certificate for palindromic-factor frequencies.

Only Python 3 standard library is used. The 64 states (residue, high bit)
exhaust every factor of length at most 15, with weight 1/64 each.
The proof of this exhaustive representation is in RESULT.md.
"""
from collections import Counter

EXPECTED = {
    1: {"0": 32, "1": 32},
    2: {"00": 16, "11": 16},
    3: {"000": 4, "010": 4, "101": 4, "111": 4},
    4: {"0110": 8, "1001": 8},
    5: {"00100": 4, "01110": 4, "10001": 4, "11011": 4},
    6: {"001100": 2, "110011": 2},
    7: {"0011100": 2, "0110110": 2, "1001001": 2, "1100011": 2},
    8: {},
    9: {"001101100": 2, "011000110": 2, "100111001": 2, "110010011": 2},
    10: {},
    11: {"00011011000": 1, "11100100111": 1},
    12: {},
    13: {"0111001001110": 1, "1000110110001": 1},
    14: {},
    15: {},
}


def paperfolding_bit_one_based(m):
    assert m >= 1
    while m % 2 == 0:
        m //= 2
    return "1" if m % 4 == 1 else "0"


def model_window(residue, high_bit, length):
    assert 0 <= residue < 32 and high_bit in "01" and 1 <= length <= 15
    result = []
    for j in range(length):
        m = residue + j + 1
        # At most one multiple of 16 in a window of length <= 15.
        result.append(high_bit if m % 16 == 0 else paperfolding_bit_one_based(m))
    return "".join(result)


def verify():
    total_cases = 0
    for length in range(1, 16):
        weighted = Counter()
        for residue in range(32):
            for high_bit in "01":
                w = model_window(residue, high_bit, length)
                total_cases += 1
                if w == w[::-1]:
                    weighted[w] += 1
        assert dict(weighted) == EXPECTED[length], (
            length, dict(weighted), EXPECTED[length]
        )
    assert sum(map(len, EXPECTED.values())) == 28

    # Independently check correspondence to actual 2-adic word, both at
    # the ordinary indices and in high-valuation exceptional windows.
    direct_count = 0
    for n in range(131072):
        r = n % 32
        for length in (1, 5, 9, 13, 14, 15):
            exceptional = [j for j in range(length) if (n + j + 1) % 16 == 0]
            assert len(exceptional) <= 1
            high_bit = (
                paperfolding_bit_one_based(n + exceptional[0] + 1)
                if exceptional else "0"
            )
            actual = "".join(paperfolding_bit_one_based(n + j + 1)
                             for j in range(length))
            assert model_window(r, high_bit, length) == actual
            direct_count += 1
    print("VERIFY_OK 2adic_states=64 lengths=15 state_cases=", total_cases,
          "palindromic_factors=28 direct_windows=", direct_count)


if __name__ == "__main__":
    verify()
