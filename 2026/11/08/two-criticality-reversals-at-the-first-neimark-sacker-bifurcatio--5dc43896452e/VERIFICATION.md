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

Execute `python VERIFY_NS5.py` in a Python 3 environment with SymPy. The program checks exact cyclotomic relations for the five-cycle, exact denominator discriminant, four rational sign brackets and an explicit half-coupling sign; it symbolically evaluates the nonresonant discrete Neimark–Sacker coefficient from the two quadratic homological terms, and compares exact normal-form expressions at three independent rational couplings. It also computes high-precision roots only for display.

The analytic proof, not a finite scan, establishes that these are the only two positive sign reversals. The program does not prove that no earlier paper has the same result. It provides no information at the excluded resonances or zero-cubic parameter values. Independent scientific validation has not been performed.
