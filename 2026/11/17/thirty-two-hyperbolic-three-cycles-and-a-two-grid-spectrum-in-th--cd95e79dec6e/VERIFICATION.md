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

The composition of two slope ±2 tent shears has exactly 16 canonical affine/wrap branches per step, hence all third-return fixed points are covered by 4096 length-three itinerary words including fold equalities. Each return linear part is determinant one, trace in {-98,-82,-34,-2,22,38,102,198} and never trace 2; thus I−M is nonsingular and there is at most one rational fixed point per word, excluding fixed arcs. Independent rational enumeration of all words and all ordered branch inequalities yields 177 admissible incidences, 100 distinct H³ points, four H fixed points, 96 primitive points in 32 3-cycles. Independently recomputed 16 cycles of derivative trace 102, eight -34 and eight -98, each regular with |tr|>2. The parity of M−I yields denominators dividing |2−tr|/2, so primitive points lie on 1/18 or 1/50 grids; inspected exact checker proves grid counts 28 and 76 intersecting at the four fixed points. The census is exhaustive for one map, not empirical time sampling.

## originality

PASS

The same-map Myers Hill–Sturman–Wilson 2021/2023 papers define and analyze symmetric two non-monotonic tent shears and their mixing and period-two line segments, without a third-period exact count/trace grid in inspected sections. Published 80 primitive fourth-period cycles concerns distinct divisibility; the cited period-three arc theorem uses a one-tent, one-linear shear and is not the same map. No matched stronger all-period formula or period-3 exact table was identified. Originality is best-of-knowledge with full-text priority risk.

## value

PASS

Period three is the first odd prime period beyond the documented neutral 2-cycle lines for a canonical nonuniformly hyperbolic torus cusp. The exact finite symbolic classification sharply separates all regular hyperbolic 3-cycles from singular 2-/4-period structures; the two rational denominator grids and three return-trace classes are reusable dynamical invariants, a natural complete period cutoff not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
