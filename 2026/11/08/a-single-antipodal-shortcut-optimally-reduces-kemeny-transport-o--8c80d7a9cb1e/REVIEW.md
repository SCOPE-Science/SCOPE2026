# Scientific review: single-chord Kemeny transport on cycles

## Correctness — PASS
For each integer \(n\ge4\) and each nonedge chord-distance \(2\le d\le\lfloor n/2\rfloor\), the statement specifies a discrete-time, neighbor-uniform random walk with degrees updated after inserting the chord. The proof reconstructs the resistance-weighted Kemeny identity from the commute-time and random-target identities, then applies the rank-one electrical update with exact cycle currents. The weighted potential variance and resistance sum yield the stated rational difference. Its numerator is negative at the shortest admissible chord and strictly decreases in the chord resistance parameter; the derivative of the full quotient is strictly negative. The asymptotic quarter improvement follows from either parity. Exact independent grounded-Laplacian computations agree on all 100 chord distances for \(4\le n\le22\); the general result is a proof, not an extrapolation from computation.

Risk: the result applies to Kemeny's stationary-target hitting-time average, not an unweighted target average, arbitrary edge weights, or spectral-gap mixing time. These distinctions are explicit in the claim.

## Originality — PASS on inspected evidence, provisional
The principal nearby full-text source is Kirkland--Zeng (2016), which derives a general forest identity and studies additions to trees, including path-to-unicyclic and lollipop examples. It does not evaluate a chord added to an already cyclic graph or optimize chord distance. The full-text Pitman--Tang Kemeny formulas are universal symbolic identities without a cycle-chord evaluation. Later inspected Braess-clique (2026) and Erdős--Rényi (2026) treatments apply to distinct graph regimes. Searches for chorded-cycle, three-path theta, Kemeny--Braess, and effective-resistance aliases yielded no direct explicit counterpart. Available existing claims were compared at the level of objects and implications; none supplies this exact optimizing random-walk result.

Residual risk: bibliographic retrieval cannot rule out unindexed earlier exact evaluations, and universal resistance formulas in the literature can be specialized algebraically to recover the result. No priority certification or independent literature audit is claimed.

## Mathematical value — PASS
A one-edge intervention on a cycle is a natural minimal shortcut design problem for stochastic transport, not an arbitrary parameter slice. The exact formula resolves all possible chord placements, completely rules out a Braess anomaly for this whole family despite anomalies on trees, identifies a strict optimal separation, and quantifies a non-vanishing asymptotic efficiency improvement of one quarter. This is an explicit infinite-family optimization law rather than a routine restatement of a universal identity; its primary significance is the sharp structural classification, not the method of computation.

Self-review: passed. Independent audit: not yet performed.
