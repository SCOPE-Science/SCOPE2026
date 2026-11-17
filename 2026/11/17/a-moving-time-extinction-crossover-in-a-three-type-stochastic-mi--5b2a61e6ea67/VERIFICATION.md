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

# Reproducibility and limits

Run `python3 check.py` with SymPy and mpmath installed. The checker asserts the three-coordinate simplex identity, the exact derived recurrence, and the third-coordinate multiplicative identity, and tests finite tuned-parameter trajectories at 500-digit precision. The executed checker printed `symbolic transition and barycentric identities PASS`, `moving parameter checks PASS`, and `fixed positive mixing ratio checks PASS`.

The proof of the infinite-time and moving-time statements is the exact recurrence, a geometric product bound for fixed mixing, the explicit logarithmic deviation estimate for vanishing mixing, and a fixed-offset induction. Numerical agreement does not prove limits or global novelty. The complete tested code is embedded as `check.py`. This package does not contain a formalized proof or independent mathematical audit.
