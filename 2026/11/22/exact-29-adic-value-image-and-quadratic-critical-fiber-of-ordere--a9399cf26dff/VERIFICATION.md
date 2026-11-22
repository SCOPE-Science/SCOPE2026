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

# Reproduction and limitations

Run `python3 check_fubini29.py` with Python 3. It computes exact residues by the Stirling recurrence, checks all 28 finite-difference rows, confirms the normalized nondegenerate branch and its center modulo \(29^3\), and enumerates all output multiplicities for the first three exponents. Its reported period and image counts are 28/17, 812/465, and 23548/13471. The script has no external packages. The proof of the infinitely many levels uses the bounded 29-adic moment measure, unit-derivative inverse function theorem, and one-variable 29-adic quadratic normal form; finite enumeration does not certify them in isolation.
