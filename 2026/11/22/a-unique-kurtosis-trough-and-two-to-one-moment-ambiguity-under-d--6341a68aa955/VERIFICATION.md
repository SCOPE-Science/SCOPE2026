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

# Verification scope

The package includes `CHECKER.py`, a runnable Python 3 / SymPy exact-algebra checker. It computes stationary moments independently by two methods: the complete-reset Markov generator recurrence and direct polynomial integration of telegraph multi-time correlation functions. It also checks the full rational kurtosis expression, its derivative, the exact crossing against Gaussian-white acceleration excess kurtosis, endpoint limits and the unique positive critical-root location.

# Actual verification

Executing `python CHECKER.py` produced the successful symbolic-check message and numerical diagnostic values \(z_*=0.339462271566093694\ldots\), \(K(z_*)=56.5770470882562612\ldots\), and \(z_c=0.851982255870633336\ldots\). The checker does not numerically sample any infinite family of parameters; the proof supplies the strict positivity of the cubic derivative, sign changes and regenerative uniqueness that establish those statements for all parameters.

# Limits

The complete-reset protocol, strictly positive switching and resetting rates, symmetric acceleration sign and stationary one-time position moments are essential. Moment matching does not imply full distribution matching. Source comparison and algebra were performed in the self-review only; independent audit and independent validation have not been performed.
