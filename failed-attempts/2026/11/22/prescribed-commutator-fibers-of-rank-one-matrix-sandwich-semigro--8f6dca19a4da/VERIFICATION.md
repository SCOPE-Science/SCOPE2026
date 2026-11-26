---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Factor A as a nonzero column times a nonzero row; independent base changes reduce it to E11 while preserving the predicates and transporting fibers bijectively. In this basis the product difference is UJV with shared first-row/first-column data t and independent lower blocks supplying q^{2h} lifts. The top-left coefficient vanishes and rank is at most two, including characteristic two. In rank two both factors have full rank. Both zero axes force t=0 and the usual GL2 number of factorizations; exactly one zero axis is impossible; both nonzero axes with zero corner impose one nonzero determinant value, giving an SL2 coset. For the terse rank-one step at line 64: if t is nonzero and the first row vanishes, every column of V is in ker(tJ)=span(t^T). A vanishing first column then forces UJt^T=0, hence the entire target is zero. Thus rank one with both axes zero really does force t=0. Count lower-block factorizations by the dimension of the first factor's image (one or two) to get the claimed fiber. With one zero axis and one nonzero axis, t is nonzero, one factor is forced by that axis and the other has one linear condition per lower row (or column). A rank-one target with both axes nonzero cannot have corner zero. The zero count splits into t=0 (unconstrained lower-block zero-product pairs) and t nonzero (q^{alpha+beta} solutions per such t, given the two vanishing axes). The sum gives exactly equation (26). All target counts follow by the rank-one scalar quotient, the standard rank-two block count, and (for both axes nonzero) q^{alpha+beta-1} lower blocks per nonzero axis pair. To see the last count directly, for Z=(0,r;c,D) with c,r nonzero, rank two means D=c s+t r; the map (s,t) to D has a one-dimensional kernel. Independent enumeration matched every target in (2,2,2), (2,3,3) and (3,3,3) and the target-class counts; at (3,3,3) sorted in the table's order the counts are 32,72,72,48,1728, with reduced rank-two fiber sizes 48 and 24. The zero fibers were 88,29889,6987465 respectively.

## originality

FAIL

The central prescribed-target result is already stated by the distinct same-date rectangular-band record e74f328cc322, in an exactly equivalent coefficient algebra. All nonzero rank-one sandwiches are isomorphic to the all-ones sandwich, so changing the middle matrix is not a genuine generalization. The added target-count column is real additional printed content, but is obtained by elementary rank stratification (including one affine block count), not a distinct substantive result. The November 2 aggregate census establishes only earlier partial overlap. This conclusion is about coverage and lack of a separate established contribution, not relative chronological precedence between the two same-date originals.

## value

FAIL

The GL2/SL2 distinction is an informative part of the shared classification, but is not an additional invariant obtained by reformulating it as rank-one sandwich multiplication. The surplus target counts come from ordinary rank-one vector choices, ordinary rank-two matrix counts and one affine block dimension. No new distinct classification, meaningful boundary, or nonmechanically implied exact invariant remains to support the separate record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
