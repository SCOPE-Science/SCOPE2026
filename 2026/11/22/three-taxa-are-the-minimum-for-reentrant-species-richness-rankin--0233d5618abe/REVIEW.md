# Review of a two-method Poisson-capture richness comparison

## Correctness — PASS
For exact Poisson detection, expected richness is a sum of one-minus-zero probabilities. The complete two-taxon classification follows from a hyperbolic ratio with monotone derivative; all boundary cases are addressed in the proof. The three-taxon alternating signs follow from an exact polynomial factorization into two strictly increasing functions with distinct positive roots. The standalone checker verifies the polynomial identity, rational root brackets, and supplementary integer-rate instances; it does not substitute finite experiments for an infinite proof.

## Originality — PASS, with historical-priority risk
Comparison against the original eDNA method study, conventional rarefaction sources, Chase et al.'s empirical multiple-crossing discussion, and the closest two published research notes found no directly covering three-taxon unequal-total Poisson-method theorem. Crossings of species-accumulation curves are prior art and are not claimed new. The published four-species minimum concerns normalized iid probability profiles at equal draws; the finite three-species single-crossing note concerns equal-census hypergeometric rarefaction. Both have assumptions unavailable for the unequal capture-rate totals \(16\) and \(15\). An unlocated Laplace-transform or stochastic-order reduction remains possible.

## Value — PASS, restricted to model structure
Field method selection is sensitive to taxon-specific capture efficiency, and richness measured at one effort can obscure later ranking reversals. The theorem provides a minimality result and a usable two-taxon crossing criterion, with explicit nondegenerate two-switch construction. It does not demonstrate such reversals in actual samples or prescribe field volumes.

## Evidence and limits
The motivating research data were publicly archived 2024-08-27; the journal article appeared later, on 2024-12-16. Scientific limitations are positive constant Poisson capture rates, perfect detection given capture, fixed species presence, and expectation-level rather than realized rankings. General crossing phenomena and basic species-accumulation formulas are established prior mathematics. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
