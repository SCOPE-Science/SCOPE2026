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

# Exact certificate verification

Place `CERTIFICATE.json` and `verify.py` in the same directory and run `python3 verify.py` with Python 3 and no external dependencies.

The checker enumerates all ternary strings at each length from one through nine; rejects every string containing a nonempty contiguous square; verifies the reported source counts; checks that the supplied disjoint confusable pairs cover every length-six and length-seven source exactly once; expands the specified full alphabet-permutation and reversal orbits; verifies exact rational weight one on all length-eight and length-nine substitution balls and the totals 63/2 and 48; verifies 48 distinct square-free length-nine codewords at pairwise Hamming distance at least three; and checks the 48 one-substitution balls are disjoint.

The final success output includes `DUAL_8_OK`, `DUAL_9_OK`, `CODE_9_OK`, `THRESHOLD_OK`, and `VERIFY_OK`. All inequalities are exact and involve finitely many explicitly enumerated objects. No numerical optimizer, solver status, extrapolation, third-party file or external service is required for the assertions. The theorem does not assert a sharp length-eight integer capacity or a classification for lengths above nine.
