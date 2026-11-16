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

Execute `python3 checks/verify_spin2_caps.py` from the package root with Python 3 and no third-party packages. Successful execution emits `SPIN2_DEGREE3_EXACT_CAP_SPECTRUM_AND_GAPS_PASS`. The script constructs seven Wigner-component density polynomials, verifies normalization and the \(\pm m\) symmetry, obtains the eigenvalues by exact antiderivatives, checks the six stated factorizations, evaluates independently the finite factorial Wigner series at sample points, checks rational cutoff probes, and verifies the thin-cap leading coefficients. The proof of the *global* ordering is the sign argument in RESULT.md; finite probes alone cannot certify it.

The theorem's assumptions are strict \(0<c<1\) and one complex spin-two degree-three harmonic space. No independent audit or external verification has been performed. The 2018 doctoral thesis was identified from its abstract but its complete text was not available for comparison.
