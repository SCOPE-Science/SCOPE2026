# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Triangular versus quadrilateral fibre in dP5
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1801
- **Disposition:** AUDIT_1_REJECT
- **Domain:** symplectic topology
- **Method:** Vianna neck-stretching Maslov-2 hull with lens-space Reeb data and wall-crossing support

## Problem

Let X be the monotone degree-5 del Pezzo (CP^2 blown up at four general points) with its monotone form. Let L_tri be the monotone central fibre of a triangular Vianna almost-toric diagram with one weighted-projective limit orbifold, and let L_quad be the monotone fibre of a quadrilateral almost-toric diagram for X from a different toric degeneration with a non-isomorphic limit orbifold fan and different boundary lens-space data. Are L_tri and L_quad Hamiltonian isotopic in X? A complete answer either constructs a Hamiltonian isotopy or proves Hamiltonian non-isotopy by Vianna-type neck-stretching: rigorously determining the convex hull of Maslov-2 relative homotopy classes in pi_2(X,L) (lens-space Reeb data and relative disk lattice read from the two base diagrams) and showing the two lattices are not carried to each other by any Hamiltonian isotopy, with the Pascaleff-Tonkonog mutated potentials as supporting wall-crossing evidence.

## Attempted claim

Let X be the monotone degree-5 del Pezzo (CP^2 blown up at four general points) with its monotone form. Let L_tri be the monotone central fibre of a triangular Vianna almost-toric diagram with one weighted-projective limit orbifold, and let L_quad be the monotone fibre of a quadrilateral almost-toric diagram for X from a different toric degeneration with a non-isomorphic limit orbifold fan and different boundary lens-space data. Are L_tri and L_quad Hamiltonian isotopic in X? A complete answer either constructs a Hamiltonian isotopy or proves Hamiltonian non-isotopy by Vianna-type neck-stretching: rigorously determining the convex hull of Maslov-2 relative homotopy classes in pi_2(X,L) (lens-space Reeb data and relative disk lattice read from the two base diagrams) and showing the two lattices are not carried to each other by any Hamiltonian isotopy, with the Pascaleff-Tonkonog mutated potentials as supporting wall-crossing evidence.

## Research outcome

Resolved TARGET (non-isotopy horn): explicit triangular vs quadrilateral dP5 limits with Maslov-2 hull areas 10 vs 7 give a GL(2,Z) obstruction to Hamiltonian isotopy.

## Why this attempt failed

Failed axes: correctness.

correctness: Combinatorial data verified by re-running verify_hulls.py: fans complete primitive CCW, dets 4,1,5 and 1,1,2,3, anticanonical degree 5, T-witnesses, hull areas 10 vs 7, (B,I) (8,2) vs (7,1) all reproduce. The geometric core fails: the neck-stretching lemma asserts minimal Maslov-2 boundaries are exactly the fan rays for BOTH triangular and quadrilateral limits, with hull Hamiltonian-invariant up to GL(2,Z). Vianna Theorem 5.1 proves this only for triangular ATBDs, explicitly warning positivity is lost if the limit moment polytope is not a triangle and that non-triangular hulls cannot be described. The draft applies the triangular positivity/Reeb/minimal-orbit argument to a 4-ray limit (H2 rank 2) without addressing self-intersection, extra disk classes, or smoothing/ATF compatibility beyond a rank count, and its supporting wall-crossing sentence is false (algebraic mutation changes Newton polygons beyond GL+translation). The quadrilateral exact-hull identification, on which non-isotopy depends, is therefore unproved.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The neck-stretching invariance lemma assembles published SFT/ATF results (Vianna; Bourgeois-Ekholm-Eliashberg; Pascaleff-Tonkonog) for the two explicit fans rather than reproving transversality from scratch; compatibility/monotonicity of the ATF diagrams with the stated Q-Gorenstein smoothings is used via T-singularity theory and the rank checks, with exact computation covering all combinatorial data.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
