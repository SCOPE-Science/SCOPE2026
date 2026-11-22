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

The standalone script `verify.py` uses SymPy for exact matrix inversions and radical identities, and NumPy for installed numerical dependencies. From the folder containing `verify.py` and `requirements.txt`, install the listed packages and run `python verify.py`.

Successful replay output: `VERIFY_OK: 2008 independent exact/numerical checks; bridge and Kemeny asymptotic limits`.

It verifies: the Kirchhoff-index / trace-pseudoinverse identity on 16 heterogeneous rational-weight double stars; all prescribed optimizer row sums; 1,800 feasible randomly weighted asymmetric competitors; monotonicity over integer shapes with up to 64 leaves; 39 balanced fastest-mixing reference allocations; an exact radical factorization of the Kemeny gap; and the analytic leading limits. The finite tests are diagnostic only, not an exhaustive check over infinite parameters or a substitute for the proof. Exact uniqueness is shown by the Cauchy equality case and strict convexity. The independently published SLEM optimum supplies a comparator rather than a new certification channel.

There has been no independent mathematical audit.
