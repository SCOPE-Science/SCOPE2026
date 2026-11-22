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

# Mathematical verification record

The proof uses an exact common-clock Gaussian conditional-variance representation and a bounded scalar jump process. The formulas for its stationary first, second, and third moments, generator, polynomial semigroup, and three-time cumulant are reproduced in `verify.py` using exact symbolic simplification. The program asserts the positive factorizations of both the temporal arrow and the sign threshold, and checks four parameter choices at five lag values. Running `python verify.py` returned success.

An independent `simulate.py` samples the Poisson event clock and the scalar conditional-variance process directly, rather than integrating its polynomial semigroup. Four Monte Carlo comparisons, spanning negative and positive correlation regimes, agreed with the exact formula within five reported standard errors. Running `python simulate.py` returned success.

These are self-review. They do not constitute independent audit or validation and do not replace the algebraic proof. Tests do not cover measurement noise, interactions, or feedback/reset clocks other than fixed-rate common Poisson contraction.
