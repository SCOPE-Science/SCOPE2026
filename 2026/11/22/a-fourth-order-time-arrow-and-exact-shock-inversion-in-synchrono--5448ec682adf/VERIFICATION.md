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

The proof uses exact generator identities and the stationary conditional-Gaussian representation, with no asymptotic or numerical step needed for the theorem. The accompanying `verify.py` checks those identities at representative parameters and independently simulates backward Poisson gaps to reproduce the mixed squared-position covariance without sampling from the generator moment formulas. Run `python verify.py` (Python 3 and NumPy). Fixed-seed independent-clock Monte Carlo gave 0.031831955 versus the exact 0.031926947 in the indicated example. Finite samples do not certify parameter-uniform claims; the analytic generator and Markov-semigroup argument do.

Scientific scope: strictly positive harmonic strengths and diffusivities, stationary two-coordinate process, common independent Poisson contractions by one fixed factor in the interval \([0,1)\). Independent audit and external experimental validation have not been performed.
