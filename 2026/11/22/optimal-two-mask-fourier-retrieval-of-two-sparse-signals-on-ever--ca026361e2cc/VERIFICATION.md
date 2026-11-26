---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproducibility and evidence boundaries

The unchanged Python 3 diagnostic `CHECK.py` uses only the standard library. It specializes to phases \(1,i\) and amplitude budget \(\rho=1\). Its recorded result was `CHECK_OK exact_integer_pair_sums=145789 decoder_tests=1660 antipodal_tests=132`. The exact integer checks cover even orders through \(N=120\); the finite Fourier decoding checks cover even orders through \(N=18\).

The analytic argument in `RESULT.md` proves the full criterion. For every positive contrast budget the amplitude exponents keep both their ordering and their pair-sum distinctions. For a noncollinear phase pair the antipodal projection matrix is invertible because the sine of the relative phase is nonzero; for collinear phases a conjugate-antipodal pair gives identical intensities. The fixed-parameter finite diagnostic does not verify all real contrast and phase choices, nor any noise-stability claim.
