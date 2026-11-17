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

The stated toral map is two continuous piecewise-affine orthogonal slope-±2 tent shears. Its exact fourth iterate can be subdivided into 2,337 full-dimensional rational polygons with integer-affine return maps. I inspected the actual checker.py and the proof of area-one coverage, convex half-plane clipping, singular-return analysis, torus-edge identifications, and exact period-2 exclusion. The source certificate explicitly reduces 574 nonsingular incidence solutions to 336 toral fixed representatives, removes 16 points of period dividing 2, giving 320 primitive points or 80 cycles. The nine singular affine cells yield only the four known period-two segments or no fixed locus; no uncounted positive-dimensional primitive-four family. The differentiated 256 primitive points have trace counts −574:128, +578:64, +178:64 and 64 switching points. All three smooth traces have absolute value >2 and determinant 1, hence the 64 differentiable cycles are hyperbolic. This is a complete finite rational subdivision argument, not evidence from an unbounded numerical orbit sample. The entire exact source checker was read but not independently executed in this run.

## originality

PASS

Best-of-knowledge PASS for a sharply defined finite-period exact census. The relevant Myers Hill–Sturman–Wilson original toral non-monotonic shears papers define the same family and explicitly identify four period-two segments and prove mixing/correlation properties, but the accessible inspected results do not supply the submitted complete fourth-period orbit census or trace partition. No Resultary alternative with mathematically identical map and fourth-period count emerged; this negative search alone cannot certify priority.

## value

PASS

The complete first nontrivial isolated primitive period-four orbit count, including boundary-switching cycles and exact hyperbolic trace classes, is a natural finite exact dynamical invariant of a studied piecewise symplectic map. Distinguishing period-two continua, smooth hyperbolic cycles and nonsmooth cycles matters to periodic-orbit zeta and stability investigations; no global zeta or long-period conclusion is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
