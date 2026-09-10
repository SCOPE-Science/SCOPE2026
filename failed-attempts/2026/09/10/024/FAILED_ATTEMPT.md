# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** First single-digit explicit universal constant for the sharp O(n) thin-shell inequality via constant-tracked parallel coupling
- **Round:** 2026-09-07-first-light-01
- **Lane:** 549
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** Eldan stochastic localization with parallel coupling and constant-tracked covariance-trace control

## Problem

Let X range over all isotropic log-concave random vectors in R^n for all n>=1 (no window restriction). Klartag-Lehec 2025 (arXiv:2507.15495) proves Var(|X|^2)<=C n with unspecified universal C, and Klartag-Lehec GAFA 2025 (DOI 10.1007/s00039-025-00718-w) resolves Bourgain slicing via Guan E Tr[A_t^2]<=C n with only an absurdly large extractable constant. Prove the first single-digit explicit universal form Var(|X|^2)<=8 n by re-running the parallel-coupling plus Eldan-localization argument with fully tracked constants; or establish the explicit constant-tracked Guan certificate E Tr[A_t^2]<=8n uniformly in t>=0 as the independently valuable localization lemma.

## Attempted claim

For every dimension n>=1 and every isotropic log-concave random vector X in R^n: Var(|X|^2) <= 8 n, with explicit constant 8 proved by a fully constant-tracked re-run of the Klartag-Lehec parallel-coupling plus Eldan stochastic-localization argument.

## Research outcome

Target Var<=8n upper bound NOT closed: as-written KL chain forces a certified constant floor >=6.01e21 (alpha=1/8, beta=16). Fallback trace certificate likewise not reachable. Consolidated emergent sharpness theorem: i.i.d. shifted-exponential witness gives Var(|X|^2)=8n exactly for all n, so optimal universal constant C*>=8 and target constant 8 is exactly sharp if valid. Machine-checked by two replay-passing stdlib scripts.

## Why this attempt failed

Failed axes: originality.

originality: FAIL. Claim route is EMERGENT_FINDING (research_report.claim_route='EMERGENT_FINDING'); discovery context (logged EMERGENT_CANDIDATE E1 while auditing KL tightness examples, same universal scope, constrains target constant) verifies it genuinely arose from target work rather than scope evasion, so ordinary full originality standard applies with no presumption. Under that standard the exact witness is anticipated by Chen-Klartag arXiv:2607.23307 (submitted 25 Jul 2026, before audit), which proves the strictly stronger sharp thin-shell theorem. Abstract and Theorem 1.1 state Var(|X|^2)<=8n for all isotropic log-concave X AND 'The constant 8 is optimal: equality is attained when X1,...,Xn are i.i.d. standard, centered exponential random variables' with density e^{-x-1}1_{x>=-1} — literally the submitted X_i=Y_i-1, Y_i~Exp(1) i.i.d. witness and the submitted value 8n. The submitted lower-bound-only certificate is therefore a strict subset/corollary of a published stronger fact. Elementary-derivation honesty in DRAFT s7 does not restore priority; a timestamp/failed search never establishes priority, and here the prior timestamp affirmatively defeats it. Originality failure is never repairable.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: Proved only the lower bound C* >= 8. NOT proved: target upper bound Var <= 8n; fallback uniform Guan certificate E Tr[A_t^2] <= 8n; 1D maximality E Z^4 <= 9 (only subfamily scan evidence, not a theorem). Originality is to the auditable certificate per triage-checked sources, with elementary-derivation honesty stated. No new literature search beyond admitted sources plus full KL fetch is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
