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

# Reproducibility and limits

Execute `python3 verify_bishop4_quotient.py` from the directory containing this document. Standard Python 3 is the only requirement. No imported repository, external certificates or network are used. The checker exhaustively enumerates faces and flags, checks each group permutation, verifies Burnside fixed-flag counts, performs and checks the free-face collapses, verifies the signed cellular chain condition, computes boundary ranks modulo 2, 3, and 5, and carries out unimodular integer cancellation with a final two-by-three Smith calculation.

The checked finite computation does not establish any statement for larger boards or a complete homotopy type. Full integral homology and simple connectivity are supported by the stated argument. The external independent audit remains not performed.
