# Independent mathematical audit

## correctness

PASS

Theorem 6.6 uses the stated two column types and lengths. The simplex block is full rank. An r-space U has exactly 2^(m-r)-1 nonzero columns in its annihilator, so its simplex support is B_r. The block omission conditions are containment in two distinct hyperplanes; their intersection has dimension m-2. The four frequencies are respectively G(m-2,r), twice the individual frequency G(m-1,r)-G(m-2,r) in the two separate single-block cases, and G(m,r)-2G(m-1,r)+G(m-2,r). This proves all four rows by inclusion–exclusion, including zero counts at the top ranks. For r≤m-2 the neither-active case is attainable; for r=m-1 exactly either of the two hyperplanes activates just one block; for r=m all coordinates are supported. No equal-length tie is possible under the stated parity hypotheses, but the aggregation rule is correct. The analytic calculation is universal; the frozen verify.py and recorded output for m=3,4 are supplementary, not the proof. The r=1 layer agrees with the published Table VIII.

## originality

FAIL

The distinct indexed systematic-simplex result already counts r-subspaces with every specified identity-coordinate support. The frozen all-r spectrum is a weighted two-coordinate marginal of that count after a binary row-basis change. This is a statement- and implication-level overlap, not an assertion that the two complete codes have identical lengths or a priority inference from a date.

## value

FAIL

The source construction and higher-support invariant are mathematically natural, but the precise frozen result is mechanically determined by a stronger specified-support count: relabel the two positions, discard the other systematic positions and assign the two multiplicities. This yields every histogram and hence its hierarchy. No independent exact fact or additional structural lemma remains after that reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
