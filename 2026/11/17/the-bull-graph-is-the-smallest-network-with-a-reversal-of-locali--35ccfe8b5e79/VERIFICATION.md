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

# Verification record
The complete proof appears in RESULT.md. The reproducible exact arithmetic check is `python verify.py`, requiring SymPy and NetworkX, with mpmath for a displayed high-precision root. It reconstructs exact orthogonal projectors, ten connected graph isomorphism types through four vertices, the seven strictly positive degree-class differences, and all five bull spectral projector coefficients including the zero mode.

The boundary \(t=0\) is equality for every vertex input. The initial derivative difference is strictly negative for the bull comparison and the slowest asymptotic spectral weight is strictly positive. A monotone transformed derivative proves a unique positive crossing for **all** times: the numerical root by itself is not the proof.

The theorem is limited to combinatorial-Laplacian deterministic linear consensus with equally sized vertex impulses and squared Euclidean error. No independent validation or external certification has been performed.
