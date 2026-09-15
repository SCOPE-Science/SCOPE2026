# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact lower envelope of the BRW maximum at the critical stretched-exponential index r = 2/3
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20414
- **Disposition:** NO_RESULT
- **Domain:** Probability Theory
- **Method:** spine decomposition and many-to-few moment analysis

## Problem

Under Assumptions 1-2 of Dyszewski-Gantert-Hofelsauer (centred, unit-variance i.i.d. displacements with upper tail P[X>x]=a(x)exp(-lambda x^r), a(x)->a>0, lambda>0, r=2/3, plus the stated lower-tail/moment condition; supercritical Galton-Watson with mean m>1 and E[Z_1 log^+ Z_1]<infinity), let M_n=max_{|v|=n} S_v, alpha=((log m)/lambda)^{1/r}, sigma=alpha^{1-r}/(lambda r), P^*[.]=P[. | forall n Z_n>0]. It is known that P^*-a.s. limsup_{n->infinity} (M_n - alpha n^{3/2})/sqrt(n log n)=sigma and -infinity<liminf_{n->infinity} (M_n - alpha n^{3/2})/sqrt(n log n)<infinity. Determine the exact P^*-a.s. value of this liminf (constant or explicit function of the martingale limit W=lim m^{-n}Z_n), or equivalently the sharp integral test on lower functions psi separating liminf=-infinity from finite liminf at r=2/3, via spine decomposition and many-to-few analysis of the joint big-jump plus bulk contribution.

## Attempted claim

Under Assumptions 1-2 of Dyszewski-Gantert-Hofelsauer (centred, unit-variance i.i.d. displacements with upper tail P[X>x]=a(x)exp(-lambda x^r), a(x)->a>0, lambda>0, r=2/3, plus the stated lower-tail/moment condition; supercritical Galton-Watson with mean m>1 and E[Z_1 log^+ Z_1]<infinity), let M_n=max_{|v|=n} S_v, alpha=((log m)/lambda)^{1/r}, sigma=alpha^{1-r}/(lambda r), P^*[.]=P[. | forall n Z_n>0]. It is known that P^*-a.s. limsup_{n->infinity} (M_n - alpha n^{3/2})/sqrt(n log n)=sigma and -infinity<liminf_{n->infinity} (M_n - alpha n^{3/2})/sqrt(n log n)<infinity. Determine the exact P^*-a.s. value of this liminf (constant or explicit function of the martingale limit W=lim m^{-n}Z_n), or equivalently the sharp integral test on lower functions psi separating liminf=-infinity from finite liminf at r=2/3, via spine decomposition and many-to-few analysis of the joint big-jump plus bulk contribution.

## Research outcome

Target BLOCKED at the critical index r=2/3: bulk gap M_n-N_n is same-order not negligible, first moment diverges for every threshold K, spine second moment stays inflated by early-jump clumping, and the stated normalization is inconsistent with DGH Prop 3.5. All routes attempted with a reproducible probe; clean exit with no alternative meeting the Audit bar.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The exact r=2/3 liminf remains undetermined: no finite-vs-infinite threshold K was found, no joint big-jump plus bulk lower-tail estimate was derived, and the sqrt(n log n) versus sqrt(n) log n normalization ambiguity in the target transcription was identified but not resolved into a corrected sharp integral test. Simulation evidence is limited to binary branching with Weibull(2/3) displacements at small n=4..12 and R=1500 runs, supporting but not proving the bulk non-negligibility and correlation claims.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The exact r=2/3 liminf remains undetermined: no finite-vs-infinite threshold K was found, no joint big-jump plus bulk lower-tail estimate was derived, and the sqrt(n log n) versus sqrt(n) log n normalization ambiguity in the target transcription was identified but not resolved into a corrected sharp integral test. Simulation evidence is limited to binary branching with Weibull(2/3) displacements at small n=4..12 and R=1500 runs, supporting but not proving the bulk non-negligibility and correlat…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
