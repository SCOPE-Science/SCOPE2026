---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Distance cannot decrease under deletion. For adjacent terminals the edge is compulsory. For nonadjacent terminals the original distance is two, so every geodesic has one intermediate vertex. A terminal intermediate is already dealt with by the compulsory edges; a nonterminal v forbids retaining both edges to any nonedge in G[L_v]. Thus the retained terminal neighbors form exactly a clique, independently at each nonterminal. Nonterminal-nonterminal deletions are free. This proves the polynomial and works when original nonterminal components or newly disconnected terminal pairs are present. Local maximum cliques minimize and count the minimum sets, while inclusion-maximal cliques give inclusion-minimal sets, with no free deletions. For example a cone on K2 disjoint union K1 has local maximal clique sizes 2 and 1. The cone on two triangles has e_T=6, d_v=6, local clique counts (1,6,6,2), hence z^9(z^3+6z^2+6z+2); the cubic's discriminant is -108. In the multipartite case a terminal part of size p_i>0 contributes one factor z^(p_i-1)(z+p_i) for every nonterminal outside it. Local maxima and maximal choices coincide (choose one from every available part); two optima differ by one edge swap exactly when they differ in one of these disjoint choice coordinates. The factors give nonpositive real zeros and the strictly stronger normalized Newton inequality gives strict log-concavity wherever three positive coefficients occur. For t>=3, three or more occupied parts already cost at least t compulsory edges. Two parts give pq>=p+q-1, with equality requiring one singleton terminal count and all nonterminals in the part with t-1 terminals. One terminal part costs (t-1) times the number of outside vertices. These cases give precisely stars, and a star realizes equality in each possible terminal placement.

## originality

PASS

Credit the existing geodesic-hitting characterization and universal lower bound, standard generating-function multiplication, and the exact overlap in the complete bipartite subclass. The inspected statements do not cover the full terminal-diameter-two enumerator and its clique-polynomial realization, or the combination of multipartite factorization, optimum exchange structure and rigidity beyond two parts.

## value

PASS

Counting all size classes is a natural refinement of the published semi-cutting minimization question. The factorization tells a future researcher exactly which local graph invariants control every coefficient and optimum, and the cone construction explains why real-rootedness from the bipartite or multipartite cases cannot persist under just the terminal diameter condition. The multipartite result describes all optima and their exchange graph, and tests sharpness of the published bound for each placement rather than merely reproducing that bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
