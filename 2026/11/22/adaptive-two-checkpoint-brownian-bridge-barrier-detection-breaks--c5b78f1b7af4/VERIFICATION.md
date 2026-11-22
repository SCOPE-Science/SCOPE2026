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

The analytic proof in `RESULT.md` establishes the conditional one-query optimum, the measurable optimal second-query policy, the exact success functional, its one-sided derivatives, and existence of mirrored off-center global optimizers for all strictly positive endpoint clearances.

`verification.py` is executable with the Python 3 standard library and was run from the packaged contents. It independently computes finite-grid one-query comparisons and numerical quadrature for five positive endpoint levels, checks exact midpoint symmetry and the gamma-function slope, and verifies one strict numerical improvement. These finite checks do not establish universal inequalities without the analytic argument.

The conditional sampling law presumes a Brownian bridge with known positive pinned endpoints, no measurement error and retrospective access to times on either side of an existing observation. Global uniqueness of the off-center first-sampling optimum is neither proved nor claimed. The named prior-paper comparison is historical-priority evidence, not an independent mathematical audit.
