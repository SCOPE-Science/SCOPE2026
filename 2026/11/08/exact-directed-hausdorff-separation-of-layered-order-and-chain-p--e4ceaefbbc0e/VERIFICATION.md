---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For k>=2 antichain layers the chain polytope is a coordinatewise downward-closed intersection of chain inequalities, so the farthest order point is the unique all-ones vertex. Permuting coordinates inside each layer reduces its Euclidean projection to strictly convex water filling with t_i=(1-lambda/m_i)_+ and sum_i t_i=1. Reverse squared distance maximizes at an antichain vertex, whose order-polytope isotonic projection pools a selected layer subset of size a with U_i higher coordinates, giving a U_i/(a+U_i). Strict monotonicity in a yields the stated max over full layers; two-layer equality and strict k>=3 forward dominance follow from the quadratic comparison, and k=1 is handled separately. Independent exact/rational water-filling calculations yielded (1,2,3): (h(O,C)^2,h(C,O)^2)=(11/5,6/5), reversed (3,2,1):(11/5,3/2), equal unit layers k=3:(4/3,2/3), k=4:(9/4,3/4). These sample tests corroborate the unrestricted convex proof, not replace it.

## originality

PASS

The direct canonical-position Euclidean Hausdorff problem is not equivalent to Ehrhart equality, f-vector inequalities, edge counts, edge lengths or 1-skeleton graph diameter. Accessible abstracts of Ahmad–Fourier–Joswig, Freij-Hollanti–Lundström and Lee address those other invariants, not the exact directed Hausdorff separation; no stronger result was identified in Resultary. Because complete texts of the closest papers could not be read here, this is a best-of-knowledge result with noncoverage NOT inferred from snippets alone.

## value

PASS

Stanley's order and chain polytopes are a canonical equi-Ehrhart pair; exact coordinate-space metric comparison quantifies a geometric discrepancy invisible to their lattice-point enumerators. The water-filling and suffix-mass formulas determine both directions for every fully layered poset, and the sqrt(k-1) unbounded ratio is a meaningful structural phenomenon, not merely a numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
