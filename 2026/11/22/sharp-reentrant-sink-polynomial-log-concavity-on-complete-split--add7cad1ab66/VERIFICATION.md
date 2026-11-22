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

# Verification notes

Run `python3 artifacts/verify.py` using Python 3 standard library. It independently enumerates all orientations of each small labelled complete-split graph, computes sinks directly, uses a topological-sort cycle test and compares both resulting polynomials with the exact formulas. Additional integer-only checks verify the necessary-and-sufficient log-concavity inequalities for a parameter grid and the exact reentrant boundaries.

The proof in `RESULT.md`, not these finitely many executions, establishes all assertions for unbounded parameters. The root classification uses explicit derivative and convexity arguments, not numerical root-finding. Failure of finite checks would require scientific reassessment, rather than an inference about the infinite theorem.
