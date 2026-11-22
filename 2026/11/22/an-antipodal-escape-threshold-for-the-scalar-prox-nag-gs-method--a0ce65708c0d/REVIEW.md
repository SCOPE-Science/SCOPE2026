# Research assessment

## Correctness — PASS

The current argument derives the exact constant-parameter proximal update from Algorithm 1 of the motivating paper. It checks all three scalar Jury inequalities, hence global boundedness under the strict subcritical inequality, using the uniformly bounded soft-threshold residual. In the supercritical regime, direct substitution proves existence and uniqueness **within antipodal two-cycles**; a two-dimensional positive matrix recurrence on an invariant pair of cones establishes true exponential escape, including after an admissible diagonal initialization. The local threshold dead zone yields attraction near the zero minimizer at every positive curvature ratio. The algebra is complete for the stated inequalities. `checker.py`, executed from the supplied package, passed 160 exact rational parameter cases; these tests support but do not replace the proof.

## Originality — PASS, subject to historical-priority risk

Wiykiynyuy–Ekuri–Leplat (2026), arXiv:2605.26260v1, Sections 2.3, 3.1 and 3.7, presents the two-state proximal method and sufficient linear-convergence analysis when the algorithmic curvature dominates smoothness; it does not state a finite-amplitude antipodal cycle, an invariant escape cone, or prescribed-start divergence at the explicit ratio. Leplat and collaborators (2022), arXiv:2209.14937, analyzes the smooth quadratic NAG-GS stability interval, which supplies the linear spectral comparison but has no strictly positive absolute-value regularizer or locally stabilized zero beyond that interval. Parikh–Boyd (2014), Beck–Teboulle (2009), and pertinent inertial proximal publications use different updates. Related published records on composite ProxSPS, fixed-radius trust-region steps and noisy semi-implicit NAG-GS were compared by mathematical implication; they do not directly cover this method-specific two-cycle and invariant-cone result. There remains historical-priority risk from older piecewise-affine inertial-proximal dynamical classifications.

## Value — PASS

The contrast between a locally stable minimizer for all proximal curvature ratios and escaping genuine source-initialized iterates beyond a sharp ratio is a motivated diagnostic for a new semi-implicit composite scheme. The explicit antipodal cycle, its amplitude divergence at the frontier, and a positive invariant escape cone distinguish the nonsmooth scheme from its underlying smooth Schur analysis. The result warns that local proximal identification is not a global stepsize guarantee; it does not assert global convergence below the threshold or classify the critical equality case.

## Closest literature and limits

- Wiykiynyuy, Ekuri, Leplat (2026), *Prox-NAG-GS: A Semi-Implicit Proximal Method for Composite Optimization*, arXiv:2605.26260v1, original public posting 2026-05-25: sections 2–3 and theorem statements examined.
- Leplat et al. (2022), *NAG-GS: A Semi-Implicit Stochastic Optimizer with Large-Step Stability*, arXiv:2209.14937, original 2022-09-29: smooth quadratic spectral analysis examined.
- Parikh and Boyd (2014), *Proximal Algorithms*, and Beck and Teboulle (2009), *A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems*: proximal background, not the same two-state semimplicit map.

Self-review: passed. Independent audit: not yet performed.
