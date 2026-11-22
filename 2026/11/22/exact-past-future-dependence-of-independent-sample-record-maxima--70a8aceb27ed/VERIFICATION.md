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

# Verification record

The main claim is an analytic identity, not a simulation-based inference. The independent `checker.py` script evaluates exact rational cases, exhaustive order permutations, numerical overlap integration and seeded random experiments. It also checks the expected uniform-singular fraction and the sharp small-ratio constant. The exact identity is justified by the copula density and singular decomposition, and extension to the two sigma fields is justified by equality under common conditional Markov kernels. No finite checker constitutes a proof of an infinite process statement.

Run `python checker.py` using Python 3 and its standard library. The script reports the number of passed conditions, and returns a failing exit code if any assertion fails. Independent mathematical validation has not been performed.
