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

The proof starts from exact Fourier moments of two equal arcs and reduces the four-character concentration Gram to a real Toeplitz matrix. The symbolic certificate verifies all four reversal-block determinant formulas and their common strictly negative determinant sum. For any fixed admissible nonantipodal separation, both comparison matrices have a negative direction, which proves the two sharp spectral edge inequalities. The optimal double spectrum, condition-number formula, cusp perturbation and narrow-aperture asymptotics are derived analytically in RESULT.md.

Run `python CHECK.py` with the dependencies declared in `requirements.txt`. A completed run returned `FOUR_MODE_TWO_ARC_CHECKS_PASS 1106`. The script uses symbolic matrix identities and independent midpoint integration, together with finite numeric spectral checks. These checks validate formulas, not the universal claim by exhaustive enumeration. No independent mathematical audit or external formal certification has been performed.
