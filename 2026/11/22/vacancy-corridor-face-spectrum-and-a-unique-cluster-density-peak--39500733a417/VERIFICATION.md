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

# Reproducibility and checks

Run `python3 verify.py` from the directory containing this document and the standalone script, using Python 3.9 or later. It needs no network connection and no third-party libraries. For each length from one through five columns it checks all configurations, calculates components by graph connectivity rather than assuming the face formula, and compares them with the unit-square and vacancy-corridor counts. It also checks exact expected component counts and corridor intensities at rational occupation probabilities. A successful execution reported 37,631 assertions.

The all-length face classification and uniqueness of the density maximum are analytical assertions proved in RESULT.md. The finite checker is not exhaustive over unbounded lengths, and its rational sampling does not establish polynomial identities for every real probability. Neither historical priority nor independent validation has been certified.
