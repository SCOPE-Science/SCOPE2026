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

# Verification

The accompanying `CHECK.py` is a standalone Python 3 script requiring NumPy. Running `python CHECK.py` enumerated 55,365 actual labelled deletion masks of sizes one through four in dimensions \(5\le N\le13\), directly reconstructed the two-basis frame, and compared all erased Gram largest eigenvalues with the analytical formulas to absolute tolerance \(2\times10^{-9}\). It also checked 18,336 complete retained-frame spectra of the two-plus-two deletion type, all exact minimizing-mask counts, and the singular dimension-four boundary. The observed output terminated with `CHECK_OK total_masks=55365 two_plus_two_spectra=18336 dimension_four_boundary=singular`.

All-dimensional validity is based on the exact matrix proof and modular counting argument in `RESULT.md`; finite floating-point checks are corroboration, not exhaustive coverage of infinitely many dimensions. No independent validation or external formal proof was carried out. The numerical thresholds are absolute, not interval-arithmetic certificates.
