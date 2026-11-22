---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Independently formed the exact 9×9 real Hermitian-lift analysis matrix of rank-one Weyl measurement projectors and symbolic determinant, reproducing -5832(s-1)^6(s+1)^2(2s+1)^2(s²+2). Deleting row (0,0), the supplied explicit symmetric H_s spans its kernel when full A is invertible; direct symbolic multiplication A[1:,:]H_s-coordinate vector gives exactly zero and det(H_s)=-(s²+s+1)^4 q(s) with q=2s^4+2s³+5s²+6s+3=2(s²+s/2)^2+(9/2)(s+2/3)^2+1>0. A one-dimensional erased projector kernel therefore has no Hermitian rank≤2 obstruction to pure-state phase retrieval. Weyl conjugation transfers the result to all nine missing points. At exceptional real s, full A ranks 3/7/7, giving real kernel dimension≥2; an odd determinant on a circle in this kernel forces a nonzero singular Hermitian obstruction or an unspanned measurement system. Any seven intensities likewise yield a ≥2-dimensional Hermitian kernel, proving the universal lower bound. This is exact algebra, not a finite-parameter extrapolation.

## originality

PASS

A directly related earlier published exact one-coordinate Gabor projector-rank result already characterizes the full 9-vector span for g=(s,1,1), equivalent up to cyclic shift, and thus covers the exceptional full-tomography ranks; that component is NOT counted as new. However full informational completeness alone does not imply one-erasure pure-state phase retrieval. The explicit full-rank H_s kernel after any erasure and universal exact 8-threshold are distinct; neither the inspected earlier full rank theorem nor the primary Gabor sufficiency results state that conclusion.

## value

PASS

Exact single-erasure robustness for a small canonical Gabor orbit and critical two-tap s=0 window, together with sharp eight-observation global phase-retrieval threshold and complete exceptional parameter phase diagram; this isolates a natural tomography distinction not captured by full-orbit informational completeness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
