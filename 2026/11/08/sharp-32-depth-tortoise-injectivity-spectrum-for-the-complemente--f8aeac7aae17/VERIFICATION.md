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

# Verification of the finite certificate

The attached `thresholds.csv` contains a row for every integer depth from 1 through 32. `verify.py` reconstructs the complete factor sets at both the threshold and its preceding length by applying the two-block formula proved in `RESULT.md`, and separately compares them to length-matched substrings of an independently evaluated valuation-based prefix. It checks output equality between successive tortoise iterations and deletion of the first k ones. Each threshold fiber partition must be discrete and each preceding partition must have exactly one nontrivial two-word class, matching the recorded witnesses. The exhaustive two-block lemma plus the prefix-inheritance proof extends the claim to every longer word length.

Command: `python3 verify.py`

Observed output: `PERIOD_DOUBLING_REVERSED_TORTOISE_VERIFY_OK 32`

Dependencies: Python 3 standard library only. The valuation-prefix comparison is a cross-check, not the infinite proof. There is no assertion for unlisted depths or other substitutions. Independent audit has not been conducted.
