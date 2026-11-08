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

Run `python3 verify_strong_subdiv.py` with Python 3.9 or newer; only standard-library modules are used. This file accompanies the proof in `RESULT.md`. It constructs graphs from their adjacency relations and makes no assumption about the target MMD edge set when calculating distances. For orders four through seven, the independently computed MMD graph equals the disjointness graph, and exhaustive edge-family enumeration agrees with the star/triangle polynomial. For orders four and five, all vertex subsets are additionally tested against the original pairwise strong-resolution definition, followed by all single-deletion minimality checks.

Observed counts by graph order: 8, 15, 26, 42. The verifier tests 2,131,008 edge-family bitmasks and 33,792 strong-resolving candidate vertex sets, and prints `VERIFY_OK`. These are finite tests, not an infinite certificate. Unrestricted quantifiers are addressed by the explicit distance cases, the established vertex-cover correspondence, and the self-contained maximal-intersecting classification.

No independent audit has been performed.
