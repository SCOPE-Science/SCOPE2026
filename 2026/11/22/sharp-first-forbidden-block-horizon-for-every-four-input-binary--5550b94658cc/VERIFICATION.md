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

The exact finite census can be reproduced with `python3 verify_census.py` and, independently, `c++ -std=c++17 -O2 verify_census.cpp -o verify_census && ./verify_census` using files in this package. Both traverse **all 65,536** rule tables and use complete breadth-first search on the 256 subset states of the eight-vertex labeled de Bruijn graph. The former also performs direct binary-block cross-checks and proves the eight missing words at length 18 via exhaustive integer state-count propagation.

The semantic soundness of the check is justified in the theorem's de Bruijn path and subset-state induction. Computational enumeration alone does not certify claims outside the finite four-input family. All declared checks were executed successfully; no independent external mathematical audit has been performed.
