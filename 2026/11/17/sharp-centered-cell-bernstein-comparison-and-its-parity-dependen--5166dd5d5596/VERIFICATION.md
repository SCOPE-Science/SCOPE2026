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

# Reproducible finite checks

Execute `python3 verify_jitter.py` using the Python standard library. The script is standalone; no external paper, dataset, working-directory-specific path, or nonstandard package is needed.

It independently computes one-dimensional Wasserstein-1 by sorting the atoms of two measures and integrating the absolute cumulative signed mass; compares that exact rational value with the candidate weighted coupling cost; and evaluates the single universal interlacing spline at each source and target atom. It verifies 216 rational binomial/jitter configurations and 70 non-binomial configurations with distinct cell distributions, plus 1,890 rational binomial MAD and cell-peak identities. It corroborates the Stirling-scale limit numerically at four larger degrees. The output concludes with `ALL_CENTERED_BERNSTEIN_JITTER_CHECKS_PASS` when all assertions succeed.

The asserted arbitrary-dimensional sharpness, minimax over all Borel measures, equality classification, and asymptotic result are established by the separate mathematical proof. Neither exhaustive finite data nor asymptotic spot checks are used as substitutes for those arguments. No independent audit or external certification is claimed.
