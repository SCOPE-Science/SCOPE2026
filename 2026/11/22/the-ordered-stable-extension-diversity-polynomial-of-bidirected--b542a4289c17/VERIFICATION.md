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

Execute `python3 check.py` in the same directory as the research documents. The test is self-contained in standard-library Python 3 and uses exact integer arithmetic. It checks the six-state determinant against \(D(x,z)\), evaluates 43 transfer and rational coefficients in parallel, and computes all ordered-pair distances by independent subset tests through \(n=16\) (17 tested orders, 17,206 pairs). It checks that the maximum exponent always has coefficient two for \(n\ge2\) in this finite test range. The expected first output line starts `VERIFY_OK exact determinant and 43 generating coefficients`.

The full infinite-\(n\) assertion depends on the displayed state orbit proof and formal matrix inverse, not on the finite test. The asymptotic relies on a simple uniquely dominant pole of the factored denominator at \(z=1\). Both are mathematical arguments; no independent external proof verification has been performed. Originality is assessed only relative to inspected primary and published sources, with possible earlier equivalent transfer methods still at risk.
