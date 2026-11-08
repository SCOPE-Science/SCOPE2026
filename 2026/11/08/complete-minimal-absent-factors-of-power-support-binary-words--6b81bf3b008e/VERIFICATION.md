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

The mathematical proof in `RESULT.md` establishes the statement for all integer bases \(b\ge2\) and all lengths; enumeration does not establish those infinite quantifiers.

Run `python3 verify.py` with Python 3 and only its standard library. The verifier constructs a factor-complete finite prefix for each stated cutoff, enumerates its distinct factors, independently identifies minimally absent words from occurring immediate prefixes and suffixes, and compares the result against the four-family theorem and exact counting formula.

Observed output:

`VERIFY_OK complete_prefix_cases=42 factor_sets=17750 minimal_absent_words=936 formula_ranges=2..20,1..700`

The checked cases are \(b\in\{2,3,4,5,6,7,8\}\) at lengths through \(40\) for direct factor comparison, and \(2\le b\le20\), \(1\le N\le700\) for generated-family versus counting-formula comparisons. The nonregularity conclusion and completeness for all parameters rely on the proof, not on this script. Independent external review has not been performed.
