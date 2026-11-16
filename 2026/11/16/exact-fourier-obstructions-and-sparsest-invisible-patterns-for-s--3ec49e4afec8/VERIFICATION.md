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

# Verification record

Run `python verify_hexagonal.py` in a directory containing the standalone script; Python 3 standard library is the only dependency. The script exhaustively verifies 162 partitions, 176400 modular root pairs, 48 complete cyclotomic zeros, the seven-primary two-line condition, and all 49 twelve-support crosses by integer convolution and the arbitrary-erasure component formula by direct algebraic proof and 201 exact-rational rank comparisons. The maximum 37 matching-value cells is independently checked over all nontrivial integer partitions of seven. The mathematical proof is in `RESULT.md`; execution checks the finite certificate, not the infinite quantifier on its own. The certificate has been run successfully. The self-review is passed; independent audit is not performed.
