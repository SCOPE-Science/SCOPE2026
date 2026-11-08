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

# Verification of the rank-vector formula

Two standalone source files accompany this result. Run `python check_orthogonal_annihilating.py` and `python check_orthogonal_formula.py` in a directory containing both source files. The former needs Python 3 and NumPy; the latter needs only the Python 3 standard library. Their exact captured terminal outputs are `orthogonal_check_output.txt` and `orthogonal_formula_check_output.txt`.

The direct checker constructs every symmetric coefficient matrix for a fixed orthogonal Gram form and converts it to a self-adjoint operator. It evaluates every square using literal modular matrix multiplication, computes exact modular ranks, then tests every ordered pair for zero multiplication and records the combined image rank. Both split and nonsplit four-dimensional ternary forms are exhaustively included, as are odd-dimensional three-spaces over fields of orders three and five. The four-dimensional full rank-vector histograms are compared with the theorem rather than merely with total counts.

The independent arithmetic checker uses integer Gaussian coefficients, the exact symmetric rank count, the polar-space isotropic-frame formula and subspace Möbius inversion; it compares every four-dimensional ternary rank-vector coefficient with literal-matrix totals. It also checks that summing all rank vectors agrees with the unrefined formula for dimensions four, five, six, tuple lengths two, three, four, and odd field orders three, five and seven.

Observed completion markers: `ALL_ORTHOGONAL_ANNIHILATING_CHECKS_PASS` and `ALL_ORTHOGONAL_FORMULA_CHECKS_PASS`.

The unbounded dimension, field-extension, and tuple-length claims follow from the proof, not from the finite checks. The code does not enumerate all tuples in these infinite parameter families. There has been no independent external audit or historical-priority certification.
