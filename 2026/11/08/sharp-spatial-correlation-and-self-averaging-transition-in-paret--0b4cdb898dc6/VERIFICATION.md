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

# Verification and scope of checks

The theorem is analytically established in `RESULT.md` through the Glauber generator, killed first-passage representation, equilibrium-renewal age mixing, tilted first-passage law of large numbers, Mellin integral asymptotics, and exact window covariance identity. The independent computation is supplemental and finite.

Run `python check.py` in an environment with `scipy>=1.10,<2` as recorded in `requirements.txt`. On the packaged source, 324 deterministic finite algebraic, first-passage integral, and monotonicity assertions passed. The computations check the cut-off continuity of the age survival function, walk first-passage transforms, exact zero-temperature inverse moment, and several asymptotic prefactor ratios.

No numerical experiment establishes the infinite-separation limits or the tail-summability boundary. The source's equilibrium-age law requires α>1; no extension to infinite-mean resetting is claimed. No external independent scientific audit was performed. The available literature comparison is qualified and does not certify publication priority.
