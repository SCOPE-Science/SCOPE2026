# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform cusp-modulus band for twist-knot fillings of the Whitehead link
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1831
- **Disposition:** NO_RESULT
- **Domain:** hyperbolic 3-manifolds / Dehn filling
- **Method:** Thurston cone-deformation normalized-length estimates plus interval-arithmetic certification

## Problem

Let W = S^3 minus the Whitehead link, with cusps C0 (left unfilled) and C1 (to be filled) in the standard meridian-longitude framing. For each integer n with |n| >= 6 let K_n be the 1/n Dehn filling on C1, i.e. the twist-knot complement with geometric limit W as |n| -> infinity. Normalize the remaining cusp C0 at its maximal horoball so its meridian has length 1 and let tau_n in the upper half-plane be its cusp modulus. Prove or disprove that every K_n is hyperbolic and satisfies the two-sided band 1.70 <= Im(tau_n) <= 2.30 and |Re(tau_n)| <= 0.30. A complete answer is either a rigorous proof of hyperbolicity plus the band for all |n| >= 6 via explicit Thurston cone-deformation normalized-length estimates from the certified parent shape, or an explicit integer n with |n| >= 6 proved hyperbolic whose interval-arithmetic certified tau_n lies outside the band; numerics alone do not count.

## Attempted claim

Let W = S^3 minus the Whitehead link, with cusps C0 (left unfilled) and C1 (to be filled) in the standard meridian-longitude framing. For each integer n with |n| >= 6 let K_n be the 1/n Dehn filling on C1, i.e. the twist-knot complement with geometric limit W as |n| -> infinity. Normalize the remaining cusp C0 at its maximal horoball so its meridian has length 1 and let tau_n in the upper half-plane be its cusp modulus. Prove or disprove that every K_n is hyperbolic and satisfies the two-sided band 1.70 <= Im(tau_n) <= 2.30 and |Re(tau_n)| <= 0.30. A complete answer is either a rigorous proof of hyperbolicity plus the band for all |n| >= 6 via explicit Thurston cone-deformation normalized-length estimates from the certified parent shape, or an explicit integer n with |n| >= 6 proved hyperbolic whose interval-arithmetic certified tau_n lies outside the band; numerics alone do not count.

## Research outcome

Target blocked: uniform cusp-modulus band for 1/n Whitehead fillings could be neither rigorously proved nor certified-disproved within the pass; clean exit with no fallback available.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No Sage-backed interval-arithmetic certification exists in this environment and the single permitted literature-retrieval call failed with an infrastructure error, so neither the rigorous uniform band proof nor a certified counterexample required by the success criterion could be produced; all modulus values cited are non-certified floating-point orientation only.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No Sage-backed interval-arithmetic certification exists in this environment and the single permitted literature-retrieval call failed with an infrastructure error, so neither the rigorous uniform band proof nor a certified counterexample required by the success criterion could be produced; all modulus values cited are non-certified floating-point orientation only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
