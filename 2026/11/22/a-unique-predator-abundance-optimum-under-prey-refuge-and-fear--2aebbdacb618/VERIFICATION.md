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

# Verification of the mathematical claim

The general result uses analytic inequalities and implicit-function arguments in `RESULT.md`. The separate `checker.py` confirms the exact rational example \((u,v,b)=(1,1,4)\), stationary equation, Jacobian determinant \(32\), critical curvature \(-11/320\), the algebraic invasion threshold and illustrative numerical samples. Run `python checker.py` with Python, SymPy and SciPy. A successful local run printed:

```
PASS exact stationary, derivative, Jacobian and rational curvature identities
PASS supplementary sample of the unimodal equilibrium curve (not a proof)
```

The numerical samples do **not** certify an infinite-parameter theorem; that theorem rests on the proof's strict signs of \(f_v\), \(f_{uu}\), the nullcline monotonicities, both boundary limits and the uniqueness-of-maxima argument. The proof does not certify independent review, global convergence or an empirical refuge benefit. Both publication date and model equation come from the cited primary 2026 article. Historical-priority claims have the literature limitations described in `REVIEW.md`.
