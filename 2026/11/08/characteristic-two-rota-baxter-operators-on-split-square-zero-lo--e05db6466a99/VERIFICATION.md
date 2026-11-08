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

# Independent finite computation and proof limits

The attached standard-library Python checker enumerates every linear map of \(A_m\) over \(\mathbb F_2\), for \(m=2\) and \(m=3\), and over \(\mathbb F_3\) for \(m=2\). It reconstructs multiplication of \(k\oplus V\), verifies the original weight-zero Rota–Baxter identity on all ordered basis pairs, and independently compares the parameter equations. In characteristic two it exhaustively constructs \(\mathrm{GL}_m(\mathbb F_2)\) and computes orbits of all valid operators. It also counts square-zero matrices of size four over \(\mathbb F_2\).

Expected exact outputs are saved in `check_output.txt`. The principal finite cases give \(16\) operators, \(6\) of index three, and five automorphism orbits over \(\mathbb F_2\) with \(m=2\); and \(176\) operators, \(84\) of index three, and six orbits over \(\mathbb F_2\) with \(m=3\). The odd-characteristic control gives \(33\) operators and none of index three over \(\mathbb F_3\) with \(m=2\).

Run `python3 verify_rb_square_zero.py` and compare stdout byte-for-byte to `check_output.txt`.

These computations are exhaustive only at the stated finite parameters, and do not prove an arbitrary-field claim, the general count, or the general orbit classification. Those conclusions are established by the algebraic steps in `RESULT.md`. No independent audit has been performed.
