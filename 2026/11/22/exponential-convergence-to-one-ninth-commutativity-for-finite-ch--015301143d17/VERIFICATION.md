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

The theorem is established by the explicit forest component count and an independent-set bound for commuting-translation constraints, not by finite enumeration.

Run `python3 verify.py` with the Python standard library. The program exhaustively constructs every order-preserving partial isometry on sets of sizes one through nine and counts commuting ordered pairs, the partial-identity subset, and each one-idempotent commuting-rank fiber. It compares its results to every finite-size identity claimed in `RESULT.md` and prints `VERIFY_OK_ODP_COMMUTING` on success. Its output is saved in `verification_output.txt`.

The verifier is finite and does not test the infinite asymptotic conclusion; the latter follows from a uniform, explicitly proved large-displacement tail bound and a bounded-degree dependency graph for short displacements. The numerical convergence exponent is a proved upper-bound exponent, not a claim of asymptotic optimality.

Self-review: passed. Independent audit: not yet performed.
