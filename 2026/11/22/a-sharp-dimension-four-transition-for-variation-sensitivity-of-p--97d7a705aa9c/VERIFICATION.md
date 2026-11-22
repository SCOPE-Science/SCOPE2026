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

Run `python3 tv_ball_exact_check.py` using only Python's standard library. The script uses exact rational arithmetic and checks every nonzero signed active-support pattern through eight vertices, independent evaluation of Green-kernel interpolation against the selected inverse matrix, sign-alignment identities and their induced column bounds, and explicit witness data through 100 vertices. The final expected line is `ALL_PATH_TV_BALL_PROJECTION_CHECKS_PASS`.

The proof covers every dimension and every positive radius, not merely the enumerated range. External historical priority has not been independently certified; the full primary algorithmic paper was not accessible. The checks use no randomized or floating-point assertions.
