# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp fixed-canonical-determinant rank-two Brill-Noether nonemptiness on a general irreducible one-nodal curve
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20229
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Geometry
- **Method:** Brill-Noether degeneration and limit linear series

## Problem

Let g>=3 and let X_0 be a general irreducible projective nodal curve of arithmetic genus g with exactly one node, with normalization a general smooth curve of genus g-1 and canonical line bundle L_0=omega_{X_0}. Let U_{X_0}(2,L_0) be the moduli space of semistable rank-2 torsion-free sheaves with determinant L_0 and B_{X_0}(2,L_0,k)={[E]: h^0(X_0,E)>=k}. Is B_{X_0}(2,L_0,k) nonempty if and only if rho_omega(k,g):=3g-3-binomial(k+1,2)>=0, and when nonempty does it contain an irreducible component of dimension rho_omega(k,g) whose general point is locally free and smooths to the nearby smooth general curve?

## Attempted claim

Let g>=3 and let X_0 be a general irreducible projective nodal curve of arithmetic genus g with exactly one node, with normalization a general smooth curve of genus g-1 and canonical line bundle L_0=omega_{X_0}. Let U_{X_0}(2,L_0) be the moduli space of semistable rank-2 torsion-free sheaves with determinant L_0 and B_{X_0}(2,L_0,k)={[E]: h^0(X_0,E)>=k}. Is B_{X_0}(2,L_0,k) nonempty if and only if rho_omega(k,g):=3g-3-binomial(k+1,2)>=0, and when nonempty does it contain an irreducible component of dimension rho_omega(k,g) whose general point is locally free and smooths to the nearby smooth general curve?

## Research outcome

Target blocked on both halves: existence reduces to an unavailable full smooth existence theorem and emptiness to an unavailable sharp nodal upper bound; bounded recovery test confirms the gap, so clean exit with no result claimed.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The investigation could not close either half of the sharp if-and-only-if claim: the existence half requires the full smooth rank-two canonical-determinant existence theorem for all rho>=0 pairs, and the emptiness half requires a sharp nodal or special-determinant upper bound; available tools (Teixidor 2008 Petri injectivity, Osserman lower bounds, Clifford/wedge estimates) provably fall short, as documented by the reproducible gap script in output/artifacts/clifford_gap.py.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The investigation could not close either half of the sharp if-and-only-if claim: the existence half requires the full smooth rank-two canonical-determinant existence theorem for all rho>=0 pairs, and the emptiness half requires a sharp nodal or special-determinant upper bound; available tools (Teixidor 2008 Petri injectivity, Osserman lower bounds, Clifford/wedge estimates) provably fall short, as documented by the reproducible gap script in output/artifacts/clifford_gap.py.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
