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

# Verification

Run `python artifacts/verify.py` from the package root with Python 3 and SymPy available. The checker returned `VERIFY_OK` on the actual packaged scientific source before embedding. It independently constructs the Laplacian and squared resolvent, checks rational transition entries of two-, three-, and four-state graphs, confirms conservation and symmetries at exact rational steps, and checks \((T_1(8))_{12}=-440/194481\). For unweighted paths from two through nine vertices, it tests the pseudoinverse formula with exact arithmetic. It checks the leading stiff-limit scalar factor for filter orders one through eight. These tests are finite corroboration. The proof in `RESULT.md`, rather than the finite checks, establishes universal graph-order claims, arbitrary positive steps, and the general-order expansion.

Verification did not include independently commissioned mathematical review, nonlinear diffusions, large-scale numerical PDE tests, or a proof of literature priority.
