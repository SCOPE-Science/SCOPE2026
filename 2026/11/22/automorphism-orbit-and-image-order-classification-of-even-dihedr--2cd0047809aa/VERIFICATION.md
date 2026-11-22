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

The full proof consists of an exhaustive generator-pair analysis, CRT reduction of idempotent residues, and a direct formula for the automorphism-conjugacy action. The finite checker `verify_dihedral.py` constructs the complete finite group for each even rotation order from 4 to 32, independently enumerates all presentation-compatible endomorphisms, tests composition idempotence by evaluating the images of the two generators, and compares exact pairs, image orders, and full automorphism orbits with the statement. All fifteen tested cases passed; raw output is in `verify_output.txt`.

The checker is standard-library Python and requires no external data or packages. Run `python verify_dihedral.py` in the directory containing the two verification artifacts. It does not establish correctness beyond the finite tested range and it does not certify novelty. Literature coverage and any uninspected historical priority remain separate limitations.
