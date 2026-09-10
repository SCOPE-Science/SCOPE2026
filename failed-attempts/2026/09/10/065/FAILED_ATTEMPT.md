# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Characteristic-2 failure of rank-2 canonical Petri injectivity on genus-5 curves: a k=4 kernel witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 656
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Geometry
- **Method:** limit linear series degeneration with Petri-map kernel analysis

## Problem

Decide sharpness of the characteristic-not-2 hypothesis in rank-2 canonical Brill-Noether theory on genus 5: does the canonical Petri map S^2 H^0(E) -> H^0(S^2 E) remain injective for stable rank-2 bundles with canonical determinant and 4 sections on a general ordinary genus-5 curve in characteristic 2, or does an explicit kernel witness produce an oversize/singular B^4_{2,K} contrasting characteristic zero? Attack by specializing the published Teixidor (5,4) limit linear series on a chain of 5 ordinary elliptic curves to characteristic 2 and computing the limit Petri kernel by component linear algebra, then testing one smoothing criterion.

## Attempted claim

Over an algebraically closed field of characteristic 2, let C be a general ordinary smooth projective curve of genus 5. Then there exists a stable rank-2 vector bundle E on C with determinant det(E) = K_C and h^0(C,E) = 4 such that the canonical Petri map S^2 H^0(C,E) -> H^0(C, S^2 E) has nontrivial kernel of dimension at least one; hence B^4_{2,K}(C) is singular or of dimension exceeding the Bertram-Feinberg-Mukai expected dimension rho(5,4) = 2, in direct contrast to Teixidor generic injectivity in characteristic not 2.

## Research outcome

Target (generic ordinary genus-5 char-2 Petri kernel) blocked: special-fibre mechanism does not lift (open condition, no char-2 smoothing theorem). Revealed fallback (exhibited central-fibre kernel tensor) directly attempted via per-component limit-product pattern census: middle-summand collisions separate in diagonal summands, so no kernel vector is forced and none was exhibited. CLEAN_EXIT with VERIFY_OK negative-pattern scripts.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Full H0(S^2 E) matrix rank over explicit component coordinates not computed; pattern-level analysis only.', 'Ordinarity of the F2 chain components assumed from setup, not certified by Hasse invariant computation.', 'No char-2 smoothing criterion proved.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Full H0(S^2 E) matrix rank over explicit component coordinates not computed; pattern-level analysis only.', 'Ordinarity of the F2 chain components assumed from setup, not certified by Hasse invariant computation.', 'No char-2 smoothing criterion proved.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
