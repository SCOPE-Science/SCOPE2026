# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Arbitrary distortability at the ratio-1 geometric boundary: the reflexive mixed-Tsirelson cell T[(S_n, 2^{-n})]
- **Round:** 2026-09-07-first-light-01
- **Lane:** 464
- **Disposition:** NO_RESULT
- **Domain:** Banach Space Geometry
- **Method:** Bourgain-Delbaen block-sequence construction with Szlenk-ordinal and spreading-model Ramsey-tree index analysis

## Problem

Decide arbitrary distortability versus bounded-distortion rigidity for the single named reflexive cell X0 = T[(S_n, 2^{-n})_{n in N}], the regular mixed-Tsirelson space built on Schreier families S_n with geometric weights theta_n = 2^{-n}. Either produce a distortable-renorming witness or isolate a stabilized subspace with ordinal-index logs.

## Attempted claim

The regular mixed Tsirelson space X0 = T[(S_n, 2^{-n})_n] is arbitrarily distortable: for every lambda > 1 there exists an equivalent norm ||| . ||| on X0 with distortion at least lambda (i.e., for every infinite-dimensional subspace Y of X0, sup{|||y|||/|||z||| : y,z in Y, ||y||=||z||=1} >= lambda under the original norm equivalence).

## Research outcome

Target (arbitrary distortability of X0=T[(S_n,2^{-n})]) remains open: finite-window exact norm computations confirm implicit-norm behavior and level-1 dominance but yield no distortion witness. Preset fallback Sz(X0)<=omega^{omega} not proved: no epsilon-Szlenk derivation certificate produced. Artifacts (norm_log.json, level_log.json, engines) and WORKLOG persist as replayable partial evidence.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No lambda-distortion witness produced: probed finite-window vectors show level-1 dominance with no two-norm separation >=2.', 'No epsilon-Szlenk derivation certificate produced for every epsilon>0; fallback success criterion (termination in <omega^{omega} steps with logged weakly-null tree) not met.', 'Literature route (Leung-Tang Bourgain-index corollary) identified but Szlenk transfer not established in-lane; not claimed.', 'Finite-window exact-rational norm logs (N<=7) do not extend to asymptotic statements without further analysis.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No lambda-distortion witness produced: probed finite-window vectors show level-1 dominance with no two-norm separation >=2.', 'No epsilon-Szlenk derivation certificate produced for every epsilon>0; fallback success criterion (termination in <omega^{omega} steps with logged weakly-null tree) not met.', 'Literature route (Leung-Tang Bourgain-index corollary) identified but Szlenk transfer not established in-lane; not claimed.', 'Finite-window exact-rational norm logs (N<=7) do not extend to asy…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
