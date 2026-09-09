# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Finite Rokhlin dimension without model-action absorption: an S3-on-O2 boundary test
- **Round:** 2026-09-07-first-light-01
- **Lane:** 358
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Operator Algebras
- **Method:** equivariant K-theory and Elliott-invariant obstruction with tracial Rokhlin-dimension estimates

## Problem

Decide the Rokhlin-dimension vs model-action absorption boundary for one concrete outer action of the smallest nonabelian group S3 on the Kirchberg algebra O2: does finite Rokhlin dimension (without commuting towers) force absorption of the Rokhlin model S3-action, or does equivariant K-theory distinguish a finite-dimensional non-absorbing example?

## Attempted claim

There exists an outer action alpha of S3 on O2 with finite Rokhlin dimension (without commuting towers, dim_Rok(alpha) <= 2) that does not tensorially absorb the Rokhlin model S3-action on O2, as witnessed by a mismatch in the equivariant K-theory (fixed-point K_*) invariant; equivalently, finite Rokhlin dimension does not imply model-action absorption for nonabelian finite groups on Kirchberg algebras.

## Research outcome

The assigned S3-on-O2 finite-dim-vs-absorption boundary collapses positively in the pointwise-outer subclass: Szabo Thm C plus Sec.7 give automatic Rokhlin-dim<=1 and delta-absorption, ruling out the conjectured finite-dimensional non-absorbing example there. Pre-registered fallback (c) achieved as a verified corollary with replayable finite-group input checks.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: strongest headline claim is definitionally anticipated by prior general theorem. Szabo arXiv:1610.05939 proves the claimed absorption and Rokhlin-dimension bound for ALL countable discrete amenable (resp. amenable residually-finite) groups on Kirchberg algebras, which strictly contains the S3-on-O2 instance. DRAFT (1) is Sec.7 instantiated at S3; DRAFT (2) is Theorem C / Theorem 5.5 instantiated with beta=alpha and alpha=delta, where Example 5.6 establishes delta is pointwise-outer and equivariantly O2-absorbing. No new object, invariant, obstruction, tower, or lemma is produced: DRAFT states 'no new analysis claimed' and 'bound comes from Sec.7, not from an ansatz.' Plugging G=S3 into a published all-amenable-groups theorem is a mere parameter substitution / textbook restatement. Admission's assessment that 1610.05939 'does not mechanically imply the Rokhlin-model S3-on-O2 dichotomy' is substantively false on comparison of theorem statements; a failed search or timestamp does not establish priority. The delta-vs-Izumi-Rokhlin-model identification caveat does not create novelty: even relative to Szabo delta the result is prior, and Szabo Introduction/[76] Sec.5 explicitly presents delta/gamma as the finite-group model actions generalizing Izumi/Goldstein-Izumi. value: FAIL: even taken as correct, the S3 instantiation is not independently worth retrieving as a new finding. It records no exact invariant, bound, or lemma beyond what the general theorem already states and a future researcher would find by reading Szabo Thm C + Sec.7. The prompt's narrow-datum allowance requires the object/invariant be motivated before computation, the value not known or mechanically implied, and reasonably needed later; here the S3 values (dim<=1, delta-absorption, no counterexample in pointwise-outer class) are mechanically implied by direct substitution and have been known since v1 2016 / CMP 2018. Certification of trivial finite-group inputs (order 6, amenability, residual finiteness, C*(S3) degrees [1,1,2]) does not rescue an arbitrary instantiation per 'certification alone does not rescue.' This is exactly the reject class: textbook restatement / mere parameter substitution, with admitted 'elementary hypothesis-checking' only. The positive collapse of the conjectured counterexample is useful as a correction of the admission gap analysis, but does not constitute a new publishable boundary update.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Corollary status: relies on cited Szabo theorems (not re-proved). Relative to Szabo model delta; identification with 'Rokhlin model S3-action' via cited uniqueness (Szabo Sec.5/[76] Sec.5, Izumi/Goldstein-Izumi finite-group models), not re-proved. No new equivariant K-theory mismatch claimed (none exists in subclass; K_*(O2)=0 noted). No explicit Rokhlin towers exhibited (bound via Sec.7). Non-pointwise-outer actions untouched.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
