# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Seneta–Heyde large deviations for heavy-tailed branching random walks
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20013
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Probability Theory
- **Method:** many-to-few spine change-of-measure

## Problem

Let T be a supercritical Galton–Watson branching random walk on R with finite progeny mean E[Z]=μ>1, displacement point process jointly regularly varying with tail index α>0, and offspring law satisfying E[Z log⁺ Z]=∞. For γ_n satisfying μ^n P(|X_1|>γ_n)=o(1), what is the correct normalization r_n in terms of the Seneta–Heyde norming sequence for Z_n, and what is the explicit limiting Radon measure m^*_{SH} for r_n P^*(N_n∈·)→m^*_{SH} in M_0, where N_n=∑_{|v|=n}δ_{γ_n^{-1}S(v)}; in particular, does the one-large-displacement cluster description persist and how is its intensity changed?

## Attempted claim

Let T be a supercritical Galton–Watson branching random walk on R with finite progeny mean E[Z]=μ>1, displacement point process jointly regularly varying with tail index α>0, and offspring law satisfying E[Z log⁺ Z]=∞. For γ_n satisfying μ^n P(|X_1|>γ_n)=o(1), what is the correct normalization r_n in terms of the Seneta–Heyde norming sequence for Z_n, and what is the explicit limiting Radon measure m^*_{SH} for r_n P^*(N_n∈·)→m^*_{SH} in M_0, where N_n=∑_{|v|=n}δ_{γ_n^{-1}S(v)}; in particular, does the one-large-displacement cluster description persist and how is its intensity changed?

## Research outcome

TARGET claimed: Seneta-Heyde large-deviation rate stays r_n=1/(mu^n P(|X1|>gamma_n)) with explicit one-big-jump limit m*_SH; the SH norming decouples via defect factor d_n=mu^n/c_n.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET proof route is incomplete and contains a false moment claim. Under only E[Z]=mu<inf, E[Z^2] may be inf, so step-2 two-jump bound O(r_n^{-1} n Fbar) and Fuk-Nagaev maximal bound are asserted without proof; union-pair expectation can be infinite. Step-4 states spine size-biased mean 'still requiring only mu<inf', but E[Z^*]=E[Z^2]/mu needs second moment and is infinite when Var=inf. The core KS gap is bypassed by assertion: prior BEJ proof uses UI of W_n=Z_n/mu^n and sup W_k integrability for dominated convergence and K->inf residual, which fails when W_n->0 a.s. under E Z log Z=inf. Then E[1-(1-p_n)^{Z_{n-K}}]/(E[Z_{n-K}]p_n)->1 needs tail E[W 1_{W>T_n}] with T_n~r_n->0 control that is not shown; saturation on huge families can break r_n rate. Artifact sh_check.py verifies only deterministic identities Pareto rate, geometric sum, toy c_n/mu^n, not the M0 limit. Hence experimental evidence, not proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The argument cites without re-proof the Seneta-Heyde norming existence and standard regular-variation tools (Potter bounds, Karamata theorem); mu=infinity and critical/subcritical cases are excluded; step 2's maximal inequality is given as a complete but condensed route that a journal version would expand line by line. No literature search was used; originality rests on Admission review plus the local deduction above.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
