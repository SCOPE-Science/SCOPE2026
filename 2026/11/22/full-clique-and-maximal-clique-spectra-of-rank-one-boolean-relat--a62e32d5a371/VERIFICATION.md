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

Run `python3 verify.py` using Python 3 and only its standard library. The checker independently builds nonzero rank-one Boolean matrices as row-bitmask tuples, composes matrices by OR/AND, enumerates every clique recursively, tests maximality against the complete adjacency graph, and compares all bivariate coefficients with the signed Stirling formula and maximal-size coefficients with the second-kind Stirling formula. For ground-set sizes 1, 2, 3, 4, there are respectively 1, 9, 49, 225 vertices; 2, 11, 123, 6042 total cliques including empty; and 1, 8, 65, 725 maximal cliques. The final output line is `VERIFY_OK`.

This is an exhaustive test for those four finite sizes only; the all-size claims rest on the explicit proof in RESULT.md. No external computational libraries, datasets, or unprovided artifacts are required. Independent audit has not been performed.
