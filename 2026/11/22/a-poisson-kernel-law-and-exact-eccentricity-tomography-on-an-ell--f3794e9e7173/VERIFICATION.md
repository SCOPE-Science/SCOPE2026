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

# Verification evidence and limits

The standalone standard-library program `verify.py` was run directly from these files and produced `checks.txt`. It reports 327,728 deterministic successful checks across circular, moderately eccentric and slender ellipses, including director-radius identities, inverse Jacobians, second/fourth Fourier moments, density normalization, exact total variation, and local Cauchy-profile diagnostics. These computations only test finite grids and finite parameter values; the full theorem is established by the symbolic proof in `RESULT.md`.

Proof-critical identities independently reduced in the text: \(h(\theta)^2+h(\theta+\pi/2)^2=a^2+b^2\), \(4h(\theta)^2h(\theta+\pi/2)^2=(a^2+b^2)^2-(a^2-b^2)^2\cos^2 2\theta\), the inverse Jacobian from the conic tangent equation, and the Poisson-kernel normalization and Fourier series. The weak-limit statement is for \(c\uparrow1\), not for an actual zero-minor-axis ellipse. External independent mathematical review is not asserted.
