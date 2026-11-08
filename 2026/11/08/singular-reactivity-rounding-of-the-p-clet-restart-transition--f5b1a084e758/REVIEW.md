# Scientific assessment: singular reactivity rounding of the Péclet restart transition

## Correctness — PASS

The theorem concerns the optimizing **mean killing time**, with a full-line delta sink, finite positive reaction strength, and drift toward the sink. The rank-one resolvent and renewal identity yield the exact dimensionless objective; its derivative numerator has a strictly increasing normalized power series. The critical coefficients are computed explicitly, and monotonic-root bracketing converts each local balance into a genuine global-optimum asymptotic. The critical scaling is uniform for the bounded crossover parameter, with no unsupported claim of uniformity outside this range. The embedded standard-library numerical diagnostics pass 1,591 bounded checks; these are supporting diagnostics, not proofs of asymptotic statements. The finite-parameter optimizer's existence and uniqueness are used as an auxiliary baseline rather than asserted as the novel finding.

## Originality — PASS, qualified

The 2026 drifted delta-trap paper already gives the full reset-free resolvent, survival transform and mean-time objective, as well as driftless optimization and weak-drift corrections. Its exact mean-time formula is therefore not original. The 2019 drift-diffusion paper already establishes the perfect-absorber Péclet transition; that phase boundary is not original. The 2013 imperfect-absorption work treats the driftless setting. The 2022 discrete-time biased-walk work supplies broader renewal and partial-defect formulas. The newly assessed statement is the **singular limit of the positive finite-reactivity optimizer**, with sharp powers on opposite sides of the Péclet transition and the universal cubic critical-window scaling law. These statements were not identified in the inspected primary material or in the searched mathematical records.

The remaining publication-priority risk is an unlocated more general singular-perturbation theorem, or a derivation of exactly the same scaling law in the discrete-defect or partially reactive boundary literature. Derivability from known transforms alone is not treated as proof of novelty; the value and originality judgment pertains to the nontrivial optimized asymptotic classification, not to the underlying renewal identity.

## Value — PASS

For a perfectly absorbing target, sufficiently strong drift toward the target makes a positive resetting rate disadvantageous. Finite reactivity removes that sharp zero-control region even when reactivity is extremely large. The exact inverse-square-root and inverse-cube-root rates, and the cubic interpolation at a drift window of width proportional to \(k^{-1/3}\), explain how a seemingly discontinuous control decision is rounded by a small physical imperfection. This supplies a natural finite-reactivity scale for experiment and optimization, not an arbitrary parameter slice or a routine numerical gain.

## Scope and limits

All parameters and limits are those stated in `RESULT.md`. No claim is made about optimized exponential survival tails, multiple targets, drift away from the point, or non-Poissonian controls. No external mathematical or publication-priority audit has been completed.

Self-review: passed. Independent audit: not yet performed.
