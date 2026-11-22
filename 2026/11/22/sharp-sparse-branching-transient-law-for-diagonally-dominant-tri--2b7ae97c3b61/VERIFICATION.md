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

# Reproducible checks and limits

Run `python verify.py` with Python 3.9 or later. The program uses only the standard library and compares the exact claimed maximum number of depth-\(k\) descendants with exhaustive enumeration of chronological parent forests at small dimensions. It verifies the \(7\)-vertex binary construction using exact rational arithmetic and checks finite-dimension threshold arithmetic. It does not purport to enumerate continuous row-simplex matrices or prove the all-dimension result; those require the analytic argument in `RESULT.md`.

The proof's critical nonstandard steps are the separate-affinity of a strictly triangular matrix power with respect to an individual row, the consequent row-simplex extremal reduction without new support, and the exact minimum-size bound \(S_{d,k}(m)\) for a branching tree with \(m\) depth-\(k\) descendants. All statements refer to exact arithmetic. The finding has undergone a self-review; independent audit has not been performed.
