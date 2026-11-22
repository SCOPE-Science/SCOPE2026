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

The supplied standalone `check_joint_qfim.py` requires Python 3, NumPy and SymPy. Execute `python check_joint_qfim.py` from the directory containing the script. It rederives the symbolic determinant and derivative, tests the sharp algebraic endpoint identities, and independently evaluates the full two-parameter SLD matrix directly from finite differences and a spectral matrix formula for 60 parameter triples. Twelve optimizer instances are bracketed by bisection. All checks passed in the packaged computation.

The infinite-domain uniqueness, strict brackets and monotonicity follow from the analytic proof in `RESULT.md`, not from finite numerical sampling. The code assumes double-precision arithmetic only in its independent numerical comparisons; the exact identities are checked symbolically. A fixed single-copy measurement is not asserted to realize the entire information matrix. No external scientific review or independent audit is claimed.
