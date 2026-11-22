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

Run `python3 verify_hot_domains.py` in a Python 3 environment with no third-party packages. The code constructs a finite full-spin master generator separately from the analytical two-point equations and checks stationary heat injection against the cold-run formula for five sample bath assignments (five or six sites). It further solves exact rational two-point equations for every placement of at least two hot spins in all rings of 4–8 sites, totaling 456 placements, and validates the combinatorial extremum bounds for each fixed count, at the rational parameter \(\gamma=3/5\). A second parameter \(\gamma=7/9\) tests initial strict concavity and splitting relations.

Actual run: completed with all assertions passing. This is finite evidence and does not prove the theorem for arbitrary ring sizes; the self-contained proof is in `RESULT.md`. Exact computational normalization uses \(J=1\) and physical flux scales linearly in \(J\). No third-party paper contents or auxiliary data are needed to execute this checker. Independent audit: not performed.
