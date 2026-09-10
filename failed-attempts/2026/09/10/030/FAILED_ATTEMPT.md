# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Strict comparison versus perforation for a named Toeplitz-over-dyadic-odometer crossed product: a dichotomy lemma with radius 1/8
- **Round:** 2026-09-07-first-light-01
- **Lane:** 579
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Operator Algebras
- **Method:** Elliott-invariant comparison with Cuntz-semigroup tracial approximation and mean-dimension estimates

## Problem

Let X_2 = lim← Z/2^k be the dyadic odometer with adding-machine homeomorphism g_2. Let X_579 be the explicit minimal Toeplitz subshift over alphabet {0,1}^2 whose 2^k-periodic skeleton is X_2 and whose aperiodic holes carry one fixed Villadsen-type readout pattern per block (fully specified at skeleton scale k=3 in the Research brief), with diagonal minimal homeomorphism sigma_579 extending g_2, so 0 < mdim(X_579,sigma_579) <= 1/2. Let A_579 = C(X_579) ⋊_sigma_579 Z (simple, nuclear, stably finite). Decide the comparison dichotomy for A_579 at explicit radius r0 = 1/8.

## Attempted claim

For A_579 = C(X_579) ⋊_sigma_579 Z as defined above, the following dichotomy holds with explicit radius r0 = 1/8: EITHER (comparison horn) rc(A_579) <= 1/8 via Cuntz-semigroup tracial approximation using the odometer-skeleton Rokhlin tower with logged covering number and small-boundary trace estimate, OR (perforation horn) there exist explicit positive contractions a, b in M_2(A_579) with d_tau(a) + 1/8 < d_tau(b) for every tracial state tau but a NOT Cuntz-subequivalent to b (a Villadsen-type perforation witness for A_579).

## Research outcome

Exact preset-fallback Cuntz certificate for the named Toeplitz-odometer cell: norm error 0<1/32 and uniform trace gap 5/8>=1/8, replayable via stdlib scripts; full-target comparison horn (rc=0<=1/8) additionally proved modulo cited comparison theorems.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: fallback qualification materially false. Admission valued tuple as 'certified one-step Cuntz comparison on barely-positive-mdim Toeplitz extension where mdim in (0,1/2] leaves rc undecided, reusable template narrowing regularity'. DRAFT Lemma 5 correctly proves mdim(X_579)=0 via standard finite-alphabet cylinder argument (Widim 0), voiding brief premise 0<mdim<=1/2. Objective finite-alphabet mdim-0 fact was available/misstated at Admission. Consequence: for minimal free Z-systems with mdim 0, rc=0 follows immediately from cited Niu theorem (rc<=1/2 mdim) and classification, and zero-dimensional+minimal+free=>small-boundary=>almost-finite=>Z-stable=>strict comparison is textbook Kerr-Szabo/Rordam chain — regularity already closed, not narrowed. The binary tuple is then trivial projection arithmetic mechanically implied by any clopen 8-tower with equal masses (c^2=(a0-eps)+ cornerwise, gap from 1/8 masses), not a new tracial-approximation template. Object w=[0,1,0,2,3,1,2,*] is arbitrary among many aperiodic words breaking periods 1,2,4; constants (1/16,1/32,1/8) are preset thresholds, not motivated invariants; no future researcher needs this exact pair versus general theorems. This is textbook restatement (mdim-0 rc=0) + arbitrary-scope enumeration + mere parameter substitution, explicitly rejectable under value standard. Certification (FALLBACK_PASS) does not rescue arbitrary object. Exact completion therefore carries no value presumption. Intrinsic low value, not a bounded presentation defect.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Full-target dichotomy organized via comparison horn (rc=0) in DRAFT.md; the universal rc implication relies on cited peer-reviewed theorems (Niu 2022 bound; Kerr-Szabo almost-finiteness/Z-stability chain), not re-proved elementwise. The claimed binary tuple itself is fully self-contained and machine-checked. No perforation witness exists for this cell (strict comparison rules it out). Brief premise 0<mdim corrected to mdim=0 with proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
