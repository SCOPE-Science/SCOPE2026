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

Run `python3 verify.py` from the directory containing the files. The script directly enumerates all proper, named three-colourings of \(C_n\) for \(3\le n\le12\), calculates each allowable one-vertex recolouring degree, and compares the complete multiplicity map against the closed binomial-congruence formula. It also checks the known chromatic total, exact edge count and extrema. Expected final line: `CHECKS PASS`.

The unbounded length claim is proved in `RESULT.md` by the signed-increment correspondence, cyclic run compositions and the root-of-unity filter, not by the finite checker. Literature-priority checks were performed against specified accessible sources, with possible unindexed priority and one abstract-only source explicitly retained as limitations. No independent audit or external validation has occurred.
