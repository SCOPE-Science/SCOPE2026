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

# Verification and limits

The mathematical proof in `RESULT.md` gives the all-field assertion. Recompute the independently defined set and its complete integer-valued additive energy by executing `python3 CHECK.py`. No third-party package is required. Twelve finite-field instances are checked, including quadratic extension representations of the fields of sizes \(9\) and \(25\), with exact integer equality. For five small fields, every Fourier coefficient is also checked by an independent direct finite character sum; these floating-point comparisons use a tolerance only for numerical character evaluations, not for the integer energy equalities.

The expected first line is `CHECK_OK independent_integer_energy_cases=12 independent_fourier_cases=5`. Passing these tests does not certify infinitely many prime powers or establish publication priority. Those obligations rest on the proof and cited literature comparison, respectively. The self-review has been completed; no independent mathematical audit has been performed.
