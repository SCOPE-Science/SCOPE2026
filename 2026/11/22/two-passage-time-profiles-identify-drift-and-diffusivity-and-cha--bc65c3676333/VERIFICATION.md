---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the finite interval with absorption at 0 and normal reflection at L, the mixed backward equations are L tau=-1 and L m2=-2 tau. The diffusion product rule gives L v=-2D(tau')^2. Multiplying this equation by tau' and subtracting v' times the mean equation gives DW=v'. With I=exp(integral b/D), the derivatives are I(x)^(-1) times the rightward integrals of I/D and 2I(tau')^2, respectively, so both are strictly positive for x<L. Substituting the inverse coefficients, with the stipulated C1 uniformly elliptic extension and the four mixed conditions, solves both equations; a homogeneous difference has derivative proportional to 1/I, zero at L, and value zero at 0. This proves both realization and uniqueness including the limiting coefficients at L. Writing s=L-x gives tau'(L-s)=s/D(L)+O(s^2); the variance integral then gives v'(L-s)=2s^3/(3D(L)^2)+O(s^4), with the stated quartic constant on integration. In the mean-blind family the two terms in L tau cancel the eta-dependence, and the integrand ratio sqrt((1+eta s^2)/(1+eta u^2)) is strictly increasing in eta for 0<u<s. At eta=0 the exact variance is [1-(1-x)^4]/6. The frozen numerical checker was inspected, not used as a proof or replayed.

## originality

PASS

Credit the classical backward moment hierarchy and the algebraic nature of elimination. The supported distinction is the explicit identification and necessary-and-sufficient realization from the first two full spatial passage-time moments for this same mixed-boundary diffusion, with the wall signature. The inspected closely related coefficient-identification results need different data or stronger prior information. This is a best-of-knowledge comparison, not a priority certification.

## value

PASS

The result answers a concrete inverse-data question: one spatial mean can be shared by inequivalent diffusion generators, whereas the mean and variance from the same experiment suffice and also admit a compatibility test. The boundary vanishing order both recovers wall diffusivity from a local invariant and identifies where the interior ratio has a vanishing denominator. These conclusions add usable structural information beyond the routine moment equations. This is exact profile identification, not a numerical stability or finite-sample claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
