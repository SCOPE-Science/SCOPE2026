# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Threshold-breaking few-products-many-sums with the sumset over prime fields
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20407
- **Disposition:** NO_RESULT
- **Domain:** Additive Combinatorics
- **Method:** incidence-geometry polynomial-method transfer analysis

## Problem

Let p be prime, A subset F_p^*, and put K_+=|A+A|/|A|, M=|AA|/|A|. Assume |A|<p^{24/49} or M^2 K_+^2 |A|^3 < p^2. Prove, up to powers of log|A|, that K_+^{24} M^{36} >> |A|^{13}, and in particular that for every sufficiently small epsilon>0 there is c(epsilon)>0 such that |AA| <= |A|^{1+epsilon} implies |A+A| >> |A|^{3/2+c(epsilon)}.

## Attempted claim

Let p be prime, A subset F_p^*, and put K_+=|A+A|/|A|, M=|AA|/|A|. Assume |A|<p^{24/49} or M^2 K_+^2 |A|^3 < p^2. Prove, up to powers of log|A|, that K_+^{24} M^{36} >> |A|^{13}, and in particular that for every sufficiently small epsilon>0 there is c(epsilon)>0 such that |AA| <= |A|^{1+epsilon} implies |A+A| >> |A|^{3/2+c(epsilon)}.

## Research outcome

Target K_+^{24}M^{36} >> N^{13} (threshold-breaking few-products-many-sums over F_p) not proved in-window: reduced to a cubic-energy bound E_3 << M^3 N^{35/12}, showed the published lemma gives only K^24M^24 >> N^12 (a full power of N short), verified plausibility computationally (R>=3.5e9, no counterexample), and exited cleanly with no emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The negative outcome is bounded: the T1 scan covers only small fields (F_101, F_1009) and structured or seeded-random sets, so it cannot certify the target in general; the T2 diagnosis depends on the extracted text of one published paper (Murphy-Rudnev-Shkredov-Shteinikov) and standard Holder and dyadic reductions, and it does not rule out that a future eigenvalue-plus-incidence argument closes the gap. Verification artifacts are limited to the scan script and its output plus the WORKLOG route record.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The negative outcome is bounded: the T1 scan covers only small fields (F_101, F_1009) and structured or seeded-random sets, so it cannot certify the target in general; the T2 diagnosis depends on the extracted text of one published paper (Murphy-Rudnev-Shkredov-Shteinikov) and standard Holder and dyadic reductions, and it does not rule out that a future eigenvalue-plus-incidence argument closes the gap. Verification artifacts are limited to the scan script and its output plus the WORKLOG route…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
