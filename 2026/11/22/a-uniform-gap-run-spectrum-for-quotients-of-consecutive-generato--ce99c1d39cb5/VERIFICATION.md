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

# Verification

Run `python3 CHECK.py` using Python 3 (standard library only). It directly verifies every target integer through a safety tail beyond the claimed Frobenius bound for each of 975 pairs \((p,k)\), where \(2\le p\le40\), \(1\le k\le25\). The independent criterion reduces a two-generator membership test to one modular residue. The program checks the number, position and length of every maximal missing-number run, and the exact genus and Frobenius number. It passes on 246,675 enumerated maximal missing-number runs.

The proof for all \(p,k\) is mathematical, not computational: fixed-coin-number intervals have explicit integer endpoints, and their consecutive endpoint differences provide a complete partition of the positive-length gap blocks. The test does not establish the infinite quantifiers by itself. The literature originality assessment has residual risks and no independent mathematical review has occurred.
