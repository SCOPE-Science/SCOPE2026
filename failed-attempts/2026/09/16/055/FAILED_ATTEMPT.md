# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Polynomial-degree abelian Cayley complexes below the trickling-down threshold in dimension >= 3
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20507
- **Disposition:** NO_RESULT
- **Domain:** Spectral Graph Theory
- **Method:** representation-theoretic and random-walk mixing analysis

## Problem

Fix an integer d >= 3 and a constant 0 < lambda < 1/d. Do there exist explicit infinite families of d-dimensional, simple, pure, translation-invariant (weighted) Cayley complexes X_n over F_2^n with n -> infinity, full-support top-face distribution, connected one-skeleton and connected positive-dimensional links, Cayley degree |S_n| = n^{O_{d,lambda}(1)}, such that on every codimension-two link the random-walk operator A satisfies ||A - Pi|| <= lambda on the orthogonal complement of the constants (two-sided local spectral expansion strictly below the 1/d Oppenheim trickling-down threshold)? In particular: can the endpoint bound 1/d of Mao's Theorem 1.3 be improved to any fixed lambda < 1/d while keeping Cayley degree polynomial in n, or is there a lower bound forbidding it?

## Attempted claim

Fix an integer d >= 3 and a constant 0 < lambda < 1/d. Do there exist explicit infinite families of d-dimensional, simple, pure, translation-invariant (weighted) Cayley complexes X_n over F_2^n with n -> infinity, full-support top-face distribution, connected one-skeleton and connected positive-dimensional links, Cayley degree |S_n| = n^{O_{d,lambda}(1)}, such that on every codimension-two link the random-walk operator A satisfies ||A - Pi|| <= lambda on the orthogonal complement of the constants (two-sided local spectral expansion strictly below the 1/d Oppenheim trickling-down threshold)? In particular: can the endpoint bound 1/d of Mao's Theorem 1.3 be improved to any fixed lambda < 1/d while keeping Cayley degree polynomial in n, or is there a lower bound forbidding it?

## Research outcome

Target blocked: beating Mao Theorem 1.3 endpoint 1/d at polynomial Cayley degree (d>=3) has no credible route. Exact small-scale spectra show 1/d attainment invariant under reweighting, clique-completion is vacuous where tested, the d=3 near-regime model exceeds 1/3, and the true-regime recovery test is infeasible; no emergent finding resulted. Clean exit per output/target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Small-scale exact spectra only: reachable models stay below the Golowich parameter regime (s>=2K, |V|>=4, K=2d with cube base needs ~10^6 K-faces and timed out), so numerics confirm endpoint tightness at toy scale but cannot rule out an unknown asymptotic construction. No lower-bound proof is offered either; the NO_RESULT reflects blocked routes within this pass, not a theorem that beating 1/d is impossible. One literature call and all fulltext reads concerned the admitted baseline paper only.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Small-scale exact spectra only: reachable models stay below the Golowich parameter regime (s>=2K, |V|>=4, K=2d with cube base needs ~10^6 K-faces and timed out), so numerics confirm endpoint tightness at toy scale but cannot rule out an unknown asymptotic construction. No lower-bound proof is offered either; the NO_RESULT reflects blocked routes within this pass, not a theorem that beating 1/d is impossible. One literature call and all fulltext reads concerned the admitted baseline paper only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
