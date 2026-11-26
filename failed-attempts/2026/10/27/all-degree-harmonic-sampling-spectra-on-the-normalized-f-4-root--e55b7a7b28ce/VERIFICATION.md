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

With probability surface measure, the zonal kernel is a multiple of U_ℓ and its diagonal is dim H_ℓ=(ℓ+1)^2; U_ℓ(1)=ℓ+1 fixes the multiple. Dividing the evaluation rows by √(ℓ+1) yields the claimed Gram. Direct dot products give 0, ±1/2, ±1/√2 off the diagonal. Their trigonometric periods divide 4,6,8; exactly the diagonal increases under a 24-step shift. Independently constructed all signed representatives, computed U_ℓ by exact recurrence in Z[√2], and used integral similarities and exact characteristic polynomials (not the frozen power-sum method). All 24 rows in RESULT.md matched; the first shift checked entrywise in the similar matrices. Positivity and the universal shift imply full rank for ℓ≥24; the table gives the smaller ranks and the two scalar residues. At degree 7 the ratio of squared singular values is 12/6. Replay: python /workspace/review_checks/f4.py (SymPy); output /workspace/review_checks/f4.txt. The frozen checker was inspected, not executed.

## originality

FAIL

The full spectrum, not just the rank, is mechanically determined by the classical SU(2) branching law for the binary octahedral group and ordinary character projection. With a quaternion coordinate identification the kernel is exactly the restricted Sym^ℓ character. Branching supplies every eigenvalue and multiplicity, including zero sectors, after the elementary antipodal compression. This is verified prior mathematical coverage, not an assertion that the numerical table was previously printed. There is also material indexed rank overlap for the identical sample geometry.

## value

FAIL

The exact spectral question is natural, and the table may be useful for reference. But its full content is routine recomputation of a classical branching recurrence after recognizing the standard quaternionic group, with no scientifically distinct spectral invariant or structural result beyond the central character projection and elementary period calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
