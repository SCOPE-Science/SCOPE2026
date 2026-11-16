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

# Verification and reproducibility

The analytical proof reduces the boundary-to-interior zero to a sign change in the real numerator of the rank-one-compressed annular Szegő kernel. The positive- and negative-index Laurent tails are bounded geometrically for the six rational arguments involved. The certificate evaluates \(H_{32}\), \(D_{32}(-3/8)\), and \(D_{32}(-3/4)\) with exact rational arithmetic; every strict inequality is checked rather than inferred from floating-point output.

Execute `python CHECK.py` in the extracted package directory. It uses only Python's standard library and exits without error only after verifying the exact finite-sum signs and remainder margins. The two printed decimals are diagnostic illustrations and are not used to establish the signs.

The proof does not require locating the zero numerically, and the exact uniqueness or position of the zero is not established. The reproducibility checks do not constitute an independent audit or formal certification.
