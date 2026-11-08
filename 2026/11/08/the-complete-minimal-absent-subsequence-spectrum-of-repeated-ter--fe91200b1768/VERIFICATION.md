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

The proof relies on greedy embeddings and exact nine-state identities in `RESULT.md`. With `verify.py` and `certificate.json` in one directory, run `python3 verify.py` using Python 3 and the standard library. The certificate checks every entry of \((I-T)H=QB\), the scalar identity \(AH=N\), and the invertible constant term of \(Q\); these finite polynomial identities establish the claimed rational expression for all lengths and repeat counts. Direct brute-force comparisons additionally cover 103,784 candidate-word tests, with the 12-step coefficient cross-check and ten exact total counts. Computations were replayed from these exact files and passed. Finite testing alone does not prove an infinite family. Full scholarly independent audit has not been performed.
