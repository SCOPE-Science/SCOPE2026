---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The high-root PGF partitions edge states by existence of a low vertex with both edges retained, which is equivalent to connectivity of the two high vertices. The low-root PGF conditions on zero, one or two retained seed edges. Independent enumeration of the 64 states for each orbit at b=3 reconstructs both moment differences. The displayed odds-transform coefficients have one sign change; the positive constant and negative leading coefficient give existence and Descartes gives uniqueness. The mean factor is 1+p+p²+2p²(1−p)>0 for 0<p<1. For any fixed b≥3, exactly one retained incident edge yields the first-order variance deg(v)p, giving a difference (b−2)p+O(p²). With at most two failed edges, at least one of the b length-two paths between the high vertices survives, so the only possible disconnection is isolation of a low vertex. The high-root squared deficits contribute b; the low-root deficits contribute (b+1)²+(b−1). Their expectations squared are O(q⁴), so the variance difference is −b(b+2)q²+O(q³). Opposite signs and polynomial dependence force a sign-changing zero. The b=2 boundary is vertex-transitive.

## originality

PASS

The new content supported by this review is the structural sign reversal by seed orbit across a natural graph family and the unique transition in the smallest asymmetric biclique with both parts of size at least two. The underlying bond-percolation interpretation, rooted distribution and finite-state methods are prior work.

## value

PASS

The reversal shows a concrete failure of seed-degree ranking for final-size variability in a basic family: around p=0 degree determines the first-order variance, whereas around p=1 rare isolation of the low-degree seed dominates squared loss. K_{2,3} is the first asymmetric case in the stated family and gives a sharp threshold while the mean always favors the high-degree seed in the open interval. This is a reusable counterexample and endpoint mechanism, not an arbitrary numerical comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
