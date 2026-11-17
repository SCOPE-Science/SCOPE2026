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

# Verification record

The standalone exact Python checker in `checks/verify.py` reconstructs all 519 faces, checks that the full graph automorphism group has 72 elements, computes all signed fixed-face Lefschetz numbers, and verifies the exact mod-two boundary ranks 24, 126, 64, 15. Its recorded stdout is in `checks/output.txt`. An explicit complete character table for all permutations is in `tables/character_table.csv`.

Install the declared dependency in `checks/requirements.txt` and run the checker. Each computation is finite and exhaustive for this specific complex. The rational quotient conclusion follows from averaging the character, not from any claim of integral acyclicity. No external independent verification is claimed.
