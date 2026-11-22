---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For a finite-dimensional real centrally symmetric polytope, its norm additivity ∥u+v∥=2 occurs exactly when u,v lie on a common exposed facet. Every vertex can be uniquely exposed by a norm-one functional and every relative-interior facet point belongs to exactly its facet. Sufficiency: choose a norming vertex of f and an orbit facet containing both that vertex and gy; a common supporting functional gives ∥v+tgy∥=1+t for arbitrary t=∥T∥>0. Necessity: if a vertex misses the orbit of a facet, the rank-one f⊗y with f uniquely exposing v and y in relint(F) cannot satisfy norm 2 for any g; compactness and equality in triangle inequality force x=±v, yielding contradiction. The action of the isometry group is faithful on the vertices, hence finite. For a regular even N-gon, each subgroup acts on facets by step-L translations and optionally j↦s−j; every pair of adjacent facet residues meets all orbits iff L≤2. Cases L=3,4,≥5 exclude all reflective and nonreflective subgroups, proving R² membership exactly. Isometry group is dihedral (can prove orthogonality from the second moment matrix of regular polygon vertices). This argument treats t>0, N=4, arbitrary even N, and arbitrary real polyhedral dimensions without relying on finite extrapolation.

## originality

PASS

Best-of-knowledge PASS for the combined precise finite vertex-facet incidence criterion and complete subgroup classification of every regular even-gonal plane. Dantas–del Río–Raunig introduce the underlying G-Daugavet property and give a general slice/invariant-hull characterization plus a C8 octagon example. Their stated results do not classify all dihedral subgroups, especially C_{N/2}, nor establish the exact necessary and sufficient two-step rotation threshold; the new face and subgroup arguments are substantive. Resultary returned the same submitted finding (excluded as independent predecessor) and unrelated Euclidean norm profile work, not direct coverage. There remains priority risk from implicit or unindexed polyhedral specialization.

## value

PASS

The result makes the infinitely quantified rank-one group Daugavet equation exactly decidable by a finite geometric incidence relation for every real polyhedral norm. On regular even polygons it resolves a natural minimal-group question left open by the full-rotation example: an order-N/2 cyclic subgroup is sufficient and necessary inside every qualifying dihedral subgroup, with reflections unable to substitute. This is a structural classification and exact boundary, not only a computational or renaming exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
