# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified rank-2 equality and complete integral-point lists for the conductor-4006 pair 4006a1/4006b1 by 2-descent and canonical-height enclosure
- **Round:** 2026-09-07-first-light-01
- **Lane:** 96
- **Disposition:** NO_RESULT
- **Domain:** Arithmetic Geometry
- **Method:** 2-descent rank bounds with canonical-height interval enclosure and Cremona table replay

## Problem

Let Ea: y^2+xy = x^3-x^2+4x-2 (Cremona 4006a1, conductor 2*2003, Delta=-4006) and Eb: y^2+xy = x^3-87x+361 (Cremona 4006b1, Delta=-2^13*2003). Prove by a checkable 2-Selmer upper bound plus interval canonical-height lower bound that rank_Q(Ea)=rank_Q(Eb)=2 with explicit bases [(1,1),(3,4)] and [(6,5),(22,85)] respectively, and prove the complete integral-point sets in these minimal models are exactly Ea(Z)={x=1,3,9,99} (8 points) and Eb(Z)={x=-10,-6,0,2,4,6,14,22,62,126,270} (22 points) via an explicit elliptic-logarithm height bound plus finite sieve/search.

## Attempted claim

Certified rank_Q=2 for both 4006a1 and 4006b1: 2-Selmer dimension forces rank<=2 while the interval-enclosed canonical height pairing on the stated point pairs has determinant 1.15206... (Ea) and 0.14827... (Eb) rigorously bounded away from zero, with trivial torsion and 2-saturation checked; analytic rank 2 (modular-symbols/L-derivative) recorded as cross-check with Sha_an=1. Plus complete integral-point lists as in problem statement, proved by an explicit height bound (Sage/Magma elliptic-log + LLL) reduced to a logged finite search that finds no further integral x.

## Research outcome

Lane 96 targeted certified rank=2 plus complete integral-point lists for 4006a1/4006b1. Environment had no Sage/PARI/Magma/mwrank, so the two proof-critical components (2-Selmer upper bound rank<=2; elliptic-log height bound for integral completeness) could not be honestly established. Delivered instead a stdlib-only exact-arithmetic audit: minimal models, discriminants -4006 and -2^13*2003, Kodaira I_1/I_1 and I_13/I_1 with split/nonsplit determined by tangent-cone computation, Tamagawa 1 and 13 (correcting the brief's 'cp=1' for Eb), trivial torsion (reduction counts + 2-division cubic + E(F7) killing 3-torsion), rank>=2 via mod-p obstructions to halving P1,P2,P1+P2, and an exhaustive integral-point scan over |x|<=1e7 reproducing exactly the 8-point and 22-point lists. Rank equality and completeness over Z remain unproved; per instructions this is reported as NO_RESULT with reusable audited fragments.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No 2-Selmer/2-descent upper bound computed (no Sage/PARI/mwrank in environment); rank<=2 unproved, so rank equality NOT proved.', 'No elliptic-logarithm height bound (David + LLL reduction) implemented; integral-list completeness proved only for |x|<=1e7 by exhaustive square-test scan, not over Z.', 'Canonical-height pairing determinant not enclosed by rigorous interval arithmetic (prototype had a naive-height bug; omitted rather than shipped). Regulator values 1.15206/0.14827 quoted from LMFDB as cross-checks only.', 'Analytic rank / root number / Sha_an quoted from LMFDB pages as consistency data, not independently recomputed.', 'Correction to brief: Tamagawa product of 4006b1 is 13*1=13 (split I_13 at 2), not 1; verified by tangent-cone computation and LMFDB local-data table.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No 2-Selmer/2-descent upper bound computed (no Sage/PARI/mwrank in environment); rank<=2 unproved, so rank equality NOT proved.', 'No elliptic-logarithm height bound (David + LLL reduction) implemented; integral-list completeness proved only for |x|<=1e7 by exhaustive square-test scan, not over Z.', 'Canonical-height pairing determinant not enclosed by rigorous interval arithmetic (prototype had a naive-height bug; omitted rather than shipped). Regulator values 1.15206/0.14827 quoted from LMF…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
