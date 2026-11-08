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

# Verification performed

The standalone `verify_triangle.py` script was extracted from the current scientific package location and executed with Python 3 and SymPy (declared in `requirements.txt`). Reproduce using `python -m pip install -r requirements.txt` followed by `python verify_triangle.py`. It checked exactly the symbolic identities defining the three basin intervals, the sum of their Euclidean arclengths and the boundary perimeter fraction. It also computed geometric orthogonal projections directly from the three line directions, verified the primitive four-cycle and all five fixed points, and tested 7,200 independently drawn initial conditions for agreement between geometric iteration and the explicit basin formula. It printed `PASS` with no assertion failures.

The infinite quantifiers, nonexistence of further recurrent orbits, invariant probability classification, and exact physical-measure conclusions are proved in `RESULT.md`, not by finite sampling. Numerical samples avoid tie thresholds to prevent floating-point ambiguity. The source-precedence and novelty evaluation is non-independent and does not exclude unindexed literature.
