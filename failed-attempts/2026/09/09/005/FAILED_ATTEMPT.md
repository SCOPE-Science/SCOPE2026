# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Complete lattice-width classification with sharp symmetric flatness bound over centrally symmetric reflexive 3-polytopes
- **Round:** 2026-09-07-first-light-01
- **Lane:** 282
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** closed-family filter from Kreuzer-Skarke census plus primitive-direction width enumeration with determinant-triangulation cross-check

## Problem

Over the closed family F of all GL(3,Z)-equivalence classes of centrally symmetric reflexive lattice 3-polytopes, obtained by exact symmetry-plus-reflexivity filtering of the fixed 4319 Kreuzer-Skarke census with equivalence deduplication, compute exact lattice width w(P) for every class by primitive-direction enumeration with facet-normal completeness certificates, and establish the sharp family bound W*=max_{P in F} w(P) with attaining class, attaining primitive direction, and integer runner-up gap, stratified by normalized volume and lattice-point signature.

## Attempted claim

Complete lattice-width classification over the closed centrally symmetric reflexive 3-polytope family F with facet-normal completeness certificates, establishing the sharp bound W*=max_F w attained at an explicit class with primitive direction and explicit integer gap over the runner-up width.

## Research outcome

Uniform lattice width 2 over the closed family of centrally symmetric reflexive 3-polytopes: general elementary lemma (any dimension) plus a complete replayable census certificate — exactly 13 GL(3,Z)-classes from the 4319-list symmetry filter, each with attaining direction, two-method determinant volumes, point counts, and dual width-2 direction-pair counts (VERIFY_OK).

## Why this attempt failed

Failed axes: value.

value: Intrinsic low value: textbook restatement plus mechanical database slice, even though correct and new. The sharp bound W*=2 with gap 0 is a 3-line corollary of standard definitions requiring no census: any facet normal attains 2 and symmetry forces >=2. Runner-up gap 0 means no non-trivial flatness boundary; Blanco-Santos precedent is disanalogous (non-trivial 74/2 distribution requiring enumeration vs degenerate uniform 2 provable without enumeration). Census table adds no substantive invariant a future researcher needs to retrieve: normalized volumes and point counts are bare KS/GRDB invariants recomputed to identical numbers; attaining directions are trivial (any facet normal); w2-pair counts (dual boundary lattice points mod sign, 3..13) had no pre-existing demand, motivate no flatness/hollow/Ehrhart question, and support no downstream theorem — an unexplained enumeration. Motivation (flatness/hollow/Mahler programs) collapses because lemma alone settles the width question in seconds; the 13 KS numbers are obtainable by a seconds-long V=-V filter anyone with the public list can run. Exact-invariant protection does not apply because the value IS mechanically implied by definitions and certification alone (VERIFY_OK, two triangulations) does not rescue a trivial invariant per standard. No bounded addition (motivation paragraph, literature pointer) can make uniform trivial width non-trivial; defect is intrinsic, not presentational.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The sharp bound W*=2 itself follows from a 3-line general proof (facet-distance-1 plus central symmetry) and is presented as an elementary lemma, not as new deep mathematics; computational novelty is limited to the completeness certificate, stratified table, and per-class width-2 direction census. The 13 GL-distinctness relies on the KS list being one-per-class plus invariant separation and exhaustive triple-correspondence search among same-nv pairs (no full canonical-form certification). No co…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
