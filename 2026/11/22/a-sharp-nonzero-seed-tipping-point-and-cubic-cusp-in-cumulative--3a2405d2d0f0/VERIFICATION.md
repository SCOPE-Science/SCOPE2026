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

The analytical proof is in `RESULT.md`; its crucial identity is \(H'(z)=H(z)q(z)/(1-z)\), with \(q(z)=B-1+(A-B)z-Az^2\). The positive-root discriminant and endpoint signs give the globally exhaustive branch classification.

Run `python verify.py` in Python 3 with SciPy. The checker performs exact rational arithmetic for two-fold and three-fold roots, numerical derivative tests, two-sided branch inversion, signed cubic-root scaling, and independent integration of the original three-state ODE at seeds on both sides of the threshold. For the benchmark \(B=1/2\), \(A=3\), the first crossing jumps from \(1/3\) to approximately \(0.574237376735705\). For the cusp benchmark \(B=3/4\), \(A=9/4\), the certified coefficient in the theorem is approximately \(0.9713135232363942\).

Finite numerical tests corroborate examples but do not certify the universal statement; the latter follows analytically from the quadratic turning-point argument, first-crossing selection, and Taylor expansions. No stochastic network equivalence, empirical validity, or independent audit is claimed.
