# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Silting-discreteness of cluster-tilted algebras: does representation-finiteness imply silting-discreteness?
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20505
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Representation Theory
- **Method:** Auslander-Reiten and silting-discreteness analysis

## Problem

Let k be algebraically closed and B=End_{C_Q}(T) a cluster-tilted algebra (equivalently B=C \ltimes Ext^2_C(DC,C) for a tilted algebra C). Classify which B are silting-discrete: is every representation-finite (Dynkin-type) cluster-tilted algebra silting-discrete, and are no others? In particular, either prove that B is silting-discrete if and only if B is representation-finite, or exhibit a Dynkin-type (representation-finite) cluster-tilted algebra that is silting-indiscrete and describe the silting-discrete subclass.

## Attempted claim

Let k be algebraically closed and B=End_{C_Q}(T) a cluster-tilted algebra (equivalently B=C \ltimes Ext^2_C(DC,C) for a tilted algebra C). Classify which B are silting-discrete: is every representation-finite (Dynkin-type) cluster-tilted algebra silting-discrete, and are no others? In particular, either prove that B is silting-discrete if and only if B is representation-finite, or exhibit a Dynkin-type (representation-finite) cluster-tilted algebra that is silting-indiscrete and describe the silting-discrete subclass.

## Research outcome

Proved the target equivalence: a cluster-tilted algebra over an algebraically closed field is silting-discrete iff representation-finite (Dynkin type), with type-A via gentle/derived-discrete theory and D/E via derived classification plus mutation criterion.

## Why this attempt failed

Failed axes: correctness.

correctness: Direction (=>) is a valid reduction: silting-discrete implies 2-silting-finite at B, hence tau-finite via AIR/DIJ bijection, hence rep-finite via Zito plus BMR. Direction (<=) is not proved. Type A claims every Dynkin normal form is derived-discrete, but An with t>=2 triangles (e.g. A5 two-triangle, Cartan det 3) has two cycles, infinite global dimension and det !=1, so it is neither gentle one-cycle nor piecewise-hereditary Dynkin and hence not derived-discrete under Vossieck/BGS; clock condition never checked. Types D/E confuse Bastian-Holm-Ladkani good (Brenner-Butler module) mutation connectivity with full iterated irreducible silting-mutation reachability, and assert without evidence that every End(P) stays finite-type hence tau-finite. Computation over GF(7) multiplicity-free boxes is correctly labeled bounded evidence and cannot replace the finiteness argument.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The D/E direction relies on the Bastian-Holm-Ladkani standard forms and good-mutation connectivity plus the Aihara-Mizuno criterion, rather than a from-scratch recomputation of every mutation endomorphism algebra here; type-D classification has minor stated open subtleties that do not affect the finiteness propagation. Computational evidence is a bounded multiplicity-free GF(7) 2-term box, supporting rather than replacing the theoretical argument. Base field is algebraically closed as in the ta…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
