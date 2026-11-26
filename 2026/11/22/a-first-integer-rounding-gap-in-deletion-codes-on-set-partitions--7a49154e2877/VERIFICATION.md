---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A restricted-growth word bijects with an order-retaining partition with unnamed blocks: on appending one point there is one choice per existing block and one new singleton choice. Deletion removes a position and orders surviving block labels by first occurrence; the incidence is a set, not a multiset or an observed deck. Pairwise disjoint shadows are exactly cliques of the compatibility graph. In the frozen search each color class is independent, and a reverse-order branch has only the remaining prefix of the coloring, making selected size plus prefix color count an admissible bound. Separately re-enumerating the graph and using exact pivoted Bron–Kerbosch with a cardinality bound returned (1,1,2,3,6,14) through length six, including 275,862,687 recursive nodes in that separate n=6 computation (not the frozen search's node count). At n=1 the only source has the only empty receiver. Independent certificate arithmetic checked the explicit code's 14 admissible pairwise disjoint shadows covering 45 receivers, the 41 positive fractional numerators summing to 972 with per-output load at most 64 on all 52 receivers, and the length-four and length-five covers, of total 3 and 25/4. The latter are dual feasible by summing weight over each distinct shadow, so the code sizes and receiver-count bounds prove floor(P_n)=M_n through five. At six, 14<15<243/16≤P_6; no exact P_6 or claim past six follows or is needed. The frozen replay entry point is verify.py with CERTIFICATES.json; uploaded code was inspected, not run. The exact enumerations are finite mathematical checks, not formal verification.

## originality

PASS

Qualified best-of-knowledge pass for the first rounded packing gap and the actual zero-error optimum in the all-partitions channel. Disjoint-shadow packing and the abstract LP are well established; the novelty claim is not the method or the Bell enumeration.

## value

PASS

Ordered positions with unnamed blocks give a natural zero-error channel distinct from conventional word deletion. The finite cutoff is the least failure of a standard relaxation, not a preselected numerical slice. An exact upper obstruction with an explicit feasible packing of weight greater than 15 shows why rounding the standard bound is insufficient despite the small input size. These exact outcomes and witnesses are useful benchmarks independent of any claimed law at larger n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
