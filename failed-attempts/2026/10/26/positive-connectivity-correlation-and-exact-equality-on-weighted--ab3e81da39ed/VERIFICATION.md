---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Acyclicity is a separate constraint on each cycle block, so the weight law factors across edge-disjoint blocks. A simple connecting path must traverse the unique block-cut route, and the resulting block demands suffice. On one shared cycle, after rescaling by the full-cycle weight, a nonempty missing set carries product weight in the reciprocals. The first event confines it to one row, the second to one column, and their intersection to one cell, giving exactly R,S,H after subtracting empty-set terms. As an algebra check, writing U=X+Y, one has Z=U+P+Q+XY+PY+QX+PQ and RS=U^2+UXY+QX^2+PY^2-4PQ, yielding the stated positive identity and strictness. Shared bridges have covariance p(1-p)>0. Every factor in the global product comparison is positive (a positive-weight local spanning tree satisfies both demands), so strictness is preserved exactly as claimed. For any shared cycle both partitions have two nonempty arcs, and a 2-by-2 support with no empty row or column contains a pair of opposite occupied cells; thus the criterion also simplifies to sharing any route block.

## originality

FAIL

Distinct indexed findings already cover both the theorem and the cycle certificate. In particular, the October 25 weighted-cactus arboreal-gas record gives the same all-positive-edge-weight covariance theorem and the equivalent common-block strictness criterion. Its four-cell variables are exactly the frozen variables shifted by one. The October 12 weighted-cactus forest record also states the same theorem and strictness. This is verified catalogue coverage, not a claim about author priority or first publication timestamps.

## value

FAIL

The underlying all-weight cactus theorem is worthwhile, but this record adds no identified mathematical gain over the existing theorem and four-cell proof. Its more detailed-looking cycle criterion is automatic for every shared cycle, and the local formula is the existing calculation in different variables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
