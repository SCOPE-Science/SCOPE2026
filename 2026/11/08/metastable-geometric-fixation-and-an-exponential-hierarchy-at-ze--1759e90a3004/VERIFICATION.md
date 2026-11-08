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

Run `python3 check.py` using Python 3 and the standard library. The checker reports 2,501 assertions passed, independently enumerating the complete ballot allocations for small states and checking the finite Markov, holding, hitting and finite-horizon tail formulas. It also prints exact-fraction-derived expectation diagnostics. The proof of the infinite hierarchy and the total-variation error rate is written in `RESULT.md` and does not rely on finite numerical extrapolation.

The first-public date of the motivating preprint was verified against the arXiv submission history. Some historical literature was accessible only through abstracts or introductory material, so definitive historical priority requires an external literature audit. No independent mathematical audit was conducted.
