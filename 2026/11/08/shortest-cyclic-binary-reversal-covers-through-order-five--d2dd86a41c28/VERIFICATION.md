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

# Reproducibility of the exact finite classification

Execute `python3 verify_dp.py` and `python3 verify_census.py` in the folder containing this document and the two cycle lists. Expected terminal markers are `DP_VERIFY_OK` and `CENSUS_VERIFY_OK`. These are separate algorithms: the first compresses all suffixes into exact integer dynamic-programming states; the second enumerates complete binary suffixes and compares full cyclic factor sets directly. No external packages, download, randomization or solver calls are needed.

The exact outputs tested are as follows:

| Order | Required reversal classes | Shortest circular length | Rooted complete strings | Shortest necklaces | Reversal/complement symmetry classes |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 1 | 1 | 1 |
| 2 | 3 | 4 | 1 | 1 | 1 |
| 3 | 6 | 8 | 2 | 2 | 1 |
| 4 | 10 | 14 | 8 | 8 | 3 |
| 5 | 20 | 26 | 128 | 128 | 36 |

At each order the recurrence tests every integer length between the number of required factor classes and the candidate optimum and obtains zero shorter covers. The direct program independently validates the counts and the literal canonical cycle lists. The claimed equalities are finite certified counts, not an inference from a random sample. The methods do not verify originality against all historical literature or any claim for larger orders.
