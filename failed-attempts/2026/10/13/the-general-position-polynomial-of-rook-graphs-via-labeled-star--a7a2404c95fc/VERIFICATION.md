---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A rook graph has diameter at most two. Under its line graph identification, the three distinct cells of a forbidden geodesic are exactly three selected edges forming a simple three-edge path in K_{m,n}; the fourth rectangle edge may be present. In each connected path-free bipartite component a spanning tree must be a star, and no extra edge can join two leaves in the same bipartition class. Conversely, stars have no such path. The labeled component series has isolated rows and columns, one type for a single edge, and one center choice for each higher-degree star. Summing gives ue^{vz}+ve^{uz}−uvz, and taking a set gives the stated exponential; differentiating by u gives the recurrence, including the empty-board bases. A forest has number of edges equal to occupied vertices minus nontrivial components. When both sides are at least three equality at m+n−2 needs two spanning components with opposite-side centers; selecting these centers specifies all edges, yielding mn. With m=2<n, a degree-two column would use both rows and isolate that star, leaving at most two edges; at the maximum n each column therefore chooses one of two rows, yielding 2^n. The 2×2 and one-row cases are immediate from the cycle and complete graph. An independently written finite check at /workspace/audit_evidence/replay.py (rook) compared metric-triple enumeration with the exact truncated component product on 28 boards and 78,035 subsets. The frozen 50 small boards are included in, not disjoint from, the 484 positive-side size pairs with extremal checks; this is only a wording issue in the verification summary.

## originality

FAIL

The assigned mathematical statement is covered in the inspected catalogue. A distinct record has the same labeled rook-graph family, star-forest equivalence, edge-weighted bivariate EGF, and every leading-coefficient case, and additionally gives a finite coefficient formula. The recurrence is a direct coefficient form of that same EGF, not a surviving distinct result. This is a statement-level coverage decision, not a finding that the frozen record was later in origin or derived from the other work. The archive paths of the matching records are dated after the frozen path; dates alone do not establish priority or independence.

## value

FAIL

A full all-size enumerator for this family is a useful mathematical object, going well beyond the known extremal cardinality. But the exact same bivariate enumerator and extremal table are already available in the matched result. The only additional presentation item is a coefficient recurrence obtained by a single formal derivative, which adds no independent exact fact. There is no surviving substantive increment in this finding to justify a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
