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

Run `python3 verify.py` with a standard Python 3 interpreter. No nonstandard libraries or external datasets are needed. The script builds a compatibility relation on the nine named two-coordinate cultures and checks all support subsets and all maximal compatible palette pairs. It verifies the exact formula via finite support-surjection summation for 576 positive shore-size pairs and independently counts every assignment for eight small bicliques. It also tests the four-family decomposition directly for five small instances.

The expected successful final line is `VERIFY_OK`. The script contains no stochastic experiments. The general all-order identity, exact classification and limiting distribution are proven by finite nine-culture neighbour-set arguments followed by inclusion-exclusion and exponential estimates, as set out in `RESULT.md`. Neither the finite sweeps nor script execution constitute an independent mathematical audit.
