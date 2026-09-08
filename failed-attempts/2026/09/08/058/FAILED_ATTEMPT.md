# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** First coloured Jones values for the Conway / Kinoshita-Terasaka mutant pair via braid-closure R-matrix
- **Round:** 2026-09-07-first-light-01
- **Lane:** 169
- **Disposition:** NO_RESULT
- **Domain:** Knot Theory
- **Method:** braid-closure quantum R-matrix evaluation of coloured Jones in higher A1 representations

## Problem

Determine the first coloured Jones exact values for the Conway / Kinoshita-Terasaka mutant pair: starting from published braid/PD presentations of K11n34 and K11n42, evaluate the A1 quantum R-matrix in representation n=2 (stretch n=3) to obtain exact J_2 (and attempted J_3) Laurent polynomials in stated unknot-normalisation, with logged transcripts and n=1 reduction checks against tabulated Jones polynomials.

## Attempted claim

Exact coloured Jones polynomials J_2 for K11n34 and K11n42 (both 11 crossings) in unknot-equals-quantum-dimension normalisation, computed by braid-closure R-matrix from published presentations with logged transcripts, with n=1 reduction matching tabulated Jones -q^4+2q^3-2q^2+2q+q^-2-2q^-3+2q^-4-2q^-5+q^-6; stretch goal J_3 for both knots from the same pipeline.

## Research outcome

No exact coloured-Jones J_2 value established for K11n34/K11n42. Verified partial progress: (1) live Atlas gap confirmed (coloured_jones_2..7 = NotAvailable on both K11n34/K11n42 pages; braid words BR[4,{1,1,2,-3,2,1,-3,-2,-2,-3,-3}] and BR[4,{1,-2,3,-2,3,-2,-2,-1,2,-3,-3,2,2}] extracted from katlas.org API wikitext); (2) two independent exact Kauffman-bracket implementations reproduce the tabulated Atlas Jones polynomial exactly for trefoil, K11n34 and K11n42, including computational mutant equality; (3) a planar TL-tangle engine validated (E^2=dE, brute-force agreement); (4) JW-projector J_2 calibration vs Atlas CJ_2(trefoil) failed, so no J_2 value is reported.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Exact J_2 polynomials for K11n34/K11n42 were not obtained; no coloured-Jones value is claimed.', 'Jones-Wenzl cable/projector route calibrated against Atlas CJ_2(trefoil) failed under all tested cable styles, projector placements, and framing shifts; cause unresolved within budget (likely cable-framing/projector-trace convention error, not diagram error, since all bracket terms were triple-verified).', 'U_q(sl2) R-matrix braid-closure route was debugged to a braid-valid representation (braid relation + spectrum verified) but closure/framing normalization never reproduced Atlas Jones for the trefoil; abandoned to avoid an unverified claim.', 'No new mathematical theorem is proved; mutant equality of ordinary Jones reconfirmed computationally only.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Exact J_2 polynomials for K11n34/K11n42 were not obtained; no coloured-Jones value is claimed.', 'Jones-Wenzl cable/projector route calibrated against Atlas CJ_2(trefoil) failed under all tested cable styles, projector placements, and framing shifts; cause unresolved within budget (likely cable-framing/projector-trace convention error, not diagram error, since all bracket terms were triple-verified).', 'U_q(sl2) R-matrix braid-closure route was debugged to a braid-valid representation (braid…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
