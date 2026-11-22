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

# Reproducibility and scope

Run `python verify_heterogeneous.py` with Python 3.10 or later. No third-party packages, random sampling, downloads, or network access are required.

The script constructs the all-subset stationary moments using exact rational arithmetic, obtains full joint probabilities by Walsh inversion, and checks the independent continuous-time master-equation balance for every state on 21 heterogeneous stars of sizes one through seven. It also verifies positivity, normalization, exact hub-to-leaf and leaf-to-leaf correlations, and current-balance identities. The execution reported `HETEROGENEOUS_EXACT_STATIONARITY_OK cases=21 state_checks=1524`. A separate check compares exact homogeneous-subset moments with the beta-mixing moments for stars of sizes one through eight and two parameter families; it reported `HOMOGENEOUS_BETA_MOMENTS_OK sizes=1..8 two-rate-sets`.

The tests verify only the finite parameter choices explicitly hard-coded in the program. The theorem for every star size and every stated strictly positive parameter follows from exact generator identities, subset induction, Walsh inversion and the stationary two-state transport equations in `RESULT.md`. The historical novelty comparison is bounded by the checked literature. No independent scientific audit has been performed.
