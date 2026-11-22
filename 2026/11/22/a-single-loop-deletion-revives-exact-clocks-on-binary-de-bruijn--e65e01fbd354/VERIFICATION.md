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

The shipped reproducibility programs are `verify_linear.py` and `verify_states.py`. `verify_linear.py` constructs the arc-deleted adjacency matrices explicitly, validates all power ranks through \(m=7\), and checks exact characteristic polynomials against integer symbolic determinants for \(1\le m\le4\). It relies only on Python and SymPy. `verify_states.py` independently iterates all configurations at \(1\le m\le4\), tests the \(m+2\) return on the recurrent orbit, and counts every entry-time shell; it uses only the Python standard library. Both passed before packaging.

These checks are finite. The infinite-family statements rely on the separate suffix-support, invariant-subspace, and quotient-rank proof in `RESULT.md`; they are not extrapolated from computations. No independent audit was undertaken.
