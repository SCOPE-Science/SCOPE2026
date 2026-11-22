# Scientific review

## Correctness (C): PASS

The exact proof covers all nonnegative outer and inner zero gaps, including adjacent ones and the two-letter degenerate case. Counting occurrences rather than distinct strings is made explicit. Classifying possible borders of factors with zero, one and two marked letters gives a complete list of maximizing intervals; the resulting disjoint cases yield the rational generating functions and exact coefficient formulas. The joint limit follows from uniformly distributed simplex spacings and direct area calculations. Independently implemented KMP-interval and integer-family checks agree on every tested case, as documented in VERIFICATION.md and the reproducible outputs.

## Originality (O): PASS for the assessed claim

The two-marker longest-border spectrum, together with the equality of longest unbordered length and least period in this specific family, already covers the *univariate length law*; that law is deliberately not asserted as original. The new claim is instead the **complete occurrence multiplicity classification, four-valued all-length enumerator, and joint length–multiplicity limit**. The full 2026 Mieno algorithm text was inspected and treats arbitrary-instance reporting and complexity rather than the symbolic fixed-weight census. The full earlier independent-letter random-source analysis was inspected; it does not apply to the rare fixed-weight-two conditioning. The full published scientific RESULTS of the two-marker border-spectrum and three-marker longest-factor studies were read: both classify scalar lengths, without enumerating longest-unbordered occurrence intervals or their joint count distribution. An unindexed equivalent remains a priority risk.

## Value (V): PASS

The newest global algorithm returns **all occurrences**, so their exact output multiplicities form an intrinsically motivated combinatorial invariant. The theorem solves this output-size question at every length for the smallest nontrivial sparse binary ensemble, identifies the unique four-occurrence extremizers and gives the probability of genuine multiplicity under a natural fixed-content source. The joint limit separates one- and two-occurrence cases by different conditional maximum-length laws. This is a structural and enumerative benchmark, not merely a restatement of the previously known longest-length marginal or a claimed improvement in running time.

## Limits

The result concerns only words with exactly two ones and counts interval occurrences. No claim is made for other Hamming weights or unrestricted random sources. Publicly indexed scientific coverage remains incomplete, and no independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
