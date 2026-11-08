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

# Verification of the antisquare factor and density theorem

The bundled standalone `verify.py` constructs the bits from the divisibility definition for all integer bases 2 through 14, generates every antisquare of order 1 through 32 starting at 16,000 consecutive positions, checks the exact predicted factor set and occurrence counts, and repeats the comparison for 18 finite cutoffs. It prints `VERIFY_OK bases=2..14 starts=16000 order_max=32 prefix_checks=18` when all assertions pass. The executable was run from bytes extracted from this package.

The scientific proof does not use finite enumeration to assert infinity. The universal classification is proved using an upper bound on the ones in any window, the forced alternating form at base two, and parity of the central valuation. Exact finite-prefix counts are proved by valuation-class inclusion/exclusion and the density laws follow from explicit geometric series. No external formal certificate or independent validation is claimed.
