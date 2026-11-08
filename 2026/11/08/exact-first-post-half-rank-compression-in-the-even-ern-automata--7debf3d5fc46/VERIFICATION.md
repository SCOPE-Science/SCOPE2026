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

# Reproduction

Run `python3 artifacts/verify.py` with Python 3. The program uses only the standard library. It constructs the actual transition images and computes breadth-first-search minimum word lengths for the first post-half target at even state counts \(6,8,10,12,14,16,18\), obtaining \(12,15,18,21,24,27,30\). Independently, it evaluates the displayed witness for all \(3\le m\le500\), checking both its length and its rank.

Successful output ends in `VERIFY_OK bfs_n=6..18_even witnesses_m=3..500`. The finite computations do not certify the universal quantifier; the full proof is in `RESULT.md`. Independent audit has not been performed.
