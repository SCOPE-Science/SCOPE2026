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

The standalone Python 3 file `verify.py` enumerates the complete square-zero candidate pool for three small ambient matrix rings: \(M_2(\mathbb F_4)\), \(M_3(\mathbb F_3)\), and \(M_4(\mathbb F_2)\). The field \(\mathbb F_4\) is implemented through the irreducible polynomial `0b111`. Matrix multiplication and Gaussian elimination are implemented directly, without external libraries.

For every tested fixed matrix \(A\), the code computes \(\operatorname{rank}A\), \(\operatorname{rank}(A^2)\), enumerates every candidate \(B\) satisfying \(B^2=AB=BA=0\), and checks each pair \((\operatorname{rank}B,\dim(\operatorname{im}A\cap\operatorname{im}B))\) against the closed formula. It also checks the predicted maximum rank. In particular, \(J_3(0)\oplus0\) and \(J_2(0)\oplus[1]\oplus0\) have equal two-step rank data over \(\mathbb F_2\) and the same tested distribution.

Run `python verify.py`. The expected terminal line is `VERIFY_OK`. The enumerated square-zero candidate pool sizes are respectively \(16,105,316\). These finite checks are not a proof over all finite fields. The general correctness argument is the subspace-and-kernel bijection in `RESULT.md`.
