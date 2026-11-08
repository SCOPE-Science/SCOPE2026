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

# Reproducibility and limits

Run `python3 verify_direct.py` in a Python 3 environment using only its standard library. It independently checks both maps for all cyclic lengths \(5\le n\le16\) and compares brute-force configuration testing against integer transfer traces. The last line should be `VERIFY_DIRECT_OK`; the captured output is in `verify_direct_output.txt`.

Run `python3 verify_symbolic.py` in Python 3 with SymPy available. It independently constructs the transfer matrices and complement-symmetry blocks and checks their characteristic polynomials with exact arithmetic, together with trace decompositions. The last line should be `VERIFY_SYMBOLIC_OK`; the captured output is in `verify_symbolic_output.txt`.

Proof of the general claims rests on the closed-walk bijection and the explicitly described finite matrices, whose determinant factors can be reconstructed by the symbolic script. Exhaustive enumeration stops at \(n=16\), and therefore is **not** itself a proof for all \(n\). Numerical eigenvalue approximations are illustrative; algebraic root separation is proved in `RESULT.md`. Reproducibility does not establish historical novelty or independent validation.
