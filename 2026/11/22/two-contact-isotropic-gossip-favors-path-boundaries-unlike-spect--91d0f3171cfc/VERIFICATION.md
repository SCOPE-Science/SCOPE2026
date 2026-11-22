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

# Verification record

The standalone standard-library script `verify.py` was executed from the corresponding science directory. Its output was: `PASS: 297 exact assertions for two-contact trace, path optimum and spectral-gap benchmark`.

Checks cover direct exact-rational projected-matrix traces on complete, star, cycle and path networks, independently compared with the line-graph formula; rational tridiagonal inverse systems and positive entries on thirty path sizes; the all-edge optimality equations; the exact four-vertex loss and uniform-sampling deficit; and the weighted path's parabolic Laplacian eigenvector with unit total edge mass. The irrational explicit root is checked against rational solutions at high numerical precision as a consistency test.

These finite tests are not an exhaustive proof of infinitely many sizes. The general projection-trace identity, positive definiteness, tridiagonal recurrence solution, boundary asymptotics, and spectral-gap lower/equality certificate are established analytically in `RESULT.md`. External or independent mathematical validation has not been performed.
