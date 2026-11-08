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

# Verification and limits

Run `python3 CHECK.py` in the same directory as the extracted research files; the checker requires only the Python standard library. Its successful terminal line is `ALL_SECOND_HERMITE_PLATEAU_CHECKS_PASSED`.

The exact-arithmetic tests cover the Laguerre factorization and derivative and the critical cubic identity. Numerical tests independently evaluate the centered ambiguity integral using the explicit unit-normalized second Hermite function, find the plateau exit, test endpoint/interior equalization and the full radial condition on sampled test grids, and exercise the asymptotic formulas. The printed numerical examples are reproducible cross-checks, **not** proof of continuous optimization or of infinite-radius asymptotics; those follow from the proof in `RESULT.md`.

Both the source-based originality assessment and the correctness check here are self-review. Independent scientific audit and publication-priority validation have not been performed. The margin concerns a pointwise ambiguity-domain inversion coefficient only, not global nonlinear reconstruction stability.
