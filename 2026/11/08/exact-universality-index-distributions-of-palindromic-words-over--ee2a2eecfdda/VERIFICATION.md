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

Run `python verify_palindromes.py` with Python 3. The script uses only the Python standard library and exits nonzero on assertion failure. Its recorded successful execution generated `PASS: 52710 palindrome-index evaluations; 630 independent direct subsequence-set evaluations`. The independent method enumerates distinct scattered subsequences, not greedy arches, at half lengths at most three; at larger specified lengths the script cross-checks closed-form coefficient extraction against greedy enumeration.

The exhaustive ranges are binary half lengths 0–11, ternary 0–7 and four-symbol alphabets 0–6. Exact all-length validity is established in the mathematical proof, not the bounded checks. The midpoint lemma and usual arch method are known primary-literature inputs. The analytic renewal-limit argument is not tested numerically. No independent audit or independent validation has been performed.
