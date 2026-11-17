---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Setting t=log|x|/log(lambda) reduces the invariance equation to P(t+1)=(I+N)P(t)+lambda^(-k)v. Pascal gives P_*(t)=lambda^(-k) sum_{r=1}^m binom(t,r) N^(r-1)v; all homogeneous solutions on bounded fundamental intervals grow at most t^(m-1) under J^n. Thus first-coordinate coefficient is v_m/(lambda^k m!(log lambda)^m). A C^(k-1,1) graph has vanishing derivatives through k-1 and hence O(x^k), impossible for v_m!=0. When v_m=0, v is in ran N and polynomial graph ax^k exists. Orbit formula yields normalized n^m limit. Endpoint m=1 and both sign half-lines included.

## originality

PASS

Best-of-knowledge PASS with material priority risk: exact Jordan-length forced coefficient, graph smoothness threshold and trajectory amplitude are distinguished from the semisimple published theory. Full 2003 normal-form primary source could not be read.

## value

PASS

At fixed quadratic nonlinear forcing, the required logarithmic degree becomes arbitrarily high with Jordan length, a nonsemisimple boundary phenomenon not predicted by semisimple degree-vs-order heuristics. Sharp regularity and orbit amplitude make it structurally useful beyond finite examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
