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

The proof constructs the active face explicitly from strictly convex knot values, checks complementarity of the active multipliers, derives its discrete interpolation matrix and a tridiagonal Gram matrix, and evaluates the bulk Green kernel via a second-order recurrence. The exact infinite-spline operator norm follows from knot translation symmetry and convex combinations at nonknot outputs. The finite central-row limit and transition to every convex-regression sample count are analytic, not inferred from a finite sweep.

The packaged `CHECK.py` requires only the Python 3 standard library. Command: `python3 CHECK.py`. A successful replay reports 692 rational and numerical assertions, verifies exact finite projections at multiple sizes, and compares long-grid centered rows with the radical constant. Assertions do not certify the unrestricted global Lipschitz constant; that is bounded below only. No independent mathematical or historical-priority audit was performed.
