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

The analytic proof uses the exact continuous-time two-state master equation and the global strict log-concavity of the finite-horizon work function; no finite enumeration serves as a proof over continuous parameters. The standalone `verify_load.py` program checks the work expectation independently using transition probabilities, solves the strictly monotone first-order condition by bisection, compares its output with alternative admissible loads, and checks the predicted duration trend, including the critical exact fixed-load line. It uses only the Python standard library and a fixed deterministic random seed. Execute `python3 verify_load.py` to reproduce its printed check count.

Limits: numerical derivatives are only consistency tests. The theorem assumes constant symmetric exponential load splitting, an initial distribution above passive equilibrium, and a fixed time window. No time-dependent control or external independent review is supplied.
