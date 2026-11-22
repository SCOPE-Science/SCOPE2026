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

# Mathematical verification

The theorem follows analytically from direct two-by-two resolvent inversion, the characteristic equation and the constant-or-strictly-monotone Perron-root interpolation lemma. It does not rely on an assumed limiting form or any numerical approximation.

Run `python3 verify.py` with Python 3 and no third-party dependencies. The checker uses `fractions.Fraction` for exact construction, inversion, multiplication, traces and determinants for 1,080 parameter combinations. It also verifies the exact threshold `44/235`, exact determinant identity, and two immobile-vector limits. Floating-point calculations in the checker test only the predicted monotonic directions; the proof establishes those directions for every real positive admissible parameter.

The model is the specified disease-free linearization; no nonlinear persistence or full spatial-kernel result is verified. Some close historical-priority comparisons were limited to indexed abstracts, as disclosed in the scientific review. No external independent audit has been performed.
