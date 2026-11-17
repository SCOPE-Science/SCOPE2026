---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Write d_i=lambda_i-1/3 (sum zero) for area-uniform barycentric Dirichlet(1,1,1) coordinates. Squared radius is -A d2 d3-B d3 d1-C d1 d2. An independent SymPy exact polynomial expansion and simplex beta integration recomputed every coefficient for powers one, two and three, proving the displayed e1,e2,e3 identities. Their nonzero -e3/756 coefficient gives exact inversion; positive cubic roots plus 4e2>e1² are the necessary/sufficient Heron feasibility condition. The two explicit distinct positive-area side-square triples have e1=6,e2=11 but different e3. The area formula and strict bounds follow from Newton inequalities and positive Heron area.

## originality

PASS

Earlier 2018 Gravin–Pasechnik–Shapiro–Shapiro treats general multivariate polytope moments and fixed candidate vertex sets; Li–Qiu 2016 treats vertex-to-random-point distances; older published 2026 triangle reconstruction uses TWO independent area-uniform points, rather than distance of ONE point to its moving centroid. Although the same e1,e2,e3 structure appears, the centroidal moment observations and all-order normalization are distinct; no inspected full primary theorem yields the precise three-scalar centroidal inverse or sharp two-moment counterexample.

## value

PASS

Centroidal radial moments are natural rigid-motion-invariant shape statistics; an exact three-measurement reconstruction threshold, feasible region and area identity furnish directly reusable shape tomography for arbitrary Euclidean triangles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
