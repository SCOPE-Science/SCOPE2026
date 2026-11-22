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

# Reproducibility and limits

Run `python verify.py` (Python standard library only). This integrates the six-compartment leaky SIRI equations plus four cumulative incidence counters, tests six strictly admissible transmission/vaccination parameters, checks population conservation and vanishing infectious prevalence, compares exact aggregate-count identities in the finite-seed approximation, and checks the two bounds and per-primary ordering. The run completed with all assertions passing.

The certificate is a numerical consistency test, not a computer-assisted proof. Exact universal correctness follows instead from the backward Markov reward differential equations and positive-measure representation established in RESULT.md. Each positive finite test seed approximates a nontrivial epidemic branch with seed tending to zero; no printed numerical digit is claimed as an exact infinite-time answer. No independent audit has been performed.
