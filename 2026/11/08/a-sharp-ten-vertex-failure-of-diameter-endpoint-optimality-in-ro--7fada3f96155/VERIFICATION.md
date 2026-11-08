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

# Reproducible verification

Run `python checker.py` after installing the versions in `requirements.txt`. The checker independently performs four groups of exact operations: enumerate all ordered preferences of four and five cars for the four orbit representatives of the ten-vertex witness; count every root and car-load combination in every nonisomorphic free tree through order ten using an exact integer recursion; form the six symbolic four-car root-count polynomials using orbit equality patterns, and simplify all five differences; and compare the polynomials to separately computed integer counts at several parameter pairs.

Observed: 201 unlabelled tree types, 16,755 exact root/load evaluations, only B(3,3) at four and five cars failing the existence of a diameter-endpoint optimizer. Exact rooted counts for four cars are center 8,898, hub 8,855, central pendant 9,290, diameter pendant 9,263; for five cars center 76,140, hub 76,650, central pendant 85,500, diameter pendant 85,378. The symbolic identities are proven for arbitrary positive integers, not inferred by interpolation. An independent manual mathematical review has not been performed. Exhaustiveness depends on the standard nonisomorphic-tree generator, with orderwise known counts checked as coverage safeguards.
