---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The ordinary matching complex has face vector (12,42,44,9). Independently of the submitted Morse matching, each size-three matching extends to at most one size-four matching, because only two cube vertices remain. Collapsing a free triangle in each of nine tetrahedra leaves 35 triangles; a spanning tree of the one-skeleton identifies integral 1-cycles with 31 cotree coordinates. Unit-pivot elimination makes the remaining triangle boundaries onto on these coordinates, so reduced integral homology is Z^4 only in degree two. A distance-preserving permutation census obtains all 48 elements. An invariant matching is a union of edge cycles; each chosen cycle contributes one minus sign to the reduced Euler weight, with a further global minus sign. The resulting paired traces (4,2),(-2,0),(0,-2),(1,-1),(0,2) have multiplicities 1,6,3,8,6 in each parity and equal sign(diagonal action) times (number of fixed diagonals minus 1 plus geometric determinant). The ordinary quotient statement follows after barycentric subdivision by rational coinvariants, equivalent to invariants by averaging. No integral quotient claim follows. Independent replay: python -B /workspace/review_evidence/5_cube.py; output 5_cube.txt in the same directory. The uploaded script was not executed.

## originality

FAIL

Proved already covered by distinct October 18 and October 25 records on the same graph/complex and on the same actual 48 permutations. Their even-coordinate-flip convention is not the rotational convention but the character functions are identical. This is not a date-order inference about two same-day records.

## value

FAIL

The invariant of this natural complex would be valuable if unknown, but the exact elementwise values, integral group computation, and quotient implications are already available or are direct translations of them. The frozen verification contributes reproducibility, not a distinct scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
