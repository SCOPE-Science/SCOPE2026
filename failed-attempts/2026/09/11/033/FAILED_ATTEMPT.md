# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A Selberg-trace interval certificate for the Bolza first eigenvalue inside the Yang-Yau sandwich
- **Round:** 2026-09-07-first-light-01
- **Lane:** 758
- **Disposition:** NO_RESULT
- **Domain:** Spectral Geometry
- **Method:** Selberg trace formula with length-spectrum enumeration and interval-arithmetic eigenvalue enclosure

## Problem

Produce a Selberg-trace-certified two-sided enclosure of the first nonzero Laplace eigenvalue of the Bolza surface inside the textbook sandwich, using explicit short-geodesic enumeration with interval arithmetic and a rigorous trace tail bound.

## Attempted claim

With curvature -1 normalization (area 4pi), prove by interval-arithmetic Selberg trace formula with logged Bolza short geodesics and explicit tail bound that lambda1(Bolza) lies in [3.79, 3.87], so the upper endpoint lies strictly below the Yang-Yau bound lambda1 <= 4 and the window certifies the gap around the numerical value ~3.839.

## Research outcome

Target two-sided Selberg certificate [3.79,3.87] blocked: only executable admissible route (sub-systole sinc^4) fails the exclusion inequality by ~5x, and repair needs a full census+optimizer+upper build beyond the clock. Revealed fallback (lambda1>=3.79 interval exclusion) attempted directly with three coded probes and likewise blocked: admissible compact-support families fail (positivity or margin), only inadmissible Gaussians close. CLEAN_EXIT with no valuable original increment.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['All probes are non-rigorous floating-point; no interval-arithmetic certificate was produced.', 'Extended-support probe dropped longer geodesics and tail (optimistic) yet still failed, strengthening the obstruction diagnosis but not proving impossibility.', 'No Fuchsian model, completeness census, or variational upper bound was built.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['All probes are non-rigorous floating-point; no interval-arithmetic certificate was produced.', 'Extended-support probe dropped longer geodesics and tail (optimistic) yet still failed, strengthening the obstruction diagnosis but not proving impossibility.', 'No Fuchsian model, completeness census, or variational upper bound was built.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
