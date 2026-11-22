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

# Verification scope

The curvature identity was derived using the cylindrical moving frame and checked against the direct three-dimensional cross-product formula at many noncritical parameter points. Exact rational tests of the polynomial transform, rational sign bracketing of all four varying coefficient roots, finite-difference derivative tests, an independent bisection of the critical cubic root, and near-threshold maximum splitting checks are implemented in `check_trefoil_curvature.py`. The script reports `TREFOIL_CURVATURE_VERTEX_BIFURCATION_CHECKS_OK` when all assertions pass.

The mathematical proof, not the finite numerical tests, establishes the global count and asymptotic scaling. At the known inflection aspect ratio \(\lambda=4/13\), the curvature is not differentiable at its three zero minima; the theorem counts strict local extrema and makes no blanket differentiability assertion there.

Originality comparisons include the same parametrization and curvature plots in Oberti–Ricca (2016), and the distinct elastic-braid equilibrium model in Starostin–van der Heijden (2014). Figure captions and searchable primary text were inspected; the author-hosted PDF image screenshot could not be retrieved through one image-access route. This is a residual priority-inspection risk, not independent evidence of novelty. No independent audit has been carried out.
