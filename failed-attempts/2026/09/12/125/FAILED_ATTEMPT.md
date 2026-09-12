# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Gabor frame decision for cubic B-spline at (1/2,11/6)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1407
- **Disposition:** NO_RESULT
- **Domain:** time-frequency Gabor analysis
- **Method:** Zibulski-Zeevi matrix plus finite Janssen and Zak zeros

## Problem

Let B3 be the centered cubic B-spline supported in [-2,2] with knots at integers (B3=chi_{[-1/2,1/2]} convolved with itself 4 times, normalized continuous) and G(B3,a,b)={exp(2*pi*i*b*m*t)*B3(t-a*k)} with a=1/2, b=11/6 so ab=11/12<1 near the b~2 hyperbolic-slit regime. Decide whether G(B3,1/2,11/6) is a Gabor frame for L2(R) with uniform bounds 0<A<=B<infinity. A complete answer is either a proof of A>0 via the finite Zibulski-Zeevi Zak-matrix criterion plus Janssen representation bounds, or an explicit Zak-transform zero/Janssen-tie obstruction vector in C^q (q=12 denominator) in the kernel of the matrix-valued Zak symbol on a set of positive measure, witnessing failure of the lower bound.

## Attempted claim

Let B3 be the centered cubic B-spline supported in [-2,2] with knots at integers (B3=chi_{[-1/2,1/2]} convolved with itself 4 times, normalized continuous) and G(B3,a,b)={exp(2*pi*i*b*m*t)*B3(t-a*k)} with a=1/2, b=11/6 so ab=11/12<1 near the b~2 hyperbolic-slit regime. Decide whether G(B3,1/2,11/6) is a Gabor frame for L2(R) with uniform bounds 0<A<=B<infinity. A complete answer is either a proof of A>0 via the finite Zibulski-Zeevi Zak-matrix criterion plus Janssen representation bounds, or an explicit Zak-transform zero/Janssen-tie obstruction vector in C^q (q=12 denominator) in the kernel of the matrix-valued Zak symbol on a set of positive measure, witnessing failure of the lower bound.

## Research outcome

Target G(B3,1/2,11/6) frame decision could not be completed: neither a certified A>0 lower bound nor a rigorous obstruction was obtained, so the lane exits cleanly with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No certified lower frame bound and no rigorous obstruction was established: the corrected 11x11 Walnut fiber gives only a non-rigorous uniform numerical floor of lambda_min ~1.7e-8, the exact rational determinant at the tested point is nonzero, and the early positive toy-model scan used an incorrect Zak covering. Scripts and numerical tables are retained as working notes only and do not support any frame claim.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No certified lower frame bound and no rigorous obstruction was established: the corrected 11x11 Walnut fiber gives only a non-rigorous uniform numerical floor of lambda_min ~1.7e-8, the exact rational determinant at the tested point is nonzero, and the early positive toy-model scan used an incorrect Zak covering. Scripts and numerical tables are retained as working notes only and do not support any frame claim.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
