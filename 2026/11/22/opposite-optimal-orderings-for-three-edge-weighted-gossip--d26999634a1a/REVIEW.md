# Self-review of three-edge weighted gossip ordering

## Correctness — PASS

The exact rank-one contact matrices preserve the consensus direction and have a two-norm loss identity. Expanding the three chronological losses gives \(E_{(a,b,c)}-E_{(a,c,b)}=4abc(1-a)(c-b)\), with reversal reducing six schedules to the three possible middle choices. For the worst-case assertion, the singular-value products \(U=\prod_i(1-2p_i)^2\) and \(V=32\prod_ip_i(1-p_i)\) are independent of order; the second identity follows from the triangular edge-vector representation in the determinant of \(I-T^{\mathsf T}T\). The equation \(E=1+W+U/W-V/(1-W)\) is strictly decreasing between distinct feasible maximum squared singular values. Therefore the optimal middle coefficient is maximal for isotropic error and minimal for worst-case error. This is an all-real-parameter proof, including coincident coefficients and the possibly singular case \(p_i=1/2\). The replayed `verify.py` passed symbolic identities, exact rational root isolation, and 24 additional rational coefficient triplets. No infinite-domain conclusion is inferred from the finite checks.

## Originality — PASS on inspected sources, qualified

The strongest relevant prior work is Lu–Morse–Anderson–Yu (2010), which proves strict Euclidean contraction for complete gossip sequences and explicitly identifies optimizing the singular contraction coefficient as an open direction. Liu–Mou–Morse–Anderson–Yu (2011) proves an ordering-invariant *eigenvalue* convergence factor on trees, but eigenvalue equality does not entail the present one-sweep norms. Mangoubi–Mou–Liu–Morse (2013) optimizes a *common* mixing weight for periodic convergence, not arbitrary edge-specific weights or finite-sweep singular-value optima. Shi–Li–Johansson–Johansson (2012) treats exact finite-time consensus, not finite-sweep approximation. An indexed arrowhead Gauss–Seidel result addresses another update map and another performance criterion. An earlier path-averaging theorem covers unweighted paths, not this weighted star. Statement-level implications and material read were distinguished; inaccessible or unindexed equivalent work remains a publication-priority risk, not claimed absent.

## Value — PASS

This is a complete, parameter-uniform and sharply characterized design conflict for a natural four-agent communication graph: the best one-sweep contact schedule depends on whether a designer controls average squared disagreement or the worst initial direction. The reversal arises even though asymptotic spectra are identical for all six schedules, exposing a practical blind spot in spectral-rate-only scheduling rules. Three contacts are necessary for this star ordering effect, and the result holds for physical heat-edge transfers without optimizing the coefficients themselves. It does not assert universality on larger graphs or repeated periods.

## Scope and independent review

The claim is restricted to three fixed positive convex mixing parameters, applied once each to a three-leaf star. The historical literature search and available index are not complete publication-priority certificates. External proof verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
