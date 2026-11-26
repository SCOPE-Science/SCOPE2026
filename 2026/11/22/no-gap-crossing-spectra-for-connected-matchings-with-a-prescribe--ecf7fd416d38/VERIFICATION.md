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

A return to height zero cuts the matching into two nonintersecting chord families. For primitive words FIFO attains K and gives a Hamiltonian path because o_(i+1)<c_i at every nonfinal closer. For the lower endpoint, removing an interior UD from UvD leaves a primitive word and a strictly positive height at the insertion gap. Split the first-ending spanning arc (a,b) at the two inserted positions. The new arcs cross each other; a chord wholly on one side keeps its incidence with the piece on that side. Every other spanning chord ends after b, so it meets exactly the first piece if its opener follows a, and neither piece otherwise. Thus the previous tree vertex is split into adjacent vertices with each old incidence assigned exactly once, proving the tree endpoint including the n=1 base case. For interpolation, K−c equals the inversion count of the opener ranks in closing order: every missed available crossing corresponds to a still-unclosed older opener. Swapping adjacent inverted ranks is valid and lowers inversion count by one. For nested positions a<b<c<d, the two original interval-membership vectors on the five regions are 00,10,11,10,00; after replacing with (a,c),(b,d) they are 00,10,11,01,00. Every formerly separated pair of regions is still separated by at least one interval, so every previous neighbor attaches to the new mutually crossing pair. Other adjacencies are unchanged. Consequently bubble sorting maintains connectivity and visits each count exactly up to K, while every connected graph has at least n−1 edges.

## originality

PASS

The precise refinement that survives comparison is the support for the connected subfamily in each fixed opener fiber, including a tree with those openers and connected monotone swaps from that tree to the FIFO maximum. Neither the known lower bound for arbitrary connected diagrams nor the elementary unrestricted fixed-Dyck-word product determines that refined support. No distinct indexed result or inspected primary theorem covers it.

## value

PASS

The fixed-opener refinement keeps a natural Dyck-path constraint while imposing crossing-graph connectivity, a global rather than local restriction. The exact interval and tree construction show no losses beyond the universal lower bound on each feasible fiber; FIFO and the connected monotone swap path provide constructive extremizers and intermediate counts. This is usable support information for future enumerations of connected diagrams refining by opener set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
