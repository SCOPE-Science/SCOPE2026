---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The analytic proof uses the Ky Fan diagonal singular-value inequality; normalization \(s_j(A)\le j^{-1/p}\); strict monotonicity of \(k^{1/p-1}\sum_{j=1}^k j^{-1/p}\) by a positive Laplace integral; Fourier-harmonic witnesses; and equality in finite-dimensional trace-norm duality. The quantified theorem is independent of finite numerical tests.

Run `python checker.py` with the requirements in `requirements.txt`. The checker was executed from the working package and reported `FINITE_WEAK_PINCH_OK 22604 checks`. The diagnostic tests span \(1\le r\le n\le12\), exponents \(p\in\{1/2,3/4,1,3/2,2,4\}\), random complex rank-constrained matrices, exact rational harmonic specializations, and 2,000 terms of scalar monotonicity for each of eight positive exponents. The samples cannot establish all exponents, sizes, or equality implications; those follow from the analytical arguments.

The independent audit has not been performed.
