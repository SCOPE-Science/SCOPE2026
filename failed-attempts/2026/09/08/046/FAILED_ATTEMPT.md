# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact minimal coherence for 9 lines in R^4: a Levenshtein/LP-matching Grassmannian optimum at a proven non-ETF cell
- **Round:** 2026-09-07-first-light-01
- **Lane:** 150
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Frame Theory
- **Method:** explicit symmetric line packing with Delsarte-LP polynomial lower bound and Gegenbauer-positivity verification

## Problem

Close the exact optimal coherence mu*(4,9) = min over 9-line packings in RP^3 of max_{i!=j}|<vi,vj>| for unit vectors vi in R^4. Exhibit (i) an explicit 9-vector unit configuration with certified maximal coherence U, and (ii) an explicit Delsarte-LP polynomial with verified Gegenbauer positivity proving every 9-line set in R^4 has coherence >= L, with L = U, so mu*(4,9) equals that common value exactly.

## Attempted claim

The minimal coherence over all 9-line packings in R^4 is exactly mu*(4,9) = T (the common value of the exhibited configuration and the LP lower bound, to be fixed by the run), certified two-sided: an explicit unit 9-vector configuration attains maximal coherence T with Gram PSD of rank<=4, and an explicit Delsarte-LP polynomial with nonnegative Gegenbauer coefficients proves no 9-line set in R^4 has coherence below T.

## Research outcome

Certified two-sided enclosure mu*(4,9) in [sqrt(5/32), 0.438]: exact degree-2 Delsarte-LP Welch lower bound plus explicit 9-vector R^4 configuration with Gram PSD/rank certificate attaining coherence 0.43776 (certified <= 0.438). Pre-registered fallback interval; exact optimality NOT claimed.

## Why this attempt failed

Failed axes: originality, value.

originality: Strongest headline claim is certified interval mu*(4,9) in [sqrt(5/32),0.438]. Lower side is explicitly a textbook restatement: DRAFT remarks 'No originality is claimed for (L) itself' and it equals the 1974 Welch bound. Upper side 0.438 is numerically weaker than 30-year-old prior numerics: Sloane Grassmann table lists m=4,n=1,N=9 D=0.811419515303501 (CHS96 computer search), which converts via mu=sqrt(1-D) to coherence 0.43425854, strictly better (smaller) than 0.43775813. Sloane page provides downloadable coordinates grassc.4.1.9.txt for the same cell, so the same numpy Gram-max replay applied to prior vectors would yield a stronger upper bound. A different stochastic-search witness with worse value and identical floating-point evidence level (eig>-1e-8, max) is new digits, not a substantively new claim. No new LP lower bound beyond Welch, no exact optimum (L!=U), no exact algebraic/interval certificate qualitatively beyond prior numerics, no structural description. Nearest priors substantively cover the claim: Welch bound, Conway-Hardin-Sloane Exp.Math.1996 packing tables, Fickus-Mixon ETF tables (rules out ETF but gives no new bound), de Laat et al. k-point SDP (different axis). Failed-search timestamp does not establish priority. value: Interval [0.39528471,0.438] width ~0.0427 is not independently worth retrieving. Lower equals classical Welch (textbook restatement, explicitly disclaimed). Upper 0.4378 does not improve the recognized benchmark: it is worse than Sloane putative ~0.4343, admitted in DRAFT limitations ('slightly above... contribution is certification, not a numerical record'). It therefore fails its own admission requirement of strictly improving on Welch and putative status. Floating-point PSD/rank replay is same evidence level as prior computer-search numerics, not an exact algebraic order/constant/witness with new mathematical interpretation; stochastic local search (~130 restarts, no symmetry or exact form) yields an unexplained number. Certification alone does not rescue an arbitrary numerical vector set with worse value per shared standard. Future researcher needing mu*(4,9) would retrieve Welch plus Sloane 0.4343, not this weaker interval. No reusable LP pipeline beyond degree-2 Welch, no downstream use enabled. Reject as textbook lower plus tiny negative gain upper.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Bounds do not meet (width ~0.0427). Lower bound equals classical Welch (no strict improvement; higher-degree LP sampling found nothing better but proves nothing). Upper bound 0.4378 is slightly above the uncertified putative catalogue ~0.43; contribution is certification, not a numerical record. Configuration is numerical, no exact algebraic form.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
