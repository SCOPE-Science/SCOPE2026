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
# Verification of the orthogonal tuple classification

The algebraic proof identifies the split orthogonal Lie algebra with two commuting copies of \(\mathfrak{sl}_2\), proves the square-zero dichotomy for individual matrices, and reduces all tuple solutions to choices of nilpotent lines and scalars. The finite-field count follows from the \(q+1\) points on a nonsingular conic and inclusion-exclusion. The nonsplit rational obstruction follows from even rank and Witt index one. The geometric components are obtained as products of irreducible nilpotent-line cones; this is an algebraic proof, not a computational certificate.

Run `python3 check.py` with Python 3.8 or later. It uses only the Python standard library. The script constructs actual orthogonal Lie matrices \(X=H^{-1}S\) for all alternating matrices \(S\) over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\). For every actual square-zero matrix, it checks the rank. It then computes all pairwise products and commutators and exhaustively enumerates ordered commuting tuples for \(r=2,3,4\) over \(\mathbb F_3\), \(r=2,3\) over \(\mathbb F_5\), and \(r=2\) over \(\mathbb F_7\), for both Witt types. Its output must equal `check_output.txt` and end with `ALL_ORTHOGONAL_COMMUTING_SQUARE_ZERO_TESTS_PASS`.

The computational checks do not directly test nonprime extension fields, the full geometric component scheme, or independent originality. All such claims depend on the written proof, and the independent audit remains unperformed.
