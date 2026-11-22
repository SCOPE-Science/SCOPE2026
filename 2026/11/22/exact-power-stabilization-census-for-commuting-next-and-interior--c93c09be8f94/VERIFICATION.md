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

# Reproducibility and scientific limits

Execute `python verify.py` using Python 3 with only the standard library. The program prints `VERIFY_OK 8158` if all assertions pass. It directly enumerates every total map and every valuation of the finite upper-set chain up to five vertices, testing the two-sided next/interior commutation without assuming the normal form. Independently, it generates binary-word normal-form maps up to twelve vertices, computes literal function powers to their first stable stage, and compares the exact two-parameter histogram to the claimed recurrence, rank marginals, attainable-time spectrum, and maximum-time multiplicities. The enumerated results are finite evidence only; the all-size proof appears in `RESULT.md`.

No external theorem prover or independent validation is asserted. A source-comparison search cannot prove publication uniqueness; earlier general transformation-semigroup iterate counts remain a residual bibliographic risk. The explicit finite-domain theorem avoids claiming results for all continuous Alexandroff maps or all temporal models.
