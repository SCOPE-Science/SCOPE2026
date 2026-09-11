# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Bilinearized Strictness Gap on a Named 6_3 Pair with Matched Linearized Data
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1036
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Contact Topology
- **Method:** Chekanov-Eliashberg DGA with bilinearized homology over augmentation pairs

## Problem

Let G1 and G2 be the two explicit Legendrian fronts of smooth type 6_3 with tb=-1 and r=0 in the research record, each admitting at least two graded Z/2 augmentations with identical linearized contact homology Poincaré polynomials. Determine whether some ordered augmentation pair yields bilinearized Legendrian contact homology of different rank on G1 versus G2, separating the fronts beyond linearized data.

## Attempted claim

For the named 6_3 fronts G1 and G2 with tb=-1, r=0 and identical single-augmentation linearized Poincaré polynomials, there exist ordered graded augmentation pairs (eps1,eps2) on each front such that the Bourgeois-Chantraine bilinearized homology over Z/2 has rank 2 on G1 and rank 0 on G2 in degree 0, proving the fronts are not Legendrian isotopic.

## Research outcome

Disproved the 6_3 bilinearized-gap target: recomputed HOMFLY-PT gives MFW bound tb+|rot|<=-3, so tb=-1,r=0 fronts cannot exist.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: Headline 'no Legendrian 6_3 with tb=-1,r=0' is substantively implied by long-known public data plus a textbook theorem, not a new computation. Katlas 6_3 page lists Maximal Thurston-Bennequin number [-4] and the exact HOMFLY-PT z^4-a^2z^2-z^2a^-2+3z^2-a^2-a^-2+3 with min a-degree -2; the MFW inequality tb+|rot|<=mindeg-1 is a 1980s theorem. Either route (max-tb table lookup tb=-1>-4, or MFW from the known polynomial) mechanically implies impossibility. Independently recomputing the known polynomial with a skein engine is known-database recomputation and does not create originality under STANDARD. value: FAIL with ADMISSION_DEFECT: The admitted worthy negative resolution in topic.audit_preflight was an augmentation-category equivalence proving all ordered-pair bilinearized homologies coincide for existing G1/G2. The submitted negative resolution is a different, cheap classical vacuity: tb=-1 exceeds the known max-tb -4 for 6_3. ADMISSION_DEFECT: topic.audit_preflight target_integrity ('each front is unstabilized 6_3 tb=-1 r=0 admitting >=2 graded augmentations'), triviality_preflight, and cheap_falsification_checks (which predicted classical sanity PASS and 'no destabilization') are all false; Admission audit_alignment repeated the false PASS. Per TARGET policy a negative resolution that is only vacuity / cheap small-instance mismatch / direct table lookup / arbitrary parameter fact fails value even if literally true. No new strictness witness, ledger, or structural rigidity for existing fronts is delivered.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The Morton-Franks-Williams inequality tb+|rot|<=mindeg_v(P)-1 is cited as a published theorem (Morton-Franks-Williams; Fuchs-Tabachnikov exposition), not re-proved here; all downstream inputs (HOMFLY-PT polynomial, degrees, atlas DGA data) are recomputed in-repo with replayable scripts. The disproof addresses the target exactly as stated and does not classify nearby Legendrian pairs admitting bilinearized gaps.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
