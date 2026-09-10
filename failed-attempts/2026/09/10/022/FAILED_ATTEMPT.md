# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact radius of comparison 1/2 for a self-similar Villadsen first-type limit over (S^2)^n with 2+1 diagonal maps
- **Round:** 2026-09-07-first-light-01
- **Lane:** 551
- **Disposition:** NO_RESULT
- **Domain:** Operator Algebras
- **Method:** Elliott-invariant classification with Cuntz-semigroup comparison and nuclear-dimension tracial estimates

## Problem

Let V* be the Villadsen first-type diagonal system with A_i=M_{m_i}(C(X_i)), X_i=(S^2)^{n_i}, n_1=3, m_1=6, n_{i+1}=3n_i, m_{i+1}=3m_i, and connecting maps phi_i diagonal with 2 coordinate-projection pullbacks (first two n_i-blocks of (S^2)^{3n_i}) plus 1 point-evaluation at a fixed basepoint, with standard density so the limit is simple with unique trace. Determine its radius of comparison: prove rc(V*)=1/2 via a certified vector-bundle perforation pair with Chern/Euler logs, deciding this self-similar dim/rank-1 cell of the Toms-Winter regularity program.

## Attempted claim

For the named simple unique-trace Villadsen first-type limit V* defined above (A_i=M_{m_i}(C((S^2)^{n_i})), n_1=3, m_1=6, tripling dimensions and matrix sizes, 2 coordinate-projection plus 1 point-evaluation maps), the radius of comparison is exactly rc(V*)=1/2, witnessed by the stage-2 rank-(5,10) Euler-class perforation pair for the lower bound and a matching dim/(2m) upper-bound argument from the constant dimension-rank ratio dim(X_i)/m_i=1.

## Research outcome

Target rc(V*)=1/2 and exact preset fallback rc(V*)>=1/4 both unproven. Verified 5/18+1/4=19/36<20/36=10/18 arithmetic, but the literal stage-2 Euler non-embedding lemma is false (machine-checked Chern-ring: no vanishing failure; stable-range trivialization gives P2 ≾ Q2), and the only obstructing repair washes by stage 3. Honest NO_RESULT with auditable negative certificate in output/artifacts/verify.py and output/WORKLOG.md.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Literal fallback Euler obstruction fails: verified c(E)^{-1} = 1-s1+s2-s3 has max k=3 <= 5, so no Chern/Euler contradiction; E (+) G (dual Hopf lines) is stably trivial of rank 8 over the 6-dimensional base hence trivial by complex stable range, so P2 is MvN-subequivalent to Q2 in A2.', 'Tensor-line repair obstructs at stage 2 (s^6 coeff 720 != 0) but washes by stage 3 (12 coords vs complement rank 15, s^16 = 0); fixed stage-2 pair cannot witness limit rc without stage-growing persistence argument.', 'Upper-bound argument to exact rc=1/2 (dim/(2m) comparison estimate in limit) not closed within remaining time.', 'No new long computations started per checkpoint; no CLAIMED route established.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Literal fallback Euler obstruction fails: verified c(E)^{-1} = 1-s1+s2-s3 has max k=3 <= 5, so no Chern/Euler contradiction; E (+) G (dual Hopf lines) is stably trivial of rank 8 over the 6-dimensional base hence trivial by complex stable range, so P2 is MvN-subequivalent to Q2 in A2.', 'Tensor-line repair obstructs at stage 2 (s^6 coeff 720 != 0) but washes by stage 3 (12 coords vs complement rank 15, s^16 = 0); fixed stage-2 pair cannot witness limit rc without stage-growing persistence arg…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
