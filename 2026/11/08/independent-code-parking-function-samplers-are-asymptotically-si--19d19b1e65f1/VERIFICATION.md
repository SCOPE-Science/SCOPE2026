---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The first k=floor(n/2) factorial-code coordinates always lie <=k, so bulk surplus S_n is a sum of independent indicators from j>k; hence Var_Q(S_n)<=E_Q S_n. For mean <=n^(2/3), Chebyshev gives Q mass 1-o(1) in a window of width n^(5/12), while U mass there vanishes via the atomless weak limit S_n/sqrt(n)=>e(1/2). For mean >n^(2/3), Q mass concentrates above half its mean while U puts o(1) there by tightness. Both bounds uniform in all marginals. Mallows independently generated code is a special case. Small n=3..5 factorial-code surplus enumerations checked independently; finite tests not a substitute for the Brownian limit.

## originality

PASS

Pinsky explicitly posed the full-law TV approximation question; the submission answers it uniformly negatively and in greater generality; no located prior result resolves that same quantification. Best-of-knowledge only.

## value

PASS

Solves a concrete published open question about whether Mallows-generated parking functions can approximate uniform full parking functions, and proves a structural obstruction for the entire independent factorial-code sampler family. Full-law TV distinction is significant even when low-dimensional marginals agree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
