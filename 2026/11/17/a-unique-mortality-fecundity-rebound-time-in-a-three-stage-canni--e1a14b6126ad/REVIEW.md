# Scientific review — nonlinear single-crossing rebound

## Correctness — PASS

For precisely the three-stage coupled mortality–fertility ODE, the positive equilibrium, Jacobian factorization and resolvent have been independently recalculated. For \(c,\kappa,m>0\), all three linearized eigenvalues are negative. The exact finite-step initial curvature is \(\delta Z_m(m^2-m-c)/m\), while the equilibrium population shift is \(\delta[2-c/(m(m+\delta))]/\kappa\). Both signs hold in the asserted open wedge. The sensitivity has the exact representation \(F(t)=Z_m[Ah(t)+BH(t)]/m\) with \(A<0<B\). Log-concavity of the positive convolution \(h\), its analytic strictness, and monotonicity of \(H/h\) establish a unique transverse limiting crossing; uniform hyperbolic attraction and smooth dependence transfer its uniqueness to all sufficiently small nonlinear shocks. The finite checker passed exact-rational resolvent tests and independent trajectory diagnostics. No numerical extrapolation is used in the proof.

## Originality — PASS within inspected evidence

The starting equations and equilibrium population formula occur in Xia–Li–Chou, arXiv:2303.00864 (2023), version 1 Appendix D.3 (equations 64–66) and version 2 Appendix F.3 (equations 95–97). Its positive equilibrium sensitivity accounts for the lower wedge threshold and is explicitly credited. The inspected original manuscript does not give an exact nonlinear single-crossing law, distinguish the short-time curvature boundary from the equilibrium boundary, or produce the time-limit convolution. Sorenson–Cortez's stage-structured equilibrium hydra analysis concerns a different birth/maturation architecture and supplies neither this exact model's shocked transfer function nor nonlinear single crossing. Cortez–Abrams provides general equilibrium restrictions, not these temporal conclusions. The 2024 Physica D journal full text could not be materially inspected; the 2023 lawful public manuscript was inspected and that uncertainty is retained. published-finding corpus searches for the source, model, parameter window and equivalent impulse-response formulations did not produce a covering finding, which is evidence of checked overlap rather than proof of universal novelty.

## Mathematical value — PASS

Hydra effects ordinarily concern the sign of an equilibrium response. The theorem shows that in a parameter-open biologically interpretable three-stage specialization, the initially observed sign and eventual equilibrium sign are opposite, yet the entire intervening nonlinear history has exactly one crossing for all small shocks. The separate sharp sign boundaries and a computable limiting rebound time answer a natural transient-management question not answered by the source's equilibrium derivative alone. The exponential-convolution monotonicity argument supplies the structural reason a second crossing is impossible. This is a dynamical classification in a motivated model, not merely an algebraic differentiation of known equilibrium formulas.

## Closest literature and limits

- Xia, Li and Chou, arXiv:2303.00864 (2023), Appendix D.3: exact source model and stationary Hydra threshold; temporal single-crossing theorem not seen in material inspected.
- Sorenson and Cortez, Theoretical Ecology (2021), DOI 10.1007/s12080-020-00488-1: n-stage equilibrium hydra mechanisms with different interaction architecture.
- Cortez and Abrams, Ecology (2016), DOI 10.1890/15-0648.1: general equilibrium hydra restrictions.

This theorem is local in shock size and initial equilibrium and concerns a linked change in adult fertility and mortality, not mortality in isolation. Independent journal-priority verification, particularly of the 2024 Physica D full text and unindexed formulations, remains to be performed.

Self-review: passed. Independent audit: not yet performed.
