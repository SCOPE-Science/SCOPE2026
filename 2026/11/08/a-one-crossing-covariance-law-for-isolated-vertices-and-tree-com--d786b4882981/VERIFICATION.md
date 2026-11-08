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

# Reproducibility and limitations

Run `python3 verify.py` using Python's standard library. The checker enumerates all graphs with 3 through 6 vertices by edge count, comparing independently computed empirical covariances against the exact formula. It also checks the algebraic cross-product identity and the monotonicity of the entire feasible sign sequence for 4 through 34 vertices. The recorded execution completed with `CHECK_OK 41472`.

The general claims are established by the finite-edge conditioning argument and the cross-product factorization in `RESULT.md`, not by the finite computations. Originality comparison remains incomplete for the full 1990 tree-census paper; no independent audit has been performed.
