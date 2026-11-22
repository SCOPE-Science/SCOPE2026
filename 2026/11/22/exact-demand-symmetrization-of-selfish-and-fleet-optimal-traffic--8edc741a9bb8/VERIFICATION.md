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

# Reproduction and limits

Run the included Python 3 file using `python fleet_symmetrization_checker.py`. Its exact-fraction water-filling routine computes the low and high Wardrop allocations, checks all demand totals, verifies the selfish and fleet complementary slackness conditions, and asserts the rational two-road inefficiency formula. The deterministic random generator seed is fixed in the script. The executed script returned `PASS: 2100 exact multi-road equilibria; 1344 exact two-road formula/cost cases`.

Finite test success is supplementary, not an infinite mathematical certificate. The universal theorem is proved by the strict quadratic potential and feasible decoupling in RESULT.md. Source priority depends on accessible research comparisons rather than a formal worldwide uniqueness guarantee. Independent external review has not been performed.
