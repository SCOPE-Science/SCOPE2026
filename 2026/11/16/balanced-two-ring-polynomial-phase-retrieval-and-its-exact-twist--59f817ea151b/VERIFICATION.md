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

Run `python3 verify.py` with Python 3 and NumPy. The script directly forms real traces of arbitrary Hermitian matrices, computes the \(2K\)-sample discrete Fourier transforms for each ring, and reconstructs all trigonometric coefficients by the normalized two-channel linear inverse. It checks \(432\) combinations across six polynomial-degree bounds, verifies the counterexamples for coincident radii and resonant offsets, and checks the exact angular Nyquist singular values.

Recorded execution: `BALANCED_TWO_RING_PHASE_RETRIEVAL_PASS hermitian_cases=432 degrees=1,2,3,4,5,7 maximum_coefficient_error=3.39e-14 resonance_and_equal_radius=checked`.

The numerical tests do not exhaust all degrees, radii, angles, or polynomials; they do not independently establish the rational-reflection rigidity or a global noise-robustness bound. Universal correctness depends on the analytical argument in `RESULT.md`. No independent mathematical audit has been performed.
