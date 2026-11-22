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

# Reproduction and scope of checks

Run `python3 verify_geometry.py` and `python3 verify_independent.py` (Python 3 standard library). Both assert the finite totals \(24,48,18,1088,2616\), the component histogram, face-boundary rank 18, and the charge-class distribution. The first additionally checks the six full-octahedral symmetry component-orbits; the second derives the graph from exact coordinates and independently enumerates induced square cycles. The programs contain all graph data and the mathematical operations needed; no fetched inputs, third-party packages, or floating-point evidence are required.

The proof's exhaustion criterion is recurrence on the least uncovered vertex, so each perfect matching is listed once. Every allowed face is included, and an edge in the resonance graph exists precisely when toggling all four face edges yields a second perfect matching. Thus the verified finite census is exhaustive rather than experimental sampling. The quotient-rank and two-component-per-charge checks are exact over \(\mathbb F_2\). For \(v=t>0\), the exact graph-Laplacian kernel theorem gives 69 zero-energy modes; for \(v>t>0\), the strict positivity of each active pair block leaves exactly the 14 frozen states. No eigenvalue spectrum outside zero, other flip classes, or unbounded-family assertions are verified.

Published-source comparisons establish established background, not definitive historical uniqueness. The 1,088 matching count and general medianity are not claimed as new. An unrelated fullerene manuscript could only be checked at abstract level. Independent external scientific audit has not been performed.
