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

# Verification

The associated `verify.py` uses only the Python 3 standard library and is standalone. It builds the directed collapse alphabet of a labeled path or cycle, independently simulates all actual functions for paths of orders 1–6 and cycles of orders 3–6, and retains exactly those length-\(m\) words with rank \(n-m\). It separately evaluates a different dynamic program on image subsets for path orders 1–12 and cycle orders 3–12. The first algorithm does not use the forest bijection or the subset recurrence; the second does not compose entire transformations. It additionally checks the exact rank-by-rank cycle/path factor for 65 combinations of orders and ranks.

The file `verification_output.txt` is the output of running `python3 verify.py`. It reports `VERIFY_OK direct_cases=10 subset_cases=22 ratio_checks=65`. All numerical comparisons use exact integers. The complete proof of the arbitrary-size results appears in `RESULT.md`; no finite enumerations are presented as exhaustive evidence for arbitrary sizes.

Scope limits: the result concerns words that attain the maximum possible rank drop at each step. Nothing is claimed about the multiplicities of longer words of the same final rank, about distinct semigroup transformations represented by such words, or about arbitrary graphs. No independent audit has been performed.
