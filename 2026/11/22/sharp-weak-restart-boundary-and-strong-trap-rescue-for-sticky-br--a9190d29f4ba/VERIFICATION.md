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

## Reproduction
Run `python3 verify.py` with Python 3, SymPy, NumPy and SciPy in the same folder. The checker exits with status zero after 118 assertions, or raises an error if any assertion fails. It checks the backward Wentzell resolvent and boundary data symbolically, derives the second moment from the differential equation independently of the Laplace formula, verifies the polynomial identity, compares a separately discretized sticky finite-volume generator with the analytic transform, and probes rates, thresholds and strong-stickiness asymptotics.

## Proof-only parts and limits
The exact sign, unique root, monotonic threshold, leading \(1/6\) constant and boundary-start no-benefit law use analytic arguments in `RESULT.md`, not finite experiments. Tests check representative parameter values and grid convergence but do not certify entire continua. The analysis concerns full-state Poisson restarts and does not imply a global beneficial-rate interval for interior starts. No independent scientific audit has occurred.
