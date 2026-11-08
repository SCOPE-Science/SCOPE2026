#!/usr/bin/env python3
"""Finite reproducibility checks for the Galois-word border-spectrum theorem.

No external packages are required. The theorem for unbounded word lengths rests
on the mathematical proof; the checks here are exhaustive only for n <= 16.
"""
from itertools import product


def alternate_less(a: str, b: str) -> bool:
    assert len(a) == len(b)
    for j in range(len(a)):
        if a[j] != b[j]:
            return a[j] < b[j] if j % 2 == 0 else a[j] > b[j]
    return False


def galois(w: str) -> bool:
    return bool(w) and all(alternate_less(w, w[j:] + w[:j])
                           for j in range(1, len(w)))


def spectrum(n: int) -> set[int]:
    return {b for b in range(1, n) if b % 2 == 1 and
            (n % 2 == 1 or 2 * b < n)}


def witness(n: int, b: int) -> str:
    assert b in spectrum(n)
    if n % 2:
        return '01' * ((n - 1) // 2) + '0'
    if b == 1:
        return '01' + '0' * (n - 2)
    d = n - b
    return '01' + '0' * (d - 1) + '1' + '0' * (b - 2)


def is_period(w: str, p: int) -> bool:
    return all(w[j] == w[j + p] for j in range(len(w) - p))


def full_exhaustive_check(max_n: int = 16) -> tuple[int, int]:
    words = galois_words = 0
    for n in range(2, max_n + 1):
        achieved = set()
        for letters in product('01', repeat=n):
            w = ''.join(letters)
            words += 1
            if not galois(w):
                continue
            galois_words += 1
            achieved.update(b for b in range(1, n) if w[:b] == w[-b:])
            for p in range(1, n // 2 + 1, 2):
                assert not is_period(w, p), (w, p)
        assert achieved == spectrum(n), (n, achieved, spectrum(n))
    return words, galois_words


def all_explicit_witness_checks(max_n: int = 256) -> int:
    cases = 0
    for n in range(2, max_n + 1):
        for b in spectrum(n):
            w = witness(n, b)
            assert len(w) == n
            assert w[:b] == w[-b:]
            assert galois(w), (n, b, w)
            cases += 1
    return cases


def main() -> None:
    words, successful = full_exhaustive_check()
    cases = all_explicit_witness_checks()
    print('PASS: exhaustive binary words:', words)
    print('PASS: Galois words checked:', successful)
    print('PASS: explicit witnesses:', cases)
    print('PASS: border spectra for every length 2 through 16; witnesses through 256')


if __name__ == '__main__':
    main()
