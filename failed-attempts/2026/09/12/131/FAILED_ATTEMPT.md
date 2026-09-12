# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Intensive dimension-free Sinkhorn-divergence small-eps rate
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1448
- **Disposition:** NO_RESULT
- **Domain:** entropic optimal transport asymptotics
- **Method:** Benamou-Brenier/Sinkhorn asymptotics with tensorization and per-dimension bounds

## Problem

Let mu, nu be kappa-uniformly log-concave probability measures on R^n (kappa > 0) with per-dimension second moments and per-dimension Fisher informations bounded by M and F respectively, let c(x,y) = |x-y|^2/2, and define with pinned normalization the entropic cost C_eps(mu,nu) = inf_pi {int c dpi + eps H(pi | mu x nu)} and the debiased Sinkhorn divergence S_eps(mu,nu) = C_eps(mu,nu) - (C_eps(mu,mu)+C_eps(nu,nu))/2, so all entropy references and additive log normalizations cancel and no (n eps)log(eps) coefficient is asserted. Does there exist an explicit threshold eps_0(kappa,M,F) and remainder R(kappa,M,F), both independent of n, such that for all 0 < eps <= eps_0, |(1/n) S_eps(mu,nu) - (1/n) W_2(mu,nu)^2/2| <= eps R(kappa,M,F) uniformly in n over the class? A complete answer proves the stated intensive n-free remainder for the full class, or disproves it with an explicit sequence of dimensions and kappa-log-concave marginals in the class (e.g. tensorized Gaussians with admissible per-dimension parameters) violating the claimed n-free eps-rate.

## Attempted claim

Let mu, nu be kappa-uniformly log-concave probability measures on R^n (kappa > 0) with per-dimension second moments and per-dimension Fisher informations bounded by M and F respectively, let c(x,y) = |x-y|^2/2, and define with pinned normalization the entropic cost C_eps(mu,nu) = inf_pi {int c dpi + eps H(pi | mu x nu)} and the debiased Sinkhorn divergence S_eps(mu,nu) = C_eps(mu,nu) - (C_eps(mu,mu)+C_eps(nu,nu))/2, so all entropy references and additive log normalizations cancel and no (n eps)log(eps) coefficient is asserted. Does there exist an explicit threshold eps_0(kappa,M,F) and remainder R(kappa,M,F), both independent of n, such that for all 0 < eps <= eps_0, |(1/n) S_eps(mu,nu) - (1/n) W_2(mu,nu)^2/2| <= eps R(kappa,M,F) uniformly in n over the class? A complete answer proves the stated intensive n-free remainder for the full class, or disproves it with an explicit sequence of dimensions and kappa-log-concave marginals in the class (e.g. tensorized Gaussians with admissible per-dimension parameters) violating the claimed n-free eps-rate.

## Research outcome

Target blocked: full-class intensive dimension-free Sinkhorn-divergence O(eps) rate could be neither proved (uniform correlated lower bound and n-free threshold unclosable in-pass) nor disproved (Gaussians provably O(eps^2) with exact log-cancellation; worst-case two-level search max R1~0.005). Clean exit with no independently valuable emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No complete TARGET resolution was reached: neither the full-class intensive n-free O(eps) upper and lower bounds with explicit eps_0(kappa,M,F) and R(kappa,M,F), nor an explicit admissible violating sequence, was established. Evidence is limited to Gaussian, product, and one-dimensional slices plus a validated upper-bound competitor; the uniform correlated n-dimensional lower-bound machinery and n-free threshold construction remain open. Grid Sinkhorn probes carry discretization error and cover only eps>=0.02 in 1D.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No complete TARGET resolution was reached: neither the full-class intensive n-free O(eps) upper and lower bounds with explicit eps_0(kappa,M,F) and R(kappa,M,F), nor an explicit admissible violating sequence, was established. Evidence is limited to Gaussian, product, and one-dimensional slices plus a validated upper-bound competitor; the uniform correlated n-dimensional lower-bound machinery and n-free threshold construction remain open. Grid Sinkhorn probes carry discretization error and cover…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
