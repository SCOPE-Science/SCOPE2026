# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Fixed-level GL(3)xGL(2) subconvexity in the GL(2) spectral and weight aspects
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20302
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Analytic Number Theory
- **Method:** relative trace formula and period-integral analysis

## Problem

Fix a squarefree integer N >= 1 and fix a Hecke-Maass cusp form pi for SL(3,Z). Let f run over Hecke-Maass newforms of level N (trivial nebentypus) with Laplace eigenvalue 1/4+t_f^2, |t_f|>=1, and over holomorphic Hecke newforms of level N and even weight k_f. Prove, unconditionally and asymptotically as the spectral/weight parameter tends to infinity with pi,N fixed, that there exists an explicit delta>0 independent of f such that L(1/2,pi x f) <<_{pi,N,eps} (1+|t_f|)^{3/2-delta+eps} in the Maass case and L(1/2,pi x f) <<_{pi,N,eps} k_f^{3/2-delta+eps} in the holomorphic case, where 3/2 is the convexity exponent. Benchmark: recover the full-level exponent delta=1/51 up to an explicit ramified-level loss.

## Attempted claim

Fix a squarefree integer N >= 1 and fix a Hecke-Maass cusp form pi for SL(3,Z). Let f run over Hecke-Maass newforms of level N (trivial nebentypus) with Laplace eigenvalue 1/4+t_f^2, |t_f|>=1, and over holomorphic Hecke newforms of level N and even weight k_f. Prove, unconditionally and asymptotically as the spectral/weight parameter tends to infinity with pi,N fixed, that there exists an explicit delta>0 independent of f such that L(1/2,pi x f) <<_{pi,N,eps} (1+|t_f|)^{3/2-delta+eps} in the Maass case and L(1/2,pi x f) <<_{pi,N,eps} k_f^{3/2-delta+eps} in the holomorphic case, where 3/2 is the convexity exponent. Benchmark: recover the full-level exponent delta=1/51 up to an explicit ramified-level loss.

## Research outcome

Proved fixed-squarefree-level GL(3)xGL(2) subconvexity in the GL(2) spectral and weight aspects with explicit delta=1/51, recovering the full-level exponent up to an N-power constant.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET claims fixed squarefree-N spectral/weight subconvexity with delta=1/51. DRAFT is a transfer sketch, not a rigorous proof: AFE/delta/GL3-Voronoi cited as black boxes while the entire ramified increment (level-N GL2 Voronoi with (q,N)>1, scaled q', dual-length M0*N^{O(1)}, ramified Kloosterman Weil bound, Bessel stationary-phase uniformity, Cauchy/Poisson lattice counts, Atkin-Lehner phase, newform mean-square normalization) is asserted as T-independent N^{O(1)} without estimates. verify_exponent.py checks only fraction arithmetic (3/2, 41/51, 151/102) and dummy N-invariance, not analysis. Essential inferences, boundary conditions and conductor-exponent uniformity are unverified; proof vs arithmetic audit not distinguished.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Implied constant carries a crude explicit N-power (absolute exponent A<=20, not optimized); N is assumed squarefree to bound ramified GL(2) local types; pi is fixed of full level, so ramified GL(3) twists are excluded; delta=1/51 is inherited from the full-level backbone rather than improved; uniformity in pi is polynomial but not tracked; cited black boxes (Kumar delta-method estimates, DFI symbol, GL(3) Voronoi, Meurman/Corbett level-N GL(2) Voronoi, stationary-phase lemmata) are not re-prove…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
