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

# Verification notes

The exact reduction to equation (1) and the logarithmic periodicity argument are analytical. The curvature bound for the commensurate example uses
\[
\varepsilon\sqrt{(2-\omega^2)^2+9\omega^2}<2,
\]
which makes the second derivative strictly negative at every positive argument. The global regularity conclusion follows from bounded second derivatives of the squared profile near zero, and smooth inversion of the squared-radius profile at each axial tip. Finite numerical diagnostics do not establish results for all profiles, heights, or scales.

The standalone `check_discrete_coring.py` ran successfully from the packaged source. It checks 100 scaled-volume quadratures, 3000 profile-concavity points, and 6000 scale-identity evaluations, plus a discrepancy at scale \(3\). No exact symbolic or independent external certificate is claimed. Literature priority is provisional because standard sources on discrete scale invariance may have equivalent consequences.
