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

The `direct_states.py` script independently implements vertex-by-vertex synchronous majority on the labelled bridge barbell. Run `python3 direct_states.py`; its captured output is in `direct_states_output.txt`. It exhaustively traverses 170688 configurations across all 21 size pairs 3 <= m <= n <= 8.

The `class_states.py` script derives the evolution of the two nonhub counts and the two hub bits without using the direct simulator. Run `python3 class_states.py`; output is in `class_states_output.txt`. It verifies weighted quotient state counts, total populations, exact periodic orbits and sharp times across 2304 ordered size pairs 3 <= m,n <= 50.

The `witnesses.py` script uses the count recurrence to verify the explicit sharpness witnesses for each of 9604 ordered pairs 3 <= m,n <= 100. Run `python3 witnesses.py`; output is in `witnesses_output.txt`. Execute it in the same directory as `class_states.py` because it imports its recurrence.

These are finite verification exercises. The unbounded claims for all clique orders follow from the separate algebraic case analysis in RESULT.md, not extrapolation from numerical tests. There is no claim of independent audit or external certification.
