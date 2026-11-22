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

The self-contained `verify.py` regenerates the 27 exact projection trace costs symbolically in parameter \(q\), checks that only permutations have zero dual-certificate slack, and checks strict repeat slack at the graph value \(q=1/4\). It computes the rank-five marginal system and verifies the full equality-family parameterization, the exact IID and reshuffling graph fractions, and the relative improvement. Execute `python verify.py` with Python 3 and SymPy installed. These checks supplement an all-parameter analytic proof; no external audit has been performed. Numerical floating-point sampling does not establish global optimality.
