# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact Gordian distance between the Conway and Kinoshita-Terasaka mutants via determinant-neighborhood and Floer lower bounds with a logged crossing-change path
- **Round:** 2026-09-07-first-light-01
- **Lane:** 231
- **Disposition:** NO_RESULT
- **Domain:** Low-Dimensional Topology
- **Method:** determinant-1-neighborhood crossing-change obstruction with knot Floer tau / Rasmussen s profiles plus explicit logged crossing-change path search

## Problem

Fix the Jones-equal mutant pair K11n34 (Conway) and K11n42 (Kinoshita-Terasaka) by frozen DT codes and planar diagrams. Determine their exact Gordian (crossing-change) distance d_G(K11n34, K11n42): prove a lower bound d>=2 by a determinant-1-neighborhood obstruction (Wright/Lickorish type: no single crossing change carries one to the other, certified by exact determinant lists over all one-crossing neighbors) corroborated by knot Floer tau / Rasmussen s profiles, and exhibit an explicit logged <=2-step crossing-change path through a named intermediate diagram, hence d=2. All diagrams, neighbor-determinant lists, and path coordinates replayable offline from the frozen DT codes.

## Attempted claim

d_G(K11n34, K11n42) = 2: (a) no single crossing change converts a minimal diagram of one into the other, proved by disjoint determinant-1-neighborhood lists (exact integer lists for all 11 one-crossing neighbors of each diagram) plus tau/s incompatibility; (b) an explicit logged 2-step crossing-change path K11n34 -> J -> K11n42 with frozen intermediate diagram J and crossing coordinates, each step verified by diagram isomorphism.

## Research outcome

Attempted exact Gordian distance d_G(K11n34 Conway, K11n42 Kinoshita-Terasaka). The admitted determinant-neighbourhood route provably cannot separate the pair: dual-verified exact computation (Gauss/Fox-colouring + independent PD cross-check, output/artifacts/det_neighbors.py, pd_crosscheck.py, results.json) shows both frozen diagrams have det 1 and IDENTICAL one-crossing-change neighbour-determinant multisets {1,15,15,17,17,27,33,33,39,53,59}. Tau/s corroboration is vacuous (s=tau=0 both). Corrected envelope: both knots have u=1 (KnotAtlas), so d_G<=2 via the unknot and the topic's '{2,3}' fallback pin is arithmetically impossible; distinct 3-genera (3 vs 2) give d>=1, leaving d in {1,2} open. No CLAIMED distance; verification-critical scripts archived.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['The admitted d>=2 determinant-1-neighbourhood obstruction failed as designed: the two neighbour-determinant multisets coincide exactly ({1,15,15,17,17,27,33,33,39,53,59}), so determinant neighbourhoods cannot exclude a 1-step conversion for this pair.', 'No verified 1-step crossing-change path and no alternative d>=2 obstruction (tau/s, genus, signature, Alexander/Jones/HOMFLY all coincide or vanish) was established in-lane; the d=1-vs-2 question remains open.', 'The archived neighbour-determinant lists are diagram-relative (frozen KnotAtlas Gauss/PD codes); a different choice of minimal diagram could in principle give different lists, so they certify a diagram-level fact, not a knot-type invariant.', 'Unknotting-number and genus values used for the d<=2 envelope and distinctness are cited from the live KnotAtlas pages (which agree with KnotInfo), not recomputed in-lane; the recomputed artifacts are the determinants and neighbour lists only.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['The admitted d>=2 determinant-1-neighbourhood obstruction failed as designed: the two neighbour-determinant multisets coincide exactly ({1,15,15,17,17,27,33,33,39,53,59}), so determinant neighbourhoods cannot exclude a 1-step conversion for this pair.', 'No verified 1-step crossing-change path and no alternative d>=2 obstruction (tau/s, genus, signature, Alexander/Jones/HOMFLY all coincide or vanish) was established in-lane; the d=1-vs-2 question remains open.', 'The archived neighbour-determ…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
