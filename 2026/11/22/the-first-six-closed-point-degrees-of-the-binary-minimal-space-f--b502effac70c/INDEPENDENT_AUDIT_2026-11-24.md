# Independent mathematical audit

## correctness

PASS

Independently enumerated normalized points using the last nonzero coordinate and alternate irreducible moduli for degrees 3–6; counts are (15,15,15,19,50,15), with closed-place counts (15,0,0,1,7,0). The four affine Jacobian ideals are unit ideals. The stated linear map has order five, preserves the ideal, and fixes precisely four geometric eigenlines, which are the degree-four Frobenius orbit on the curve. Strictly, these points on C are the ramification locus, and their images form the branch locus on B; the quotient is injective on the four fixed points, and the branch place downstairs also has degree four. Tame Riemann–Hurwitz gives genus three. On degree-five places the independently computed permutation is (1,1,5); its two invariant places lie over rational points because geometric fibers of the quotient are deck orbits and Frobenius preserves those two orbits. Every rational fiber is unramified, with Frobenius acting as a translation of a C5-torsor, so the three rational deck cycles and two invariant degree-five places give exactly three split and two inert fibers. The truncated closed-point Euler product gives 1,12,77,350,1261,3827,10157 through degree six. The all-curve assertion uses the earlier one-orbit theorem, also independently checked: a cubic vanishing on binary projective space is a linear combination of the six alternating-coordinate cubics, and rank two factors into planes and cannot contain the nonplanar integral complete intersection. For the standard rank-four cubic, the space of vanishing quartics modulo its linear multiples has dimension 16. Enumerating the nonzero classes under symplectic transvections gives 127 orbits, with 125 rejected by a rational singularity, one by an extension-field singularity, and just one smooth orbit of size 144 containing the representative. Replay: python3 /workspace/branches/independent_exact.py curve and python3 /workspace/branches/independent_curve_orbits.py (SymPy). No evidence for the higher-degree spectrum or full numerator is claimed.

## originality

PASS

The scoped additional arithmetic is distinct on the sources inspected. The construction, one embedded projective class, order-five automorphism, genus-three quotient, degree-four branch orbit, exclusion of degree-two places, and the first two coefficients are prior. The exact remaining low-degree data, deck permutation, rational quotient fibers, and coefficients of degrees three through six are the supported increment, not new classification of the curves themselves.

## value

PASS

The uniquely distinguished binary embedded curve supplies a nonarbitrary test case. The new counts distinguish the first unramified nonrational places from the previously known branch place; the deck permutation makes the difference between split and inert rational fibers explicit. These are usable inputs for later Frobenius, low-degree divisor and zeta calculations on this curve, without an unsupported claim to determine the full zeta function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
