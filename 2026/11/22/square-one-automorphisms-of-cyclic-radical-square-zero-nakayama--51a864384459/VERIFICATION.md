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

The reproducibility script `checker.py` is self-contained Python 3, with no third-party dependencies. Run `python checker.py`; the output should reproduce `checker_output.txt` exactly. Direct finite-field matrix enumeration verifies square-one counts, fixed-space dimensions, and semidirect-product multiplication for three configurations; a generating-set conjugation search verifies all seven classes for the four-vertex algebra over \(\mathbb F_3\). The proof of the general formulas requires the explicit lifting and eigenspace arguments in RESULT.md and does not follow merely from these samples.
