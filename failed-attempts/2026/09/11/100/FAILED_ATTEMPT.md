# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Pair-of-pants excision anomaly after framed skein completion
- **Round:** 2026-09-07-first-light-01
- **Lane:** 955
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Higher Category Theory
- **Method:** collar-gluing excision via relative 2-Deligne tensor product

## Problem

For C=2Vect_{Z/2} with framed skein completion, decide whether the canonical collar-gluing excision 2-functor for the pair of pants decomposed along an embedded cylinder is an equivalence onto the relative 2-Deligne tensor product of the pieces over the cylinder value.

## Attempted claim

After framed skein completion, the canonical pants excision 2-functor for 2Vect_{Z/2} is not an equivalence: a named skein 1-morphism on the pants has Hom-dimension strictly larger than its relative-tensor image, witnessed by an explicit non-invertible anomaly 2-morphism blocking the gluing.

## Research outcome

Disproved the pants excision-anomaly target: proved preservation (excision is an equivalence) for 2Vect_{Z/2} with exact separability, contraction, DW dimension, and pullback certificates.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: claim is preservation/disproof (excision 2-functor is an equivalence after Cauchy completion). verify.py replays VERIFY_OK, but checks only toy linear algebra, not the bicategorical claim. (1) Separability: P=(I+U)/2 split idempotent over Q is correct as 2x2 algebra, but no derivation identifies the cylinder value or its balancing action with Fun(Z/2)=k^2 and this P in the framed skein-completed setting; citation to Decoppet does not supply the quoted commutation theorem. (2) Contraction: N vs C agreement on 64 entries is tautological because A is set to identity delta_{a,z} and B to delta_{z+b,c}, so C=A*B equals N by construction; no actual skein Hom-category or relative 2-Deligne universal property is computed. (3) Dimensions do not prove equivalence: equality of decategorified pants rank 16 and closed genus-2 dim 16 (correct toric-code Verlinde number, though DW formula is misstated as |G|^{2g}/|G|=4^g, off by factor |G|) cannot imply fully faithful + essentially surjective for a k-linear 2-functor; two non-equivalent 2-categories can share ranks. (4) Groupoid pullback cardinality 4=4 does not imply completed 2-functor equivalence; linearization plus Cauchy completion preserving finite pullback is asserted without proof and pentagonator/quasi-inverse coherence is explicitly deferred. Hence essential inferences are unproved: computation is not proof of the headline equivalence. ADMISSION_DEFECT: none identified; preflight nonvacuity assumptions are assumed, not refuted.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Scope is exactly the admitted input (2Vect_{Z/2}, standard framed collar cut, characteristic-zero algebraically closed k); no claim about non-connected or non-separable fusion 2-categories where anomalies may genuinely occur. The disproof kills the literal target witness (strict inequality) exactly; the full bicategorical pentagonator display for the positive equivalence is cited via Decoppet commutation rather than typeset diagram by diagram.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
