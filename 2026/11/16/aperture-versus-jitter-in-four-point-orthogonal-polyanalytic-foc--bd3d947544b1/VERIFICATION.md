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

The executable `CHECK.py` is self-contained and uses Python 3.10+ with no external dependencies. Run `python CHECK.py` from the directory containing that file. It computes all four-point anchored Euclidean Gram determinants **exactly** in \(\mathbb Q(\sqrt3)\); enumerates the \(64\) labeled four-point long/short edge patterns and \(1024\) five-vertex patterns; verifies the two explicit four-point constructions; and numerically cross-checks weighted Gram first derivatives and the Gaussian factors. The direct human-readable proof supplies the finite class table, the five-vertex graph counting contradiction, both minimal enclosing circles, and the exact spectral-norm derivative. Small finite differences illustrate rather than prove the derivative limits. Publication priority and independent mathematical audit have not been established.
