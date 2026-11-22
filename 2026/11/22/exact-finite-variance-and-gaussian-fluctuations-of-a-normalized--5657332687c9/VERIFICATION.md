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

Execute `python3 check_random_fourier.py` in the directory containing this package. It prints a PASS summary only after independent combinatorial construction of the integrated Gaussian fourth-norm polynomial, exact factorial Wick expectations of its first two moments in degrees one through seven, finite Dirichlet additive-energy counts, the exact rational variance simplification, and the two-coefficient beta check. The recorded run passed 46 assertions.

For the infinite sequence, verification is by the mathematical proof: a proper-complex Wick identity, independence of coefficient length from direction, the exact Dirichlet fourth-energy sum, and connected Wick diagrams controlled by a spanning-tree integral bound. Numerical experiments and finite symbolic checks cannot establish the central limit theorem. The argument does not establish a finite-sample normal-approximation rate or extend to arbitrary coefficient laws.
