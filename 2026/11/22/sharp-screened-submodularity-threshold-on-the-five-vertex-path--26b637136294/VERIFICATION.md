---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The four-term F submodularity slack is J(S)+J(S+ef)−J(S+e)−J(S+f), with common 1/μ terms cancelling and positive product denominator. Independently constructed all 64 characteristic polynomials using traces of Laplacian powers and Newton identities, rather than the supplied Leibniz code. Over all 240 unordered pair/base-set tests, the numerator is the asserted exceptional factorization once, identically zero 29 times, and strictly positive on μ≥5/4 by nonnegative shifted coefficients and positive constant 210 times. The least such constant after multiplying by 4^15 was 2607034601472000. The quartic changes sign between 5/4 and 13/10 and has exactly one positive root by Descartes' rule. Its numerator has the quartic's sign for μ>0, including equality at the root. At zero screening p′(0)/p(0) is the pseudoinverse trace; on the {24} witness the four traces are 8/3, 41/20, 41/20, 146/105, giving slack −3/70. Replay: python3 /workspace/evidence/p5_newton.py. The supplied script was inspected, not run.

## originality

PASS

Credit the existing unscreened edge-addition counterexample, not priority for that example. The supported distinct claim is the exact positive-screening iff threshold on all six candidate edges and its strictness classification. Retrieved comparisons concern unscreened edge coherence or a genuinely different vertex-set objective, and do not imply the quartic, its global threshold role, or the equality counts.

## value

PASS

P5 is a named counterexample to an edge-design submodularity guarantee, not an arbitrary tiny graph. The complete lattice restoration threshold answers exactly how much uniform screening repairs that failure, including a different obstruction at μ=0 and exact strictness. A pointwise test or the old counterexample cannot answer this interval question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
