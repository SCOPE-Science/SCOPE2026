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

# Verification details

Run `python3 verify_border_spectrum.py` with Python 3 and no third-party packages.

The script enumerates all 131,068 binary words for lengths 2 through 16, tests Galois minimality against every nontrivial rotation, and compares exactly the realized proper-border sets with the claimed spectrum. It identifies 8,798 Galois words in that range. It also checks all 12,224 explicitly constructed witness pairs for lengths 2 through 256, including exact length, border coincidence and strict rotation minimality.

The proof, not the finite experiments, establishes every length and every alphabet with at least two ordered symbols. Comparisons with previous literature establish scope but do not certify universal uniqueness of the theorem.
