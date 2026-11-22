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

Run `python3 verify_dp.py` and `python3 verify_bruteforce.py` with Python 3. Both completed successfully. The first traverses all vertices and all bit masks of the complete finite overlap graph for orders two through six. The independent second test exhaustively checks all binary circles at every shorter length and verifies explicit examples at the claimed optima. This is a complete finite-domain proof for the five orders and does not justify extrapolation beyond six.

No independent mathematical audit has been performed.
