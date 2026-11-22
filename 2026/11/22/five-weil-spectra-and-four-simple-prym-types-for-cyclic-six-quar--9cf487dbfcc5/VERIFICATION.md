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

# Verification of exact arithmetic

Run `python3 verify.py` from the same extracted directory using Python 3 with no optional packages. The source program independently constructs two quadratic field models, checks irreducibility against every ground-field element, performs complete 289-element sums for all fourteen parameters using cube-character and direct cube-fiber counting, checks five reciprocal Weil factors and their four rational-irreducibility conditions, and verifies both distinct-curve isogeny collisions. A separate multinomial expansion calculates the complete three-by-three Hasse–Witt matrix for each of the fourteen quartics, confirming vanishing precisely at the maximal parameter pair. The computations involve finite fields of specified order, no sampling, and explicit assertions. The mathematical deductions and their limits are stated in RESULT.md.

This establishes the asserted finite computations and a self-review only. External independent replication has not been performed. A broader classification of twists and complete historical priority are not asserted.
