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

# Verification record

Run `python3 verify.py` from the extracted directory. The script requires only the Python standard library. It constructs the projected section knots and derivative jumps for a square and a right triangle directly from polygon geometry, independently evaluates the fractional-energy formula for \(p=3\) and its logarithmic \(p=2\) endpoint, and compares them against independently integrated closed Fourier expressions. It also confirms the exact square formula off the diagonal and the predicted angular horn coefficients for the square and the triangle.

Expected output: `GEOMETRIC_FOURIER_POLYGON_CHECKS_OK 12`. This has been obtained on the actual newly staged script. Scientific limits: 12 finite and asymptotic numerical comparisons do not certify the all-polygon theorem; the proof uses the chord-spline distributional derivative, fractional cosine identity, Fourier boundary identity, and oscillatory integration as written in RESULT.md. No machine-formal or external mathematical verification is claimed.
