# Mathematical review: entropy-limiter radial projection boundary

## Correctness — PASS

The theorem quantifies over every positive weight vector and all means, budgets and candidates for a fixed strictly convex \(C^3\) scalar entropy. The decisive geometric step is justified: when radial and metric projections agree, the smooth entropy level-set normal at each nonzero mean-zero vector must align with that vector. Since the mean-zero space has connected spheres precisely from dimension two onward, the entropy functional becomes even under sign reversal. Its third-order Taylor odd part and an explicit nonzero weighted third-moment direction force the third derivative of the entropy to vanish at every mean. The reverse quadratic implication and the exceptional two-node interval case are proved directly. The Simpson-rule comparison was independently recomputed with exact rational arithmetic using the standalone checker. The example does not substitute for the proof for arbitrary dimensions.

## Originality — PASS with specified historical risk

Wu (arXiv:2604.00301) establishes a maximal scaling factor **on a specified ray**, with a closed-form quadratic-entropy example. Liu, Guo, Jiang and Sun (arXiv:2603.27478) similarly optimize a factor along a conservative ray, not the weighted Hilbert projection over the whole entropy-feasible set. The tested claim concerns operator equality for all budgets and candidates, and identifies both a two-point exception and the sharp three-point boundary. The abstract of N'guessan–Kim (arXiv:2602.08419) supplies related radial/additive-separability rigidity, but describes a different full-coordinate-space hypothesis, not the mean-zero weighted hyperplane projection classification. Its full paper could not be inspected, so historical priority is not independently certified. Related positivity-only limiter distortion addresses a different polyhedral constraint, not strictly convex entropy sublevels.

## Value — PASS

A conservative entropy limiter is often described as minimal modification *along the prescribed mean-to-candidate ray*. That is not equivalent to minimum weighted \(L^2\) modification over all entropy-feasible mean-preserving arrays. This theorem precisely identifies when those two natural optimization tasks agree, including the smallest nodal count where they can disagree, and supplies a positive-state Simpson-rule example that makes the distinction quantitative and reproducible. It does not claim an error or stability defect of entropy-preserving DG methods.

## Limitations and sources

The claim is limited to a scalar globally \(C^3\) strictly convex entropy, one cell's fixed mean, and one entropy inequality. No theorem is asserted for coupled systems, joint invariant-domain constraints, or PDE accuracy. Full-text inspections covered the explicit entropy-radius construction in arXiv:2604.00301 and the scaling-limiter formulation in arXiv:2603.27478; the related radial-separability manuscript could only be inspected by its abstract. A further uncatalogued mathematical equivalence remains a possible priority risk.

Self-review: passed. Independent audit: not yet performed.
