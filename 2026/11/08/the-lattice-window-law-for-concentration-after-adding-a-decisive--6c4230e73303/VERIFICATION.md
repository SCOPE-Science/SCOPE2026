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

# Reproduction and proof limits

Run `python3 checker.py` with Python 3.9+ and standard library only. The checker constructs every labeled simple graph on three, four and five vertices, excluding the edgeless case, and checks each missing-pair comparison by two mathematically distinct finite expressions: direct squared Deegan–Packel powers before and after insertion versus the integer threshold of the wedge identity. This checks 5,305 proposed insertions.

It then enumerates all simple graphs on three, four and five vertices at each of three rational edge probabilities and compares exact rational first/second moments of \(W-cm\) to the centered-edge expansion. This checks 3,288 graph-weight evaluations. Finally, seeded geometric-skip Bernoulli simulations compare the predicted noncritical Poisson limits and three points of the critical Gaussian window; simulation has finite-sample and Monte Carlo errors and is not a proof.

The unbounded-\(n\) claims require the proof's independent-edge cumulant estimates, positive asymptotic variance, first-order laws, and asymptotic decoupling of the fixed pair's degree sum. Neither finite enumeration nor stochastic spot checks establish these asymptotic steps. No independent external audit or validation has been performed.
