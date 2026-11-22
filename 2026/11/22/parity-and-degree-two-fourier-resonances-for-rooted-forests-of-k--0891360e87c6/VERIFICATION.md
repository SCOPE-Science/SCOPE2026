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

# Verification notes

Run `python3 checks/check_rooted_forest.py` with Python 3. The program constructs the counting kernel without relying on the matrix-forest determinant, then checks its complete integer Walsh transform against the four-type formula for widths one through five. The checks cover 1364 coefficients, including the 1360 coefficients in the asserted range two through five. It prints the exact ranks and zero counts and terminates on any discrepancy.

Symbolic checks in the proof establish the matrix-forest formula, four-type determinant elimination, mod-two nonvanishing for every even width, explicit zeros at every odd width, and all one- and two-edge cases. The finite checks do not certify unbounded widths independently. The first public date refers to the archival matrix-forest source, not a publication date for this result. No external audit has been performed.
