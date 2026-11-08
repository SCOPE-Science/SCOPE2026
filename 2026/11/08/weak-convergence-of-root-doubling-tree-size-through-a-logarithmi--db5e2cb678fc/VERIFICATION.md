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

Execute `python verify.py` from the directory containing this document. It uses only the Python standard library, with a fixed seed for reproducible finite diagnostics. Its completed run printed `PASS finite assertions: 2952`, simulated a continuous-process mean of approximately `1.99322` and second moment `4.9883`, and simulated a discrete scaled-size mean of `2.00432` after `100000` steps.

The reproducible checks verify exact rational mass conservation and mean drift for the discrete chain (13 transitions), polynomial generator identities through degree 30, the reciprocal-hazard identity and one-jump path formula for a grid of parameters, a one-jump minorization support inequality, and diagnostic simulations using exact event times. The analytic result is based on the coupling error bound and the explicitly checked hypotheses of the standard Harris ergodic theorem; finite assertions alone cannot certify either an infinite limit or originality.

No separate independent audit or external proof certification has been performed.
