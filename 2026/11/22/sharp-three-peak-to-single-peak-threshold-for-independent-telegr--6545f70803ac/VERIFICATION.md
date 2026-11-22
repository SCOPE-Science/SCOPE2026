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

The analytic proof is contained in RESULT.md, equations (1)–(6), including the single external stationary distribution premise, a strict convexity lemma, central/edge integral asymptotics, monotonicity in all parameter regimes and the near-critical implicit minimizer expansion.

The bundled `checker.py` depends only on Python's standard library and evaluates the derivations on rational and numerically convergent finite examples. Execute `python checker.py` in the directory containing the extracted files. Expected output: 1,341 conditions passed. This is not a formal or independent proof certificate. Independent assessment has not been performed.

The exact domain is two independent identical stationary symmetric telegraph filters for all positive speeds, relaxation and switching intensities; the mode classification is an infinite theorem proved by the displayed analysis. No extrapolation from tests is used.
