---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Undirected Hamilton cycles are rooted at binary vertex 0000; DFS over all injective cube walks, closing at the root, enumerates 1344 edge masks without double counting. Every one of 24 coordinate faces is tested for two opposite used edges and the symmetric-difference mask is retained iff Hamiltonian. An independent newly written DFS/square-scan graph program enumerated all 1344 states, all 1920 edges, exactly 240 isolated vertices and one connected 1104-state component, and BFS from each of 1104 sources yielded radius 10, diameter 12 and eccentricity counts 10:96,11:192,12:816. It reproduced degrees 0:240,1:384,2:192,4:288,8:240 and nine orbit sizes 48,96,96,384,192,96,192,48,192 under 384 affine coordinate automorphisms; all neighbor-orbit vectors were constant on each orbit. Those finite exhaustive operations are an exact proof for this finite object, not a statement for general Q_d.

## originality

PASS

The 2018 primary publication already defines the identical subsequence inversion / coordinate-square switch and reports isolated Gray-code types in dimension four; Gilbert 1958 gives nine orbit types. Inspection of the 2018 full open text and Table 2 found the prior 3 isolated symmetry types of nine, but not the exact 1104 mobile-state connectedness, all-pairs distance spectrum, radius/diameter or nine-by-nine equitable adjacency quotient. Resultary semantic search found metric results for perfect-matching flip graphs on Q4, which are different configurations. On available evidence this combined full Hamilton-cycle flip graph metric and quotient is original.

## value

PASS

A complete metric and orbit quotient of the natural reconfiguration graph for cyclic Gray codes answers exactly which nonfrozen codes communicate and how many square inversions suffice (at most 12), and distinguishes local transition types. A specific meaningful finite classification remains useful even without an all-dimensional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
