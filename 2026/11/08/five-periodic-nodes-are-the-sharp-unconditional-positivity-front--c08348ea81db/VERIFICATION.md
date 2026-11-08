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

The exact rational and symbolic checks were run from the standalone `artifacts/verify_gauss_cycle.py` script with Python 3 and SymPy. Its output, `artifacts/verification.txt`, records 16,391 successful assertions, including the complete rational matrix identities for the three, four and five node cycles and the exact negative six-node witness. The verifier was also replayed from the embedded record on packaging.

The infinite family \(n\ge6\) is not certified by finite enumeration. Its proof is the exact discrete Green function and fixed-dimension spectral expansion in `RESULT.md`. Verification applies to the particular equal-neighbor periodic stencil and the two-stage Gauss–Legendre end-step, not arbitrary numerical schemes or meshes. Independent scientific audit has not been performed.
