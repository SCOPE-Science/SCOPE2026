# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Simplicial case of the 3D volume conjecture at three interior points: counterexample or proof with delta-vector audit
- **Round:** 2026-09-07-first-light-01
- **Lane:** 124
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Discrete Geometry
- **Method:** simplex-weight decomposition and Hermite-normal-form enumeration with determinant volume and Ehrhart delta-vector verification

## Problem

Resolve the simplicial case of the Zaks-Perles-Wilkes volume conjecture (Conjecture 1.5 of Balletti-Kasprzyk) in dimension 3 at k=3: over the natural scope of all lattice tetrahedra with exactly 3 interior lattice points, decide whether every tetrahedron satisfies Vol(P)<=36*(3+1)=144 with equality only for S^3_3, seeking a certified counterexample or a certified verification, and simultaneously test the associated Ehrhart-coefficient conjectures delta1<=16*3+19=67 and delta2<=19*3+16=73 on this family.

## Attempted claim

Over all lattice tetrahedra T in dimension 3 with exactly 3 interior lattice points, either (A) there exists an explicit tetrahedron with normalized volume >144, disproving Conjecture 1.5 at (d,k)=(3,3), certified by vertex matrix, determinant volume log, lattice-point enumeration proving exactly 3 interior points, and recomputed delta-vector; or (B) every such tetrahedron satisfies Vol(T)<=144 with equality only for the Zaks-Perles-Wilkes simplex S^3_3=conv{(0,0,0),(2,0,0),(0,3,0),(0,0,24)}, certified by the complete weight/HNF enumeration log plus per-case volume and delta-vector recomputation.

## Research outcome

First certified census of 3-interior-point lattice tetrahedra up to normalized volume 144: 741 classes, all satisfying the conjectured Vol/delta bounds with unique maximizer S^3_3; pipeline validated by exact reproduction of the known 225/471 counts at k=1,2. Bounded-range result only; global conjecture left open.

## Why this attempt failed

Failed axes: value.

value: The achieved result is a volume-truncated partial enumeration, not the natural-scope theorem the topic admitted and not the fallback complete census. The admitted scope was ALL 3D tetrahedra with exactly 3 interior points (fixed-interior stratum) with a proof-or-counterexample verdict on Vol<=144 and delta1<=67/delta2<=73; the admitted fallback was the first COMPLETE 3-point-tetrahedron census (exact total count, W(3,3), global maxima/maximizers). What is delivered is 'exactly 741 classes with V<=144', with V>144 explicitly left open (DRAFT sec.6; stage3 killed with no output). Consequences: (a) the volume 'verification' in-range is tautological — every enumerated case satisfies V<=144 by construction of the range, and existence of S^3_3 at V=144 was already the conjectured extremal; the conjecture Vol<=144 for the family remains undecided because a V>144 three-point tetrahedron remains logically possible; (b) the delta verifications d1<=67/d2<=73 are nontrivial in-range (V<=144 permits e.g. d1=100/d2=10) but remain conditional on V<=144, since V=1+d1+d2+3 means any large-V violator would also move d1+d2 — no global delta verdict is established; (c) '741' is an unstable lower bound on the true total, not a citable total — it will grow if any V>144 case exists, so a later worker needs the complete classification, not this truncation; (d) the V<=144 cutoff is the conjecture bound itself, i.e. a conjecture-defined window rather than a natural parameter stratum, closely resembling previously-failed fixed-volume h*-censuses (e.g. hollow/once-punctured tetrahedra at volume 20) and Goldbach-to-N style partial evidence: correct, new, honestly disclosed, but not independently worth finding later as a theorem. Either a genuine V>144 violator or a finiteness-bound-backed complete verification (e.g. sweeping to the explicit AKN nearly-optimal bound) would change the boundary; this artifact does neither. Hence fails the value bar (textbook-method enumeration in a truncated range without boundary-changing verdict).

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Bounded range only (V <= 144): the V in 145..200 violator sweep was started but produced no output before the consolidation deadline, so a large-volume counterexample remains logically possible and no global verdict on Conjectures 1.5/6.1 at k=3 is claimed. Class-completeness depends on the standard triangular-presentation lemma (every tetrahedron has a presentation with acf=V in the superset bounds), which was not machine-checked. One ad-hoc stdlib spot-check of the extremal witness mis-framed…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
