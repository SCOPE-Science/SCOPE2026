---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The cyclic difference set {0,1,3} gives the Fano incidences: its six ordered nonzero differences are all distinct. A face is a set inducing maximum degree at most one. Independent enumeration gives the stated f-vector (14,91,322,651,728,392,58), 1121 disjoint cover pairs, exactly one critical vertex and thirteen critical 5-faces, and a topological ordering of all 2256 nodes over 10150 directed covers. Acyclicity can also be seen directly: a directed cycle must alternate matched up and unmatched down edges, since two successive up edges cannot occur. Choose the earliest pairing phase of any up edge on the cycle, toggling vertex v. Some down edge must remove v. Its two endpoints, participating in cycle pairs no earlier than this phase, would both have been available for the v-toggle, which pairs disjoint candidates and would orient that edge up. This is a contradiction. Discrete Morse theory thus gives one 0-cell and thirteen 5-cells. The attaching maps all land at the point, giving the integral homotopy equivalence and not just a field-specific Betti calculation.

## originality

FAIL

The identical integral homotopy classification is explicitly stated in a distinct same-day Resultary record with a stronger rotation-character finding and in additional later indexed records. This is established equivalent coverage, not a finding of which same-day record came first or evidence of dependence. The frozen invariant is fully covered, and a different matching certificate does not yield a separate stated scientific result.

## value

FAIL

The Heawood graph is a natural test case outside several understood graph classes, and an integral wedge classification would be a meaningful exact invariant if distinct. Here the only finding is an already covered invariant; the alternate reproducible count does not give a new method, theorem about the matching, or consequence beyond the known classification. No separate valuable remainder is stated or established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
