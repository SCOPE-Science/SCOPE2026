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

The standalone `verify.py` uses only the Python 3 standard library and exact rational arithmetic. It separately evaluates focal payoffs by enumerating all incident 2-games and 3-games, compares both possible actions with the proposed closed form for all labeled profiles from three through eight players at a collection of rational intensities including both sides of every critical value, and checks the exact counts. It also checks onset and one-defector cutoffs for sizes three through thirty-nine. Command: `python verify.py`. Actual successful output: `VERIFY_OK 49976 exact payoff-advantage comparisons; n=3..39 threshold and one-defector checks`. The proof treats every integer size; finite tests do not establish an infinite theorem. No outside validation or independent audit is claimed.
