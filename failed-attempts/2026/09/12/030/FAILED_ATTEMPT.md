# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Resonant-tree finite-part shift rate and regulator law at sigma 5/2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1105
- **Disposition:** NO_RESULT
- **Domain:** Stochastic Analysis
- **Method:** single-tree Polchinski scale-integral versus BPHZ valuation with tail-rate analysis

## Problem

For the fractional KPZ model at sigma=5/2 on T^2 with Fourier cutoff N, let T_res be the explicitly defined second-order bilinear resonant tree in the DPD expansion beyond the Wick cherry, V^{Pol}_N(T_res;mu,chi) its Polchinski valuation at reference scale mu with cutoff function chi, and V^{BPHZ}_N(T_res) its BPHZ valuation. With matched cutoff N and mu=1, define D(N)=V^{Pol}_N-V^{BPHZ}_N. The target is an explicit finite D_*, explicit K<infinity and beta>0 such that |D(N)-D_*| <= K N^{-beta} for all N>=1, plus regulator covariance: recomputing V^{Pol}_N with heat-kernel cutoff chi_heat instead of sharp shell chi_sharp shifts the limit by the explicit universal amount Delta_reg stated in closed form, within the stated tolerance; certified divergence, a different limit, a slower-decay lower bound, or a shift mismatch falsifies the claim.

## Attempted claim

For the named resonant tree T_res at sigma=5/2 on T^2, the Polchinski-minus-BPHZ difference converges, D(N)->D_* with |D(N)-D_*| <= K N^{-beta}, and the heat-kernel-for-sharp-shell regulator swap moves D_* by exactly the stated universal Delta_reg; exhibiting divergent growth, a different limit beyond tolerance, a certified slower decay, or a shift mismatch falsifies the claim.

## Research outcome

Target blocked on proof-theoretic grounds: genuine numeric support for D*=0 with N^{-1/2} rate at 11 cutoffs including out-of-sample N=96, but no uniform all-N tail certificate and fit-based rather than BPHZ-character counterterms, so no auditable claim can be made.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No all-N tail certificate was proved: evidence covers only 11 sampled cutoffs (N=3..96), and the counterterms are least-squares fits rather than the BPHZ forest character the audit plan requires, so no theorem or emergent finding is claimed. Reproducible numeric artifacts are preserved for future sessions.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No all-N tail certificate was proved: evidence covers only 11 sampled cutoffs (N=3..96), and the counterterms are least-squares fits rather than the BPHZ forest character the audit plan requires, so no theorem or emergent finding is claimed. Reproducible numeric artifacts are preserved for future sessions.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
