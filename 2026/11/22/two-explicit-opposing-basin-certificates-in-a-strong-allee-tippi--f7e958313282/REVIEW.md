# Self-review

## Correctness — PASS

The dynamics, parameters, and quantifiers are reconstructed in `RESULT.md`. The identity \(\dot H=-\phi(u-1)^2(u-u_c)\) and compact sublevels establish a positively invariant attraction certificate, followed by a LaSalle conclusion. The bound \(v(t)\ge v_0e^{-t}\), exact maximum of \(f\), logarithmic prey inequality and unique minimizer of the comparison threshold prove the extinction certificate. Exact rational identities and high-precision example inequalities were independently recalculated in `checker.py`; finite trajectories are supporting illustrations only. The statements hold for arbitrary \(\varepsilon>0\). No unproved existence or basin uniqueness is smuggled into the final statement.

## Originality — PASS, literature-bounded

The exact cubic prey/type-I predator equations are not new. Hennessy–Popović–Sattar (2026) establish singular bistability geometry and nonautonomous ramp-rate tipping. Wang–Shi–Wei (2010/2011) establish a broader general phase-portrait and bifurcation framework that encompasses this ODE. Van Voorn et al. (2007) analyze a matching polynomial type-I family and compute global heteroclinic boundaries. The new limited claim is a *pair* of explicit, analytically justified sufficient initial-condition certificates for each frozen-flow basin, plus a nontrivial same-prey example below the fold. The inspected primary sources and related scientific search results provide no implication-equivalent pair. Classical entropy, comparison and Lambert methods are not themselves original. Residual risk: older specialized texts or less-indexed results may contain an equivalent bound; absolute novelty is not certified.

## Value — PASS

A bistable ecological model with an Allee threshold has a concrete mathematical gap between local stability and the ability to classify individual initial population states. The new inequalities certify guaranteed coexistence and guaranteed extinction under identical model parameters and the same prey abundance, making the two outcomes quantitatively demonstrable rather than relying only on a phase portrait or numerical continuation. Both certificates remain valid outside the slow–fast asymptotic regime. They are sufficient and not optimal as whole-basin boundaries.

## Closest literature and limitations

Hennessy, Popović, Sattar (2026), arXiv:2610.12319; Wang, Shi, Wei (2010/2011), DOI:10.1007/s00285-010-0332-1; van Voorn et al. (2007), DOI:10.1016/j.mbs.2007.02.006. Full-text source sections and exact implication comparisons are recorded in AUDIT.json. This is for the frozen carrying capacity, not the ramped problem, and gives no stochastic, spatial, or full-separatrix theorem. Independent validation was not performed.

Self-review: passed. Independent audit: not yet performed.
