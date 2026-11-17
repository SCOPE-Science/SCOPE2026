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

The exact-count synchronous model, occupancy mismatch clock, labelled exponential generating function, maximum transient and periodic-orbit counts are proved in `RESULT.md`.

Run `python check_census.py` and `python check_direct.py` in the extracted directory. The first uses exact rational coefficients and independent multinomial occupancy counting for 340 parameter triples, and checks the sharp maximum and total partition. The second simulates each labelled configuration and detects its actual first repetition, comparing with the claimed entrance time and least period across 112 systems and 1,834,800 initial states. Both use only the Python standard library. Observed outputs are stored in `census_output.txt` and `direct_output.txt`.

Finite checks are corroborative, not substitutes for the all-parameter combinatorial argument. Historical priority is not exhaustively established. No independent audit has been performed.
