---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For r≥3 shores, any r-clique must pick a vertex from each shore. Deleting E⊆A1xA2 yields CF_r as iterated homotopy pushout of two simplicial cones, naturally Σ^(r-2)Ind(K_{A1,A2} minus E). The neighborhood containment N(u)⊆N(v) gives a free simplicial pivot pairing, deleting v. For a bipartite deleted forest, remove vertices isolated in F and then nontrivial-tree leaves via legal folds until c isolated missing edges remain. Complement independence complex becomes two full shore simplices connected by c parallel edges, giving S0 (c0), point (c1), wedge^(c-1)S1 (c≥2); suspension gives stated integral types. For a nested matching-deletion filtration, c independent bridges attach sequentially; first kills the reduced H0 generator, subsequent bridges create primitive H1 generators, naturally shifted by Mayer-Vietoris to degrees r-2 and r-1. Six-cycle deletion instead yields perfect matching complement and Ind ≃S2, hence CF_r≃S^r; demonstrates essential forest hypothesis. Inspected verify_forest_clique_free.py enumerates all 328 bipartite forests on 3x3 with mod2 homology/fold tests plus higher-partite/cycle tests. Independent small face-Euler check confirms c0,c1,c2,c3 and the six-cycle boundary.

## originality

PASS

Ghosh–Selvaraja establishes clique-free complexes and shellability but does not classify all missing bipartite forests or integral persistence. Previous triangle-free joins cover an overlapping suspension special case, and a published two-degree matching-defect formula has different threshold q strictly less than total number of shores, while the present theorem has q=r, arbitrary forest shapes and a c-component classification. The general fold lemma is explicitly prior. Originality is the combined forest-shape invariance and exact persistence, not an uncredited suspension.

## value

PASS

Changing an arbitrary missing forest without changing its count of edge-bearing components is a nontrivial shape-invariance theorem in natural forbidden-clique topology. Full integral homotopy and persistent inclusion maps supply exact natural invariants beyond finite mod2 experiments; six-cycle boundary pinpoints a sharp failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
