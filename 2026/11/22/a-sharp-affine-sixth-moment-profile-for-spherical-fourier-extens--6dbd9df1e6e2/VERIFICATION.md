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

# Reproduction

From this directory, run `python verify.py`. The script uses Python's rational fractions to compute \(h_k''(0)\) from six finite truncated-power convolutions and verifies the four exact radial moments. It then uses SymPy to confirm the sixth-order moment identity, the exact sum-of-nonnegative-terms deficit and the normalized cubic profile. Optionally, when NumPy and SciPy are installed, three independent angular/radial quadratures compare with the exact formulas.

The exact computation is finite and is supported by the distributional convolution argument in `RESULT.md`; the script is not an exhaustive test of continuum inputs. The universal claim follows from the exact angular tensor identities and the nonnegative polarization deficit. No external or independent mathematical audit is asserted.
