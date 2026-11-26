---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independent replay: python /workspace/branches/audit5.py. The program generates the 1440 column-ordered six-rook words and 3600 deleted-column equations from the capacities, and the 15-by-20 inclusion equations from subsets. The orientation sign (-1)^j is constant within each boundary row and does not change its kernel; the separate column-action sign is retained. The ranks modulo 101 are 1435 and 15, giving rational lower bounds. Lifting the free-coordinate vectors to integers, checking every original integer boundary equation, and using their identity projections proves both upper bounds and integral saturation. This gives a different pair of integral bases. All three row generators act trivially and the column action on the entire basis is verified. Using only a generating 6-cycle and transposition gives a 50-equation intertwiner system of rank 24 over Q. Its primitive integer generator has determinant -162 and Smith factors (1,3,3,3,6), reproducing the reported quotient in the independent bases. Primitivity on a rational line forces every integral map to be an integer multiple, hence index 162|k|^5. There are no higher simplices, so the top kernel is H5 integrally. Young's rule for the subset modules and surjectivity of W over Q leave precisely S^(3,3) in L, and the nonzero determinant transfers the representation to K. The frozen proof/checker and captured matrix evidence were inspected, not executed.

## originality

PASS

The supported distinct contribution is the primitive integral comparison with its cokernel and minimal index for this natural pair of lattices, not the rational representation framework, the incidence lattice by itself, or the already known nonequivariant homotopy type.

## value

PASS

The pair is motivated by the structured row-capacity complex and its rationally identical column-subset model. The explicit obstruction shows that a natural replacement by the incidence kernel cannot be made integrally equivariant. The Smith factors distinguish the 2- and 3-primary defects and give a precise benchmark for characteristic or coefficient-sensitive comparisons, beyond the known homology ranks and rational type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
