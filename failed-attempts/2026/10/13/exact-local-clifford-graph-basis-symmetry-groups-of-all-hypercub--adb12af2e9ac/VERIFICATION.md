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

Graph-basis preservation is equivalent to preserving the unsigned graph stabilizer space {(x,Ax)}, since its joint eigenspaces are the graph-basis rays. The stated diagonal-block symplectic equation and local determinants follow. Neighbor pairs force opposite-parity a/e values and distance-two pairs have two common neighbors, forcing their b values equal. Distance-two moves connect each parity class, also allowing the vacuous singleton classes in d=1. The diagonal gives c_v as the sum of neighboring b values. This yields the determinant rw+(d mod 2)st=1, exactly six inverse-transpose pairs in odd dimension and four independent shears in even dimension. On label vectors the linear part is diag(e)+A diag(b), and a Pauli gives a translation. Its diagonal recovers e and each column has a neighbor entry recovering b, so the linear action distinguishes the patterns, with the other bits determined. Every translation occurs, giving the stated orders. The two attached finite verification programs were inspected, not executed; the all-dimensional argument was checked symbolically.

## originality

FAIL

The strongest earlier source is Englbrecht–Kraus, not merely a general graph-equivalence criterion. Its exact one-copy Clifford symmetry classification of graph states, up to local Paulis, evaluates to the full claimed list by the parity and common-neighbor identities of the cube. The graph-basis reformulation and label count are immediate consequences of this list, not an independent extension beyond it.

## value

FAIL

The natural symmetry question is useful, but the claimed contribution evaluates an exact general classification by the elementary parity and common-neighbor rules of a cube. The label count is the immediate affine extension, not a surviving independently motivated new invariant, so the correct specialization does not supply independent scientific value under the stated criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
