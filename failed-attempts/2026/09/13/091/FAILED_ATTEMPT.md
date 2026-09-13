# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Displaceability energy of degree-1 monotone fibre
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1655
- **Disposition:** AUDIT_2_REJECT
- **Domain:** symplectic topology
- **Method:** symplectic probe versus pearl Floer lower bound

## Problem

Let X1 be a smooth monotone del Pezzo surface of degree 1 (CP^2 blown up at 8 points in general position) with monotone symplectic form normalized so a line in CP^2 has area 3 and each exceptional divisor has area 1. Let T0 be the monotone almost-toric fibre at the monotone barycentre of a fixed triangular almost-toric base diagram of X1. Prove or disprove: T0 is Hamiltonian displaceable in X1 with displacement energy e(T0) <= 1 (in these units, i.e. at most the area of one exceptional divisor). A complete answer either exhibits an explicit Hamiltonian isotopy displacing T0 with Hofer energy at most 1 (e.g. via a toric symplectic probe / extraordinary probe of controlled affine length) or proves a rigorous lower bound e(T0) > 1 or nondisplaceability via a nonvanishing pearl-complex Floer class, deciding displaceability and the stated energy bound.

## Attempted claim

Let X1 be a smooth monotone del Pezzo surface of degree 1 (CP^2 blown up at 8 points in general position) with monotone symplectic form normalized so a line in CP^2 has area 3 and each exceptional divisor has area 1. Let T0 be the monotone almost-toric fibre at the monotone barycentre of a fixed triangular almost-toric base diagram of X1. Prove or disprove: T0 is Hamiltonian displaceable in X1 with displacement energy e(T0) <= 1 (in these units, i.e. at most the area of one exceptional divisor). A complete answer either exhibits an explicit Hamiltonian isotopy displacing T0 with Hofer energy at most 1 (e.g. via a toric symplectic probe / extraordinary probe of controlled affine length) or proves a rigorous lower bound e(T0) > 1 or nondisplaceability via a nonvanishing pearl-complex Floer class, deciding displaceability and the stated energy bound.

## Research outcome

Repaired TARGET disproof: degree-1 monotone fibre T0 is nondisplaceable (e=+infinity>1) via mutation-plus-blowup-tracked nondegenerate critical point and pearl-model Floer nonvanishing.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route (claim_route=TARGET): draft claims proved nondisplaceability e=+inf. Machine checks reproduced (W0/W' grads/Hessians, Markov (2,3,6)/(1,5,5) enumeration, 18-term balanced-hull det 36963). But headline depends on explicit unproved hypothesis (H-mono): true endpoint W_T0 has nondegenerate positive-real critical point. Only the unit-count model (all n_beta=1) is verified; true open-GW coefficients are admitted uncomputed. Openness/support-disjointness cannot create existence of a critical point nor its nondegeneracy without the true coefficients. One-step cluster demo does not cover 8 blowup term-adding steps. Sheridan/FOOO criterion therefore has no verified antecedent. This is evidence plus cited theorems with a load-bearing gap, not a proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Single explicit residual hypothesis (H-mono): invertibility of the log-Hessian of the true endpoint W_T0 at its positive-real critical point (open, checkable, shown exactly satisfiable on this Newton triangle). Full enumeration of true open-GW coefficients n_beta not attempted. Probe non-exhibition is consistency only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
