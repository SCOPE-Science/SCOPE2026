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

Run `python3 checker.py` in a standard Python 3 installation. It uses only the standard library, enumerates the finite labeled machines for k=1,...,4, constructs their full orbits under state swap and alphabet conjugacy, and compares them to the general partition sum and the expected labeled count. It also evaluates the partition formula for k=1,...,9 by exact integer arithmetic.

The finite enumeration cannot establish an all-k formula. The proof of the Burnside formula in RESULT.md supplies the infinite mathematical argument. The full text of the directly relevant 2026 Curtin--Savchuk work remained inaccessible; historical priority is not independently certified.
