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

The theorem is proved by explicit Walsh block transforms, first-two-one-bit sign classification, finite cylinder counts, and geometric sums. The executable checker `check.py` runs without nonstandard Python packages. It independently computes exact Walsh–Hadamard transforms for orders \(2^n\) with \(1\leq n\leq12\), tests the sign boundary up to bit \(84\), and compares closed and independently counted formulas through \(n=60\). All comparisons use integers or exact rational arithmetic.

These computations cannot replace the analytic proof for arbitrary integer \(n\). The 2026 motivating paper was not available as full text; originality remains subject to further bibliographic inspection. An independent mathematical audit has not been performed.
