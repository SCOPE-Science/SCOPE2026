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

# Computational verification

Run `python3 verify.py` in a directory containing the supplied script. The checker uses only the Python standard library and reconstructs the one-grain overwrite outputs independently from the algebraic proof. It enumerates all maximal independent sets of the exact conflict graph for lengths 2 through 10 and tests every constructed optimal codebook for lengths 11 through 30. Representative construction endpoints and interior cases are also tested for lengths up to 512. The observed ending is `VERIFY_OK`.

Exhaustive finite checks do not establish the theorem at arbitrary lengths; the all-length proof uses singleton descendants, equality structure and the explicit elimination of triple collisions. No symbolic algebra or external solver is required for the theorem.
