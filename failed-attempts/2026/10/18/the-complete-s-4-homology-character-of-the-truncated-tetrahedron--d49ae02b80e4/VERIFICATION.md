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

The graph vertices are ordered pairs of distinct labels. Its only triangles are the four fixed-first-coordinate triples, because reversal edges are a matching and each distinct pair of triangles has only one reversal edge between them. An automorphism must permute the triangles and their six connecting edges, and this determines each vertex uniquely. Thus the specified S4 action is the full graph action. Inspected the frozen face enumeration, cover pairing, acyclicity test and character calculation. Independently ran `python3 /workspace/checks/5.py`: a fresh matching enumeration gave the stated face vector, and unit pivots in the augmented integer simplex boundaries reduced the complex to exactly 22 surviving generators in degree 3, verifying free integral homology and absence of other groups without assuming that vanishing rational ranks exclude torsion. For the character the reproduction builds the orbit compatibility complex: an edge orbit can appear only if internally a matching, and selected orbits must have disjoint vertex supports. A matching with r included edge orbits contributes (−1)^(r−1) to fixed-point Euler characteristic. Enumeration on all 24 elements and conversion by χ_3=1−L give (22,0,2,−2,−2). The exact five class-weighted inner products give (0,1,3,2,3); averaging over the even classes gives (22+6−16)/12=1. The tested integral result is about groups, not an integral Specht-module decomposition; the Morse matching is nonequivariant.

## originality

FAIL

The strongest distinct indexed primary result gives the identical rational character, Specht decomposition and invariant consequences for the identical graph and group action. The previously known integral sphere wedge is already explicitly excluded from novelty and supplies no surviving increment. Exact equivalent coverage in the present corpus is established; the November catalogue date does not make that record prior art for the October record, and no finding about historical priority is made.

## value

FAIL

The object and action are natural, and the precise character would distinguish symmetric from merely ordinary homology in a way that a user could need. For acceptance as a distinct narrow exact invariant, however, that precise fact is already available in the exact indexed comparison, including both invariant dimensions. The frozen result offers no additional invariant beyond it, and no new useful nonequivariant result beyond the earlier wedge. This does not say that the character is intrinsically uninteresting or that the later record was historically first.

The dated certificate retains the supplied scientific assessment, sources and limitations.
