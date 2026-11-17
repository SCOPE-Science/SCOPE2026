---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The exact Gaussian and first-Hermite centered ambiguity factors are exp(-s/2) and exp(-s/2)(1-s). Consequently the squared two-channel singular value is exp(-s)[1+a s(s-2)] on 0<=s<=T, whose essential infimum equals its continuous minimum, including boundary by annular localization. Differentiating gives exp(-s)[-1+a(2-(s-2)^2)]; for a>1/2 its interior minimum decreases strictly in a while the boundary value increases strictly for T>2. Their unique crossing proves all stated minimax phases including plateau a∈[0,1/2] at T=2, with T→∞ asymptotics. The proof is correct for this precise *linear* multipler, not full nonlinear phase retrieval.

## originality

FAIL

The 2026-10-25 earlier published theorem Sharp diskwise ambiguity conditioning for the first two Hermite windows has IDENTICAL h0,h1 and identical normalized disk multiplier, optimal weight phases, all equality cases, implicit optimizer, and the squared margin improvement (T-1)^2; original x=2-u reparametrizes its root equation exactly. Hence the entire submitted final claim is a direct restatement/corollary of the stronger earlier result.

## value

FAIL

The model is a motivated stability design question, but this complete precise answer had already been published; repackaging its formulas, equal-active-minimum argument, and leading asymptotics offers no new mathematically useful fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
