---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The repaired theorem retains exact recognition width four, without the separate symmetric-design classification. Expanding S in clauses 1–4 binds a local w where only x,y,z are used outside the abbreviation. The two other clauses use no S. Clauses 1–3 make S an equivalence with exactly two classes, and clause 4 makes those classes independent. Equality-or-common-neighbor gives existence for distinct same-side pairs; clause 6 gives uniqueness. Degree at least three lets one choose two fresh points on each of two lines through a point; the lines meet only at the original point and any triple of the four new points has two on one line and one off it. This gives a quadrangle, so the finite structure is a nondegenerate projective plane; the converse follows from the plane axioms. In the two fourteen-vertex witnesses, same-side anchors give opposite-side cell sizes (1,2,2,2) and (2,2,2,1), respectively. With opposite-side anchors each degree and nonneighbor set has size at least three, so excluding an occupied vertex never blocks an adjacency bit. Matching side, equality and adjacency survives every move. The block complement fails uniqueness and is a nonmember, which proves sharpness at arbitrary depth. The original broader design proof is correct as well: v−2r+λ>0 and λ<r imply v−r≥2, so the opposite-side case has its needed fresh nonneighbor. Syntax, semantic and pebble scripts and their recorded output were inspected; they corroborate finite cases only and were not executed. The repaired RESULT.md supplies the all-graphs proof and direct witness check.

## originality

PASS

PASS for the repaired ambient class-recognition result, not for the original independently asserted design collapse or Fano/complement equivalence. Both latter assertions are covered by the distinct November 2 indexed theorem on nontrivial symmetric designs. The corrected files remove the separate design claim and explicitly credit the known lower bound. The retained contribution is the closed four-name pure-graph recognizer for the entire finite projective-plane class and the resulting exact width using the known obstruction. The strongest other inspected statements concern equivalence within a preselected family, fixed quantifier rank, or extremal or already bipartite graph characterizations. They do not supply that ambient four-name definition.

## value

PASS

The repaired result answers a natural exact recognition question about a full, standard graph class. The four-name formula defines the missing sides internally and verifies nondegeneracy uniformly over arbitrary input graphs and over plane orders and coordinatizability. Combined with the known obstruction, it shows exactly how much bounded-variable information is needed for class membership; it is more than the separation of two graphs or the recomputation of known design parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
