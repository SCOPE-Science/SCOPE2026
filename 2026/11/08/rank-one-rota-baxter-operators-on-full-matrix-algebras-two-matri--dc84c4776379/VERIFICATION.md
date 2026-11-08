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

The reproducible command is `python3 verify_rank_one_rb.py`. It needs only the Python standard library and tests the original rank-one Rota–Baxter identity by evaluating matrix units; rank-one maps are represented by \(R(X)=\operatorname{tr}(BX)A\).

The checker exhaustively compares the matrix-pair classification and the original identity for all normalized nonzero tensor representations on \(M_2(\mathbb F_2)\) and \(M_2(\mathbb F_3)\). It separately checks every normalized representation on \(M_3(\mathbb F_2)\) against the algebraic criterion and compares the resulting type counts; 100 of these are also tested against the original equation. It evaluates the closed formula at two larger parameters without claiming exhaustive original-identity checks there.

The confirmed counts (nilpotent image / idempotent image / total) are \((3,12,15)\), \((8,48,56)\), and \((315,336,651)\), respectively. The additional formula evaluations are \((4160,3744,7904)\) at \((n,q)=(3,3)\) and \((56805,20160,76965)\) at \((4,2)\). The recorded final marker in `verification_output.txt` is `RANK_ONE_MATRIX_ROTA_BAXTER_EXACT_COUNTS_OK`.

These checks are finite and do not certify the theorem for arbitrary matrix order or field. That part follows from the exact rank-one algebraic reduction and standard finite-field subspace counts in `RESULT.md`.
