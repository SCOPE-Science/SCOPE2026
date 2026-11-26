#!/usr/bin/env python3
"""Exact finite checks for base-two spin-3/2 charge multiplicities."""
def closed_form(L, r):
    maximum = 3 * (2**L - 1)
    if r < 0 or r > maximum: return 0
    if r <= 2**L - 3: return r // 2 + 1
    if r <= 2**(L + 1) - 1: return 2**(L - 1)
    return 3 * 2**(L - 1) - r // 2 - 1

def direct_coefficients(L):
    coefficients = [1]
    for k in range(L):
        shifts = (0, 2**k, 2**(k + 1), 3 * 2**k)
        updated = [0] * (len(coefficients) + 3 * 2**k)
        for degree, multiplicity in enumerate(coefficients):
            for shift in shifts: updated[degree + shift] += multiplicity
        coefficients = updated
    return coefficients

def main():
    for L in range(1, 13):
        c = direct_coefficients(L); maximum = 3 * (2**L - 1)
        assert len(c) == maximum + 1 and sum(c) == 4**L
        for r, d in enumerate(c):
            assert d == closed_form(L, r), (L, r, d, closed_form(L, r))
            assert d == c[maximum-r], (L, r)
    print('PASS: exact integer checks for L=1,...,12')
if __name__ == '__main__': main()
