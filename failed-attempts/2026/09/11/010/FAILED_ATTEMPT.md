# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** First certified Turing GRH verification height to T=50 for the least-discriminant S5 sextic Dedekind zeta
- **Round:** 2026-09-07-first-light-01
- **Lane:** 693
- **Disposition:** NO_RESULT
- **Domain:** Computational Number Theory
- **Method:** Turing-method zero isolation with rigorous Euler-product enclosure and interval remainder replay

## Problem

Let K be the S5 sextic field of smallest absolute discriminant listed in LMFDB (record its label, defining polynomial, discriminant, signature, and Galois-closure group). Using its computable functional equation and a rigorous Euler-product tail bound, apply Turing-method zero counting plus interval argument-principle boxes to certify GRH for zeta_K up to imaginary height T=50 with an exact zero count and a replay log running in under 60 seconds.

## Attempted claim

For the field K above, zeta_K satisfies GRH for |Im(s)| <= 50: produce the exact integer N_50 = #{rho: zeta_K(rho)=0, 0<|Im(rho)|<=50} and an interval Turing-remainder certificate replayable in under 60 seconds proving that all N_50 zeros lie on Re(s)=1/2 with no zero off the line in the strip segment.

## Research outcome

Target (certified GRH to T=50 with exact N_50, <60s replay) and exact preset fallback (T1>=20 with exact N1, <60s interval replay) both BLOCKED after bounded concrete attempts. Exact K-identity partials proved (signature (0,3), irreducibility, index 3); HSW inequality priced as ~1000x too wide for exact counts; recovery tests proved raw/smoothed Dirichlet tails swallow the critical-line signal and stdlib has no certified complex Gamma, so no rigorous Xi(t) sign, no winding box, and no (T,N) pair could be closed. Route-matching output/target_exit.json records CLEAN_EXIT with fallback_assessment ATTEMPTED_AND_BLOCKED; no emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Heuristic (non-rigorous) artifacts only: F_p-degree a_n table to N=8000 with uncertified ramified entries; smoothed Z(t) oscillation scan; mpmath (non-interval) theta values. None is a certificate.', 'Galois group S5 (6T14) not proved (Frobenius types only consistent); integral basis / certified ramified Euler factors not computed.', 'mpmath.iv complex-gamma wrapper audited but not validated as theorem-grade and not used for any claimed enclosure; stdlib-only replay terms unmet.', 'No (T1,N1) pair certified; no winding box closed; no off-line exclusion proved at any height.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Heuristic (non-rigorous) artifacts only: F_p-degree a_n table to N=8000 with uncertified ramified entries; smoothed Z(t) oscillation scan; mpmath (non-interval) theta values. None is a certificate.', 'Galois group S5 (6T14) not proved (Frobenius types only consistent); integral basis / certified ramified Euler factors not computed.', 'mpmath.iv complex-gamma wrapper audited but not validated as theorem-grade and not used for any claimed enclosure; stdlib-only replay terms unmet.', 'No (T1,N1)…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
