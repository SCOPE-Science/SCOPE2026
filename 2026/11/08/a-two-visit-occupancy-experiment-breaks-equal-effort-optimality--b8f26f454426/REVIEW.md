# Review: two-visit occupancy information design

## Correctness — PASS

The four binary histories have explicitly normalized probabilities. Direct differentiation gives all three Fisher information entries and the determinant in equation (1). For fixed total effort the determinant is maximized by the scalar objective \(f(x)+f(\theta-x)\). The proof obtains strict small-budget concavity from a uniform analytic expansion, an exact non-equal-budget witness by rational arithmetic, and the universal short-probe asymptotic by compactness and uniqueness of the maximum of \(f\). The finite symbolic and rational checks in `verify.py` independently reproduce the critical algebra; they do not substitute for the continuum proof.

## Originality — PASS within inspected evidence, provisional

MacKenzie–Royle (2005) treat occupancy-estimator precision and allocation across sites and replicate counts. Guillera-Arroita–Ridout–Morgan (2010) explicitly treat D-optimality of *replicate counts* under identical detection probabilities, making them the closest known source, but do not establish fixed-two-visit, unequal-duration D-optimality or its universal occupancy-prevalence independence and large-budget short-probe law. Moore and colleagues (2014, 2016) optimize detection probability under stochastic between-visit detection conditions; Bornand and colleagues (2014) exploit observed detection times, which are not available under the present binary data reduction. The 2020 Reich paper is highly relevant to occupancy design but emphasizes MSE for occupancy and alternative visit policies, not the same joint-information objective in its accessible descriptions. An older equivalent specialization in experimental-design or cure-mixture literature remains possible. Neither nonmatching titles nor unsuccessful searches establish historical uniqueness.

## Value — PASS

The simultaneous estimation of occupancy and detectability is a real motivation for replication in ecological monitoring. With exactly two budgeted binary survey opportunities, the theorem identifies a counterintuitive departure from equal allocation, supplies exact quantitative improvement at a natural budget, and derives the asymptotically unique short-probe scale. The optimized duration split is insensitive to the unknown occupancy prevalence even though inference for both parameters remains the objective. The result provides a mathematical benchmark for protocol comparison, not a direct prescription for field surveys with heterogeneity, overhead, or scarce site counts.

## Limitations and closest literature

The conclusion assumes independent Poisson detections with a common rate, closed site occupancy, no false positives, predetermined two-visit binary observations, and fixed local Fisher D-optimality. It does not establish a globally unique finite-budget bifurcation threshold or independent priority. Closest inspected literature: https://doi.org/10.1111/j.2041-210X.2010.00017.x ; https://doi.org/10.1111/j.1365-2664.2005.01098.x ; https://doi.org/10.1371/journal.pone.0115345 ; https://doi.org/10.1111/2041-210X.12564 ; https://doi.org/10.1111/2041-210X.12171 .

Self-review: passed. Independent audit: not yet performed.
