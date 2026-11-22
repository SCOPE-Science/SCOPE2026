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

Run `python check_moment_collision.py` from the package directory with Python 3 and SymPy installed. The checker supplies 71 exact symbolic/rational checks and crossing diagnostics. It recomputes the positive integer certificate \(8409^2-401^3=6230080\), symbolic PGF identities, and first three factorial-cumulant derivatives.

The theorem's infinite continuum of moment collisions is established analytically using strict convexity and the intermediate-value theorem. The checker does not prove uniqueness of a maximizer, count all preimages, or establish asymptotic properties. The publication date of the source is its verified first preprint appearance on 12 June 2023; no independent mathematical audit is claimed.
