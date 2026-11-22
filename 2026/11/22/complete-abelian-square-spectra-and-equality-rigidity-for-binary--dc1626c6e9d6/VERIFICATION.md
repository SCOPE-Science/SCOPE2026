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

The proof enumerates all possible contiguous Abelian squares by their number of ones and derives an explicit count. The sharp minimum and equality cases follow by integer inequalities and parity case distinctions for all admissible nonnegative parameters. `verify.py` independently enumerates literal substrings and their actual Abelian-square property, checking 8,820 triples, then checks the predicted equality set for each length from 6 through 300. `verify_output.txt` captures the actual result. Computations are finite corroboration; the proof is all-parameter. This is a self-reviewed mathematical claim; no independent audit has been performed.
