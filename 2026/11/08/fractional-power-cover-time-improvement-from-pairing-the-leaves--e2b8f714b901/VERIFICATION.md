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

The exact identity is derived by Poisson thinning of independent hub excursions, Wald's identity, and a dominated-convergence asymptotic of a maximum of independent petal-completion times. The full mathematical argument appears in `RESULT.md`.

Run `python verify.py` with Python 3, SymPy, SciPy and NumPy. Exact rational computations agree among the finite binomial expansion and petal-state first-step recurrences for \(1\le m\le10\). An independent full visited-set Markov-chain solver agrees for \(1\le m\le4\). Numerical integration checks a sequence of scaled gaps against the asymptotic coefficient; these numbers are corroborative and not substitutes for the proof. The infinite limit is justified by an explicit integrable dominator and the evaluation of the gamma integral.

Unverified limits: no proof of sign for every finite \(m\) and no result for peripheral starting points. Priority among all possible historical literature is not independently certified.
