# Scientific review: exact two-point resetting local-time law

## Correctness — PASS

The killed Brownian Green function is the explicit Dirichlet half-line resolvent at Poisson rate \(r\). The first-cycle geometric renewal produces the full occupation kernel \(U\), with success probability \(e^{-R\sqrt{r/D}}>0\), so there is no hidden improper stationary assumption. Its values at the two observation sites form an exact two-by-two matrix. The Feynman–Kac gauge equation solves to the claimed full Laplace transform. Direct derivatives give the covariance and variances; strict monotonicity follows from an elementary strictly increasing hyperbolic function, and normalized convergence from convergence of joint Laplace transforms. Independent discrete-generator calculations agree under mesh refinement. Finite checks do not establish the continuum statement; the explicit Green/Kac proof does.

## Originality — PASS, subject to stated residual literature risks

The first-passage single-local-time calculation in Singh–Pal (2022) is not already the joint law for two distinct lower sites. Pal et al. (2019) treat fixed-time local time, not our stopped pair, and flag spatial correlations as worthwhile to examine. The spatially homogeneous Lévy model of Li–Zhou (2017) does not subsume a process jumping back to a prescribed state \(R\) from arbitrary positions, without additional reasoning. Marcus–Rosen (2023) supplies general Markov local-time theory but was not found to state the explicit transform, reset-position invariance, or strict rate monotonicity. The mathematical novelty assessed is the combined explicit two-site first-absorption law and synchronization classification, not invention of the Green-kernel or Kac machinery. Unlocated equivalent specialization remains possible; independent priority assessment has not been performed.

## Mathematical value — PASS

Simultaneously measuring local exposure at two distinct reactive locations is natural in first-passage transport, whereas one-site means cannot determine covariance. The exact joint law quantifies a nontrivial spatial dependence, a sharp rate-controlled monotone synchronization, and the surprising invariance to how far upstream the particle resets. Its large-reset diagonal exponential limit predicts strong coupling between normalized local exposures. These are structurally motivated and materially stronger than routine single-point normalization or small parameter tabulation.

## Closest literature and limits

- Pal, Chatterjee, Reuveni, Kundu, 2019, arXiv:1902.00907v1: fixed-horizon one-site local time; nearby motivation, distinct stopping setup.
- Singh and Pal, 2022, arXiv:2202.02715v1: first-passage single-site local time at reset point; no distinct-two-site transform in inspected results.
- Li and Zhou, 2017, arXiv:1705.01289v1: general joint Lévy local times; state-dependent reset jump does not fit the spatially homogeneous Lévy premise.
- Marcus and Rosen, 2023, arXiv:2302.10262v1: broad Markov-process local-time theory, possible implicit specialization.

The result is limited to two interior point local times before absorption with a constant Poisson reset clock, and does not prove priority or verify by independent external audit.

Self-review: passed. Independent audit: not yet performed.
