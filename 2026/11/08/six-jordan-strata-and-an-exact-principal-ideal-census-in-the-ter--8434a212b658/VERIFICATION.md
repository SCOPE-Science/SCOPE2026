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

The reproducible test is `python3 checker.py` with Python 3.10+ and no third-party packages. The implementation constructs the original nine-dimensional algebra multiplication matrices from monomial exponents, computes the ranks of \(M_f\), \(M_f^2\) and \(M_f^3\) by field arithmetic, and derives distinct principal ideals from reduced row-space bases of the multiplication matrices.

Over \(\mathbb F_3\), it exhaustively checks all \(3^8=6561\) radical elements and all their generated ideals. The rank multiplicities are \(1,2,24,216,486,5832\) at ranks \(0,1,2,3,4,6\); the distinct proper ideal multiplicities are \(1,1,4,12,9,12\) at the same dimensions. Both match the proved formulas, including the total of \(39\) proper ideals.

Over \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\), it uses independent extension-field addition and multiplication tables to directly check 1064 deterministic cases: 40 canonical examples and 1024 pseudorandom elements. It verifies their predicted power ranks and vanishing cubes. The printed formulas for \(\mathbb F_9\) are symbolic predictions and have **not** been enumerated exhaustively; random tests are not a proof of generality. The proof in RESULT.md supplies the arbitrary-field argument and exact finite-field counts.

`verification_output.txt` contains the output from the actual packaged checker and ends with `TERNARY_GROUP_ALGEBRA_JORDAN_AND_PRINCIPAL_IDEALS_CHECKS_OK`. Neither this code nor the finite tests provide independent mathematical certification.
