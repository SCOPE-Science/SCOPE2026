"""Exact finite verification of the exponential-plus-linear dyadic covering theorem.
No external packages are required. Checks are finite, not a substitute for the proof.
"""


def covers(a, b, k, stop):
    modulus = 1 << k
    observed = set()
    power = 1
    for n in range(1, stop + 1):
        power = power * a % modulus
        observed.add((power + b * n) % modulus)
    return len(observed) == modulus


def sharp_witness(a, b, k):
    modulus = 1 << k
    residue = b * (k - 1) % modulus
    # In the eventual affine segment k,...,modulus+k-2 this is the sole omission.
    return all((pow(a, n, modulus) + b * n) % modulus != residue
               for n in range(1, k))


def check():
    checked_triples = 0
    verified_witnesses = 0
    for k in range(1, 9):
        modulus = 1 << k
        bound = modulus + k - 1
        for b in range(1, modulus, 2):
            witnesses = []
            for a in range(modulus):
                assert covers(a, b, k, bound), (k, a, b, 'coverage')
                checked_triples += 1
                if a & 1:
                    assert covers(a, b, k, modulus), (k, a, b, 'odd-permutation')
                elif sharp_witness(a, b, k):
                    witnesses.append(a)
            assert witnesses, (k, b, 'missing-sharpness-witness')
            assert not covers(witnesses[0], b, k, bound - 1), (k, b, 'early-cover')
            verified_witnesses += 1
    # Independent exercise of the existence argument for further exponents and all
    # odd multipliers in three sample residue classes per exponent.
    additional = 0
    for k in range(9, 17):
        modulus = 1 << k
        for b in sorted({1, 3, modulus - 1, modulus // 2 - 1}):
            assert b & 1
            witness = next((a for a in range(2, modulus, 4)
                            if sharp_witness(a, b, k)), None)
            assert witness is not None, (k, b, 'no-valuation-one-witness')
            assert not covers(witness, b, k, modulus + k - 2)
            assert covers(witness, b, k, modulus + k - 1)
            additional += 1
    print('VERIFY_OK all_moduli=2^1..2^8 all_b_odd all_a_mod_2^k triple_checks=',
          checked_triples, 'sharp_witness_b_classes=', verified_witnesses,
          'larger_sample_classes=', additional,
          'odd_base_permutation=PASS even_base_sharp_cutoff=PASS')


if __name__ == '__main__':
    check()
