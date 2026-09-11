# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Central-sequence characters versus Z-stability in a threshold fast-growth Villadsen second-type limit
- **Round:** 2026-09-07-first-light-01
- **Lane:** 746
- **Disposition:** NO_RESULT
- **Domain:** Operator Algebras
- **Method:** Central-sequence character construction with Elliott-invariant classification and Cuntz-semigroup radius-of-comparison estimates

## Problem

Decide Jiang-Su stability for one explicit threshold (fast-growth, non-slow-growth) Villadsen second-type diagonal AH limit W_fast: A_1=M_4(C((S^2)^3)) with dim(X_1)=6, m_1=4; X_{i+1}=X_i^{t_i} x (S^2) with t_i=2^{i+1} (4,8,16,...); phi_i = t_i coordinate projections plus one Villadsen second-type S^2 Euler-class bundle embedding plus s_i=1 point evaluation; m_{i+1}=m_i*(t_i+2); dim_{i+1}=t_i*dim_i+2; point-evaluation fraction 1/(t_i+2)->0 so the limit is simple with unique trace tau; rho_i=dim_i/m_i decreases to rho_inf>=1/2 (finite-product floor), hence W_fast provably lacks slow dimension growth and has positive mean dimension. Either construct an explicit character chi: F(W_fast)->C on the central sequence algebra (certifying non-Z-stability), or certify a positive radius-of-comparison floor.

## Attempted claim

The threshold Villadsen second-type diagonal limit W_fast defined in problem_statement (seed (S^2)^3, t_i=2^{i+1), unique trace, rho_inf>=1/2, no slow dimension growth) admits an explicit character chi: F(W_fast)->C on its central sequence algebra built from the logged point-evaluation subsequence, and hence W_fast is not Jiang-Su stable.

## Research outcome

CLEAN_EXIT: TARGET blocked by a structural representation-theoretic no-go (no unital *-homomorphism from any matrix corner M_k(C(Y)), k>=24, or from A_2=M_24(C(X_2)) to C, so the designed point-cone evaluation is the zero map, not a character); preset fallback binary test also fails (trace-gap arithmetic verifies as 1/6 but the Euler obstruction sits over the wrong base and limit persistence plus tail-distortion budget never closed). No original increment; see output/target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Stage/rho arithmetic replays (verify.py VERIFY_OK) but proves no theorem about W_fast; the M_n no-character lemma is textbook; the Chern sketch is unverified and over the wrong base; Cuntz persistence and the <1/24 distortion budget were never closed.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Stage/rho arithmetic replays (verify.py VERIFY_OK) but proves no theorem about W_fast; the M_n no-character lemma is textbook; the Chern sketch is unverified and over the wrong base; Cuntz persistence and the <1/24 distortion budget were never closed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
