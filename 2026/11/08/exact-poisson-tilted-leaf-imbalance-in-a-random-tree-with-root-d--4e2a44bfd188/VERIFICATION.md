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

Verification consists of analytical generator reconstruction, checking every transition and its rate, proving finite moments to justify Dynkin's equations, solving the exact differential equations, and verifying the continuous extension at the generating-function boundary. The accompanying standard-library script `verify.py` checks 10,263 exact rational generator identities and Taylor coefficients. A separate finite-time Monte Carlo sanity check was performed, but its approximate results are not proof. The exact generating formula supplies all conditional first moments; neither a conditional distribution nor a discrete-time fluctuation theorem is asserted.
