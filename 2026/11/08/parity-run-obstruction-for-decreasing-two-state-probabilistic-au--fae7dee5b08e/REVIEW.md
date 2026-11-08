# Scientific review

## Correctness — PASS
For two states, the determinant of the row-stochastic letter matrix equals the slope of the corresponding affine probability update, so the negative determinant hypothesis is exactly strict order reversal. Taking minima and maxima after one step yields the envelope recursion. Two steps yield monotone envelope compositions, so their parity-indexed orbits are monotone. Strict unique maximization at total length forces every prefix to attain the unique relevant minimum or maximum depending on remaining parity. Each chosen letter strictly maximizes or minimizes an affine envelope at the monotone extremal input. Strict winner and loser regions for each letter are convex intervals, preventing reappearance after an intervening different letter on a fixed position parity. Standard distinct-run enumeration gives the exact necessary-family count; the finite rational checker confirms examples but is not used as an infinite proof.

## Originality — PASS relative to inspected sources; priority risk remains
Gill, arXiv:2402.13376, Section 4, proves a complete *binary* two-state classification, not an arbitrary alphabet bound. Kjos-Hanssen, arXiv:2607.26275, gives a three-state universal construction for all alphabets rather than a negative-determinant two-state obstruction. A separate nonnegative-determinant two-state result concerns increasing, not decreasing, affine maps and does not imply the parity-dependent choice argument. Searches of available research-index descriptions for 'negative slope', 'two-state PFA', 'parity' and 'polynomial sparsity' did not find an implication-equivalent theorem. The claim is limited to alphabets of size at least three, avoiding presentation of binary consequences as novel. Unindexed or implicit previous results remain possible.

## Mathematical value — PASS
The 2026 three-state universality result makes the classification boundary at two states natural for nonbinary alphabets. Here a determinant-sign restriction, invariant under simultaneous state relabeling, yields a structural obstruction and a uniform exponential-density separation for arbitrary fixed alphabet size. The parity-specific run condition captures the order reversal of negative transition slopes and provides a usable filter for candidate two-state witnesses. This is not a complete two-state classification; mixed signs and sharpness remain unresolved.

## Limitations and closest literature
Source-specific comparison and residual priority risk are recorded in the structured audit. The necessary bound need not be attainable, and empirical finite checks cannot certify universal quantifiers.

Self-review: passed. Independent audit: not yet performed.
