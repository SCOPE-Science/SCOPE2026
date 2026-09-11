# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Nonzero-winding Fisher-Hartwig ladder: explicit power law and winding factor at kappa=1
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1008
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Operator Theory
- **Method:** Wiener-Hopf factorization with winding plus Borodin-Okounkov section and OPUC ratio

## Problem

Let f0(z) = |z + 1|^{1/2} g_{-1,1/4}(z) on the unit circle, the Fisher-Hartwig symbol with alpha = 1/4, beta = 1/4 at z0 = -1 and V = 0, and let w(z) = z f0(z), which has winding number kappa = 1. Let D_n(w) be its n-by-n Toeplitz determinant. Determine the large-n asymptotic of D_n(w), identifying the winding-induced power law, the alternating sign, and the explicit nonzero winding factor relating D_n(w) to the zero-winding base determinant D_n(f0).

## Attempted claim

For w(z) = z |z + 1|^{1/2} g_{-1,1/4}(z), D_n(w) = (-1)^n W-star E0 n^{-1/2} (1 + O(n^{-1/2})) as n -> infinity, where E0 = 2^{-1/8} is the base Fisher-Hartwig constant for f0 and W-star = 2^{-3/4} e^{i pi/8} Gamma(3/4)/Gamma(5/4) is an explicit nonzero winding factor of modulus 2^{-3/4} Gamma(3/4)/Gamma(5/4).

## Research outcome

Disproved the kappa=1 winding ladder: D_n(w)=0 for all n, falsifying the claimed nonzero n^{-1/2} law with constant ~0.737.

## Why this attempt failed

Failed axes: value.

value: FAIL. ADMISSION_DEFECT: topic.audit_preflight cheap-falsification checks claimed Fourier support with infinitely many nonzero negative coefficients, D1=(f0)_{-1} nonzero hypergeometric value, winding bookkeeping independent of conventions, and quote not reducible to triangular vanishing or normalization mismatch. All false: exact (f0)_{-1}=0, all negative modes vanish, D1=0 vs claimed |D1|~0.737, D_n(f0)=1 vs claimed E0=2^{-1/8}, first row identically zero. The negative resolution is therefore only triangular vanishing plus first-coefficient/tiny-instance mismatch and vacuous identically-zero sequence of the type STANDARD and TARGET policy explicitly require Admission to rule out. It exposes the alpha=beta degenerate diagonal, not the promised nonzero Gamma-Barnes ladder. Framing as winding obstruction does not create independent retrieval value; curing it requires different parameters/new direction, so intrinsic low value => REJECT, not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Standard Fisher-Hartwig branch convention shared with the cited base literature; a nonstandard cut placement would move but not remove the triangular vanishing; no replacement ladder constant is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
