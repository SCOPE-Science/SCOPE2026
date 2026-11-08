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

Run `python3 verify.py` using Python 3 with no external dependencies. It reconstructs exact rational transvectant polynomials after the natural \(a_0=1,a_1=0\) normalization and eliminates the independent pivot variables. The script tests weighted degree \(r+1\), nonzero transverse Hessian determinants for \(r=5,7,9,11,13,15\), and zero transverse derivative plus nonzero critical values \(24t^3\), \(405t^4\), \(8960t^5\) for the first three of those degrees. The \(r=5\) test is a boundary consistency check outside the asserted \(p\ge2\) range.

The output terminates in `CERTIFICATE_OK`. The proof for all \(p\ge2\) is mathematical, not an exhaustive finite calculation: it uses the \(SL_2\) moment-map differential, weights, the formal implicit-function theorem and the analytic Morse lemma. The initial complete-intersection property is established by the cited earlier theorem. This package is self-reviewed only; no independent mathematical audit is claimed.
