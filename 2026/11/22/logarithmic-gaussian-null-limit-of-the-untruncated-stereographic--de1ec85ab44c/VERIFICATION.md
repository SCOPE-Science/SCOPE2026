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

The raw null statistic on \(\mathbb S^2\) has infinite second moment, so simulation of a finite-sample variance is not a legitimate verification. The proof instead uses the exact half-angle density, a rare-event truncation, a Hilbert–Schmidt operator fourth-trace inequality, and a martingale triangular-array CLT.

Executed on the included code: \(\texttt{python CHECK.py}\). Result: `PASS 31 analytic/numerical assertions` (exact primitive identities for truncated cotangent means and second moments, logarithmic increment checks for five linear combinations, positivity/finite fourth moments, and quadratic-variation prefactors). These checks do not certify a limit law by numerical extrapolation.

The critical bounds proved in the included result are: discarded-pair probability \(O((\log n)^{-1/2})\), centering adjustment \(O((\log n)^{-1/4})\), off-diagonal predictable-variation variance \(O(\log n)\), and summed martingale fourth moments \(O((\log n)^{1/2}+(\log n)^2/n)\). Dividing by the relevant powers of \(\log n\) gives the martingale hypotheses.

Independent audit and independent validation have not been performed. The original-statistic proof covers only iid uniform samples on the two-sphere and fixed tuning parameters.
