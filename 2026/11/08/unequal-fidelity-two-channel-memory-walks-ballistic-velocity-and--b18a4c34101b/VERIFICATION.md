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

# Verification of the unequal-fidelity theorem

Run `python3 verify.py` with standard Python. Its exact-rational checks enumerate all nonnegative three-color counts of total sizes one through twelve, for twenty-five choices of ordered rational copying fidelities. For each state they compute the conditional probabilities independently from channel probabilities and test positivity, normalization, signed drift, zero-step probability, and nonzero-step drift. They additionally test the explicit interior equilibrium and identification algebra whenever parameters lie strictly above the threshold. The checker reports 45,420 successful exact assertions.

The actual infinite-horizon argument is in the theorem proof and is not inferred from these checks. Its essential probabilistic inputs are standard bounded-noise stochastic-approximation limit-set theory and nonconvergence to linearly unstable equilibria. Finite enumerations cannot verify those infinite theorems, nor can they prove historical priority. No external independent audit was performed.
