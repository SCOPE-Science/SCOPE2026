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

In the incidence graph, an outside cell sees the union of its two incident-edge stars, while a selected cell has d(row)+d(col)−2 selected neighbors. Opposite-part isolates obstruct domination; same-part isolates obstruct location through two cells in a common other coordinate. For distinct rows and columns equal nonempty signatures can use only the two cross edges, and any such edge is a single-edge component. One cross edge alone forces an isolated row and column; both give the ambiguity directly. Thus ordinary LD permits at most one isolate and at most one single-edge component, and totality excludes every single-edge component. This also accounts for a one-row complete graph and the zero LTD polynomial on 1×1. Two-sort labelled component removal and allowed reinstatement prove the EGFs and deletion of the unique single-edge component proves the factor mnz. For r+c nonisolated vertices, the maximum number of allowed components is min(r,c,floor((r+c)/3)); this is attained by starting with a row–column pair in each component, distributing one extra vertex to each and connecting each part as a tree. The edge lower bound is sharp for any permitted (r,c). The minimum is reached at (m,n−1), using m≤n and, when m=n, ceil(2(2m−1)/3)≥m. At any other support attaining the global minimum, equality in the edges-versus-components bound forces trees too. The bipartite tree formula then gives the exact optimum coefficient. For ordinary LD, allowing one component of size two gives floor((r+c+1)/3) in the component bound, attainable whenever it exceeds floor((r+c)/3) and r,c permit that many parts (one pair left unaugmented). This independently yields the stated one-cell penalty, including n=2m. Direct independent open-neighborhood enumeration on twelve small boards verified both predicates, coefficients in the 3×3 and 4×4 examples, and polynomial differences where both board sizes were included. For 5×5, a minimum has exactly one isolate and three 3-vertex components. The two part sizes force two stars of one type and one of the other; the count is 10·5!·4!/(2!^4)=1800.

## originality

PASS

The retained distinct claim is the all-rectangle incidence structure and paired size enumerators with the polynomial difference and forest-optimum census, beyond the known ordinary minimum and the two-row LTD subfamily. Both inspected two-row polynomial records genuinely cover the two-row portion and are credited. No inspected statement supplies the needed general incidence-plus-forest classification.

## value

PASS

A complete two-parameter signature characterization gives all-size counts and a deletion bijection between the two notions, not just a minimum. The sharp tree equality class explains every optimum and yields exact labelled counts with a precise condition for paying one cell for totality. These are reusable structural and enumerative results on a canonical product, beyond the known two-row tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
