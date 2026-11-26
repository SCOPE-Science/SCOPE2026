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

For the repaired RESULT.md. The frozen proof asserted a short exact sequence of augmented chains: in degree −1 the oriented incidence map has a rank-one kernel, so the left map is not injective. The replacement uses ordinary chains, exact simplex by simplex, and computes ordinary H0 before passing to reduced homology. The joins are homotopy 3-spheres and intersections homotopy circles. The exact sequence identifies H1 with the integral incidence cycle, H2 with the oriented intersection H1 groups, and H3 with the join H3 groups; each identification is an isomorphism, not an extension or a rational rank argument. An outer reflection reverses the incidence orientation in degrees 1 and 2; the degree-3 join swap has parity (1+1)(1+1), so the two endpoint characters are the only signs. Barycentric subdivision removes simplex inversions and rational coinvariants agree with invariants, giving one outer-invariant edge sum; independent inner reflections eliminate each edge and vertex coefficient and outer reflections eliminate degree 1. The frozen verifier and recorded traces for H=C5 were inspected, not executed; the modular check is supplemental and cannot resolve integral exactness.

## originality

PASS

The distinct contribution is the natural integral wreath modules and the effect of adding inner symmetries. The revised result credits both the already known nonequivariant wedge splitting and the demonstrably covered outer-quotient calculation. Neither supplies the inner-character modules or the full-wreath acyclicity comparison.

## value

PASS

The three integral modules explain why two rank-five groups have different reflection behavior and exactly what inner orientation reversals do to quotient homology, uniformly over circle-type fibers. These data are not determined by the known wedge type or the outer orbit-space homeomorphism. The repair preserves that useful classification without counting the covered outer-only result as a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
