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

The latitude slicing uses normalized area dz dphi/(4pi). Alternating 2n longitudes at spacing delta=pi/n have uncovered interval [delta-A_+-A_-]_+, giving the exact all-radii integral even when individual caps cover whole parallels. At optimum the convex polytope has precisely two polar and 2n lateral triangular facets with equal support h*, and no other maximizing normals. The local polar tangent polygon is an n-gon of inradius 1 (area n tan delta); lateral tangent region has inequalities ±s y1 + c y2<1 and -y2<1, area (1+c)^2/(c s). Disjoint small contact patches exhaust the uncovered set by strict support gap elsewhere, and smooth nondegenerate active boundaries give O_n(epsilon³), yielding [2n tan delta+2n(1+c)²/(c s)]/(4pi)=K_n. Bernoulli product from m independent probes yields exp(-K_n x²). The asymptotic is fixed n, not joint-uniform; finite quadrature only corroborates.

## originality

PASS

On the stated bounded primary literature and Resultary comparisons, the exact final claim is neither stated nor directly implied by the identified relevant antecedents; known special cases and methodology were credited. This is best-of-knowledge, not proof of global novelty. See four explicit implication checks, actual source inspections, and residual risks.

## value

PASS

Complete exact spherical nearest-site CDF for a natural family of fixed latitude-ring codes and sharp measure of deepest gaps are natural spherical-coverage invariants. Explicit all-order local tail rates and extreme-probe scaling extend known covering radius and isolated n=4 calculations; arbitrary unmotivated numerical slices are not the object.

The dated certificate retains the supplied scientific assessment, sources and limitations.
