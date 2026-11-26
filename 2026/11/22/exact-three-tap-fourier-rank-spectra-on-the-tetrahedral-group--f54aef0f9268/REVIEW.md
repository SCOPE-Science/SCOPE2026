# Independent mathematical audit

## correctness

PASS

Left translation multiplies the regular operator by an invertible permutation, and conjugation by S4 preserves rank. There are 12 Klein triples, 144 doubled-coset supports, and 64 transversals, 16 of which are cosets of a unique order-three subgroup. For the mixed case translate a doubled-coset point to e and conjugate the singleton to (234); its centralizer cycles the three nonidentity elements of V. For a noncyclic transversal normalize to e,(234),v; in the inverse quotient coset, the centralizer fixes (243) and cycles the other three choices (no other element there centralizes (234)). Conjugation induces all permutations of the three nonidentity Klein elements. Thus the representatives exhaust supports. The cyclic and Klein cases reduce to subgroup convolution times subgroup index in the regular representation; the subgroup transforms have at most two and one zeros, respectively, and the proposed witnesses attain those and intermediate counts. For the two other representatives the Fourier blocks have weights 1,1,1,3. The zero-sum permutation block determinants are 1+x³+y³−y²−y and 1+x³+xy+y³. The minor −xy in the first block and the nonconcurrently zero minors 1+x, y−x, y(x−1) in the second rule out ranks ≤1. Upon imposing any scalar zero, rotate x (and y for the transversal) by the appropriate quotient characters; the determinant is invariant and becomes −4Y(Y+1) with X=−1−Y, which cannot vanish at a genuine three-tap support. Thus scalar and 3D losses are disjoint; the mixed case allows at most one scalar loss, and the transversal at most two, by the character equations. This excludes omitted ranks for arbitrary complex coefficients. Independent /workspace/record4_replay.py classified supports by cosets rather than the orbit algorithm and verified all 696 integer-witness support/rank pairs by gcd-reduced integer row operations in the full regular matrix. A separate exact check also confirmed the polynomial identities and orbit census. Supplied scripts and outputs were inspected, not executed.

## originality

PASS

The inspected exact nearest results do not cover the variable-complex-weight, fixed-three-point A4 support question. The general uncertainty bound and representation/graph framework are credited, as are the reverse A4 support theorem, the odd-prime dihedral analogue, and the nearby unit-weight results in other groups. Distinct indexed cases were compared at the level of group, tap weights and fixed quantifier.

## value

PASS

This is a natural complete finite rank invariant of the smallest alternating group with a 3D irreducible, not a few coefficient samples. Rank gaps turn support geometry into a constraint on the dimension of the image or nullspace, and the rank-10 and rank-4 loci are not available from a support-size uncertainty bound. The nonconcurrent Fourier-block degeneracies explain the geometry-specific spectra. No numerical conditioning or larger-group claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
