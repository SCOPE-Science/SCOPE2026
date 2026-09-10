# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A 2-primary anticyclotomic Heegner-index bound for 37a1 over Q(sqrt(-7))
- **Round:** 2026-09-07-first-light-01
- **Lane:** 632
- **Disposition:** NO_RESULT
- **Domain:** Iwasawa Theory
- **Method:** Kolyvagin-derivative Euler-system induction with Iwasawa main-conjecture divisibility comparison

## Problem

Decide a one-sided anticyclotomic 2-primary rank-plus-Sha bound for the named rank-one cell (E=37a1, K=Q(sqrt(-7)), p=2): prove the Kolyvagin Heegner-index divisibility forcing analytic/algebraic rank 1 with an explicit 2-primary Sha index bound, or isolate a certified local-obstruction witness where the mod-2 Euler-system classes fail to generate the Selmer block.

## Attempted claim

For E=37a1 (y^2+y=x^3-x) over K=Q(sqrt(-7)) at p=2: the Heegner point y_K of conductor 1 is of infinite order, and Kolyvagin induction plus the anticyclotomic main-conjecture divisibility forces rank E(Q)=1 with the explicit 2-primary bound ord_2(#Sha(E/Q)) <= 2*ord_2([E(K)^- : Z*y_K]) + t_2, where t_2 is the explicit logged 2-adic Tamagawa fudge at places dividing 74 and 2.

## Research outcome

Target (2-primary Heegner-index divisibility for 37a1/Q(sqrt(-7))/2) blocked: splitting/S3/Kolyvagin-prime numerics verify but derivative class and 2-adic divisibility unconstructible. Preset fallback (single certified kappa_ell at ell=5) attempted with bounded replayable script; integer-level admissibility, class numbers, and Frobenius shape logged, but explicit cocycle plus finite/transverse local log unconstructible with lane tooling. No original increment. CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No Sage/PARI/Magma or L-value/modular-symbol library in lane (stdlib+sympy only; no pip), so no Heegner point, derivative cocycle, or 2-adic local verification constructible.', 'All covering divisibility theorems in the admission record explicitly exclude p=2; no citable 2-adic local theory available.', 'Small-height K-point search (R=6, d in {1,2}) is a bounded negative signal only, not a nontorsion or torsion certificate.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No Sage/PARI/Magma or L-value/modular-symbol library in lane (stdlib+sympy only; no pip), so no Heegner point, derivative cocycle, or 2-adic local verification constructible.', 'All covering divisibility theorems in the admission record explicitly exclude p=2; no citable 2-adic local theory available.', 'Small-height K-point search (R=6, d in {1,2}) is a bounded negative signal only, not a nontorsion or torsion certificate.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
