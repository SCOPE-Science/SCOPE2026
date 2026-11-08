# Scientific review: Poisson hub connectivity and mixed-Gaussian outbreak fluctuations

## Correctness — PASS
The proof uses the exact multinomial incidence-pattern probabilities, the rare-triple union bound, a joint Gaussian/Poisson moment-generating-function limit, an exact connectivity reduction and a tight difference bound. The total-variation estimate for the finite hub graph follows by a standard rare-cell Poisson coupling. The 96 deterministic checks in `verify.py` were executed and include exhaustive rational enumeration for small graphs; they supplement the all-size proof.

## Originality — PASS on examined evidence
The exact random-intersection representation and common-feature edge formula are classical and credited. Behrisch's component evolution theorem covers models with growing projected vertex sets, while Deijfen–Kets study degrees and clustering with a growing projected vertex count. Newman's percolation generating functions apply to a distinct triangle/edge configuration model; Rybarczyk–Stark discuss clique counts. These examined statements do not give the fixed-hub seeded joint random-graph/conditional-Gaussian outbreak law. Semantic records and 97 accessible historical claims were checked for implication, with no dominating statement identified. Historical equivalence in other notation remains an explicit priority risk.

## Mathematical value — PASS
At the natural \(n^{-1/2}\) transmission threshold, bridge formation between a finite heterogeneous hub set remains random while the ordinary infected population diverges only at \(\sqrt n\). The result distinguishes the finite random connectivity skeleton and the separate \(n^{1/4}\) Gaussian population fluctuations, with exact component-dependent mixture weights. These are meaningful physical outbreak observables rather than a routine value of a predetermined invariant.

## Boundaries and remaining risks
All activities and the hub number are fixed; bonds are undirected and independent; the theorem concerns final connectivity, not epidemic timing or directed spread. The comparison does not establish global uniqueness or independently audited priority. The full texts of Bloznelis (2010) and Rybarczyk–Stark (2010) were not inspected; their accessible statements describe different settings.

Self-review: passed. Independent audit: not yet performed.
