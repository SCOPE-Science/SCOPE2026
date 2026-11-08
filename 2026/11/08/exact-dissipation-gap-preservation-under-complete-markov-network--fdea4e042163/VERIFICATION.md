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

The standalone `check_lift.py` uses standard-library exact rational arithmetic to certify the finite-seed entropy-production ratio, including rigorous interval bounds for all logarithms. It verifies the microscopic and macroscopic formulas independently at finite block sizes and checks exact rational stationarity. In the completed run, 385 finite tests passed, including nonuniform target-weight refinements. The analytic proof in `RESULT.md` establishes the arbitrary-block-size theorem; neither the finite tests nor numerical approximations certify the infinite family on their own. No independent audit has been performed.
