---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification

Use the proof in `RESULT.md` for the unrestricted claim. Its counting argument marks an actual long-gap index in each indexed word, including when the word has a rotational symmetry. The proof includes the singleton and empty-support cases and treats an obstruction run that occupies the entire cycle.

The accompanying standard-library Python checker is a finite diagnostic for the unchanged coefficient formula and gap criterion. It tests all 524,280 vertex supports for lengths 3 through 18 and finite boundary identities through length 90. The terminal line starts with `MAXIMAL_CYCLE_SHATTERING_PASS`. These checks do not replace the unrestricted proof. No formal verification, external attestation, or historical priority is claimed.
