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

The theorem is proved by exact projection traces, strict positive definiteness of the edge-overlap quadratic, an unsigned-incidence resolvent, and a contraction on the interval cube. The sharp example is proved by exact KKT inequalities and strict convexity.

Run `python check.py` using Python 3 and its standard library. The checker tests every labeled connected simple subcubic graph with 2–5 vertices, the cube, \(K_{3,3}\), Petersen graph, eight two-hub tree sizes and the four-vertex path. It uses rational elimination, including exact comparisons for \(w_v\in[0,1/3]\), \(p_e\ge1/(6|E|)\), normalization, stationary derivatives and double-star boundary KKT conditions. Reported result: 526 passing exact graph cases.

These finite checks are supplementary and cannot establish the all-graph theorem on their own. They do not establish novelty in literature or independent verification.
