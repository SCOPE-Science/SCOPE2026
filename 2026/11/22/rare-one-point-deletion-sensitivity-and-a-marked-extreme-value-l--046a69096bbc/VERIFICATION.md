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

# Checks and limits

Reproduction: `python verification.py` with `mpmath` from `requirements.txt` passed 83 deterministic assertions. Assertions include exact rational binomial identities for \(2\le n\le15\), quadrature versus finite binomial tails, finite conditional-density evaluations, and convergence-direction sanity checks. The theorem's infinite limit is proved by the conditional density and Scheffé argument, the \(2/H_{n-1}\) exception bound, and exponential-sum concentration; no finite computation is claimed to establish convergence for all \(n\).

The independent mathematical audit has not been performed. The conditional laws apply to uniform circular points and exactly one uniformly selected deletion only; historical-priority uncertainty remains.
