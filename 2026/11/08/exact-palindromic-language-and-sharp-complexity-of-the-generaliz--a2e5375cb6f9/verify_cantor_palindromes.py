#!/usr/bin/env python3
"""Finite, dependency-free diagnostics for generalized Cantor palindromes.
The mathematical proof in RESULT.md covers all indices; this program is finite.
"""


def cantor(base, length):
    word = bytearray(length)
    for index in range(length):
        x = index
        while x:
            digit = x % base
            if digit not in (0, base-1):
                break
            x //= base
        else:
            word[index] = 1
    return bytes(word)


def predicted(base, length):
    factors = {bytes(length)}
    if length % 2 and length <= 2*base-3:
        radius = (length-1)//2
        factors.add(bytes(radius) + b"\x01" + bytes(radius))
    scale = 1
    while (base-2)*scale+2 <= length:
        lower = (base-2)*scale+2
        upper = (2*base-3)*base*scale
        if lower <= length <= upper and length % 2 == base % 2:
            core_length = base*scale
            core = cantor(base, core_length)
            padding = (base-2)*core_length
            maximal = bytes(padding) + core + bytes(padding)
            start = (len(maximal) - length)//2
            factors.add(maximal[start:start+length])
        scale *= base
    return factors


def main():
    total_cases = 0
    for base in range(3, 10):
        prefix_length = min(30000, base**9)
        word = cantor(base, prefix_length)
        for length in range(1, 161):
            actual = set()
            for start in range(prefix_length - length + 1):
                factor = word[start:start+length]
                if factor == factor[::-1]:
                    actual.add(factor)
            expected = predicted(base, length)
            assert actual == expected, (base, length, len(actual), len(expected),
                                        sorted(actual-expected), sorted(expected-actual))
            total_cases += 1
    print(f"VERIFY_OK bases=3..9 lengths=1..160 total_cases={total_cases}")


if __name__ == '__main__':
    main()
