# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Inertia dichotomy for non-spin 4-dimensional complete intersections with v_4!=0
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20430
- **Disposition:** NO_RESULT
- **Domain:** Differential Topology
- **Method:** surgery-theoretic bordism and Kreck-Stolz invariant analysis

## Problem

Let X_4(d) be a 4-dimensional complete intersection, regarded as a closed oriented smooth 8-manifold with generator x in H^2(X_4(d);Z) pulled back from CP^infty and Pontryagin integer p_1(4,d) defined by p_1(X_4(d))=p_1(4,d) x^2. Assume v_2(X_4(d))!=0 and v_4(X_4(d))!=0 (equivalently p(d) == 0 mod 4 where p(d) is the number of even degrees), so p_1(4,d) == 3 mod 4. Let Sigma^8_ex be the generator of Theta_8 = Z/2. Prove that the inertia group I(X_4(d)) := {Sigma in Theta_8 | X_4(d)#Sigma is oriented-diffeomorphic to X_4(d)} satisfies I(X_4(d))=0 if p_1(4,d) == 3 mod 8 and I(X_4(d))=Theta_8 if p_1(4,d) == 7 mod 8; equivalently X_4(d)#Sigma^8_ex is diffeomorphic to X_4(d) iff p_1(4,d) == 7 mod 8.

## Attempted claim

Let X_4(d) be a 4-dimensional complete intersection, regarded as a closed oriented smooth 8-manifold with generator x in H^2(X_4(d);Z) pulled back from CP^infty and Pontryagin integer p_1(4,d) defined by p_1(X_4(d))=p_1(4,d) x^2. Assume v_2(X_4(d))!=0 and v_4(X_4(d))!=0 (equivalently p(d) == 0 mod 4 where p(d) is the number of even degrees), so p_1(4,d) == 3 mod 4. Let Sigma^8_ex be the generator of Theta_8 = Z/2. Prove that the inertia group I(X_4(d)) := {Sigma in Theta_8 | X_4(d)#Sigma is oriented-diffeomorphic to X_4(d)} satisfies I(X_4(d))=0 if p_1(4,d) == 3 mod 8 and I(X_4(d))=Theta_8 if p_1(4,d) == 7 mod 8; equivalently X_4(d)#Sigma^8_ex is diffeomorphic to X_4(d) iff p_1(4,d) == 7 mod 8.

## Research outcome

Target blocked: the claimed p1-mod-8 inertia dichotomy is exactly the open Conjecture 1.15 of Crowley-Nagy (GT 2025), whose proof needs an uncarried-out Thom-spectrum computation. Three concrete routes (bordism vanishing, Adams filtration, degree-d normal invariants) were attempted and shown to leave inertia undetermined; no independently valuable finding emerged, so the lane exits cleanly with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The target coincides verbatim with an explicitly open conjecture (Crowley-Nagy Conjecture 1.15); closing it requires a new 2-primary Thom-spectrum computation over CP^4 flagged as future work in the source. Bounded local work (three surgery/bordism routes plus a numeric p1-mod-8 check, script at output/artifacts/p1_check.py) confirmed the block but could not substitute for that missing computation. No emergent or target-adjacent alternative with independent Audit value was found.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The target coincides verbatim with an explicitly open conjecture (Crowley-Nagy Conjecture 1.15); closing it requires a new 2-primary Thom-spectrum computation over CP^4 flagged as future work in the source. Bounded local work (three surgery/bordism routes plus a numeric p1-mod-8 check, script at output/artifacts/p1_check.py) confirmed the block but could not substitute for that missing computation. No emergent or target-adjacent alternative with independent Audit value was found.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
