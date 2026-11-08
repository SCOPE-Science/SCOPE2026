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

# Reproducible finite checks

Execute `python3 verify.py`. The script uses only the Python standard library. It constructs finite vector spaces, independently enumerates all invertible matrices, and enumerates every projective-point permutation and every possible nonzero scalar factor for the listed small fields. It then tests the literal pair-interpolation property for each proposed map against all invertible linear maps, not merely the derived abstract count. Additivity is compared to the set of genuine global automorphisms.

Verified configurations are \((q,n)=(2,1),(2,2),(3,2),(2,3)\). They produce respectively \(1,6,384,5040\) two-local maps and \(1,6,48,168\) ordinary maps. The terminal success marker is `VERIFY_OK`.

The code handles only prime fields and these small finite configurations, and does not exhaust arbitrary prime powers. The general theorem, including extension fields, is proved algebraically in `RESULT.md`; the executable is supporting finite evidence rather than an infinite certificate. Independent review has not been performed.
