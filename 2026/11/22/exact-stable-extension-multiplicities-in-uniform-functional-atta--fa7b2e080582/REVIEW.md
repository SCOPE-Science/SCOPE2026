# Self-review

## Correctness — PASS
The claim fixes the attack-arrow orientation, includes loops, and treats the empty map separately. Every noncycle vertex is forced by upward grounded induction. A blocked cycle is resolved deterministically, an unblocked even cycle supplies two alternatives, and an unblocked odd cycle supplies one nonstable preferred assignment. The labelled CYC/SET decomposition with free root weight \(U\) and blocked weight \(R-U\) yields the displayed exact generating function. Analytic coefficient transfer at \(z=1/e\) yields the probabilities. The independently executable exact-arithmetic checker directly compares exhaustive preferred/stable definitions against the cycle classification for every map through six vertices. Numerical checks never replace the proof.

## Originality — PASS within inspected evidence
published-finding corpus searches for functional attack graphs, random mappings, stable/preferred multiplicity and parity-resolved laws retrieved a related one-attacker result, but its independently sampled targetwise attacker model has indegree at most one and partial pointers, not this exact-outdegree-one mapping ensemble. The 2025 bounded-degree study addresses complexity, the 2017 random-AF study uses independent edge-pairs, and the recent path-based result supplies general sufficient criteria. None of the examined complete results derives the finite EGF or the omega-constant Poisson law for this ensemble. Historical kernel enumerations and inaccessible full preprint material remain residual risks.

## Value — PASS
This is an exact size-and-multiplicity census for a natural degree-constrained attack ensemble, rather than an arbitrary finite numerical slice. It gives an intrinsic graph-theoretic obstruction to semantic agreement, a coefficient-extractable closed formula at every size, and a nontrivial limiting probability with a Poisson spectrum. The contrast with the already studied one-incoming-attacker model motivates the choice of ensemble and gives a concrete question for finite-model and argumentation probability.

## Limits
The exact enumerative proof relies on functional outdegree one and allows loops; no extension to general directed graphs or partial maps is claimed. Source comparison is best-knowledge rather than a certified global priority search.

Self-review: passed. Independent audit: not yet performed.
