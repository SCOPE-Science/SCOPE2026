# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Toric Viterbo-capacity deficit versus Mahler deficit for unconditional bodies in R^4
- **Round:** 2026-09-07-first-light-01
- **Lane:** 850
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Asymptotic Convex Analysis
- **Method:** toric moment-polytope symplectic-capacity comparison with closed-form volume products

## Problem

Establish an explicit quantitative comparison between normalized symplectic-capacity deficit and Mahler deficit on the unconditional toric B_p^4 curve in R^4, yielding a capacity-to-Mahler stability transfer with a named constant.

## Attempted claim

For toric domains X_p associated to the unconditional balls B_p^4 (p in [2,infinity], including cube p=infinity and Euclidean ball p=2), with normalized EHZ capacity c(X_p) and Mahler product P(B_p^4), there is an explicit C>0 such that (1/C)*D_Mahler(p) <= D_cap(p) <= C*D_Mahler(p) (or the stated explicit one-sided transfer with named C and calibration points p=2,4,infinity), where deficits are measured relative to the cube/toric-cube value; proved by closed-form evaluation on both sides.

## Research outcome

TARGET complete: explicit C=1 capacity-to-Mahler one-sided deficit bound on toric B_p^4 curve with p=2,4,inf calibration triple, plus proof no finite-C reverse/two-sided comparison exists.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: headline is immediate corollary/repackaging of two explicit results in the same prior source Shi-Lu arXiv:2008.04000. Cor 1.6 already states c(B_p^n x_L B_inf^n)=4 for every p in [1,inf], symplectomorphic to X_p=X_{4|B_p|} via cited [24 Thm 7] (DRAFT Sec.2 Remark acknowledges identity), so c(X_p)=4 identically and D_cap=0 is known. Thm 4.1/Claim 4.2 already proves Vol(B_p^n)Vol((B_p^n)^o)>=4^n/n! with equality iff p=1,inf via digamma monotonicity, so D_M>=0 with strict >0 at p=2,4 is known. Conjunction gives 0<=D_M and reverse impossibility by pure algebra with no new idea; named C=1 is arbitrary (any C>0 works, including arbitrarily small). No explicit deficit-ratio sentence in prior art, but prior results substantively imply and exhaustively cover the claim as special case (n=4, p in [2,inf] subset of broader 1-unconditional theorems). Fused retrieval (SerpBase/Serpent+Crossref, OpenAlex ok with 0 hits, partial=false) found no competing deficit comparison, but absence of verbatim sentence does not establish priority when implication is mechanical. See decisive_checks. value: FAIL: vacuous one-sided bound 0<=1*D_M carries no quantitative content and does not deliver admitted transfer payoff (symplectic attack on Mahler stability). Capacity blindness (constant vs >100% Mahler variation) was already implicit in known constancy + known variation; pointing out 0 vs positive is textbook observation. Calibration triple P(2)=pi^4/4, P(inf)=32/3 exact and P(4)~20.5472 is direct substitution into known closed-form (4.15), not an independently retrievable benchmark a future researcher would cite over Shi-Lu. Under narrow-datum policy: object/motivation pre-existed but value was already known/mechanically implied and future need is met by citing Shi-Lu Cor 1.6 + Thm 4.1, not this pairing. Falls under textbook restatement / mere parameter evaluation / trivial corollary even though correct. verify.py certification does not rescue arbitrary pairing of known sides.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Restricted to symmetric B_p^4 toric curve in R^4; capacity evaluated via cited toric formula; Mahler positivity at p=4 relies on cited analytic monotonicity, numerics are calibration only; no universal stability constant claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
