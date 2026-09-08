# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Honeycomb-boundary flip forcing infinite bitangents: a certified 7-vs-infinite census with real lifts in the quartic honeycomb neighborhood
- **Round:** 2026-09-07-first-light-01
- **Lane:** 115
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Tropical Geometry
- **Method:** secondary-fan flip search with bitangent-shape enumeration and real-lift sign verification

## Problem

Survey the natural secondary-fan window W of all S3-symmetry orbits of regular unimodular triangulations of 4Delta2 at flip-distance at most 2 from the honeycomb triangulation, and for each orbit determine whether the dual smooth plane tropical quartic carries exactly 7 isolated bitangent classes or infinitely many, with Cueto-Markwig 41-type shape labels and per-class real-lift counts, and prove a structural lemma tying a specific honeycomb-boundary flip to the infinite side.

## Attempted claim

There exists an explicit pair of adjacent regular triangulations in W, one the honeycomb triangulation with dual quartic carrying exactly 7 isolated bitangent classes of stated Cueto-Markwig shapes and a certified real-lift vector, and its flip-neighbor whose dual quartic carries infinitely many bitangents, with a proved lemma that this honeycomb-boundary flip forces the infinite family via the effective tropical theta characteristic deformation, each side certified by polymake TropicalQuarticCurves replay logs plus Cueto-Markwig sign computations.

## Research outcome

Certified honeycomb-type base T0 of 4Delta2 (regular unimodular, K4 skeleton core) and its full flip-distance-1 skeleton atlas: 12 neighbours, 10 staying 3-edge-connected and 2 dropping to a 2-edge-cut (no bridges), with 8/12 regularity certificates by exact rational heights; independent stdlib-only replay passes with 0 failures. Bitangent counts, 41-type shapes, real lifts, and the distance-2 census are explicitly out of scope.

## Why this attempt failed

Failed axes: value.

value: Fails independently-worth-finding-later standard despite being correct and narrowly new. The admitted problem required: full S3-orbit window W at flip-distance<=2 from the honeycomb triangulation with per-orbit 7-vs-infinite verdicts, Cueto-Markwig 41-type labels, per-class 0-or-4 real-lift vectors, plus a proved honeycomb-boundary flip-to-infinite lemma (fallback: complete certified atlas with replay logs). The draft delivers none of these: distance-1 only, no distance-2 census, no lemma, no shape labels, no lifts, no bridge/infinite witness (explicit limitation 4: no ec=1 at distance 1). What remains is edge-connectivity of 12 dual graphs around one random K4-core representative whose identity as THE honeycomb triangulation is explicitly disclaimed (limitation 3: honeycomb-type representative, uniqueness not proved; 12 classes are geometric flips with distinct canons, not a certified secondary-fan S3 quotient). A 2-edge-cut is a flexibility indicator, not the infinite-bitangent criterion (which needs a bridge/contracted loop), and the draft correctly refuses to invoke the BLMR black box — leaving an unexplained enumeration of 4V/6E core graphs with a 10/2 split and no reusable bitangent certificate. This is a tiny unmotivated fragment / textbook flip-plus-connectivity computation, not a citable genus-3 benchmark or reusable flip-to-bitangent pipeline, and adds nothing beyond polyDB/secondary-fan data for downstream real-enumerative work.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Flip-distance-1 only: no distance-2 W census, no single-flip-to-infinite lemma, no Cueto-Markwig 41-type labels, no real-lift counts.', 'Regularity certified for 8/12 neighbours; rows 4, 5, 8, 10 have heights null (triangulation/core verified, lifting vector not claimed).', "12 classes are T0's geometric flips with distinct S3-canonical forms, not a certified full-secondary-fan S3 quotient; T0 is a honeycomb-type (K4-core) representative, honeycomb uniqueness not proved.", 'No bridge (ec=1) a…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
