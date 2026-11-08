# Self-review

## Correctness — PASS

The claim uses recovery-normalized time and the explicitly stated \(C^2\), monotonicity, positivity, and initial-condition hypotheses. The proof verifies invariance, lower/upper contact comparisons, global \(O(1/t)\) infection extinction, contact convergence, a stable tracking identity \((z-h(y))/y\to0\), and the exact reciprocal-prevalence derivative. These steps establish the two limits for every positive initial prevalence, including zero baseline link-breaking. Exact algebra and five long-time numerical cases were run from the included `verify.py` and returned `VERIFY_OK`; numerical convergence alone is not used as an infinite-time proof. Scope excludes stochastic networks and nonmonotone responses.

## Originality — PASS with residual publication-priority uncertainty

The closest primary comparison is Achterberg–Sensi, arXiv:2209.01224, whose full HTML version states the same two-dimensional equations, reproduction ratio, generic equilibrium existence and no-cycle results. Its general statements do not give the present global critical-law coefficient; its detailed examples and slow-network section focus on other parameter regimes. Achterberg–Sensi–Sottile, arXiv:2407.17639, gives a multigroup monotone-response disease-free theorem only for the strict range \(\mathcal R_0<1\), so that theorem does not settle equality or the \(t^{-1}\) amplitude. Achterberg–Van Mieghem, *Phys. Rev. E* 106 (2022), studies different stochastic adaptive-network closures. Accessible research-record results concerning critical slowing in bullying indices, noncompliance, and other epidemic dynamics use different state equations and do not imply the coefficient for this contact-feedback model. Earlier accessible scientific claims include one about supercritical-focus behavior for the special \(b(y)=y,c(y)=1\) model but not the critical inverse-time limit. Indexed retrieval is incomplete, and an alternative general center-manifold treatment could contain the same formula without an indexed title.

## Value — PASS

The critical reproduction ratio is a natural dividing line in epidemic stability. The theorem closes the equality case under epidemiologically motivated monotone avoidance and gives a quantitative, response-sensitive inverse-time law, rather than a generic stability statement: the instantaneous slopes of link breaking and creation determine an exact limiting prevalence coefficient and a synchronized contact-density correction. This is a structural result across an infinite class of feedback functions and every positive-prevalence initial state, not a finite numerical sample or an arbitrary parameter slice.

## Limitations and residual risks

Priority depends on the accessible literature and searchable records; no independent external review or certification was performed. The proof's conclusions require the stated deterministic model, finite positive adjustment rates, monotone responses, and positive creation throughout the closed prevalence interval. The numerical checker is supporting evidence only.

Self-review: passed. Independent audit: not yet performed.
