# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Pressure gap and uniqueness of equilibrium states for geometric potentials on the Zorich suspension coding the Teichmuller flow
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20138
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** Ergodic Theory
- **Method:** thermodynamic formalism and transfer-operator techniques

## Problem

Fix a Rauzy class / connected component H of a stratum of Abelian differentials with its Veech zippered-rectangle countable Markov coding (Sigma,sigma) of Zorich induction and roof function r suspending to the Teichmuller flow (Sigma_r,Phi^t), as in Bufetov-Gurevich. Let phi_geom be the geometric (unstable-Jacobian) potential on the suspension and bar-phi_t its induced potential on the base for scalar parameter t. Let bad segments be those with arbitrarily large Zorich acceleration (r >= N for large N, i.e. long excursions toward the cusp / divergent-on-average Rauzy-Veech paths). Prove that there exists delta>0 such that for |t|<delta, t != 0, P_bad(bar-phi_t) < P_full(bar-phi_t) (equivalently P_infty < P), and hence deduce via the Climenhaga-Thompson / Buzzi-Sarig countable-shift criterion a unique equilibrium state for t*phi_geom, distinct from the Masur-Veech / Bufetov-Gurevich measure of maximal entropy.

## Attempted claim

Fix a Rauzy class / connected component H of a stratum of Abelian differentials with its Veech zippered-rectangle countable Markov coding (Sigma,sigma) of Zorich induction and roof function r suspending to the Teichmuller flow (Sigma_r,Phi^t), as in Bufetov-Gurevich. Let phi_geom be the geometric (unstable-Jacobian) potential on the suspension and bar-phi_t its induced potential on the base for scalar parameter t. Let bad segments be those with arbitrarily large Zorich acceleration (r >= N for large N, i.e. long excursions toward the cusp / divergent-on-average Rauzy-Veech paths). Prove that there exists delta>0 such that for |t|<delta, t != 0, P_bad(bar-phi_t) < P_full(bar-phi_t) (equivalently P_infty < P), and hence deduce via the Climenhaga-Thompson / Buzzi-Sarig countable-shift criterion a unique equilibrium state for t*phi_geom, distinct from the Masur-Veech / Bufetov-Gurevich measure of maximal entropy.

## Research outcome

Repaired proof: Y_w Bernoulli carries SPR/IFT, roof-normalized h>1 via F(1)=infty, uniform-tail continuity gives s(t) with P_infty<0=P_G, and explicit primitive loops M(1),M(200) with distinct J/r ratios give uniqueness plus distinctness from MME.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET-route proof sketch verified in part: Lemma 2 counting bound is standard and sound; artifact recomputations reproduce (rho_1=1.370137, rho_200=2.566025, tail logB(1000)=-2.42). FAIL for two affirmative defects. (1) Sec.7 distinctness witnesses are uncertified: no Rauzy permutation or winner/loser path is exhibited; admissibility is claimed via 'legal by full-shift property,' but the BG countable shift is not full, and induced fullness presupposes return words. Moreover the matrices cannot be genus>=2 closed-loop Rauzy monodromy: their characteristic polynomials (computed: x^4-6x^3+10x^2-8x+1 and x^4-6x^3+10x^2-207x+1) are non-reciprocal with no eigenvalue 1, incompatible with symplectic closed-loop KZ monodromy, so the (J,r)=(S,R) identification and Livsic non-cohomology step are unproved and headline distinctness from MME is unestablished. (2) The h>1 transfer assumes uniformly bounded connectors over all large symbols from topological mixing alone, which does not give uniformity over the infinite alphabet, so induced Z_1(0,1)=infinity is not established as written.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Complete modulo cited black-box theorems (BG coding/mixing/Lemma-3 distortion; Sarig/Buzzi-Sarig SPR-Gibbs theory; Barreira-Schmeling/Jaerisch-Takahashi/Jaerisch-Munday-Takahashi/Climenhaga-Thompson suspension-inducing machinery; AGY uniform hyperbolicity/Hilbert contraction; Eskin-Masur finite entropy; Forni/KZ periodic data; Gouzel-Sarig variance, Ruelle derivatives, Livsic), used as stated. Constants depend on the Rauzy class. Numerics are certificates of stated numbers only, not part of the…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
