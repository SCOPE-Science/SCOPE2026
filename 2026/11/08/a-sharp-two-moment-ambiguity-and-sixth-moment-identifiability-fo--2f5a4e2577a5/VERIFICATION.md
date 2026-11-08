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

The included `verify.py` is self-contained apart from the SymPy dependency; run `python verify.py`. It constructs the three-state rate generator and computes all state-resolved moment vectors through order six by inverting the stationary moment equations. It checks the analytic moment formulas, the fixed-variance parametrization, the derivative factorization, endpoint values, the two rational inverse-map equations, and a strictly different sixth moment for an explicit same-second-and-fourth-moment pair. It additionally tests thirty positive rational rate pairs. All 119 assertions passed.

The checks are exact rational/symbolic algebra except for no approximations at all. They do not constitute an independent audit. The theorem for every positive rate pair follows from the provided algebraic proof, not from finite enumeration. The claim assumes the full specified stationary model, known trap and speed scales and absence of thermal positional diffusion. Statistical identifiability from finite samples or external experimental validation has not been assessed.
