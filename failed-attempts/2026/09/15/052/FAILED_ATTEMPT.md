# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Classification of 1-cusped hyperbolic 3-manifolds with three finite nonabelian Dehn fillings
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20253
- **Disposition:** NO_RESULT
- **Domain:** Low-Dimensional Topology
- **Method:** canonical triangulation and character variety analysis

## Problem

Let M be a compact orientable 1-cusped hyperbolic 3-manifold admitting three distinct Dehn fillings M(alpha_1), M(alpha_2), M(alpha_3) each with finite nonabelian fundamental group. Is M homeomorphic to one of the SnapPy census manifolds m011, s757, v2702, v2797? Equivalently: prove that any such M admits at most three finite nonabelian fillings and that these four are the only manifolds attaining three.

## Attempted claim

Let M be a compact orientable 1-cusped hyperbolic 3-manifold admitting three distinct Dehn fillings M(alpha_1), M(alpha_2), M(alpha_3) each with finite nonabelian fundamental group. Is M homeomorphic to one of the SnapPy census manifolds m011, s757, v2702, v2797? Equivalently: prove that any such M admits at most three finite nonabelian fillings and that these four are the only manifolds attaining three.

## Research outcome

Target blocked: the claim is Dunfield Conjecture 4.1 on three finite nonabelian fillings, requiring global character-variety bounds and certified computation beyond this pass. Mapped the m011 exceptional set, certified m011(1,1) of order 12, and identified the large-order certification gap; no independently valuable original increment survived, so clean exit with no result.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No certified global proof was possible: SnapPy hyperbolicity verification requires Sage (unavailable), Regina and Recognizer recognition are not installed, and low-index subgroup census cannot scale to large finite fillings such as order 2040. All computed evidence reproduces published census data rather than establishing the claimed uniqueness over all volumes.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No certified global proof was possible: SnapPy hyperbolicity verification requires Sage (unavailable), Regina and Recognizer recognition are not installed, and low-index subgroup census cannot scale to large finite fillings such as order 2040. All computed evidence reproduces published census data rather than establishing the claimed uniqueness over all volumes.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
