# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Irreducible degree-4 edge residue for the quintic at generic weights
- **Round:** 2026-09-07-first-light-01
- **Lane:** 988
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Geometry
- **Method:** Atiyah-Bott virtual localization edge residue on stable-map moduli

## Problem

Let Mbar_0,0(P4,4) carry the diagonal torus action with weights lambda=(lambda0,...,lambda4). Consider torus-fixed stable maps with smooth domain P1 mapping as a degree-4 cover fully ramified over an ordered pair of fixed points (pi,pj), i different from j, with no contracted components and automorphism group mu4. For each ordered pair define the quintic-twisted contribution Eij=(1/4)*eT(H0(C,f*O(5)))/eT(Nvir_ij) and the partial sum Sirred(lambda)=sum_{i!=j} Eij(lambda). Evaluate at lambda*=(0,1,2,3,4).

## Attempted claim

With torus weights lambda*=(0,1,2,3,4), each Eij is regular at lambda* and the summed irreducible-edge quintic contribution satisfies Sirred(lambda*)=17281/384. The equality is exact over Q with the stated 1/4 orbifold normalization and includes the full H0(C,f*O(5)) Euler numerator of rank 21.

## Research outcome

Disproved the irreducible degree-4 edge target: E04 and E40 have double poles at (0,1,2,3,4) with exact leading coefficient -391091500800000, so the claimed regular value 17281/384 is false as stated.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: Admission triviality_preflight and target_integrity passed denominator nonvanishing and regularity, but exact census shows lambda*=(0,1,2,3,4) is inadmissible for virtual localization (D1 weights m-k vanish on extremal edges). The negative resolution therefore exposes only a type/normalization cheap defect: evaluation at a non-generic one-parameter subgroup where eT(Nvir)=0, not a finite corrected edge contribution. Per TARGET policy such a negative fails value even if literally false. The exact K=-391091500800000 is a pole coefficient at a singular point that was not motivated before computation, has no stated regularized/subtraction scheme, does not treat reducible graphs, and cannot be imported as the debugged degree-4 cover template envisioned (future work will avoid this non-generic integer weight). It is an arbitrary singular-parameter fact plus certification, which per STANDARD does not create value. No bounded topic-preserving addition can supply generic regularity or downstream use without changing weights or beginning a new regularization direction, so value fails and is not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The disproof uses the standard Graber-Pandharipande smooth-edge weight convention named in the audit plan; it does not evaluate any regularized or residue-subtracted variant of Sirred, does not treat reducible nodal graphs, and does not decide the true regularized value of the irreducible sector under a repaired summation scheme.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
