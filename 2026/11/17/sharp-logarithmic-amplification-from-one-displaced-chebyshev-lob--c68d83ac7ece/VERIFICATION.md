---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Exact one-node replacement identities follow from Lagrange cardinal uniqueness; the Lobatto angular formula has interior derivative weight n(-1)^j and endpoint twice that weight. The perturbed Lebesgue function at bounded angular offset u has harmonic coefficient (2/pi)|sin(pi u)| |1-tau/u|. The O(1) error is uniform on compact offsets by the 1/m^2+1/n estimates, and intact-grid control plus |L_k(z)| <= C/|u| excludes remote maximizers. The negative-offset profile is strictly concave on (0,1/2), has positive derivative at 0 and negative derivative at 1/2, while every competing positive/far offset is smaller. Therefore both asymptotic coefficient and concentration of all maximizing points follow. Independent nodal-product computations at n=500,2000,6000 for tau=.25,.5,.75 and bulk positions .32,.67 corroborated the predicted slow approach (finite-n additive constants persist); these are not proof of the limit.

## originality

PASS

The exact one-defect logarithmic Lebesgue multiplier and universal bulk-offset optimizer are not implied by a worst-case small-perturbation stability condition, by full-grid Lebesgue bounds, or by the linear asymptotics after deleting a node and reducing degree. Best-of-knowledge original with specific residual Wu full-text access risk.

## value

PASS

A single mesh-fraction displacement is the minimal controlled perturbation beyond classical Chebyshev interpolation, relevant to sensitivity of operator norms. The sharp constant, asymmetry of maximizing locations and independence from bulk index supply a substantive boundary between intact and perturbed interpolation, not merely reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
