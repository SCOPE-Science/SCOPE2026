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

# Exact verification and limitations

Run `python3 VERIFY.py` in an ordinary Python 3 environment; no third-party dependencies are used. The script checks all three local monomial matrices, each primitive tensor product of Jordan blocks of lengths two or three, every cubic-zero matrix among all \(3^9\) three-by-three matrices over \(\mathbb F_3\), and all canonical Jordan types through dimension five. The verified three-dimensional conjugacy counts are 1, 104, and 624, with induced ranks 0, 12, and 16. The successful terminal line is `TRUNCATED_SYMMETRIC_JORDAN_RIGIDITY_VERIFIED`.

All finite calculations use exact arithmetic modulo three, with monomial bases and row operations explicitly implemented. Since those fixed matrices have entries in the prime field, their rank holds over every field of characteristic three. The unbounded-dimension assertion is **not** an experimental extrapolation: it follows from the displayed exact Green-ring tensor identities and block decomposition. The finite test does not verify unrestricted nonlinear derivations, does not test every dimension, and does not constitute independent mathematical validation.
