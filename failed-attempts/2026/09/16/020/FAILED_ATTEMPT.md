# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified Courant-sharp classification for the Bolza surface via finite-element enclosures
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20469
- **Disposition:** NO_RESULT
- **Domain:** Spectral Geometry
- **Method:** certified finite-element and interval-arithmetic analysis

## Problem

Let B be the Bolza surface (closed genus-2 hyperbolic surface of area 4π, e.g. y^2=x^5-x), with spectrum 0=lambda_0<lambda_1<=lambda_2<=... counted with multiplicity. Determine, by a fully rigorous interval-arithmetic certificate combining certified finite-element two-sided eigenvalue enclosures on a hyperbolic fundamental domain with gluing/side-identification error control and a Faber-Krahn-Pleijel counting cap, the complete list of k for which there exists a lambda_k-eigenfunction with exactly k+1 nodal domains; in particular, decide whether any k>=4 is Courant-sharp on B. This is an unconditional finite-exact classification, not an asymptotic Pleijel bound and not conditional on the Bolza-maximizes-lambda_1 conjecture.

## Attempted claim

Let B be the Bolza surface (closed genus-2 hyperbolic surface of area 4π, e.g. y^2=x^5-x), with spectrum 0=lambda_0<lambda_1<=lambda_2<=... counted with multiplicity. Determine, by a fully rigorous interval-arithmetic certificate combining certified finite-element two-sided eigenvalue enclosures on a hyperbolic fundamental domain with gluing/side-identification error control and a Faber-Krahn-Pleijel counting cap, the complete list of k for which there exists a lambda_k-eigenfunction with exactly k+1 nodal domains; in particular, decide whether any k>=4 is Courant-sharp on B. This is an unconditional finite-exact classification, not an asymptotic Pleijel bound and not conditional on the Bolza-maximizes-lambda_1 conjecture.

## Research outcome

Target-only Bolza Courant-sharp certification is BLOCKED: three concrete routes plus a bounded mesh prototype all terminate at missing validated-numerics infrastructure, and no emergent or adjacent alternative passes Audit. Clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No certified result is claimed. The target's interval-arithmetic certificate (two-sided FEM enclosures, gluing error control, Pleijel cap) could not be built without a validated-numerics stack; the mesh prototype carries a >50 percent area bias from missing geodesic/side-pairing treatment; and no emergent alternative met the Audit bar. This is a clean negative outcome, not a partial classification.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No certified result is claimed. The target's interval-arithmetic certificate (two-sided FEM enclosures, gluing error control, Pleijel cap) could not be built without a validated-numerics stack; the mesh prototype carries a >50 percent area bias from missing geodesic/side-pairing treatment; and no emergent alternative met the Audit bar. This is a clean negative outcome, not a partial classification.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
