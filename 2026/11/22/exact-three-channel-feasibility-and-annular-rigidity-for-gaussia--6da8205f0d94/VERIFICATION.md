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

# Reproduction and proof boundaries

Run `python3 checker.py` from a directory containing the standalone embedded checker. It uses only Python's standard library and evaluates 147 bounded step masks, including 146 strictly interior \((p,q)\)-moment configurations for which it verifies both exact quadratic gap identities. The reported maximal absolute discrepancy is about \(7.50	imes10^{-16}\), with the symmetric \((p,q)=(1/2,1/2)\) boundary values also checked.

The exact, all-measurable-mask result follows from the signed-linear and signed-quadratic integral identities in `RESULT.md`. Finite numerical checks do not establish an infinite-dimensional optimization theorem. The inverse scalar equation is uniquely solvable by monotonicity, and its endpoints are interpreted by continuity. No independent audit has been performed.
