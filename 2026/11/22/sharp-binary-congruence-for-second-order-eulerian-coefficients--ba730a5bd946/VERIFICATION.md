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

Run `python3 check.py` in a folder containing the included `check.py` file; it uses only Python 3 standard library. The program builds the recurrence directly, independently enumerates small Stirling permutations by inserting adjacent new maxima, and checks the normalized parity, digit containment, first occurrences and binary periods. Expected printed result: `PASS 195380 exact assertions; N= 360`.

# What is mathematically established

The unlimited theorem is proved by recurrence-level divisibility, formal differentiation in characteristic two, a binomial generating-function coefficient identity and Lucas's mod-two theorem. The finite diagnostic is not an infinite certificate, and does not independently certify originality or mathematical value. When normalized parity is even, the exact higher two-adic valuation is not determined here.

No independent audit has been performed.
