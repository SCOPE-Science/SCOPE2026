#!/usr/bin/env python3
"""Exact arithmetic checks for the erasing-map transfer formulas.

No external libraries or downloaded datasets are needed. All checks use
finite dyadic cylinders; the infinite-observable assertion is proved in
RESULT.md and is not inferred from these finite checks.
"""
from fractions import Fraction


def rho(word):
    # Position is counted in the input word, starting at one.
    return ''.join('1' if pos % 2 == 0 else '0'
                   for pos, digit in enumerate(word, 1) if digit == '1')


def rho_twice(word):
    return rho(rho(word))


def transfer(values, bits):
    """Push a function on 2^bits equal cylinders through the transfer law."""
    assert bits > 0 and bits % 2 == 0 and len(values) == 2**bits
    half = bits // 2
    result = [Fraction(0) for _ in range(2**half)]
    for j, value in enumerate(values):
        if value == 0:
            continue
        output = rho_twice(format(j, f'0{bits}b'))
        assert len(output) <= half
        scale = 2**(half - len(output))
        base = int(output, 2) * scale if output else 0
        weight = value * Fraction(1, 2**(bits - len(output)))
        for i in range(base, base + scale):
            result[i] += weight
    return result


def mean(values):
    return sum(values, Fraction(0)) / len(values)


def coordinate_residue(stage):
    bits = 2**stage
    values = [Fraction(2*j + 1, 2**(bits+1)) for j in range(2**bits)]
    for _ in range(stage):
        values = transfer(values, bits)
        bits //= 2
    assert bits == 1 and mean(values) == Fraction(1, 2)
    coefficient = (values[1] - values[0]) / 2
    return 2**stage * coefficient


def run():
    # Hand calculation for the two nonconstant cylinder eigenvectors.
    P_left = transfer([Fraction(1), Fraction(1), Fraction(0), Fraction(0)], 2)
    P_right = transfer([Fraction(0), Fraction(0), Fraction(1), Fraction(1)], 2)
    assert P_left == [Fraction(3, 4), Fraction(1, 4)]
    assert P_right == [Fraction(1, 4), Fraction(3, 4)]
    assert transfer([Fraction(1)]*4, 2) == [Fraction(1)]*2
    # Exact preservation of all 2^m elementary cylinder masses and degree-halving.
    checked_words = 0
    for bits in (2, 4, 6, 8):
        outputs = [rho_twice(format(j, f'0{bits}b')) for j in range(2**bits)]
        assert all(len(word) <= bits//2 for word in outputs)
        assert transfer([Fraction(1)] * (2**bits), bits) == [Fraction(1)] * (2**(bits//2))
        for j in range(2**bits):
            indicator = [Fraction(0)] * 2**bits
            indicator[j] = Fraction(1)
            pushed = transfer(indicator, bits)
            assert mean(pushed) == Fraction(1, 2**bits)
            checked_words += 1
    exact_residues = [coordinate_residue(n) for n in (1, 2, 3, 4)]
    assert exact_residues == [Fraction(1,4), Fraction(9,32),
                              Fraction(1181,4096), Fraction(38745189,134217728)]
    # The proven infinite tail bound is at most 2^(n+3-2^n) for Lip(x)=1.
    lower = exact_residues[-1] - Fraction(1,512)
    upper = exact_residues[-1] + Fraction(1,512)
    assert Fraction(0) < lower < upper < Fraction(1,3)
    print('PASS: 340 elementary cylinders, exact transfer mass, constant and bit eigenmodes')
    print('PASS: exact coordinate residues n=1,2,3,4:', *(str(x) for x in exact_residues))
    print('PASS: nonzero limiting coordinate amplitude lies between', lower, 'and', upper)

if __name__ == '__main__':
    run()
