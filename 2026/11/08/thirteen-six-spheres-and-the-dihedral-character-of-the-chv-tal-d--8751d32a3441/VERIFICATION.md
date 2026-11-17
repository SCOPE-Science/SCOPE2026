---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Independently reconstructed the specified 24-edge twelve-vertex Chvátal graph and the closed-neighborhood avoidance predicate defining its dominance complex. Exhaustive enumeration of all 4096 subsets gives 3098 nonempty faces, f=(12,66,220,495,780,840,544,141). Exact discrete-Morse pairing in stated pivot order produces 1542 pairs, one critical vertex and thirteen critical six-cells. Independent full topological sort certifies acyclicity across 16648 nonempty Hasse covering edges, so Forman yields integral ∨^13S6 without torsion ambiguity. For the source’s two explicit D4 automorphisms r,s, independently calculated signed reduced Lefschetz characters (13,-1,1,-1) on rotations and (-3,1,-3,1) on reflection coset, giving L_{1,1}+2L_{1,-1}+L_{-1,1}+3L_{-1,-1}+3E by exact character inner products, rank 13 and one invariant. The source script also specifies an exhaustive automorphism enumeration returning exactly eight, which was inspected but not independently rerun.

## originality

PASS

Best-of-knowledge exact integral Chvátal dominance complex and full D4 homology character were not found in targeted Resultary searches or inspected primary general theorems. The earlier Chvátal ordinary independence/open neighborhood S² and 2-independence S³ concern different simplex rules and homology degrees; no direct Alexander dual specialization computes Dom(G). General chordal/forest dominance results cannot include the nonchordal Chvátal graph and connectivity inequality is only a bound.

## value

PASS

The Chvátal graph is a canonical minimal four-chromatic triangle-free regular graph, a natural exact test object outside chordal dominance formulae. Its integral 13-sphere homotopy and complete faithful dihedral rational character, including one invariant line, are genuinely motivated topological/equivariant invariants; the finite-object focus does not make this a routine textbook deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
