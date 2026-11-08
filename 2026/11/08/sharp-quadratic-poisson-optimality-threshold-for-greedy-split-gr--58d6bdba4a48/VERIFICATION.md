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

Run `python3 verify.py` alongside `RESULT.md` to replay 11,717 assertions. The implementation needs only the Python 3 standard library and outputs `VERIFY_OK 11717 assertions` on success.

The checker compares direct labeled feasible-edge exhaustive transition laws with separately implemented rational count-state recursion for small complete split graphs, checks exact zero-deficit product identities, replays finite rational inequalities in the coupling proof, and verifies finite total-variation bounds for the Poisson approximation. The complete proof for arbitrary \(2\le a\le b\) and the asymptotic limits is given in `RESULT.md`; finite checks do not establish infinite claims by themselves.

No independent scientific audit has been performed.
