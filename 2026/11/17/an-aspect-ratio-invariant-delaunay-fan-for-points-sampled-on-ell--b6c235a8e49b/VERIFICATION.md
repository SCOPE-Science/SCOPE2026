---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For all n≥4 distinct fixed eccentric-anomaly points on E_{a,b} with a>b>0, the vertical-positive invertible affine transform (x,y,z)↦(x/a,y/b,(z−b²)/(a²−b²)) sends Euclidean paraboloid lifts to (cosθ,sinθ,cos²θ), independent of aspect ratio. Lower faces and all Delaunay subdivisions are therefore invariant. Expansion of the four-site incircle determinant gives −16ab(a²−b²)sin(Σθ/2) times the positive cyclic Vandermonde sine product. Rooting four iid uniform anomalies at first label gives a uniformly shifted angle U independent of the Dirichlet(1,1,1,1) cyclic gaps; conditional on gaps, sin(2U+phase) is arcsine, giving both fair diagonals and exact near-zero margin probabilities. Independent random numeric determinant checks passed on 250 quadruples; they are not the all-real proof.

## originality

PASS

PASS only for the exact normalized signed incircle-margin distribution independent of marked cyclic gaps, not for classical four-ellipse-point cocircularity or the generic lifting primitive. The classical ellipse cocircularity criterion already makes the aspect-ratio independence of four-point degeneracies, and hence the unchanged Delaunay fan, a direct corollary. No located prior source supplies the conditionally independent arcsine margin law for iid eccentric-anomaly samples; its natural random-geometric content is the distinct surviving finding. This is qualified best-of-knowledge.

## value

PASS

The normalized signed incircle determinant controls the exact proximity of random four-point samples to a diagonal flip and yields its conditional distribution even after the four cyclic spacings are revealed. This is a motivated stochastic-geometry invariant with a sharp near-degeneracy probability, not just the known binary cocircularity condition; the structural fan corollary is not presented as novel by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
