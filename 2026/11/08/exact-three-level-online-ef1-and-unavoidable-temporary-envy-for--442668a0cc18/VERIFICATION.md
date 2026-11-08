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

Exact finite-game reproducibility: run `python3 verification/verify_game.py` and compile/run `verification/verify_numeric.cpp` with a C++17 compiler. Both check four adversarial game values: three levels with unrestricted, different-second-recipient, and same-second-recipient rules; then four levels unrestricted. Expected adversary-win values are respectively `0,1,1,1`.

The Python checker uses an ordinal terminal criterion; the C++ checker implements the cardinal EF1 inequality directly. The calculations visit finitely many game states and use short-circuit evaluation of exact Boolean quantifiers. Their checked game values, not early-pruned state-visit counts, are the proof certificates. Any positive real magnitudes with the same per-agent order are covered by the cardinality/ordinal lemma in `RESULT.md`.

Not verified: polynomial-time implementability, exact EF1 for longer horizons, temporal EF1, randomized guarantees, or general utilities. No third-party independent audit has been conducted.
