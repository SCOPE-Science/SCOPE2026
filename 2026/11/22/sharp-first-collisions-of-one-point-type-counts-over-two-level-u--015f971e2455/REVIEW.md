# Self-review

## Correctness: PASS

The Katětov inequalities for old distances \(1\) and \(3\) leave precisely the two disjoint active-class cases stated in RESULT.md, yielding the polynomial. The specialization gives the unweighted count; downward binomial inversion is triangular with unit diagonal. The partition generator exhaustively enumerates nondecreasing positive compositions through \(n=16\) and includes independent partition-number checks, so its exact finite cutoffs are proved as complete finite cases; there is no extrapolation from an incomplete search. The attached verifier also compares 54 full direct Katětov diagrams with polynomial coefficient counts, and independently checks inverse recovery. The append-a-part identity proves collisions for every larger size.

## Originality: PASS, with residual risk

Conant's arXiv:1502.05002 Section 6 provides the Katětov / quantifier-free type framework but does not count cluster families. A closely related published 2026 metric type polynomial applies to old distances \(1,2\), not the crucial old distance \(3\) used here. The published ultrametric colour-refinement result examines an entirely different invariant. Searches of published mathematical findings, primary literature and accessible previous claims revealed no statement forcing the \(n=10\) and \(n=16\) scalar-collision thresholds or the displayed polynomial. A historical equivalent remains possible.

## Mathematical value: PASS

The central question asks how much of a finite parameter metric can be reconstructed from the number of complete one-point types, an invariant natural to homogeneous model theory. The finding establishes two sharp reconstruction cutoffs, a complete classification of the first ambiguity pairs, persistence of ambiguity at every larger size, and an exact finer statistic that restores complete reconstruction. Those cutoffs distinguish intrinsic base structure from information discarded by unrefined logical type counts, rather than merely recomputing a known table.

## Closest literature and limitations

Conant (2015) supplies general foundations; the 2026 \(\{1,2\}\)-graph-metric type polynomial supplies an adjacent but noncovering comparison; the 2026 finite-ultrametric colour-refinement study proves a distinct recovery theorem. The claim is restricted to pointwise-named two-level ultrametrics inside the unrestricted \(\{1,2,3\}\)-metric Fraïssé limit. The finite cutoff certificate covers exactly all integer partitions up through sixteen points, and the general proof supplies the all-size formulas and collision propagation. Search cannot establish absolute publication priority.

Self-review: passed. Independent audit: not yet performed.
