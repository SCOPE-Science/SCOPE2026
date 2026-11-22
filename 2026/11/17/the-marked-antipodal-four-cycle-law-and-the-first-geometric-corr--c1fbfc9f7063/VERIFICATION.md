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

For fixed n>=4, the near-antipodal events E_ij have cap probability p=(1-cos(delta))/2. Integrating leaves proves all forest intersections exactly p^e; for small delta an odd cycle is forbidden. Every rank-three nonforest surviving beyond three edges is exactly a 4-cycle, giving 3 binom(n,4) possible labelled cycles. Local tangent coordinates for the 4-cycle have four unit-disk constraints; Fubini yields 2 pi integral_0^2 r a(r)^2 dr = pi^3 - 16 pi/3, with a(r) the intersection area of two unit disks. A bounded-support Jacobian argument provides L1 / total-variation convergence of the conditional marked six-dimensional law, not merely weak convergence. Division by p^3 yields 1-16/(3 pi^2), and inclusion-exclusion yields the displayed cubic coefficient. Independent direct quadrature calculated volume 14.251115861154254 and coefficient 0.45962035390753186, with n=4 coefficient 13+16/pi^2. The numeric test is a check of the derived integral, not a proof of the limit.

## originality

PASS

Best-of-knowledge PASS for the combined fixed-n small-cap cubic diameter correction and labelled marked total-variation law. The exact spectral even-cycle trace is known, but the inspected separate theorem studies high-dimensional d tending to infinity at fixed density and does not assert this 3D singular cap-lens evaluation; Mayer–Molchanov studies n tending to infinity and its first-order diameter limit. No equivalence or broader prior implication was found; explicit spectral-priority risk remains.

## value

PASS

The first nonindependent geometric contribution to a natural random maximum is the forbidden triangles plus a 4-cycle dependence. Identifying its exact lens volume and limiting marked configuration provides a motivated structural geometric statistic not implied by the independent-edge approximation or a first-order large-sample extreme law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
