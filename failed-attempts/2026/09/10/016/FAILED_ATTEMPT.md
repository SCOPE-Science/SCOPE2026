# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform regularity-versus-induced-matching bound and extremal Betti shapes for edge ideals of claw-free graphs
- **Round:** 2026-09-07-first-light-01
- **Lane:** 528
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** combinatorial commutative algebra: polarization, vertex-decomposability induction, and graded free-resolution comparison

## Problem

Classify the regularity-versus-projective-dimension boundary for edge ideals of claw-free graphs: prove a uniform Castelnuovo-Mumford regularity upper bound in terms of induced matching number, and characterize the extremal graded Betti tables attaining it.

## Attempted claim

For every finite simple claw-free graph G with induced matching number nu(G), reg(S/I(G)) <= 2*nu(G); moreover any sharp example (equality) contains a prescribed minimal induced obstruction subgraph whose graded Betti table has its top regularity strand supported in a single explicitly described homological degree.

## Research outcome

No CLAIMED result. Full-target attack found zero violations of reg<=2nu (exhaustive n=6: 15272 claw-free graphs, 0 violations; ~4300 random/structured claw-free graphs n=7..11, 0 violations) and isolated two substantive negative constraints (failure of naive closed-neighborhood nu-drop induction; spread of top Betti strand and C5-free sharp graphs at n=6), but no complete proof of the infinite-class target or the nu=2 fallback bound was obtained. The fallback sharpness witness G*=2 disjoint C5s was fully certified (claw-free, nu=2, reg(S/I)=4 over QQ and F_32003 with logged Hochster replay in output/artifacts/witness2xc5.log), satisfying only half of the fallback success criterion. Honest NO_RESULT per scope rules.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No complete proof of the target inequality reg(S/I(G)) <= 2*nu(G) over all claw-free G, nor of the preset fallback universal bound over all claw-free nu=2 graphs; hence neither can be claimed.', 'The certified sharp witness G* = 2xC5 satisfies only the sharpness half of the fallback success criterion; the universal-bound half is missing, so fallback_qualification fails (pass requires proof plus certificate).', 'Exhaustive n=6 census (zero violations) and ~4300-graph random/structured stress are evidence for the target inequality, not a proof; n>=7 exhaustive checks were not completed in-budget.', 'E1 (no-nu-drop obstruction) and E2 (top-strand spread / C5-free sharps) are documented finite-census constraints on proof/shape routes, not standalone theorems with prior-art clearance; not promoted to EMERGENT_FINDING.', 'Characteristic: witness regularity certified over QQ and F_32003 by exact Hochster homology; general-case computations were over F_32003 only, so any future claim must address characteristic-independence explicitly.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No complete proof of the target inequality reg(S/I(G)) <= 2*nu(G) over all claw-free G, nor of the preset fallback universal bound over all claw-free nu=2 graphs; hence neither can be claimed.', 'The certified sharp witness G* = 2xC5 satisfies only the sharpness half of the fallback success criterion; the universal-bound half is missing, so fallback_qualification fails (pass requires proof plus certificate).', 'Exhaustive n=6 census (zero violations) and ~4300-graph random/structured stress a…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
