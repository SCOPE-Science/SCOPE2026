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

Execute `python3 verify.py` using the standard Python library; exact output is embedded as `verification_output.txt`. For each of five small commutative truncated branch algebras, the program lists every RREF subspace of the radical, tests ideal closure under each algebra generator, and exhaustively compares the actual span of products of basis vectors against the predicted capped-threshold Schur-code span. The same program independently tests the zero-product iff all-caps-crossed condition. The code computes finite cases only; the unrestricted theorem follows from the proof in `RESULT.md`.

No external mathematical audit or computational certification of the infinite family was performed.
