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

# Verification and reproducibility

Run `python verify.py` with Python 3 and the standard library; no third-party packages are needed. The checker independently evaluates exact-rational utility cancellation for 3,000 distinct samples, constructs two unobstructed target locations on exact-rational random configurations with population sizes two through thirteen, tests the pre-noise displacement bound, and checks the complementary-error-function survival normalization and its asymptotics. The first completed execution returned `PASS: 3611 exact-rational geometry/update and Gaussian-tail checks`.

The infinite-time theorem is established by the proof in `RESULT.md`. Finite checker loops and sampled states are not substitutes for that proof, and the numerical complementary-error-function checks do not establish its limiting equivalence by themselves.

The uniform tail constant is a deliberately conservative Gaussian density minorant. It is valid for all fixed positive noise scales, finite population sizes, finite positive confidence radii, and arbitrary strictly positive finite utility functions, but is not optimized. The geometric two-agent law concerns attempted updates from a receptive start; when the pair is initially incompatible, its absorption time is zero. The model has unbounded opinion space and does not add noise on an incompatible attempted encounter.
