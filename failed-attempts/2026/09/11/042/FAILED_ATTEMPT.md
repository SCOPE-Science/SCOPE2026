# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing one rank-1 quintic genus-2 curve via Coleman bound at p=5 and sieve at 29,43
- **Round:** 2026-09-07-first-light-01
- **Lane:** 779
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** Chabauty-Coleman p-adic integration at p=5 with Mordell-Weil sieving

## Problem

Let C1: y^2 = x^5 - 2x^3 + x + 1 over Q (smooth, genus 2, one point at infinity). Naively visible points are infinity, (0,+/-1), (1,+/-1), (-1,+/-1). With Jacobian rank 1 and p=5 a good ordinary Chabauty prime, prove via an explicit annihilating differential, Coleman per-disk zero bound, and Mordell-Weil sieve at auxiliary primes 29 and 43 that C1(Q) equals exactly this finite set.

## Attempted claim

C1(Q) = {infinity, (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)} with Coleman bound at p=5 and Mordell-Weil sieve elimination at 29 and 43 as squeeze witness.

## Research outcome

Target census refuted: two explicit rational points outside the claimed 7-point set, each certified by exact integer arithmetic with replayable script.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: headline witnesses are already recorded in the official database for the identical object. LMFDB 91808.b.734464.1 has simplified equation y^2=x^5-2x^3+x+1 and lists Known points (1:0:0),(0:+-1:1),(-1:+-1:1),(1:+-1:1),(7:+-127:1),(17:+-4132:16), i.e. the 7 claimed points plus exactly the four witnesses (17/16,+-1033/1024 since 4132/16^3=1033/1024). A prior source need not state the headline verbatim: this table substantively implies the 7-point equality is false and exhaustively covers the claimed extra points. Fused tri-provider search found only method templates and disjoint curves, but direct official-database check is decisive. Independent rediscovery by substitution does not establish priority. value: FAIL: no independently retrievable new fact beyond the official database. C1 is natural and motivated, but the exact witnesses and the rank-2 invariant (Z+Z, analytic rank 2) are already retrievable at LMFDB 91808.b.734464.1 as Known points / MW group data. The submission is recomputation/certificate of database-known points by elementary substitution, not the admitted payoff (new Coleman bound at p=5 + sieve elimination at 29/43 closing a new census). Certification alone does not rescue database repackaging. A future researcher needing these points or the falsity of the 7-point census would find them directly in LMFDB; the refutation is not a citable downstream advance.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Disproof of the exact 7-point census only; no determination of the full (larger) C1(Q), no rank or Chabauty/sieve claims.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
