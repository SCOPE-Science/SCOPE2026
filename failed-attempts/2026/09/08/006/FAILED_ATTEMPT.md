# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** From-scratch subgroup-lattice census for six explicit semidirect-product permutation groups of orders 24, 28, 30, 33, 35, 36 with class-equation and coset-action certificates
- **Round:** 2026-09-07-first-light-01
- **Lane:** 69
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Finite Group Theory
- **Method:** generator-closure subgroup enumeration with conjugacy-class reduction and coset-action verification replay

## Problem

Fix six explicit permutation presentations: G24=S4 as V4⋊S3 with N=< (1 2)(3 4), (1 3)(2 4) > and H=< (1 2 3), (1 2) > fixing 4 (order 24, non-nilpotent); G28=D28 dihedral of order 28 as C14⋊C2 with r=(1 2 3 4 5 6 7 8 9 10 11 12 13 14), s with s^2=1 and s*r*s=r^-1 (order 28); G30=S3×C5 with a=(1 2 3), b=(1 2), c=(4 5 6 7 8) disjoint and [a,c]=[b,c]=1 (order 30); G33=C33=< x=(1..33) > cyclic (order 33); G35=C35=< y=(1..35) > cyclic (order 35); G36=S3×S3 with a1=(1 2 3), b1=(1 2), a2=(4 5 6), b2=(4 5) on disjoint supports (order 36, non-nilpotent). From these generators only, by generator-closure enumeration without computer-algebra black boxes, compute for each Gi: (i) full subgroup count |Sub(Gi)|, (ii) normal-subgroup count, (iii) conjugacy classes of subgroups with sizes, (iv) conjugacy classes of elements and verified class equation, (v) derived series and derived length plus nilpotency/solvability verdict. For one non-nilpotent extremal witness (G24=S4) additionally publish the complete Hasse inclusion log (every cover relation with generating witnesses), an explicit normality-failure certificate (H<G, g with gHg^-1 != H exhibited as permutation inequality), and a coset-action replay (for a chosen core-free or known-core H, the action on cosets as explicit homomorphism into S_n with kernel equal to the computed core).

## Attempted claim

Per-order tables for all six Gi giving |Sub|, |Normal|, subgroup-conjugacy-class sizes, element-conjugacy-class sizes with class equation summing to |Gi|, derived length and nilpotency verdict — e.g. |Sub(S4)|=30 with 4 normal subgroups (1, V4, A4, S4), class equation 1+3+6+6+8=24, derived length 3 (S4 > A4 > V4 > 1); dihedral/Frobenius counts for G28/G30; cyclic divisor-lattice counts for G33 (4 subgroups) and G35 (4 subgroups); and full S3×S3 lattice for G36 — plus for G24 the complete Hasse log, an explicit gHg^-1 != H certificate, and a coset-action homomorphism table whose kernel equals the independently computed core, all reproducible from the stated permutations.

## Research outcome

Complete from-scratch subgroup-lattice census for the six fixed presentations with class-equation and coset-action certificates; primary script and independent verifier both pass with hard asserts on every check.

## Why this attempt failed

Failed axes: value.

value: Even taking correctness and narrow novelty as given, the result is not independently worth finding later. It is a textbook restatement + mere parameter substitution + unexplained enumeration: S4 30 subgroups with 4 normals and 1+3+6+6+8 class equation is classical textbook knowledge (DRAFT Sec.5 admits this); D28 counts follow from textbook tau+sigma formula; C33/C35 4-subgroup divisor lattices are trivial exercises; S3xC5 12 subgroups / 6 normals follow immediately from coprime direct-product decomposition (6x2); S3xS3 60-subgroup lattice is a seconds-scale brute-force/GAP exercise with no new structure, conjecture, or method advance. Hasse log, normality-failure triple, and coset-action table are automatically generated consequences of the same brute force, not independent insights. Orders were chosen as a fixed parametric sweep (24,28,30,33,35,36) contrasting cyclic/dihedral/product cases without motivating a question that needs this joint table; nilpotency/solvability verdicts use standard Sylow-uniqueness and derived-series-to-1 checks. Reusable route is 'brute-force generator closure sized to tiny orders' with no complexity claim. Prior SCOPE-FAIL-20260907-014 was REJECTed on value for a larger extremal census over 231 groups of order 96; a fortiori a six-tiny-group census with two trivial cyclic cases fails the value gate. Fallback to orders 24,30,36 does not repair this.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Covers only the six stated presentations, not all groups of orders 24-36; the S4 count (30 subgroups) is classical, the contribution is the joint auditable census plus Hasse/coset certificates; brute-force generator-closure sized to these orders with no larger-scale complexity claim; nilpotency verdicts rely on the finite-group Sylow-uniqueness criterion.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
