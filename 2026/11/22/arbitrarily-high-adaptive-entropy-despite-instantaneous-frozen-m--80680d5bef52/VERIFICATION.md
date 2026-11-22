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

# Verification details

The standalone `CHECK.py` uses exact rational arithmetic and independently implements the piecewise-affine controller-dependence function. Executing `python CHECK.py` reports PASS for values \(2\le m\le18\), tests all affine breakpoint values and signs, and verifies the \(m\)-full-branch endpoint images of the second iterate. It also constructs exact primitive even-period witnesses for the underlying scalar map (a supporting check not needed for the accepted entropy statement).

The infinite mathematical assertion is proved directly from the explicit formula, strict displacement sign, full-branch interval structure and standard entropy identities. Finite checks do not establish the all-\(m\) result. External independent evaluation has not been performed.
