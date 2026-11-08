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

The analytical proof establishes the exact two-season square factorization, Perron root formula, strict convexity, global policy cutoff, and the unique local minimum. Its domain is all \(a>b>0\), \(0<h<1\), and \(0\le p\le1\).

The Python 3 `verify.py` file uses only the standard library. It independently multiplies the seasonal matrices as exact fractions, compares with the derived square, verifies exact trace/determinant/discriminant identities, and checks finite spectral and strict-convexity diagnostics. It does not prove statements for parameters outside its finite grid; the proof in RESULT.md does.

The scientific priority comparison was based on specified literature and semantic search. Historical priority remains provisional, and no independent audit is asserted.
