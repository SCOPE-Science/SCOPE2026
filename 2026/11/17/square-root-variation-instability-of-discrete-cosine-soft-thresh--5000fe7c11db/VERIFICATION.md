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

The analytic proof is self-contained modulo standard cosine, sine-orthogonality and Rademacher-moment identities, each derived or stated explicitly in RESULT.md. The standalone command `python3 verify_dct_bv.py` was run successfully under Python 3 with no third-party dependencies. It tests every spectral mask at lengths \(2\) through \(9\), each single-step response against direct DCT reconstruction, several longer random masks, and nonlinear perturbations inside fixed active-set cells. All runs reported `ALL_DCT_VARIATION_CHECKS_PASS`.

These finite tests verify implementations and selected cases only; they are not a substitute for the all-dimension proof. The quantitative rate is \(\Theta(\sqrt n)\), and no limiting optimal prefactor is claimed.
