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

# Reproducible mathematical checks

The self-contained `check.py` requires only Python 3 standard-library modules and uses independently implemented exact rational Markov path enumeration and even-spin formula evaluations. Running `python3 check.py` returned `PASS 31924 independent assertions`. The script tests several rational latent transition factors and detection strengths, the exact five-visit algebra, one nontrivial rational interior root, and a grid of feasible gaps under three detection qualities and six horizon regimes. The finite grid is illustrative and cannot certify global optimality by itself.

The proof is analytic: a positive even-spin expansion gives strict convexity for any fixed number of visits; reversibility forces a unique symmetric optimizer; exact derivatives at the zero-gap schedule plus a strict KKT margin prove the parity law near zero horizon. For five visits, factorization of the one-variable derivative and a cubic root sign test classify all positive horizons. Equality at the threshold and perfect detector boundary are explicitly handled.

Scope: stationary, symmetric Markov availability with independent identical imperfect detectors and fixed endpoints. No field-data calibration, no adaptive sampling, no nonstationary or asymmetric regimes, and no proof of historical priority. A separate external or independent validation has not been performed.
