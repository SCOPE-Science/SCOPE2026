# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Logarithmic linear-extension growth for leaf sets in snowflaked binary trees and non-uniform free-space complementation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 714
- **Disposition:** NO_RESULT
- **Domain:** Functional Analysis
- **Method:** linear-extension versus projection duality with metric differentiation and averaging obstruction

## Problem

Determine the growth of the linear Lipschitz-extension constant from the leaf-plus-root subset to the whole snowflaked complete binary tree, and transfer it to non-uniform complementation of the corresponding Lipschitz-free subspace: prove E(S_h,M_h) grows logarithmically in height, hence lambda(F(S_h),F(M_h)) is unbounded, via linear-extension/projection duality with a metric-differentiation averaging obstruction.

## Attempted claim

Let T_h be the rooted complete binary tree of height h>=1 with graph metric rho_h, M_h=(T_h,rho_h^{1/2}), and S_h be its leaf set plus the root with induced metric, Lip0 rooted at the root. Let E_h=inf{||E||: E:Lip0(S_h)->Lip0(M_h) linear, R E=Id} with R the restriction map. Then E_h>=(1/8)log2(h+1) for all h, and by the proved duality E_h=lambda(F(S_h),F(M_h)), so the projection constant of F(S_h) in F(M_h) is unbounded and no uniform complementation holds.

## Research outcome

Target (E_h>=(1/8)log2(h+1) for all h) blocked: doubling induction unproved (signed cancellation, off-subset coarse values), all verified 1-Lipschitz families give O(1), finite checks reach only the trivial regime h<=255. Revealed fallback (every linear extender on (S3,M3) has norm>=2) pursued with a bounded exact check and REFUTED: the zero-extension operator (identity on S3, 0 on interior nodes) is linear with R E0=Id and exact norm sqrt(3)<2, machine-verified. Matching CLEAN_EXIT filed in output/target_exit.json; scripts in output/artifacts/.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No LP/MIP solver in environment (numpy-only), so no exact E_3 extension-constant computation was performed; the fallback refutation is an explicit-operator upper bound, not an exact E_3 value.', 'Only symmetric-ansatz grid search at h=2; no exhaustive h=3 certificate search.', 'E=lambda transfer was cited from admission sources, not re-proved; irrelevant to the outcomes since both quantitative claims failed/closed on direct grounds.', 'h>255 regime of the target unreachable by finite checks in this pass; the target is reported blocked, not disproved.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No LP/MIP solver in environment (numpy-only), so no exact E_3 extension-constant computation was performed; the fallback refutation is an explicit-operator upper bound, not an exact E_3 value.', 'Only symmetric-ansatz grid search at h=2; no exhaustive h=3 certificate search.', 'E=lambda transfer was cited from admission sources, not re-proved; irrelevant to the outcomes since both quantitative claims failed/closed on direct grounds.', 'h>255 regime of the target unreachable by finite checks i…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
