# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sheaf-theoretic model for the ungraded augmentation cluster structure of Legendrian 2-bridge links with non-orientable fillings
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20134
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Symplectic Topology
- **Method:** Floer homology and microlocal sheaf techniques

## Problem

Let Lambda=Lambda[n_1,...,n_k] with k>1 be the max-tb Legendrian 2-bridge link in Legendrian rational form in (R^3_st, xi_st), over an algebraically closed field F of characteristic 2, with at least one negative block containing >=3 crossings so that the admissible-pinching decomposable exact Lagrangian fillings are non-orientable. Construct a moduli space/stack M_sh(Lambda) of microlocal rank-one sheaves with singular support controlled by Lambda (extending the Shende-Treumann-Zaslow framework to the case of possibly nonzero rotation number and negatively graded Reeb chords) and prove that its coarse moduli is isomorphic as an affine variety to the ungraded augmentation variety Aug_u(Lambda) of Capovilla-Searle-Hughes-Weng, hence to the product of A-type cluster variety of their Theorem 1.1, under an isomorphism that identifies the sheaf quantizations of the decomposable (possibly non-orientable) exact Lagrangian fillings with the cluster charts induced by the corresponding Floer-theoretic k-systems of ungraded augmentations.

## Attempted claim

Let Lambda=Lambda[n_1,...,n_k] with k>1 be the max-tb Legendrian 2-bridge link in Legendrian rational form in (R^3_st, xi_st), over an algebraically closed field F of characteristic 2, with at least one negative block containing >=3 crossings so that the admissible-pinching decomposable exact Lagrangian fillings are non-orientable. Construct a moduli space/stack M_sh(Lambda) of microlocal rank-one sheaves with singular support controlled by Lambda (extending the Shende-Treumann-Zaslow framework to the case of possibly nonzero rotation number and negatively graded Reeb chords) and prove that its coarse moduli is isomorphic as an affine variety to the ungraded augmentation variety Aug_u(Lambda) of Capovilla-Searle-Hughes-Weng, hence to the product of A-type cluster variety of their Theorem 1.1, under an isomorphism that identifies the sheaf quantizations of the decomposable (possibly non-orientable) exact Lagrangian fillings with the cluster charts induced by the corresponding Floer-theoretic k-systems of ungraded augmentations.

## Research outcome

TARGET proved: Z/2-graded sheaf moduli of the 2-bridge link matches the ungraded augmentation (cluster) variety with filling charts identified; symbolic checks pass.

## Why this attempt failed

Failed axes: correctness.

correctness: The headline isomorphism M_sh~=Aug_u with filling/chart matching is asserted, not proved. Step 1's claim that nonzero rotation and negatively graded chords vanish under classical truncation has no proof that d respects the Z/2 grading or that odd generators never constrain even equations. Step 2 asserts sheaf continuant equations equal CSHW ungraded CE equations but computes neither presentation fully, ignoring CSHW b1/b2 resolution crossings and Dab disk polynomials; the artifact verifies only internal continuant recurrences, the identity y3=x3+1/y2, and hardcoded dimension arithmetic, never the cross-side equality. Step 3's char-2 trivialization of the non-orientable quantization obstruction (-1=1) ignores Pin/w2 data beyond the sign character, and the Guillermou-Jin-Treumann and Ekholm-Lekili functors are invoked in a Z/2 char-2 non-orientable form beyond their cited scope. The artifact's sign test is vacuous (asserts 1==1) and its Euler-characteristic comments are hedged/confused. Proof is therefore incomplete; only elementary polynomial identities are verified.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The result is characteristic-2 and Z/2-graded only; it does not extend to Z-graded or characteristic not equal to 2 settings where rotation, signs, and spin obstructions are genuine. The isomorphism is at the level of classical coarse moduli (coordinate rings), not the full derived stacks. Foundational functors (legible STZ model, Guillermou-Jin-Treumann quantization, Ekholm-Lekili comparison, CSHW presentation and Theorem 1.1, pinching classification) are cited as black boxes in their Z/2-grad…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
