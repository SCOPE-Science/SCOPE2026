---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In the specified orthonormal-coordinate realization the face free generators are exactly the roots annihilated by a supporting objective. Rank two in a simple triangle-free graph forces two edges, and their Gram area squared is 3 for intersecting edges and 4 otherwise. A fixed pair yields one face per chamber of the contracted arrangement. A wedge collapses to a universal vertex; a disjoint pair collapses to two adjacent universal vertices, because in a complete bipartite graph each merged block includes both types of vertices. The rest remains a biclique. The joins give acyclic-orientation counts B2 and 2B3, respectively; the pairs themselves have multiplicities p·C(q,2), q·C(p,2), and 2·C(p,2)·C(q,2). This gives exactly the asserted formulas. At fixed p the two leading coefficients have common factor p!·C(q,2)·(p+1)^(q−2) and multipliers p and p(p−1); the other wedge has base p. This checks the frequency and mean. B2(0,b)=2^b, B2(1,b)=2·3^b and B3(0,b)=3^b give the thin two-vertex formulas, including four squares and eight rhombi at p=q=2. The seven-case checker was inspected, not executed; it is finite corroboration only.

## originality

FAIL

The distinction between the unrefined f-vector and the metric histogram is real, but the strongest prior gives the count separately for the exact flat indexing each metric class, before summation. The complete claimed histogram is a direct evaluation of those existing contributions using rank-two incidence and two elementary join substitutions; the limit then follows by keeping the unique largest base in a finite standard coloring sum. This is demonstrated coverage by implication, not a claim that a published table explicitly prints the area split.

## value

FAIL

The uniform area statistic is natural, but this exact refinement is mechanically supplied by established per-flat counting plus routine edge classification and coloring. The thin-side limit adds only a dominant-term extraction from that finite sum. No independent mathematical gap, nonroutine estimate, or consequence that needs this precise evaluation is established beyond these applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
