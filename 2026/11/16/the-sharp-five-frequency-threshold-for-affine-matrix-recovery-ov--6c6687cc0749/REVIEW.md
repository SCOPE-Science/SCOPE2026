# Independent mathematical audit

## correctness

PASS

A nonzero entry of the 12x11 C_phi(m,n) rank test requires an ordered support pair with additive difference m and multiplicative quotient n. For |S|<=3 there are at most six ordered pairs. For |S|=4, rank 11 requires >=11 distinct nonzero additive differences, but they form an even set, hence all 12 and each ordered difference occurs exactly once: a planar (13,4,1) difference set. Exhaustive direct Python enumeration over all C(13,4)=715 4-subsets found 52 perfect sets, precisely affine translates/scalings of D={0,1,3,9}; each admissible translation has at most 9 nonidentity multiplicative ratios and so cannot yield column rank 11. For the five-site witness (1,2,3,4,11) with weights (1,2,4,8,16), its dominant coefficient makes all multiplicative chars of |phi|² nonzero; independently computed exact 11x11 minor determinant -2^43, so the Bartusel–Führ–Oussa criterion yields full complex 12x12 matrix recovery. Reviewed an independent finite-field 156x144 rank-mod-53 certificate in the supplied source: since 10 has order 13 mod53 it legitimately certifies a characteristic-zero nonzero maximal minor. Finite exhaustive scope is all p=13, not extrapolation.

## originality

PASS

Best-of-knowledge statement-and-implication comparison: The published prime-affine sparse cyclic tomography result recovers functions from complete coset sums and uses prime Fourier minors; it is not rank-one conjugation/projector matrix recovery. Standard phase retrieval alone may be weaker than full complex matrix recovery, another non-equivalence. Bartusel–Führ–Oussa Theorem 6.5 is a general necessary and sufficient recovery criterion; it does not itself give the min support five at 13. The rank 11 support-cover incompatibility and complete Singer-difference-set translation census provide the new finite optimization step. The prime-13 Singer (13,4,1) difference sets are classical, but the 52-set classification does not count multiplicative quotients of translates in U or certify the 5-site rank witness; Resultary's prime-affine coset-sum census concerns other measurements.

## value

PASS

The smallest Fourier support for full rank-one affine matrix recovery at p=13 is a precise natural sparse-design cutoff, and the four-point difference-set obstruction explains why naïve counting fails. It is a motivated exact finite invariant for a 12-dimensional irreducible affine measurement family, not a random arbitrary slice; no all-primes theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
