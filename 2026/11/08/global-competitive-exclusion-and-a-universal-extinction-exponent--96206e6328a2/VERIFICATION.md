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
# Verification

Run `python3 verify.py` with an ordinary Python 3 interpreter; no external packages are required. The test confirms 12 one-step log identities at the stated numerical precision, four long-orbit extinction-rate approximations, and three positive-coexistence fixed-point stability cases for weak coupling. The expected terminal marker is:

`VERIFY_OK one_step_log_identities=12 extinction_rates=4 coexistence_sinks=3`

The numerical extinction rate approximation uses 12,000 updates per test, computes the losing abundance in logarithmic coordinates to avoid underflow, and requires absolute rate error below 0.006. It samples \(R=0.6,2.5,5\) and both initial orderings; high-growth trajectories do not assume periodicity.

The proof in `RESULT.md`, not these finite tests, establishes the universal theorem. The exact log-ratio drift and time-summed population growth identities can be verified directly by substituting the stated map. The eventual positive lower bound is the critical infinite-trajectory step and is proved separately. No independent audit or external validation has been performed.
