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

# Exact finite verification

Execute `python3 verify.py` using the standard library. The checker enumerates every six-permutation and every four-position selection, constructs a 24-bit set-deck independently by rank sorting and by pairwise comparison tests, and compares both for all 720 sources. It asserts the four explicitly listed nonsingleton fibers, the 710/2/2 fiber histogram, exactly 714 decks and exactly 36 maximum full-set decoding dictionaries. It checks reversal, complement, inversion, and the 58 at-most-one-descent sources. The expected output begins `VERIFY_OK` and reports all counts. There is no random sampling or numerical tolerance.

The exhaustivity statement applies only to six distinct ranked symbols. The full deck is supplied as the channel output; a single arbitrary deletion trace is not sufficient for the asserted capacity. No external independent audit has been performed. The 2005 antecedent dissertation was not fully inspected, so the priority comparison is qualified.
