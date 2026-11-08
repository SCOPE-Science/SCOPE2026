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

# Verification details

The complete proof in `RESULT.md` has no machine-dependent lemmas. In particular, marker-pair difference uniqueness follows from elementary divisibility, the support of each square is classified by its only two marked positions, and continuation is stopped by a guaranteed unmarked position.

The standalone deterministic Python 3 test `verify.py` was run with the result:

```text
VERIFY_OK bases=2..8 periods=1..150 marked_square_windows= 372192 square_occurrences= 223 maximal_length_checks= 3376
```

The test compares formula-predicted starts with direct equality of the two halves for every searched base and period. It checks all claimed continuation lengths, the first mismatch, and any smaller period. The search is finite and does not assert exhaustive verification beyond its specified bounds. The arbitrary-base, arbitrary-scale theorem follows from the proof, not from extrapolating the search.
