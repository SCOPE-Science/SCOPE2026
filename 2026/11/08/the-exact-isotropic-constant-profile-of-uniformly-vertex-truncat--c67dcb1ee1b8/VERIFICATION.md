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

# Verification of the truncation theorem

The self-contained `check_truncation.py` uses SciPy convex-hull boundary triangulations only for geometric decomposition. It evaluates every cone-simplex determinant and centered second moment using rational arithmetic through SymPy and Python fractions. Twelve combinations (dimensions \(2,3,4\), fractional cuts \(1/5,1/3,2/5,1/2\)) contribute 330 nonzero cells. Independent cell integrations match both closed formulas exactly, and three low-dimensional derivative polynomial identities are verified symbolically.

Reproduce with `python check_truncation.py`, in an environment providing NumPy, SciPy, and SymPy. The successful observed marker is `SIMPLEX_TRUNCATION_EXACT_CHECKS_PASSED 12 330 3`.

**Limits:** The geometric hull triangulator uses floating arithmetic to choose facets, but all integral values of chosen simplices are computed exactly and checked against the analytic formulas. The computation is finite. The general, all-dimensional theorem is justified by the cap decomposition and the derivative sign argument in `RESULT.md`; no independent audit or formal machine proof is claimed.
