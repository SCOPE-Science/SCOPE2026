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

The exact support-recurrence and temporal-coefficient table can be checked by running `python3 code/verify_signatures.py` from the package root. This enumerates all 147 nonempty signatures, verifies the core-rainbow criterion for oscillation, and compares all ten counting formulas with surjection-weighted counts for 132 graph-parameter pairs.

Run `python3 code/verify_direct.py` for a separate graph-adjacency implementation. It evolved all 392,040 labelled initial states across 20 graph sizes, compared first-entry times and least periods with the formulas, and checked the five-entry profile **separately for each primitive three-cycle**. Both programs are standalone and use only Python's standard library. The recorded output is `checks/verification_output.txt`.

The finite computations verify an exact 147-case classification; the proof that this classification covers every graph size follows from the identical-input support quotient and surjection counting, not from fitting finite numerical data. No independent expert audit or external formal certification has been performed. The publication-priority comparison is necessarily bounded by discoverable and accessible sources.
