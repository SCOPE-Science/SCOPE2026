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

Run `python3 verify.py` with NumPy installed. All transforms use signed 64-bit integers; none use approximate floating-point arithmetic. The test compares two separately generated combinatorial families, evaluates all binary Fourier multipliers at orders three through seven, validates the exact 19 weight-three zeros and full Hamming-weight zero counts at order seven, and checks the complete range-projector numerator via a second integer butterfly and a Walsh involution test. The finite exhaustive computation proves the explicitly stated rank and norm when the simple encoding and Walsh butterfly identities are accepted. The translation-averaging optimality argument is presented in RESULT.md. No claim of independent mathematical review is made.
