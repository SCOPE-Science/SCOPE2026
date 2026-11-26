# Independent mathematical audit

## correctness

PASS

The quartic is smooth for p≥7: on any nonempty subset of nonzero coordinates the derivative equations reduce to the corresponding invertible submatrix of the 4-diagonal, 6-off-diagonal system in the squares. I independently obtained the lines as the signed coordinate permutations of z=((1+2i)r/5)y, x+y+z=0, and x+y+2iz=0, where i²=−1 and r²=5. For the first seed, s²=(−3+4i)/5 satisfies 5s⁴+6s²+5=0, precisely the square condition on the binary restriction. The latter two restrictions are 5(x²+xy+y²)² and (5/16)(x−y)⁴. Thus the identities persist in all stated characteristics. The exact standalone replay /workspace/branches/kk_crossings_audit.py, run with Python 3, regenerates the 28 triples from these symmetry families, computes the 3276 determinants by coefficient convolution, and verifies the complete norm support by division to 1. It gives 36 identically zero determinants. Outside the support no triple changes status; the baseline triple pattern has no pair in 26 concurrent triples, so collision of any two components would contradict that pattern. At every exceptional prime the replay checks distinctness directly and normalizes the pairwise cross products in a genuine quadratic finite field. It tallies crossings and rational components by their normalized coordinates, rather than the frozen incident-set determinant test. The seven exceptions and the four generic sign representatives reproduce every multiplicity row, the fixed-incidence corrections, and (ell,b,c). The two sign actions are inherited from the same line permutations for every prime outside the sieve, and the triple patterns determine the crossing label sets. Each rational crossing adds 1−s_P after summing rational lines, including s_P=0 for crossings on conjugate nonrational lines. Frobenius squares to the identity on lines and crossings, so extension degree parity suffices. Expanding the logarithms of the four displayed factors gives the even/odd counts and checks the zeta signs and exponents. No assertion is made below p=7 or about the quartic's own zeta.

## originality

PASS

Credit the existing complex line configuration, the Ciani specialization of the exceptional-prime support, and finite-field component splitting. On the inspected evidence the distinct result is the complete arithmetic crossing and point-count classification of the reduced 28-line union, especially the corrections at bad-incidence primes where the quartic remains smooth. Priority is bounded by the accessible literature and indexed evidence, not asserted absolutely.

## value

PASS

This is a natural exact arithmetic invariant of the canonical full bitangent arrangement of a symmetric quartic. It separates good reduction of the quartic from changes in the line arrangement, and at p=7 separates changes visible over the quadratic extension from those visible over the prime field. The coverage of every prime and every extension, including changes to rational crossing incidence, is the useful classification, not a recomputation of the complex row or the exceptional prime list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
