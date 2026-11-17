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

# Reproduction

Run `python3 CHECK.py` from this directory. It uses no nonstandard packages and performs exact arithmetic. Its exhaustive strict-order checks certify all selector matrices at sizes two through five: 2, 6, 24 and 120 permutations, yielding respectively 1, 3, 12 and 60 distinct selector maps. The exact rational Schur-complement test verifies the centered squared-norm bound two for all small chambers; analytical evaluation handles the special two- and three-site constants. Explicit perturbation vectors yield squared ratios two at four and five sites. A family of direct exact-window checks through size 100 confirms, but does not replace the uniform proof, that the two selected columns are repeated three times for every size at least six.

# Mathematical limitations of computation

Exhausting the rank permutations is mathematically exhaustive only for the finite sizes two through five. The upper bound at unbounded dimensions and the two-column witness construction are independently proved by a locality argument and a direct formula valid for all integers \(n\ge6\). Numerical sampling and independent expert audit are not claimed.
