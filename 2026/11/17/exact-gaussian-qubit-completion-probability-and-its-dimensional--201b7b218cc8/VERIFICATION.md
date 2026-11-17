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

## Reproducibility and checks
The complete argument is in `RESULT.md`. The 2-by-2 proof reduces the event to a determinant condition, uses Haar-unitary angular independence, integrates the exact eigenvalue ratio density, and verifies the final rational partial fraction decomposition. The high-dimensional zero-probability conclusion uses a necessary off-diagonal equation and absolute continuity, not sampling. `CHECKER.py` contains a standalone Python standard-library check of these identities and a seeded simulation of original complex Ginibre pairs. These are diagnostic checks, not an infinite proof or independent validation.

## Scope of verification
The mathematical proof is conditional on the established positive-completion criteria quoted from Tian's arXiv:2611.03081v1, Theorems 4.1 and 5.1. The source's determinant and positive-moment decomposition were inspected. Full independent validation and publication priority remain unperformed; the cited source does not provide the exact Gaussian probability.
