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

The independent checker `verify_reuleaux.py` constructs exact intersections of all generating unit disks with affine lines and numerically integrates the near-maximum-chord region. It passed 53 deterministic checks on regular 3-, 5-, 7-, and 9-gons, with residual divided by deficit decreasing toward zero at three thresholds. The analytic proof covers fixed irregular polygons via finite arc sectors, local active-circle separation, matched asymptotics and strict concavity of log-sine. Finite calculations cannot establish the theorem for infinitely many polygons or small thresholds. No independent mathematical audit has been performed. The specialist Gates (1987) article was only available by abstract.
