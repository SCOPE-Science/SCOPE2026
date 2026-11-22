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
# Reproducibility

Run `python verify.py` with SymPy available. The file checks the exact PGF numerator, the zero-location identities, the logarithmic jump coefficients, the strict consecutive canonical inequalities for a finite rational test grid, and a generic geometric-mixture failure with exact difference \(35/5832\). These checks supplement the analytic proof; the finite grid alone does not establish a universal \(j\)-quantifier. The all-index step is proved in RESULT.md by a unimodal beta-kernel inequality. The standard thinning self-decomposability criterion is sourced in the references. No independent mathematical audit is claimed.
