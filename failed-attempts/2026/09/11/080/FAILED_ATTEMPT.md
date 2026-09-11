# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quantized acceleration witness via determinant zero count in the complexified cocycle at coupling 3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 893
- **Disposition:** NO_RESULT
- **Domain:** Spectral Theory
- **Method:** Han-Schlag determinant zero counting with dual Jensen formula for complexified Lyapunov exponent

## Problem

For the lambda=3 golden-mean almost Mathieu cocycle, prove that for every E in [0.1,0.6] and epsilon in [0.02,0.10] the complexified slope (L(E,epsilon)-L(E,0))/(2*pi*epsilon) lies in [0.9,1.1], hence acceleration 1, via an enclosed count of zeros of the N=80 Dirichlet determinant in the strip.

## Attempted claim

Slope enclosure (L(E,epsilon)-L(E,0))/(2*pi*epsilon) in [0.9,1.1] for all E in [0.1,0.6], epsilon in [0.02,0.10], hence quantized acceleration 1, certified by enclosed N=80 determinant zero count.

## Research outcome

Target blocked after three concrete routes — (1) direct finite-eps slope scan (min slope ~0.99, no violation), (2) spectral-gap hunt via periodic approximants (uncertified candidate gap near E~=0.427), (3) gap-center scaling plus convergence ladder — none yielding a rigorous uniform enclosure, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

All Lyapunov slopes are non-rigorous floating-point transfer-matrix averages with no interval certificate; periodic-approximant spectra use dense eigensolves without validated error bounds; the candidate gap near E~=0.427 has no proven gap label or certified edge enclosure; no validated N=80 determinant zero count or Jensen remainder was produced.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: All Lyapunov slopes are non-rigorous floating-point transfer-matrix averages with no interval certificate; periodic-approximant spectra use dense eigensolves without validated error bounds; the candidate gap near E~=0.427 has no proven gap label or certified edge enclosure; no validated N=80 determinant zero count or Jensen remainder was produced.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
