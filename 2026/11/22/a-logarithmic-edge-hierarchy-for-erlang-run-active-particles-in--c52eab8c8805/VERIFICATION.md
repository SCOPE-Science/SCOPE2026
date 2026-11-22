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

# Reproduction and limits

The complete proof is in `RESULT.md`. With Python 3 installed, run `python -m pip install -r requirements.txt` followed by `python check.py`. The code performs 98 finite consistency checks in its recorded environment: Gamma equilibrium-age identities; an affine-stationary simulation with reproducible seed; an exact first-moment identity; stationary second-moment comparison against an independently constructed finite-phase generator; and convergence checks for scaled edge probabilities at shapes two and three. It prints the observed approximate constants and reports PASS on successful assertions.

The stochastic samples are finite, their estimates have Monte Carlo error, and their apparent convergence is not an infinite asymptotic certificate. The decisive analytical conditions are the existence of a unique entrance-gap perpetuity, finiteness of its critical negative moment, the equilibrium-age Gamma tail and domination of the positive-orientation contribution. These steps appear explicitly in the proof. The limit has not been independently audited, and publication priority beyond the inspected sources is not certified.
