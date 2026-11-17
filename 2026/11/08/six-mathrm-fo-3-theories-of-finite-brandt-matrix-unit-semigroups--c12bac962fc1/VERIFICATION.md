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

Automorphism orbits of three pebbled nonzero matrix units correspond to equality partitions of at most six underlying row/column index labels, plus zero positions. When moving a pebble, at most four labels remain; adding two labels is always possible at n≥6, so the 3-pebble game is preserved for all depths and all m,n≥6. Independent complete orbit computation enumerated 255 canonical three-variable patterns, all substitution successors, and rank refinement [1,2,3,5,6] stabilizing at rank4, with B5 and B6 first distinguished there. A separate source direct concrete-state verifier supplies additional finite cross-check. The finite classification is not extrapolated to unbounded indices; the 6-label back-and-forth argument proves that part.

## originality

PASS

Best of knowledge, the exact infinite-depth FO^3 six-class stabilization and rank-four B5/B6 separator are not implied by the inspected general Brandt automorphism/aleph0-categoricity theorem, generic 3-pebble correspondence, or rank-three-only results. A materially stronger depth-unbounded bound survives.

## value

PASS

Sharp unbounded-depth three-variable expressivity for a natural finite semigroup family is a motivated complete logical classification. It identifies the precise B5/B6 rank-four obstruction beyond the known rank-three analysis; 37 is the smallest cardinality of the stable family representative. The finite 255-state certificate and uniform structural game strategy together yield a useful independently stated exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
