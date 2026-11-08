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

# Reproducible verification
Run `python verify.py` with Python 3 (standard library only). The program exhaustively enumerates every permutation of sizes 3–8, weights it by the exact rational record-bias parameter, and compares the exact probabilities and finite peak expectations for five parameter choices. The recorded output from this package's program was `VERIFY_OK 270 exact assertions`.

The infinite-domain theorem follows from the independent initial-rank bijection, elementary conditional probability, a finite polynomial identity, and an exact telescoping identity, not from finite enumeration. No external or independent audit was performed. The checked parameter set is finite; the algebraic derivation covers every real positive bias.
