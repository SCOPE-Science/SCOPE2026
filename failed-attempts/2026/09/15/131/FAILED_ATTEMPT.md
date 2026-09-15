# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Depth jump for quotients of the maximal-class pro-p group
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20371
- **Disposition:** NO_RESULT
- **Domain:** Finite Group Theory
- **Method:** cohomology-ring and fusion-system invariant analysis

## Problem

Let p>3 be prime, S=C_p \ltimes Z_p[zeta] the maximal-class pro-p group, T_0=Z_p[zeta], T_i=(zeta-1)^i T_0, and G_r=C_p \ltimes T_0/T_r of order p^{r+1} as in (1.1) of Garaialde Ocana-Gonzalez-Sanchez-Guerrero Sanchez. Prove that for every r >= p-1, depth H^*(G_r; F_p)=2.

## Attempted claim

Let p>3 be prime, S=C_p \ltimes Z_p[zeta] the maximal-class pro-p group, T_0=Z_p[zeta], T_i=(zeta-1)^i T_0, and G_r=C_p \ltimes T_0/T_r of order p^{r+1} as in (1.1) of Garaialde Ocana-Gonzalez-Sanchez-Guerrero Sanchez. Prove that for every r >= p-1, depth H^*(G_r; F_p)=2.

## Research outcome

Target depth-2 claim for all r>=p-1 remains unproven: the depth-1 killing class fails to extend, no length-2 regular sequence could be constructed, and computation confirmed only the depth<=2 structural side. Clean exit with no alternative finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The depth-2 lower bound needs the unknown cohomology ring of the exponent->p groups G_r; no cohomology engine (GAP/Sage/Magma) was available to compute even the smallest open case, Carlson detection bounds do not reverse after recent counterexamples, and additive stabilization does not preserve depth. Work stopped rather than overclaim.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The depth-2 lower bound needs the unknown cohomology ring of the exponent->p groups G_r; no cohomology engine (GAP/Sage/Magma) was available to compute even the smallest open case, Carlson detection bounds do not reverse after recent counterexamples, and additive stabilization does not preserve depth. Work stopped rather than overclaim.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
