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

# Verification and limits

The theorem follows from a complete analytical section-boundary decomposition, not from computer enumeration. The independent half-plane routine in `verify.py` enumerates rational section vertices as intersections of nine defining half-planes, orders them around their centroid, and computes their inherited three-space Euclidean perimeter without calling the analytic cap-profile routine for polygon vertices.

`python verify.py` returned `THREE_CHAINLINK_SECTION_PERIMETER_CHECKS_PASSED 250`. The 250 seeded rational configurations include the boundary case \(2\ell=\min_i a_i\); for both complementary levels the script checks polygon perimeter against the explicit profile and checks each of the two profile totals separately. It also verifies the unequal edge-length multisets of complementary noncongruent hexagons and an explicit failure when \(2\ell>\min_i a_i\).

These finite tests establish only those instances; the universal proof is in `RESULT.md`. A separate historical-priority review and independent mathematical audit remain unperformed.
