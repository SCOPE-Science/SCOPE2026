# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** h*-unimodality breakdown for lattice pyramids over polygon bases: dip witness or sharp dip bound with width certificate
- **Round:** 2026-09-07-first-light-01
- **Lane:** 308
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** three-dimensional lattice-point Ehrhart enumeration with regular-triangulation h* computation and Ehrhart-series cross-check

## Problem

Over the de novo generated family F of lattice 3-pyramids Pyr(Q,h) with polygon bases Q from a committed bounding box (unimodular normal-form dedup, small interior points) and committed apex heights h, decide the h*-unimodality breakdown: either exhibit an explicit pyramid with certified non-unimodal h* (h1*>h2*) with dual-route Ehrhart certificate and lattice-width witness, or certify that all of F is unimodal and exhibit the sharp maximal-dip extremal with its width certificate.

## Attempted claim

An explicit lattice 3-pyramid over a small-interior-point polygon base with certified non-unimodal Ehrhart h* (h1*>h2*), proved by agreeing lattice-point Ehrhart counts and regular-triangulation h* computation, together with its lattice width certified by a primitive-direction witness and gap over the runner-up dip in the search window.

## Research outcome

Dual-route certified census of 2992 de novo box-generated lattice 3-pyramids: first explicit non-unimodal witnesses (unit-triangle bases, h*=(1,0,m,0) for h=2,3,4; 9 placements) plus sharp dip bound max(h1*-h2*)=9 at the 3x3-square height-1 pyramid with runner-up gap 2; every case width-1 with logged primitive witness.

## Why this attempt failed

Failed axes: originality, value.

originality: Theorem A (first explicit non-unimodal pyramid witnesses, h*=(1,0,1,0),(1,0,2,0),(1,0,3,0)) is a textbook restatement. The auditor exact integer search proves each witness pyramid is unimodularly (GL(3,Z) plus translation) equivalent to the classical Reeve tetrahedron T_h=conv{(0,0,0),(1,0,0),(0,1,0),(1,1,h)} of Reeve 1957: h=2 via U=[[0,-1,0],[1,1,1],[0,0,1]], h=3 via U=[[1,0,0],[0,-1,0],[0,-3,-1]], h=4 via U=[[1,0,0],[0,-1,0],[0,-4,-1]], each determinant +-1 and verified to map vertex sets onto each other. The invariant h*(T_h)=(1,0,h-1,0) is the standard textbook Ehrhart example (Beck-Robins Computing the Continuous Discretely; Betke-McMullen theory), the canonical dimension-3 non-unimodal family with 1>0<m pattern. Hence both the object up to the only equivalence that matters in Ehrhart theory and the number are known and mechanically implied, not a first witness. Narrow window-scoping (over this box window, apex at (0,0,h), translation placements) does not create priority: unimodular equivalence erases those distinctions, and a timestamp or failed keyword search does not establish priority over a 1957 textbook object. The cited nearest priors (Haase-Schicho 2D triples, Batyrev-Nill degree 1, Castryck-Cools width, Braun-Davis-Solus and Payne high-dimensional thresholds) are correctly distinguished, but the decisive nearest prior, the Reeve tetrahedra, was missed, and it substantively anticipates Theorem A. Originality therefore FAILS; per policy this is never repairable. value: Judging the strongest headline separately: Theorem A, the only candidate for an independently retrievable exact invariant of a natural object, is the known h*-vector of the Reeve tetrahedron, already available in textbooks, so its value was known and mechanically implied before computation and the exact-invariant clause does not save it. Theorem B (max h1*-h2*=9 at the 3x3-square height-1 pyramid, runner-up 7, gap 2, histogram over 2992 pyramids in box [0,3]^2, triangles and quadrilaterals only, h=1..4) is an unexplained enumeration over an arbitrary committed window: no reason is given why [0,3]^2 rather than any other box, why only triangles and quadrilaterals, or why h<=4; the number 9 has no mathematical interpretation, no general criterion, and no downstream use. The width corollary (extremal and witnesses all have width 1) is trivial, since width 1 is the absolute minimum and the generic value, and it tests no width-versus-unimodality interaction. The package is therefore textbook restatement plus arbitrary-slice enumeration, explicitly excluded even when correct and new. Value FAILS.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Window-bound claim only (box [0,3]^2, tri/quad bases, h=1..4); no infinite-family theorem. No regular-triangulation third route; certification is two independent count routes plus volume/Pick identities. Stanley nonnegativity machine-checked in-window, not re-proved. Witness minimality beyond the window not claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
