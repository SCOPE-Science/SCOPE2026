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

# Reproducibility and verification

Run `python3 verify_exact.py` with the Python standard library. It must report 15 passing tests. Its independent state recursion enumerates every still-feasible acceptance race in \(KG(N,2)\), using exact rational weights and no use of the claimed four-type case table. The tested sizes are \(N=5,6,7\) with \(w\in\{1/2,1,2,5,20\}\). These checks do not exhaust all \(N\) and \(w\).

If SymPy is installed, run `python3 verify_symbolic.py`. It verifies the unbiased specialization, the limit along \(w=cN\) for positive \(c\), the logarithmic derivative and the golden-ratio value. These algebraic checks complement, but do not replace, the all-parameter proof in RESULT.md.

The theorem's logical coverage is all integers \(N\ge5\), all real \(w>0\), and all positive scaling sequences with a limiting ratio in \([0,\infty]\). Neither numerical sampling nor symbolic evaluation alone establishes historical originality, and no claim about independent external validation is made.
