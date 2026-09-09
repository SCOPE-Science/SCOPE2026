# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact lattice-width-vs-volume table and certified maximal hollow witness for centrally symmetric 3-polytopes
- **Round:** 2026-09-07-first-light-01
- **Lane:** 341
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** lattice-point enumeration with Ehrhart counting replay and lattice-width direction search

## Problem

For centrally symmetric lattice 3-polytopes over even normalized volumes 4-48, tabulate exact lattice width per volume class with attaining directions and replayed lattice-point/Ehrhart counts, and certify one maximal-volume hollow witness with an explicit empty-interior check plus a width-gap summary.

## Attempted claim

Complete exact lattice-width table for centrally symmetric lattice 3-polytopes for each even normalized volume 4,6,...,48: for each volume class give minimum and maximum attained width, an explicit vertex matrix attaining each extremum, the exact width value with attaining primitive functional and exhaustive direction-search bound, and replayed lattice-point count plus Ehrhart vector; plus one explicit maximal-volume hollow witness in this window with an empty-interior certificate and a width-gap summary table.

## Research outcome

Attained-width-1 hollow table for centrally symmetric lattice 3-polytopes over all even volumes 4-48: 23 explicit vertex matrices (two twisted-prism families) with exact volume/symmetry/width-1/hollow certificates and replayed Ehrhart dilate counts, independently replayed by a stdlib verifier (VERIFY_OK). The per-volume maximum-width side of the original target is explicitly left open.

## Why this attempt failed

Failed axes: value.

value: Judging the strongest self-contained headline separately from the admittedly unfinished max-side survey (DRAFT Sec.3 disclaims maxima and global hollow maximality): the delivered headline is 'minimum attained width is 1 at each even V=4..48 via explicit slab prisms, all hollow, with L(0..3) rows.' This fails the exact-invariant clause. The value 1 is the universal lower bound for any full-dimensional lattice polytope (w>=1) and the upper bound is an elementary slab construction conv(Tx0 union (-T)x1) / quadrilateral twist with parameters (b,h)/k varied to hit volumes -- a textbook exercise and mere parameter substitution, not a sought invariant whose value was unknown. Width 1 implies hollow automatically (no integer plane strictly inside 0<=z<=1), so the 'hollow witness' adds nothing; P48 is only the largest member of its own table, not a maximal hollow body in any literature sense. The L(0..3) counts for these ad hoc witnesses had no pre-computation motivation and no plausible future retrieval need: flatness-constant calibration needs large-width hollow maxima, not width-1 minima; no downstream use, gap, or classification needs these specific dilate numbers. The 4-48 cutoff is arbitrary (all 0-mod-4 T plus 2-mod-4 Q extend indefinitely by the same formulas). Certification (exact fan sums, bbox enumerations) is real but per instructions does not rescue an arbitrary object or unexplained numbers. The missing substantive result (per-volume maxima / obstruction certificates / true maximal hollow witness) cannot be supplied by a bounded interpretive addition; it would require beginning the max-side classification. Hence intrinsic low value: textbook restatement + parameter substitution + unexplained enumeration. FAIL.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Attained-minimum (width-1) side only: no per-volume maximum-width witnesses, no obstruction/classification certificates, and no completeness claim over the class. Width exactness rests on the elementary slab/full-dimension argument with the B=8 search as corroboration. Ehrhart data are dilate counts L(0..3), not full h*-vectors. Central symmetry allows half-integer centers (standard convention), explicitly committed per row.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
