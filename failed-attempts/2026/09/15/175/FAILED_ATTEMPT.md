# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Corrected billiards description of second-generation anti-spherical p-canonical basis elements for affine type A2
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20433
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Combinatorics
- **Method:** Soergel bimodule categorification and p-canonical basis analysis

## Problem

For G=SL_3 over an algebraically closed field of characteristic p>2, let W be the affine Weyl group of type tilde A2, ^fW the minimal representatives for W_f\W, and AS_v=sgn_v\otimes_{H_f}H the anti-spherical Hecke module with KL basis {n_x} and p-canonical basis {^pn_x}. Let x_0=id, x_1=s_0, x_2=s_0s_1, ... be the wall sequence, and let ^p\zeta_i be built from Lusztig-Williamson Steps 1-3 with Jensen's corrected Step-2 wall dynamics with geometric merge rule (Types II/III). Prove: (i) ^p\zeta_i=^pn_{x_i} for 0<=i<2p(p+1); (ii) ^p\zeta_i=^pn^2_{x_i} for all i>=0. In particular establish the merge-rule cancellation at the first merging corner lambda=p\varpi_1+p\varpi_2 (for p=5: Type II giving 88(v^8) and Type III giving 87(v^7); and the listed analogues for p=7,11) where the original billiards algorithm over-predicts.

## Attempted claim

For G=SL_3 over an algebraically closed field of characteristic p>2, let W be the affine Weyl group of type tilde A2, ^fW the minimal representatives for W_f\W, and AS_v=sgn_v\otimes_{H_f}H the anti-spherical Hecke module with KL basis {n_x} and p-canonical basis {^pn_x}. Let x_0=id, x_1=s_0, x_2=s_0s_1, ... be the wall sequence, and let ^p\zeta_i be built from Lusztig-Williamson Steps 1-3 with Jensen's corrected Step-2 wall dynamics with geometric merge rule (Types II/III). Prove: (i) ^p\zeta_i=^pn_{x_i} for 0<=i<2p(p+1); (ii) ^p\zeta_i=^pn^2_{x_i} for all i>=0. In particular establish the merge-rule cancellation at the first merging corner lambda=p\varpi_1+p\varpi_2 (for p=5: Type II giving 88(v^8) and Type III giving 87(v^7); and the listed analogues for p=7,11) where the original billiards algorithm over-predicts.

## Research outcome

Target blocked: Jensen Corrected Billiards Conjecture 3.1 could not be proved in-pass; merge-rule combinatorics reproduced as a bounded test but the categorical equalities need unavailable MAGMA/HPC infrastructure. Clean exit with no claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Proving the corrected billiards equalities requires anti-spherical Soergel intersection-form computations (MAGMA ASLoc implementation at HPC scale) or new torsion-vanishing theorems, none available in this Python-only one-hour pass. The bounded recovery test verified only the combinatorial merge mechanism, not the categorical equalities, and no independently valuable original increment emerged.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Proving the corrected billiards equalities requires anti-spherical Soergel intersection-form computations (MAGMA ASLoc implementation at HPC scale) or new torsion-vanishing theorems, none available in this Python-only one-hour pass. The bounded recovery test verified only the combinatorial merge mechanism, not the categorical equalities, and no independently valuable original increment emerged.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
