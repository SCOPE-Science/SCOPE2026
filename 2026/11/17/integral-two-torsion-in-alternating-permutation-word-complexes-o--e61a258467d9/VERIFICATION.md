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

The accompanying `check_alternating_words.py` uses only the Python standard library. Running `python3 check_alternating_words.py` exhaustively reconstructs the generating even permutations, all subsequence cells, signed boundary maps, every chain-complex identity, three prime-field rank cross-checks, and a deterministic exact integer reduction to Smith factors \(1\) and \(2\). The expected last line is `ALTERNATING_PERMUTATION_INTEGRAL_HOMOLOGY_PASS`; `check_output.txt` contains the actual run output.

The computation covers \(n=3,4,5\) only. The lower-skeleton connectivity is justified by the cited Björner–Wachs theorem, not by finite enumeration. The full primary 2026 pattern-avoidance manuscript was not accessible for line-by-line comparison. Independent audit has not been performed.
