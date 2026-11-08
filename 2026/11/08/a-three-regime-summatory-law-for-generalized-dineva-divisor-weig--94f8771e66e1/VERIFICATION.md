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

# Reproducibility and limits

The standalone Python 3 checker `verification/check.py` uses only the standard library and carries out independent arithmetic checks at \(1\le n\le120\) for \(t=0,1,2\). It tests the exact finite source identity using rational arithmetic, recomputes the auxiliary multiplicative kernel, and evaluates finite sums for parameters straddling the critical \(t=1\). Its deterministic output is `verification/output.txt`.

The proof of absolute convergence for the correction Euler product, the relevant tail bounds, the real-parameter dominated-convergence argument and the critical Dirichlet hyperbola estimate are mathematical arguments in RESULT.md. No finite computation certifies their infinite range. No independent mathematical audit has been conducted.
