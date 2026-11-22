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

## Exact reproducibility

Run `python checker.py` using Python 3 (no nonstandard packages). It enumerates all nontrivial partitions up to global sign for odd sizes 5 through 15 and three rational resolvent parameters. The saved `checker_output.txt` shows 502,920 exact-rational assertions passed. Checked statements include recurrence entries, the closed variance minimum, uniqueness and optimizer counts, every window lower bound, and discrete-convex telescoping.

## Scope of checks

The source proof establishes the infinite family analytically; finite enumeration alone does not. No independently performed audit, proof assistant certificate, floating-point solver reliability test, or historical priority certification is claimed. The old circulant max-cut literature remains a specified originality risk.
