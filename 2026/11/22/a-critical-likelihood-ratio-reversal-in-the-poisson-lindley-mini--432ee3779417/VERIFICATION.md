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

# Reproduction and limits

Run `python verify.py` from this extracted package with Python 3 and SymPy installed. The checker verifies the exact Poisson–Lindley/modified-negative-binomial survival identity at initial indices, the symbolic admissibility factorization, the exact positive-coefficient polynomial certificate, and the adjacent determinant at several symbolic previous states. It also verifies a fully rational positive minor at previous state three and a negative minor at state four when both shape parameters are one.

All-state inequalities and the real crossing existence/uniqueness are supplied in the mathematical proof rather than inferred from finitely many symbolic samples. Boundary behavior follows from the exact admissibility identity and an explicit limiting argument. The computation uses only the packaged checker, not external data, cached logs or prior research artifacts.

Independent mathematical validation has not been performed. Literature comparisons include the complete accessible portions of the 2024 originating paper and later relevant work; some older full texts remain uninspected. The result does not purport to classify every TP2 minor of the chain.
