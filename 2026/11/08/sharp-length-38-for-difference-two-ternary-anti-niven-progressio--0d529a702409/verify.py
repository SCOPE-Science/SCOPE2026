#!/usr/bin/env python3
"""Exact finite checks for the ternary digit-sum interval certificate and witness."""
import math


def digit_sum_3(n):
    assert n >= 0
    s = 0
    while n:
        n, d = divmod(n, 3)
        s += d
    return s


def digit_sum_3_independent(n):
    digits = []
    while n:
        digits.append(n % 3)
        n //= 3
    return sum(digits)


# For each starting residue r mod 27, three indices among 0..12.
# In one same quotient block, their three residues have digit sums 0, 1, 2 mod 3.
TRIPLES = [
    (0,4,1),(2,0,8),(12,3,0),(1,0,7),(11,2,0),(0,2,6),
    (10,1,0),(0,1,5),(9,0,1),(1,0,4),(8,2,0),(8,12,9),
    (7,1,0),(7,11,8),(6,0,2),(6,10,7),(5,0,1),(5,9,6),
    (4,1,0),(4,8,5),(6,4,12),(3,7,4),(5,3,11),(2,6,3),
    (4,2,10),(1,5,2),(3,1,9),
]


def check_certificate():
    assert len(TRIPLES) == 27
    for r, triple in enumerate(TRIPLES):
        assert len(set(triple)) == 3
        quotients = set()
        residues = []
        for j in triple:
            assert 0 <= j < 13
            t = r + 2*j
            quotients.add(t // 27)
            residues.append(digit_sum_3(t % 27) % 3)
        assert len(quotients) == 1
        assert residues == [0,1,2], (r, triple, residues)
    # Separate all-state enumeration; allows both quotient digit sums independently.
    assert all(any((left + digit_sum_3((r + 2*j) % 27)) % 3 == 0
                   if r + 2*j < 27 else
                   (right + digit_sum_3((r + 2*j) % 27)) % 3 == 0
                   for j in range(13))
               for r in range(27) for left in range(3) for right in range(3))
    # A length-12 all-nonzero example shows that the auxiliary lemma's 13 is sharp.
    runs = [(x, [digit_sum_3(x + 2*j)%3 for j in range(12)])
            for x in range(1,1000,2)]
    valid = [(x, seq) for x, seq in runs if all(seq)]
    assert valid, 'Expected an auxiliary length-12 example'
    return valid[0][0]


def check_witness():
    a = 86699
    digits = [digit_sum_3(a+2*j) for j in range(38)]
    assert digits == [
        11,11,11,13,11,11,13,13,11,13,13,13,15,11,11,13,13,11,13,13,
        13,15,13,13,15,15,5,7,7,7,9,7,7,9,9,7,9,9
    ]
    assert all(math.gcd(a + 2*j, digits[j]) == 1 for j in range(38))
    assert math.gcd(a-2, digit_sum_3(a-2)) > 1
    assert math.gcd(a+76, digit_sum_3(a+76)) > 1
    assert all(digit_sum_3_independent(a+2*j)==digits[j] for j in range(38))
    return digits


if __name__ == '__main__':
    short_start = check_certificate()
    digits = check_witness()
    # A second no-table stress test, not used to justify the infinite claim.
    for t in range(5000):
        x = 2*t+1
        assert any(digit_sum_3(x+2*j) % 3 == 0 for j in range(13))
    print('PASS 27 residue triples; 243 independent quotient residue states')
    print('PASS auxiliary length-12 nonzero example: start', short_start)
    print('PASS 38-term anti-Niven witness: 86699 through 86773')
    print('PASS independent digit-sum implementation and 5000 additional starts')
    print('Witness digit sums:', ','.join(map(str,digits)))
