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

The mathematical derivation is given in RESULT.md, including the exact arch/incomplete-remainder bijection and a fixed-type coupling argument. Reproduce the finite verification by running `python3 verify.py` from this directory. It uses no external packages. Its successful terminal line is:

`VERIFY_OK words=48069, direct_indices=48069, coefficient_cells=1586; extreme and first-moment identities tested`

The finite enumeration covers the complete sets of words over two letters through length 13, three through length 8, and four through length 7, including the empty word and words missing ambient letters. The proof, not the finite test, supports the statements for unbounded parameters. No central limit theorem or quantitative convergence rate is asserted.
