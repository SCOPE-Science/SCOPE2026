# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Asymptotic resurgence of ladder determinantal ideals
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20024
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** tight closure and test ideal asymptotics

## Problem

Let L be an unmixed ladder in an r×n generic matrix over a field K, let m be the largest integer for which L contains an m×m submatrix, and let I_t(L)⊂K[L] be the ideal of its t×t minors, with 1<t<m. For ρ_a(I)=sup{ s/r : s,r∈N and I^(sq) is not contained in I^(rq) for every q≫0 } and α̂(I)=lim_{q→∞} α(I^(q))/q, does one have ρ_a(I_t(L))=α(I_t(L))/α̂(I_t(L))=t(m−t+1)/m for every such ladder L and every field K?

## Attempted claim

Let L be an unmixed ladder in an r×n generic matrix over a field K, let m be the largest integer for which L contains an m×m submatrix, and let I_t(L)⊂K[L] be the ideal of its t×t minors, with 1<t<m. For ρ_a(I)=sup{ s/r : s,r∈N and I^(sq) is not contained in I^(rq) for every q≫0 } and α̂(I)=lim_{q→∞} α(I^(q))/q, does one have ρ_a(I_t(L))=α(I_t(L))/α̂(I_t(L))=t(m−t+1)/m for every such ladder L and every field K?

## Research outcome

Target blocked: the sharp asymptotic-resurgence upper bound for unmixed ladder determinantal ideals needs a ladder containment mechanism replacing the (P3)/(P4) decompositions that the literature explicitly says fail for ladders (Kumar-Mukundan open question); no original independently valuable increment or auditable adjacent alternative exists, so the lane exits clean with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof or disproof of the target equality was obtained: the sharp upper bound rho_a(I_t(L)) <= t(m-t+1)/m for unmixed ladders remains open, exactly as documented in the literature. The degree-half verification (gamma_check.py) only reproduces the published Kumar-Mukundan Theorem 4.3(1) and establishes nothing about resurgence. The literature conclusion rests on full-text reads of arXiv:2402.18693 and arXiv:2305.18167 as retrieved in this session. No computer algebra system was available for explicit symbolic-vs-ordinary containment tests that might have converted the block into a disproof.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof or disproof of the target equality was obtained: the sharp upper bound rho_a(I_t(L)) <= t(m-t+1)/m for unmixed ladders remains open, exactly as documented in the literature. The degree-half verification (gamma_check.py) only reproduces the published Kumar-Mukundan Theorem 4.3(1) and establishes nothing about resurgence. The literature conclusion rests on full-text reads of arXiv:2402.18693 and arXiv:2305.18167 as retrieved in this session. No computer algebra system was available for e…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
