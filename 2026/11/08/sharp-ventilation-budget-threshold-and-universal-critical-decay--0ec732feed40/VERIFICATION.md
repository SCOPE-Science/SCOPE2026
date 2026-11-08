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

# Reproducible scientific checks

Execute `python CHECK.py` with Python, SymPy, SciPy and NumPy available. The script checks exact-radical identities, the threshold linearization, the critical asymptotic coefficient, 80 randomized KKT-constrained-optimizer comparisons, and an increasingly long deterministic trajectory from the documented two-hyperedge example. The exact proof is in `RESULT.md`; the computed finite-horizon trajectories provide checks, not a replacement for infinite-time reasoning. Model applicability is limited to the specified smooth concave and homogeneous-host closure; no outside independent review has been performed.
