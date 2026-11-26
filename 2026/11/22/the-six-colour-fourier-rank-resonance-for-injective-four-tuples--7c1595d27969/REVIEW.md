# Independent mathematical audit

## correctness

PASS

Diagonal translation kills all frequencies but the q³ with total character zero. For the remaining ones, sum over all equality partitions with Möbius weights (+1,−1,+2,+1,−6) for block-size types 1111,211,31,22,4. A block contributes q iff its character sum is zero, so four zero coordinates give the injective count, two give −q(q−2)(q−3), one gives 2q(q−3) and no zeros give q²P−6q for P opposite perfect pairings. The zero-coordinate multiplicities are 1, 6(q−1) and 4(q−1)(q−2). Among nonzero balanced tuples, the total q³−4q²+6q−3 follows by inclusion–exclusion. Three pairings mean four copies of a nonzero involution; exactly two mean permutations of (a,a,−a,−a) with a≠−a, counted as 6(q−t)/2. Counting incidences of the three patterns yields M₁=3(q−1)²−2M₂−3M₃ and M₀ by subtraction, which are exactly the claimed polynomials. Only P=1 can introduce a balanced zero, at q=6; the abelian group of order six is cyclic, t=2, so there are 48 such zeros, rank 168. The full rank on the translation-invariant subspace elsewhere gives the range equality. For q>4, 3q(q−2) is distinct from every other level, and at q=4 it also includes the trivial character, giving multiplicity t instead of t−1. The sign convention merely inverts frequencies. I read both uploaded verifiers without executing them and made an independent direct, exact finite check, replay python3 /workspace/evidence/direct_injection_characters.py. Reduce roots of unity to a finite field containing an element of the group's exponent order, with prime >2q(q−1)(q−2)(q−3), so each integer coefficient proved above is uniquely recovered without rounding. Nine groups of orders 4 through 9 tested, including the signed q=6 balanced histogram (−72:30, −36:44, 0:48, 36:92, 72:1, 360:1) and differing group laws at orders 4 and 8. These tests check instances; the proof is valid for all finite abelian groups of order at least four with unnormalized counting convolution.

## originality

PASS

The supported distinct contribution is the explicit disjoint signed multiplicity classification and the exact rank and torsion consequences. The partition-lattice identity and its general character-sum specialization are not new: Li–Wan's weighted sieve directly gives the individual-frequency multiplier after orthogonality. Neither that theorem nor Goodall nor the stronger-looking graph-family catalog results supplies the multiplicity classification and order-six behavior of K4 without the separate analysis of zero-coordinate and opposite-pair types.

## value

PASS

The complete census for the first four-vertex clique gives an exact invertibility obstruction on a naturally invariant space, isolated at one palette size. Its signed levels and multiplicities also quantify which information about the palette law survives even though the injective colouring count depends only on cardinality. This is a useful natural exact classification, not a table of isolated group examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
