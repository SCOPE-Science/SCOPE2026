---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

From nonnegative GBC plus affine precision, numerator for every vertex off a facet vanishes on that facet; if a facet form divided reduced q then normalized and weighted sums force it to divide every numerator, contradiction. At nonadjacent support-line intersections all numerators and hence q vanish. Each side has at most one parallel opposite side, and distinct nonadjacent nonparallel support-line intersections are distinct; restriction q|side has ≥m−4 roots (m−3 without parallel mate). Wachspress adjoint side restriction is a constant times the product of those nonadjacent side forms. In all-paired case any reduced q of degree≤m−4 restricts proportionally to adjoint on every side; vertex values propagate common factor and m side factors force polynomial equality, excluding lower degree or a nongeneric different adjoint. The cited Baumbach et al. Cor4.6 yields deg adjoint m−4 precisely for central symmetry and m−3 otherwise. Independent SymPy exact affine precision, side restrictions and degrees for triangle/parallelogram/trapezoid/pentagon; these examples are diagnostics, analytic facet/root argument proves all m.

## originality

PASS

Baumbach–Winter 2026 expressly pose the general m−2d denominator lower bound as Conjecture 4.1; their full article does not establish the present all-convex-polygon minimum common denominator. Baumbach–Freyer–Weigert–Winter determine adjoint DEGREE but not universal minimality among all nonnegative rational coordinate systems. The residual-root/edge restriction rigidity contributes the missing universal planar comparison, including nongeneric all-parallel-paired hexagons. Kohn–Ranestad generic uniqueness is acknowledged.

## value

PASS

Solves the natural and explicitly published d=2 common-denominator minimum-degree conjecture with complete equality classification; central symmetry and nongeneric parallel-side phenomena make the rigidity genuine rather than a routine substituted degree table. The exact minimal degree matters in rational finite-element and convex coordinate representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
