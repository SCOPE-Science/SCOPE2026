# Scientific review

## Correctness — PASS

The graph, weighted tree law, entropy convention and all integer ranges are explicit in `RESULT.md`. The weighted matrix-tree cofactor gives the positive partition function. Its differentiated spectral product and the cycle Poisson-kernel sum supply the spoke marginal, which is strictly increasing in positive conductance. Unique half-edge calibration follows. Cauchy--Schwarz gives global overlap minimality across **all** laws; KL divergence gives unique entropy selection. A monotone-root proof establishes the sharp convergence constant, while the exact ordinary-uniform marginal supplies the overlap penalty. The separate `verify.py` enumerates wheel spanning trees by cycle tests, cross-checks integer cofactors, and verifies scalar identities (1626 assertions). Finite checks are corroboration only; all-order claims rest on the displayed proof.

## Originality — PASS, qualified

Albin et al. (arXiv:1805.10112, originally public 2018-05-25) establish the general fair-edge/minimum-overlap framework, including the marginal-square objective and homogeneous-graph criterion. These are prior work. Klee and Stamps (arXiv:1903.03575) establish weighted matrix-tree techniques and give other families. London and Pluhár (2023) give broad overlap benchmarks. The numerical lower bound \(m/2\) alone is not new. The assessed additional contribution is a **constructive wheel-specific full-support entropy-maximizing optimal law**, its unique polynomial calibration and the sharp exponential parameter correction, alongside the exact uniform-law excess. The closest published wheel-weight parameter result concerned an ellipsoid of a symmetric edge polytope, not spanning-tree sampling.

Searches for exact wheel fairness, equivalent weight equalization, broader overlap theorems, and exact tables produced no directly implying statement in the inspected material. A search failure does not prove historical originality; unpublished or inaccessible priority remains a real risk. Source inspection details and exact implication comparisons appear in `AUDIT.json`.

## Value — PASS

The mathematical motivation is fair sampling of graph-spanning trees with as little expected overlap as possible, with entropy selecting a unique reproducible distribution when the optimum need not be unique. On wheels, which have distinct spoke/rim edge orbits, the ordinary uniform law is not fair except at the four-vertex complete graph. The theorem identifies a one-parameter correction exactly, proves a nontrivial exponential calibration rate, and quantifies an asymptotically linear overlap penalty for using the uncalibrated law. This is an explicit infinite-family structural result, not a routine numeric instance.

## Limits

No result is claimed about general graphs, computation time, parameter estimation or independence certification. The weighted tree enumerator, fair-edge inequality and generic entropy optimization are established techniques. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
