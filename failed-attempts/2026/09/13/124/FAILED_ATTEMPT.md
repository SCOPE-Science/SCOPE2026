# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Spectral linear stability of the Gerver Super-Eight
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1766
- **Disposition:** NO_RESULT
- **Domain:** celestial mechanics / Hamiltonian stability
- **Method:** rigorous reduced monodromy Floquet enclosure

## Problem

For the equal-mass planar Newtonian four-body Gerver Super-Eight choreography (the Gerver/Kapela-Zgliczynski/Shibayama T*-periodic zero-angular-momentum choreographic orbit with its dihedral/parallelogram symmetry, centre of mass at origin), decide its spectral linear-stability type on the symmetry- and integral-reduced phase space: either prove it is linearly (spectrally) stable with all non-trivial Floquet multipliers on the unit circle after removing the eight trivial multipliers from first integrals and symmetries, or prove it is linearly unstable by exhibiting at least one Floquet multiplier off the unit circle with rigorous enclosure. A complete answer is a rigorous computation of the enclosed reduced monodromy spectrum and the resulting stable-versus-unstable classification for this specific orbit.

## Attempted claim

For the equal-mass planar Newtonian four-body Gerver Super-Eight choreography (the Gerver/Kapela-Zgliczynski/Shibayama T*-periodic zero-angular-momentum choreographic orbit with its dihedral/parallelogram symmetry, centre of mass at origin), decide its spectral linear-stability type on the symmetry- and integral-reduced phase space: either prove it is linearly (spectrally) stable with all non-trivial Floquet multipliers on the unit circle after removing the eight trivial multipliers from first integrals and symmetries, or prove it is linearly unstable by exhibiting at least one Floquet multiplier off the unit circle with rigorous enclosure. A complete answer is a rigorous computation of the enclosed reduced monodromy spectrum and the resulting stable-versus-unstable classification for this specific orbit.

## Research outcome

Target blocked: rigorous reduced-monodromy enclosure of the Gerver Super-Eight is infeasible on this pass with only numpy and no validated-integration machinery; naive-interval recovery test failed with measured blow-up, and no independently valuable finding was produced, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No validated ODE integrator, interval arithmetic library, Lohner QR code, Taylor-model machinery, regularization, orbit initial conditions, or eigenvalue validator was available in the workspace; only python3 plus numpy could be used. A non-rigorous float integration was deliberately not pursued because it cannot satisfy the explicit rigorous-enclosure success criterion.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No validated ODE integrator, interval arithmetic library, Lohner QR code, Taylor-model machinery, regularization, orbit initial conditions, or eigenvalue validator was available in the workspace; only python3 plus numpy could be used. A non-rigorous float integration was deliberately not pursued because it cannot satisfy the explicit rigorous-enclosure success criterion.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
