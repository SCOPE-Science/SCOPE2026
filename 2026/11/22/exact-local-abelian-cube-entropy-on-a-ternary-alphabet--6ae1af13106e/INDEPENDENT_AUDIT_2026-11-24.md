# Independent mathematical audit

## correctness

PASS

The all-length formula was reproduced with signed forbidden-word clusters rather than the source's suffix quotient. The minimal forbidden set is the three constant triples and 24 length-six words formed by repeating the same distinct unordered pair three times, ordering each pair independently. A length-six word made of three identical-letter pairs already contains a constant triple. None of the 27 minimal forbidden words properly contains another. For a cluster ending in w, the recurrence is x_w = -z^|w| - sum_v x_v times the overlap polynomial sum_k z^(|w|-k) over proper suffix-prefix overlaps from v to w. Separating a signed marked word into unmarked letters and maximal clusters gives 1/(1-3z-sum_w x_w), by cancellation of marked subsets of occurrences. The exact five-class cluster system yields the stated coprime numerator and denominator and the initial values. The literal 180-state length-five suffix graph is strongly connected (forward and reverse reachability from 01201) and has cycles of lengths 3 and 4 (periodic 012 and 0012); it is primitive. Perron–Frobenius and the exact series give a simple unique dominant pole with positive residue coefficient. Q changes sign on (0,1) and (2,3), and Descartes' rule permits only two positive roots. Evaluation at the pole gives alpha=2.607914749105280... and C=1.474405450809276..., consistent with the reported approximations. The source's alternate 49-state proof, including the Cayley–Hamilton shift to n>=49 and the early coefficients, is consistent with the independent result.

## originality

PASS

The exact labelled ternary series and entropy for the root-length-two cutoff are distinct from the full-language counts and growth bound, from a reusable finite-antidictionary construction, and from the indexed binary cutoff. The precise evaluated ternary cutoff was not found in the inspected material. This is a best-of-knowledge assessment, not a priority certificate.

## value

PASS

The cutoff is motivated by the shortest two block lengths, the first regular approximation that captures nonconstant anagram cubes. Its exact growth rate shows a material gap from the published full-avoidance upper bound (2.607914749... versus 2.371237), and the exact enumerator and residue provide a reusable baseline for successive finite cutoffs. This is not a new bound for full avoidance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
