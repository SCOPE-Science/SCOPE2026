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

# Verification of joint tangent-polygon fluctuations

The geometric proof is provided in `RESULT.md`. It starts with support-contact tangent intersection geometry, derives the leading cubic-gap formulas for area and perimeter, evaluates exact first and second Poisson Palm moments, obtains the weighted joint central limit by independent truncated blocks, and reduces singularity of the limiting covariance to constant curvature radius by Cauchy–Schwarz.

`verify_poisson_tangent.py` uses Python standard-library arithmetic to construct tangent polygons from actual sampled angles for the support family \(h(\theta)=1-\varepsilon\cos(2\theta)/3\), whose curvature radius is \(1+\varepsilon\cos(2\theta)\). It checks polygonal area and perimeter by independent vertex construction, the disk identities, the cubic local approximations, and leading means and scaled joint covariances for \(\varepsilon=0\) and \(0.55\). The deterministic-seed checker reports `POISSON_TANGENT_GEOMETRY_AND_COVARIANCE_CHECKS_PASSED`.

The simulation samples finitely many polygons and tolerates sampling errors; it is not proof of the central limit, the sharp covariance, or historical originality. The general theorem rests on the exact Palm covariance identity and the Poisson-block proof. The proof is restricted to the good-gap conditioning event, on whose complement a circumscribed polygon might not be bounded.
