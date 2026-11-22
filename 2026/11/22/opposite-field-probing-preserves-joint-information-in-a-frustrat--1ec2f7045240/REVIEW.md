# Scientific review: Opposite-field probing preserves joint information in a frustrated Ising trimer

## Correctness — PASS

The exact eight-state Gibbs partition function gives the full two-parameter Fisher covariance. Equal and opposite known fields cancel the odd cross entry when allocated equally; for any nonzero magnitude this maximizes the determinant over allocation weights. The resulting rational determinant has a differentiated quartic numerator. The sequence of coefficient sign thresholds proves precisely one positive quartic root for every positive exchange fugacity, and evaluating the polynomial at the physical boundary gives an exact, unique crossover. The scaled polynomial and rational determinant prove a positive strong-antiferromagnetic limiting information determinant. A separate uniform bound and matching evaluation show that every one-field design loses its determinant. The standalone standard-library checker reproduces the covariance by eight-state enumeration and passes 114 finite cases. Finite tests are corroboration only; the infinite-range and asymptotic claims rest on the explicit analytic proof.

## Originality — PASS, with known prior ingredients and residual risk

The nearest source is Ebadi et al., arXiv:2611.08072v1, especially Section 2 and Appendix A (A.4)–(A.6): it supplies the Gibbs model, Fisher tensor, and *one-field* determinant, which are therefore prior knowledge. It does not optimize the determinant of a weighted **pair** of Fisher tensors with common unknown offset; this objective differs algebraically from the reported one-field determinant, because cancellation of the off-diagonal information changes its limiting order. The 2008 full-text study of Invernizzi et al. concerns one-parameter quantum-Fisher optimization in a transverse-field Ising chain; no implication of this classical longitudinal two-parameter trimer design follows from it. Targeted published-record comparisons yielded no direct equivalent theorem. Unindexed optimal-design analyses and simple unpublished deductions from the known Fisher tensor remain possible, so absence of indexed matches is not a proof of historical priority.

## Value — PASS

The question is motivated by local experimental design for a frustrated molecular trimer or few-spin simulator when coupling and an ambient longitudinal offset must both be learned. A single field can make their fluctuation scores nearly collinear, producing a vanishing determinant. The opposite-field protocol provides a nonvanishing per-sample determinant in the strongly frustrated regime, and proves an asymptotically unbounded relative improvement over every single-field setting. The exact quartic classification includes the transition boundary, a non-obvious threshold extending slightly into ferromagnetic couplings, and optimal field scaling. This is an interpretable structural information-design result, not an arbitrary finite table or a claim of a thermodynamic phase transition.

## Closest literature, scope, and risks

- Ebadi et al. (2026), arXiv:2611.08072v1, full relevant primary sections and Appendix A inspected. Its scalar-curvature study supplies the one-field metric but no paired-field design optimum.
- Invernizzi et al. (2008), arXiv:0807.3213v1, full-text accessible portions of the theoretical model and few-spin calculations inspected. Its transverse-field quantum chain estimates a different single parameter.
- Related quantum Ising multiparameter metrology discusses determinant criteria, but does not by itself identify the classical symmetric-trimer quartic or the opposite-field low-temperature rescue. Some full texts could not be retrieved; exact unindexed coverage remains a risk.
- Results apply only to locally calibrated opposite equal-magnitude field settings and full spin readout. They do not establish optimality among all experimental protocols, physical phase transitions, or finite-sample estimator attainment.

Self-review: passed. Independent audit: not yet performed.
