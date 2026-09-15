# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Dimension-free half-space stability versus needle-boundary counterexample for near-Cheeger sets of isotropic log-concave measures
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20315
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** needle decomposition and localization analysis

## Problem

Let μ be an isotropic log-concave probability measure on R^n, n ≥ 2, with Cheeger constant ψ_μ defined by min(μ(A),1−μ(A)) ≤ C·μ⁺(A) for all Borel A. For Borel A with μ(A)=1/2 define deficit δ_μ(A)=ψ_μ·μ⁺(A)−1/2 and half-space asymmetry α_μ(A)=inf_H μ(A Δ H) over affine half-spaces H. With μ=∫ μ_ℓ dπ(ℓ) the KLS-localization needle disintegration for f=1_A−1/2: does there exist a modulus ω with ω(δ)→0 as δ→0, independent of n and isotropic μ, such that α_μ(A) ≤ ω(δ_μ(A)) for all (n,μ,A)? If not, construct (n_k,μ_k,A_k) isotropic log-concave with μ_k(A_k)=1/2, δ→0 but α ≥ ε_0>0, and decide whether ∫ α_{μ_ℓ}(A∩ℓ)dπ(ℓ) is still controlled by ∫ δ_{μ_ℓ}(A∩ℓ)dπ(ℓ) with a dimension-free modulus?

## Attempted claim

Let μ be an isotropic log-concave probability measure on R^n, n ≥ 2, with Cheeger constant ψ_μ defined by min(μ(A),1−μ(A)) ≤ C·μ⁺(A) for all Borel A. For Borel A with μ(A)=1/2 define deficit δ_μ(A)=ψ_μ·μ⁺(A)−1/2 and half-space asymmetry α_μ(A)=inf_H μ(A Δ H) over affine half-spaces H. With μ=∫ μ_ℓ dπ(ℓ) the KLS-localization needle disintegration for f=1_A−1/2: does there exist a modulus ω with ω(δ)→0 as δ→0, independent of n and isotropic μ, such that α_μ(A) ≤ ω(δ_μ(A)) for all (n,μ,A)? If not, construct (n_k,μ_k,A_k) isotropic log-concave with μ_k(A_k)=1/2, δ→0 but α ≥ ε_0>0, and decide whether ∫ α_{μ_ℓ}(A∩ℓ)dπ(ℓ) is still controlled by ∫ δ_{μ_ℓ}(A∩ℓ)dπ(ℓ) with a dimension-free modulus?

## Research outcome

Exact Laplace certificate: 1D half-line stability fails (delta=0, alpha=1/2 interval; every mass-1/2 interval optimal) and 2D half-planes are not Cheeger minimizers (square beats them; half-plane deficit >= 0.10). Packaged as EMERGENT_FINDING; full target unresolved.

## Why this attempt failed

Failed axes: originality.

originality: The headline's load-bearing novelty — every mass-1/2 interval of the 1D exponential law is perimeter-minimizing, yielding a deficit-0 set far from every half-line so no modulus controls half-line asymmetry — is already recorded and substantively implies the submitted (delta=0,alpha=1/2) pair. Feo-Posteraro-Roberto (2014), arXiv:1401.0628, §3.4 treats the same law (two-sided exponential, rate 1 vs submitted rate 2, identical up to the dilation the DRAFT itself proves invariant) with J(t)=min(t,1-t), P((a,b))=1-p for p≥1/2, and the explicit statement that for p≥1/2 any interval and half-lines have minimal perimeter; its abstract, §4.2 and Remark 4.8(d) make the small-deficit/large-asymmetry anomaly at p=1/2 (two coexisting extremal shapes) a main result. The submitted extremal pair and no-modulus corollary follow mechanically. The report itself disclaims any literature search, so no priority presumption applies; a timestamp or failed search does not establish priority, and here body-level inspection establishes coverage.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: The packaged finding does not resolve the full admitted target: it gives no (n_k, mu_k, A_k) sequence with delta->0 and alpha>=eps_0 for n>=2 (the strip has deficit >= 0.10, not vanishing; square minimality among ALL mass-1/2 sets is unproven), and the needle-averaged remark is established only for the natural parallel-line disintegration, not quantified over every KLS-localization disintegration. Originality is claimed narrowly (see originality_check) and awaits full Audit confirmation. The sc…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
