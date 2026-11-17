---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS — Three independent Gaussian vertices admit independent edge sum and difference U,V with covariances 6Σ and 2Σ. Their radial-exponential ratios reduce the obtuse-angle probability to the stated single angular integral. Symmetrizing independent arcsine-distributed cos² angles gives A(R)=1/4−(9/4)E[(q(S)−q(T))²/(3q(S)²+10q(S)q(T)+3q(T)²)]. Since q_R=1+(R−1)s, the integrand is strictly increasing with R>1 for s≠t by a positive normalized variance derivative, proving all-R strict decrease; at R=1 it vanishes. The arcsine moment variance 1/8 yields the 9/256 quadratic loss. The large-R endpoint layer is controlled separately, giving sqrt(3)/π·log(R)/R+O(R^-1), with nondegenerate finite R and limiting R→∞ distinguished. A separate SciPy adaptive quadrature gives A(1)=0.25, A(2)=0.233776306839877, A(16)=0.0951255750851252, A(10000)=0.0005131827413711 and normalized tail 0.5571811; finite quadrature is a check, not an infinite proof.

## originality

PASS

PASS — The final assessed claim is the covariance-ratio exact law, strict all-R ordering and both sharp asymptotic constants for three iid Gaussian planar vertices, not the classical isotropic 1/4. Edelman–Strang establishes the isotropic standard-Gaussian hemisphere model; the unrelated affine-uniform ellipse-boundary dilogarithm formula has distinct sampling measure and different local coefficient. No implication from either primary result to the submitted normalized anisotropic Gaussian integral was found.

## value

PASS

PASS — Gaussian random triangles are a natural covariance-shape problem; the theorem identifies a monotone dimensionless geometric probability and both local and highly eccentric sharp rates, including a nontrivial logarithmic degeneracy. Not a routine substitution of the isotropic theorem or a short finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
