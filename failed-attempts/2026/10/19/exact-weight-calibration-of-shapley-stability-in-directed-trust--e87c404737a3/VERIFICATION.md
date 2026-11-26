---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

If r_j counts arcs to j in S from outside S, the slack of the proposed core vector is the sum over j in S of w_j(r_j−1_{r_j>0}); this is nonnegative and vanishes on each vertex complement, forcing uniqueness by efficiency. The number of incoming neighbors before a recipient is uniform on 0,…,d_j, so its Shapley share of its own worth component is d_j w_j(1−f(d_j)), and the exchangeable in-neighbors split the rest. With h_i=d_i w_i f(d_i) the deviation is (Q−I)h. Irreducibility, f(1)=0, f(d)>0 for d≥2, and scaling of h give the three cases including the upper weight cap. An independently checked example on four vertices with every ordered arc except 0→1 gives d=(3,2,3,3), π=(3/16,1/4,9/32,9/32) and calibrated w=(1/3,1,1/2,1/2). For common reciprocal weights the deviation is a signed graph Laplacian; pairing terms along edges yields the energy identity and f strictly increases with degree. In an irregular connected component a path from a minimum-degree vertex to one of larger degree furnishes a minimum-degree vertex adjacent to a larger degree, with positive deviation; tightness on its complement gives the claimed blocking. Isolates contribute zero. The frozen verifier was inspected, not executed.

## originality

FAIL

Existing indexed coverage establishes the central positive inverse calibration, including necessity and weight ratios, in a more general setting for d_i≥2. The same calibration in different coordinates does not qualify as a distinct main finding. The degree-one cases and explicit reciprocal certificate are not assertions of that indexed result; the displayed catalog date is later, and this assessment of present coverage does not establish historical priority or direction of derivation.

## value

FAIL

Positive inverse design is a meaningful objective, but its central classification and proof mechanism are already supplied by equivalent published coverage. Relative to that coverage, the extra degree-one cases are immediate fixed-vector boundary cases, and the reciprocal rigidity and blocking derive from the usual graph Laplacian energy and the already-tight vertex complements. The residual observations are useful explanations, but do not establish a distinct substantive finding of the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
