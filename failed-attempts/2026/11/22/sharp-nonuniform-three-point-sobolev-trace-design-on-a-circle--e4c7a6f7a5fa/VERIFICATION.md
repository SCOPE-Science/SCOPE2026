---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Reconstructed the continuous argument in RESULT.md lines 21–63. The distributional second derivative of the mean-zero Bernoulli kernel is 1 minus the point mass, so the norm squared is the largest eigenvalue of its evaluation Gram matrix. Every two-site principal block bounds this below by 1/12 plus the largest absolute correlation. At the candidate threshold s=G(t)=−G(2t), the admissible gaps are [t,2t] and [1−2t,1−t]. Three small gaps sum to at most 6t<1, two large gaps sum to more than 1, and one large plus two small sum to at least 1 with equality only at (t,t,1−2t). Tightening the threshold eliminates this last case. Solving 5t²−3t+1/3=0 gives the stated t; the optimal Gram matrix is (1/12+s)I−s vvᵀ, v=(1,−1,1), so the upper eigenvalue is double and its eigenvectors map through the adjoint to precisely the two-dimensional norming space. Equal gaps give the asserted 1/9. The supplied checker was inspected, not executed; the result does not depend on its finite grid.

## originality

FAIL

There is strong statement-level coverage by the distinct indexed universal three-site circular minimax theorem. It treats the same largest-eigenvalue objective, explicitly includes mean-zero periodic H^s for s>1/2, and fixes the unique gaps by K(d)+K(2d)=0. Setting s=1 gives the record's core. The radical and eigenvalue multiplicity then follow by a quadratic and the rank-one Gram calculation, not by a separate design theorem. This is a decision about coverage, not a claim about which same-day document was first.

## value

FAIL

The nonuniform optimal sampling geometry is mathematically useful, but the submitted narrower claim supplies only a mechanical H¹ specialization of a covering structural theorem. The remaining radical, double eigenvalue and explicit norming plane require only the root equation and elementary matrix algebra, rather than resolving an independent motivated gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
