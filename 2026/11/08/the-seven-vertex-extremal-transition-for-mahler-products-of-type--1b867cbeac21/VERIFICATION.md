---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Reconstructed Ehrhart matching identity of Ohsugi–Tsuchiya n!vol(B_T)=2^n M(T); in each orthant the polar |y_i|+|y_j|<=1 becomes a Stanley order polytope under bipartition reflection, giving vol(B_T^polar)=2^n L(T)/n!. Both volumes use Euclidean normalization and n>=2 tree hypothesis. Independently enumerated all unlabeled trees for n=2..7 using networkx nonisomorphic_trees, an independent matching subset recurrence and topological-sort ideal recurrence: class counts 1,1,2,3,6,11, maxima M L 2,6,25,128,793,5760; at n=7 S222 (20,288,5760), P7 (21,272,5712). Inspected packaged Prüfer exhaustive 18,248 labeled trees script; no inference beyond 7 or from approximate hull check.

## originality

PASS

The matching Ehrhart formula and Stanley volume theorem are prior art, not new. The joint tree volume-product formula and sharp first maximizer crossover at 7 survive comparison with Kohl–Olsen–Sanyal broader perfect-graph Mahler experiments, which do not state this tree-specific order-7 optimum in the inspected full text.

## value

PASS

A natural polytope Mahler extremal problem has a sharp, provably first structural transition at 7 vertices, identifying a unique non-path optimum and exact small gap 1/105. Finite complete classification on natural tree families is substantive beyond a random numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
