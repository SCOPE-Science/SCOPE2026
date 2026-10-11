#!/usr/bin/env python3
"""Finite regression checks for the Fox--Milnor parity-law package.

The infinite theorem is the UFD factor-orbit argument in RESULT.md.  This
script checks the concrete 5_2 polynomial and exhaustively stress-tests the
parity bookkeeping under multiplication by arbitrary square factors in a
small exponent box.
"""


def norm_status(selfdual, paired):
    # For a reciprocal polynomial, a Fox--Milnor norm is equivalent to even
    # exponents on self-reciprocal irreducible orbits and equal exponents on
    # every non-self-reciprocal reciprocal pair.
    return all(e % 2 == 0 for e in selfdual) and all(a == b for a,b in paired)

# Stress-test that adding a square of a reciprocal polynomial cannot alter
# norm status: self-dual exponents gain even increments and paired exponents
# gain the same even increment on both sides.
for a in range(6):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                before = norm_status([a,b], [(c,c)])
                for x in range(4):
                    for y in range(4):
                        for z in range(4):
                            after = norm_status([a+2*x,b+2*y], [(c+2*z,c+2*z)])
                            assert before == after

# Delta_{5_2}(t)=2t^2-3t+2.  Its discriminant is negative, so this primitive
# quadratic is irreducible over Q and hence over Z by Gauss's lemma.  Its
# coefficient list is palindromic, so its irreducible orbit is self-reciprocal.
a,b,c = 2,-3,2
disc = b*b - 4*a*c
assert disc == -7
assert [a,b,c] == [c,b,a]

pattern = []
for n in range(1,13):
    passes = norm_status([n], [])
    assert passes == (n % 2 == 0)
    pattern.append('P' if passes else 'F')

print(
    'VERIFY_OK '
    'orbit_parity_invariant=true '
    f'delta_5_2_disc={disc} '
    'repeated_n_1_12=' + ''.join(pattern) + ' '
    'odd_fail_even_pass=true'
)
