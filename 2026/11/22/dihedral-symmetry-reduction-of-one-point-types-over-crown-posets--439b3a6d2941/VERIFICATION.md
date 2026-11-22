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

Run `python3 verify.py` using Python 3 and its standard library. This reproduces the exact `verification_output.txt` bundled with the finding. The tests enumerate all ideals and the complete dihedral group directly for crown orders 3 through 10, and independently enumerate every ternary relation profile for 3 through 6, testing transitivity before orbit reduction. They check the three mixed orbit types and first free ideal orbit at 4; an integer recurrence/divisor test checks orders through 200. The all-order theorem is proved symbolically; finite tests cannot establish originality, asymptotics or arbitrary-size correctness.
