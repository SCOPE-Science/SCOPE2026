# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** F_13 Enriques involution descent at p=13
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1536
- **Disposition:** NO_RESULT
- **Domain:** arithmetic K3-Enriques surfaces
- **Method:** explicit involution equations versus Galois/Brauer descent obstruction

## Problem

Let X0/F_13 be an F_13-model of the supersingular K3 surface of Artin invariant 1, with geometric Neron-Severi lattice of rank 22 and discriminant -13^2. Does X0 admit a fixed-point-free involution iota defined over F_13 whose quotient Y = X0/iota is a smooth Enriques surface over F_13? A complete answer is either explicit equations for iota over F_13 with verification that it is an involution, acts without fixed points, preserves the holomorphic 2-form up to the Enriques sign, and that the quotient has the Enriques lattice and invariants, or an explicit Galois-cohomology/Brauer obstruction proving that although a geometric Enriques involution exists over F_13-bar, no such involution descends to F_13, via the computed Galois action on NS, the discriminant group, and the associated H^1/Br class obstructing rationality of the quotient.

## Attempted claim

Let X0/F_13 be an F_13-model of the supersingular K3 surface of Artin invariant 1, with geometric Neron-Severi lattice of rank 22 and discriminant -13^2. Does X0 admit a fixed-point-free involution iota defined over F_13 whose quotient Y = X0/iota is a smooth Enriques surface over F_13? A complete answer is either explicit equations for iota over F_13 with verification that it is an involution, acts without fixed points, preserves the holomorphic 2-form up to the Enriques sign, and that the quotient has the Enriques lattice and invariants, or an explicit Galois-cohomology/Brauer obstruction proving that although a geometric Enriques involution exists over F_13-bar, no such involution descends to F_13, via the computed Galois action on NS, the discriminant group, and the associated H^1/Br class obstructing rationality of the quotient.

## Research outcome

Target blocked: neither explicit free F_13 Enriques involution nor Galois/Brauer descent obstruction was established; only preliminary Kummer/branch-count evidence exists. Clean exit with obstruction preserved in target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No explicit F_13 involution equations with fixed-point-freeness and Enriques-sign verification were produced, and no Galois action on NS with obstructing H^1/Brauer class was computed. Artifact scripts exp1.py-exp5.py contain only preliminary finite-field counts and sketches; the planned Lieberman-type fixed-point analysis was never executed.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No explicit F_13 involution equations with fixed-point-freeness and Enriques-sign verification were produced, and no Galois action on NS with obstructing H^1/Brauer class was computed. Artifact scripts exp1.py-exp5.py contain only preliminary finite-field counts and sketches; the planned Lieberman-type fixed-point analysis was never executed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
