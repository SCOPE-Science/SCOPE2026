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

# Reproducibility

Run `python3 verify.py` using Python 3.8 or newer; it uses only the standard library. Successful output is `BWT_SINGLETON_RIGIDITY_VERIFY_OK`.

It exhaustively lists all unclustered words with content \((m,m,1)\) for \(2\le m\le10\), checks a separate binary-deletion generator, and verifies the exact two-word fixed-point-free classification. The reduced generator covers every admissible word at all checked parameters through \(m=100\); it also rechecks the Hamming formulas, cyclic permutation criterion, modular conjugacy over every odd modulus in that range, and four inverse BWT reconstructions.

The all-parameter proof is in `RESULT.md`. Neither a finite experiment nor any computational timeout is treated as an infinite proof. Independent mathematical audit has not been performed.
