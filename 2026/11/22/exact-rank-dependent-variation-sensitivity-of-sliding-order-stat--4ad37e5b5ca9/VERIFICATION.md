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

# Reproducibility and scope

Execute `python3 CHECKER.py` with Python 3 and no third-party packages. The script uses exact integer rank selection for all constructive witnesses and all exhaustively enumerated small permutations; the arbitrarily small witness perturbation is represented by a rational quarter-step. Seeded integer pairs provide independent numerical examples of the two-input inequality.

The relevant analytical checks are the deletion/insertion monotonicity of the right-side count among the bottom \(q\), the one-way comparison of left/right order-statistic thresholds on constant-count blocks, and the explicit rank-permutation color pattern. All are established in the proof, not inferred from finite tests. The checker runs radius \(1\) through \(64\), all ranks, permutation checks through seven sample sites, and \(3000\) two-input stress cases.

Limitations: no external independent review, no claims for cyclic or differently weighted geometry, and historical priority remains qualified by less accessible early filter literature.
