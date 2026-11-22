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

# Reproducibility and mathematical limits

Run `python3 verify_three_point.py` in a Python 3 environment using only the standard library. The checked output from the delivered source is:

`VERIFY_OK assertions=3614 exact_depths=1..6 integer_terms=3127 words=40 forbidden=24`

The checker independently generates exact central-trinomial integers from the three-term recurrence, checks the digit factorization, enumerates all sixty-four triple types at each base-five cutoff through \(5^6\), and compares each count with the closed finite formula. It also tests the forty-word support threshold, the rational limiting masses, both uniform adjacent-pair marginals and the known lag-two ratio marginal. The proof in `RESULT.md` establishes the all-depth formula, full natural density and uniform logarithmic-squared discrepancy; finite computation alone establishes none of those universal conclusions.

The scientific priority assessment relies on the cited accessible publications and indexed claims; absence from a database is not proof of priority. No independent mathematical validation has been performed.
