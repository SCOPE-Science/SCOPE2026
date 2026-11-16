---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The executable `rhombic_erasure_certificate.py` is self-contained and standard-library-only; run `python3 rhombic_erasure_certificate.py`. It verifies the 48 signed-permutation actions and four disjoint defect orbits of sizes 6, 24, 12 and 3; directly substitutes four harmonic-coordinate null vectors into every retained vertex row using rational-pair arithmetic in \(\mathbb Q(\sqrt3)\); and independently enumerates all 1001 ten-vertex and 364 eleven-vertex subsets under the two valid reductions \(\sqrt3\mapsto10\pmod{97}\) and \(\sqrt3\mapsto49\pmod{109}\). A nonzero modular minor proves the same characteristic-zero minor is nonzero because the matrix entries lie in \(\mathbb Z[1/3,\sqrt3]\). The exact null vectors certify matching upper rank bounds for the defective orbits. The expected last output line is `QUADRATIC_RHOMBIC_ERASURE_CERTIFICATE_OK; four orbit sizes 6,24,12,3`.

The finite exhaustive enumeration is the entirety of the stated fixed-grid problem. It proves neither stability in noise nor broader geometric generalization, and no independent external validation has been conducted.
