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

# Reproduction and limits

Run `python3 verify.py` using Python 3.9 or later. The script is self-contained and uses only `fractions.Fraction` and the standard library. Expected output is exactly `VERIFY_OK 522`.

The checker reconstructs the grounded Laplacian for non-symmetric edge weights on each blade and computes the rational Kirchhoff index from exact matrix inversion. It tests the proposed spectral trace identity, rational interior optima with exact ratio \(z/x=2\), the boundary and price-exclusion regime, and 360 independently generated full-budget asymmetric allocations. The entire analytic proof for all \(m,r\ge2\) is in `RESULT.md`; finite verification is a consistency check, not an exhaustive proof of the infinite statement, and does not establish priority or independent certification.
