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

The all-size theorem follows from the symmetric-difference identity and characterization of one-disagreement cells, not from finite computation. To reproduce finite evidence, run `python3 check_insertion_spectrum.py` beside this document and compare its printed lines with `check_output.txt`.

The checker generates all permutations of sizes 2 through 8, loops over all pairs of insertion gaps, and counts disagreeing named points directly using two order comparisons. It independently determines whether a permutation is a product of disjoint adjacent swaps, checks the maximal linear coefficient, verifies the complete polynomial for all equality cases, and tests exact binomial counts by swap number. The program checks 46,232 finite permutations and reports 86 matching-product extremizers across these seven sizes. Its scope is finite and is not claimed as an exhaustive computational proof for larger sizes.

No external solver, oracle, or third-party repository is required. Independent mathematical audit remains not performed.
