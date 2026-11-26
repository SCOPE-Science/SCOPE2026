---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Condition on the delivered indices. The conditional mean is the chord on each surviving gap of length L, and integrated conditional variance is L²/6. In the original-gap coordinates d_i=t_{i+1}−t_i (i=0,…,n), two gap pieces i,j belong to the same surviving interval iff all |i−j| intervening samples fail. Thus 6R=dᵀA d with A_ij=(1−p)^|i−j|. This also verifies the frozen ordered-site quadratic. The all-delivered term gives strict convexity. With q=1−p, the inverse of A is tridiagonal with end diagonals 1, interior diagonals 1+q² and neighboring entries −q, all divided by 1−q² (direct multiplication, also for n=1 and q=0). Consequently A⁻¹1 is proportional to (1,p,…,p,1), the normalized vector lies in the strict simplex interior, and 6R_min=1/(1ᵀA⁻¹1)=(2−p)/(2+(n−1)p). This yields the claimed times, uniqueness, endpoint and asymptotic statements. Repeated times add no bridge information conditional on the delivered values; zero gaps are allowed under the per-index model. Even interpreting duplicates as one common site-delivery indicator does not improve a coincident design: independent attempts at that site weakly increase the chance of acquiring its value, and even that per-index design is strictly worse than the distinct optimum. A fresh exact-rational mask check gave 56 risk and gradient assertions for n=1,…,7 and four probabilities; replay with python3 /workspace/branches/f20efe93-6320-4ae1-a122-3f47c3179813/independent_mask_check.py. The frozen checker was inspected, not executed. The finite checks are supplementary.

## originality

PASS

Within the sources inspected, the proved distinct claim is the full-path integrated posterior MSE optimum and sharp risk for a fixed, finite grid with homogeneous independent erasures. Neither Gaussian interpolation itself nor equal spacing without erasures is credited as new. The geometric matrix inverse is classical; the erasure-aware path loss and optimal design, not a new matrix identity, are the contribution.

## value

PASS

Full-path posterior error under missing exact data is a natural distinct loss. The finite-budget optimum tells how far to hold samples from the known endpoints, how the adjacent gaps shrink relative to those margins as p decreases, and the exact residual risk. It supplies a useful analytical benchmark without claiming applicability to general kernels or deployment policies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
