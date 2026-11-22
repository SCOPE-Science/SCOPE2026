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

Run `python VERIFY.py` with Python 3 and no third-party dependencies. The accompanying `VERIFY_OUTPUT.txt` contains the actual successful run. The program enumerates the full 551-face 25-vertex test complex, including the empty face; checks 320 signed Lefschetz equalities; computes boundary ranks over a prime field; and compares six independently computed homology-character triples with the exact representation formulas. These are finite checks only. The infinite-family integral theorem is justified by the natural short exact chain sequence in `RESULT.md`, not by numerical extrapolation. No external or independent audit is asserted.
