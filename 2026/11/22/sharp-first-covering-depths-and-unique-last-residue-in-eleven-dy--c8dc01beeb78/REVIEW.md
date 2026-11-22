# Scientific assessment of exact dyadic Stern-pair covering depths

## Correctness — PASS

The theorem is expressly finite: every integer precision \(1\le k\le11\). The two Stern-child identities and the binary-word correspondence are elementary recurrences. The standalone complete breadth-first enumeration checks each state in the full \(2^{2k}\)-state ambient space, confirms exactly \(3\cdot2^{2k-2}\) allowed states are reached, determines the first-discovery distances, and verifies that precisely one state is in the last distance layer. Independent frontier and integer-index recurrences confirm small cases; the full BFS is the exhaustive proof at the largest precisions. The supplied complete program and generated count histograms reproduce all eleven lines. There is no inference from the finite table to untested depths.

## Originality — PASS, with historical-priority risk

Reznick's original public 2006 manuscript, Section 4, treats exactly the same modular pair graph. Its Lemmas 4.1 and 4.5 establish reachability and eventual positivity, and Theorems 4.6 and 4.7 give limiting uniform distribution with nonquantitative constants, not the precise first index or first full dyadic-block depth. The published 2026 modular Stern/digit-weight independence theorem is likewise asymptotic. The modulus-nine discrepancy paper computes an entirely different spectral statistic, and the modulo-eight single-coordinate histogram does not fix pairs. Direct semantic mathematical-record queries for pair-covering depth, Calkin–Wilf diameter, dyadic residue bottlenecks, and the eleven-number sequence uncovered no matching full finite census. General transfer-matrix methods are not claimed as new. An older unindexed finite-radius calculation or a stronger covering-diameter theorem remains possible.

## Value — PASS

A natural arithmetic question left quantitative by modular equidistribution is: how deep must the canonical Stern enumeration go before *all* possible primitive ordered numerator–denominator residues have actually appeared? These exact first-covering thresholds resolve the complete initial 2-adic tower through modulus \(2048\), which involves over three million permitted pairs at the final level. The unique penultimate holdout throughout that tower is a striking sharp bottleneck, and the four-step jumps at levels six and ten show the onset is not simply a fixed linear increment. The information is pertinent to modular tree-covering and exact finite mixing questions, not an arbitrary value of one index. It has a reproducible exhaustive certificate rather than only a numerical assertion. This is finite mathematical value; no general infinite pattern is claimed.

## Limits of verification

The checker was executed from its actual included path and completed all specified assertions. Exact scientific claims were compared against the accessible public 2006 paper and three closely related published claims. Historical novelty cannot be proved from an incomplete index of literature, and independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
