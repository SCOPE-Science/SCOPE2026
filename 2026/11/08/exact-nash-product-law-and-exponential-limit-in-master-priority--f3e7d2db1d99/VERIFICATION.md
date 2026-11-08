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

# Computational and analytic verification boundaries

The exact finite checker is `check.py`, using Python's standard library (`itertools`, `math`, `collections`, `fractions`). Run `python3 check.py` in the same directory as the other files. Recorded actual output is `CHECK_RESULTS.txt`.

The program reconstructs the serial stable assignment for each possible complete strict male-ranking profile for one to four men and women, independently counts the joint male-score vector, and compares every positive-mass atom with the product of theoretical order-statistic masses using exact rational numbers. It also confirms first and second complete two-sided Nash-product moments. It tested 1, 4, 216 and 331776 male-ranking profiles, respectively; all checks passed.

These are exhaustive finite checks only. The proof of every population size and of the exponential limit appears in `RESULT.md`, using the master-list matching theorem, exact sampling without replacement, uniform summable moment comparisons and the method of moments. Nothing in the checker constitutes independent external audit or machine certification of the general proof.
