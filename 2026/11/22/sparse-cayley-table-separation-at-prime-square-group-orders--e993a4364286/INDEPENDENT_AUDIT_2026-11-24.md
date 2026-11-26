# Independent mathematical audit

## correctness

PASS

For t distinct names, the group equations define the quotient of Z^t by the rows e_a+e_b−e_c; a realization is a homomorphism separating all names. Split each equation row into a unit row and an oriented incidence row, keeping any appended e_i−e_j intact. Restricted incidence rows have at most one entry of each sign; induct on the minor size by expanding a row with at most one nonzero, or use the zero row sums when all rows have both signs. Multilinearity bounds every minor by 2^k, even with repeated labels, so M and each augmentation retain their rational ranks modulo p for p>2^k. A full-rank pivot minor is a p-local unit: its rows generate the localized row lattice by solving on the pivot columns, and the quotient is free. A difference lying in the row span mod p lies in the rational span by equality of augmented ranks and hence in the localized row lattice, so it vanishes in both targets. In a realizable pattern each other difference has a unit coordinate; its collision probability under a uniform homomorphism is p^(−2) in either target. The union bound binomial(3k,2)<4^k for k≥1 gives a collision-free realization in both, with unused labels filled arbitrarily. The addition chain names distinct powers of a generator in C_(p²), but in exponent p the first and last powers agree. Doubling and a final +2 give the stated families; the chains for 11, 19 and 23 give lengths 4, 5 and 5. At p=2 every one-entry equality pattern is possible in both groups (identity, doubling a suitable nonzero element, an identity factor, or two distinct nonzero summands with a third distinct sum), and the two-step chain separates. The p=3 lower bound is already 2. Inspected VERIFICATION.md and cayley_sparse_check.cpp; no uploaded executable was run. RESULT.md:63 has a prose slip: the tested primes 5,7 for k=1,2 and 11,13 for k=3 are above 2^k, not below it; they are below the reference 17. This does not affect the theorem or the stated finite partition counts. The package marker is finite corroboration only.

## originality

PASS

Credit the earlier identification invariant and order-at-most-23 computations. The supported distinct result is two-way equivalence of all sparse patterns above a uniform prime threshold and its consequences for prime-square orders, not the definition, the already tabulated small values, or a general cyclic-group upper bound in isolation.

## value

PASS

This gives a structural obstruction for the natural minimum-fill identification invariant, ruling out every sparse pattern rather than just short power witnesses. It also yields an explicit logarithmic bound and exact infinite-form prime families without implying that either family contains infinitely many primes. The p-local minor argument explains why the two different exponents cannot be detected by such patterns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
