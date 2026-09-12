# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Transverse elliptic-paraboloid point-plane incidences below N^{3/2}
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1443
- **Disposition:** NO_RESULT
- **Domain:** finite-field incidence geometry
- **Method:** polynomial partitioning with partitioning-surface versus quadric ruling analysis

## Problem

Let p be a prime with p >= 7 and p = 3 mod 4, let S={(x,y,z) in F_p^3 : z=x^2+y^2} be the elliptic paraboloid, which contains no F_p-line, let P subset S with m=|P|, and let Pi be an arbitrary set of n=m=N planes in F_p^3, each meeting S in an irreducible conic, with N <= p^{3/2}. Prove or disprove that there exist absolute constants C>0 and delta=1/16 such that every such configuration satisfies I(P,Pi) <= C N^{3/2-delta}. A complete answer is either a proof of this bound for all such primes p and all P subset S and transverse Pi in the stated range with C independent of p, P, Pi, via polynomial partitioning of F_p^3 combined with degree and ruling analysis of the partitioning surface versus S, or an explicit infinite family of such prime-field transverse (p,P,Pi) with I(P,Pi)/N^{3/2-delta} unbounded.

## Attempted claim

Let p be a prime with p >= 7 and p = 3 mod 4, let S={(x,y,z) in F_p^3 : z=x^2+y^2} be the elliptic paraboloid, which contains no F_p-line, let P subset S with m=|P|, and let Pi be an arbitrary set of n=m=N planes in F_p^3, each meeting S in an irreducible conic, with N <= p^{3/2}. Prove or disprove that there exist absolute constants C>0 and delta=1/16 such that every such configuration satisfies I(P,Pi) <= C N^{3/2-delta}. A complete answer is either a proof of this bound for all such primes p and all P subset S and transverse Pi in the stated range with C independent of p, P, Pi, via polynomial partitioning of F_p^3 combined with degree and ruling analysis of the partitioning surface versus S, or an explicit infinite family of such prime-field transverse (p,P,Pi) with I(P,Pi)/N^{3/2-delta} unbounded.

## Research outcome

Target blocked on both horns with no auditable increment: proof routes cap at N^{3/2} with unboundedly lossy p-factors, and the strongest grid family (exponent 1.4274) never crosses the 1.4375 threshold, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Classical KST/Vinh/point-circle bounds were quantified to exceed the target by unbounded p-dependent factors (up to 48.9x), and the lifted-grid family was computed only to N<=64 so its exponent fit 1.4274 is descriptive rather than conclusive; no proof or counterexample route remains within the pass.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Classical KST/Vinh/point-circle bounds were quantified to exceed the target by unbounded p-dependent factors (up to 48.9x), and the lifted-grid family was computed only to N<=64 so its exponent fit 1.4274 is descriptive rather than conclusive; no proof or counterexample route remains within the pass.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
