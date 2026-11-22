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

The standalone `verify.py` uses only the standard Python library and prints `VERIFY_OK 75108 finite exact assertions` when run using `python verify.py`. It exhaustively checks the parity equivalence for every unrestricted matching through six chords, the conditioned matching distributions through eight chords, exact simple-chord moments and binomial inversion, and all observed closed-interval component obstructions. It also verifies the rational moment comparison bound for a finite grid through 65 chords.

The all-size proof is the counting-plus-coupling argument in `RESULT.md`. Finite enumeration alone does not verify the infinitely quantified total-variation rate or historical priority. The proof's closed-interval witness is independently reasoned via noncrossing crossing components and is additionally tested exhaustively; an external mathematical audit has not been performed.
