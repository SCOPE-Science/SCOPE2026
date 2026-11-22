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

The accompanying `check.py` was executed using local SymPy and mpmath. It checked the exact scalar identity, both characteristic polynomials and non-Perron root moduli, the small-sequence upper bounds, and direct four-dimensional trajectory consistency on finite iterates of a constructed endpoint example. The infinite monotone-tail fixed point, positive Perron amplitudes, and precise asymptotics require the analytical arguments in `RESULT.md`. Finite computations do not establish those infinite claims by themselves.

The proof uses actual source equations for the four-dimensional map with \(c=1\), \(\epsilon=1\), and \(\eta=-1/2\). The all-positive endpoint initial state is reconstructed from the first three prescribed population terms and the convergent future tail. The claims do not extend to arbitrary initial data or other coupling values.
