---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Direct graph has 20 vertices, 30 edges, and dissociation faces precisely vertex subsets inducing maximum degree≤1 (equivalent to forbidding each length-2 path). Independent enumeration from induced degree and forbidden triples agreed on all 2²⁰−1 nonempty masks, with 53,670 faces and f-vector (20,190,1080,3975,9624,15050,14340,7505,1760,126). Deterministic 20-pivot matching yielded 26,823 pairs, one critical vertex and 23 critical 7-cells; independent full 335,460 directed-cover-edge DAG topological-sort visited 53,670 faces, so Forman integral Morse collapse yields wedge 23 S^7. For arbitrary n≥3, invariant faces are unions of antipodal pairs indexed by independent sets of C_n; oriented simplex sign gives reduced Lefschetz -I(C_n;-1)=-2cos(nπ/3). At n10 this is +1, and reduced H7 trace is −1, yielding +/− dimensions 11/12. No integral eigensublattice splitting asserted.

## originality

PASS

Closest published Möbius-ladder higher-independence results cover lengths 8–16, not length 20 or a uniform antipodal Lefschetz trace. Ordinary independence and matching studies of Möbius ladders use different face sets. The exact integral homotopy and all-length involution trace survive best-knowledge comparison.

## value

PASS

The Möbius ladder is a canonical highly symmetric cubic graph; its natural nonflag dissociation complex at 20 vertices has a genuinely nontrivial exact integral sphere wedge with an exhaustive acyclic matching. The uniform antipodal Lefschetz formula yields rational representation data invisible to face-count and ordinary Betti tables, motivating further equivariant classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
