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

The proof was inspected step by step: the fastest right-to-left influence path is unique; its Boolean derivative factors into local derivatives; the successive unperturbed center bits use new fair leftmost input coordinates, hence are independent; the resulting expectations give the stated trichotomy and class census.

The embedded `check_edge_influence.py` independently enumerates all 16 left-permutive elementary rules and all finite initial assignments for each time from 1 through 6. It passed 96 exhaustive rule/time comparisons plus 80 exhaustive boundary-independence and fastest-path factorization comparisons for times 1 through 5. Execute using `python check_edge_influence.py`. Finite enumeration is not used as proof for unbounded times.

Publication priority is provisional. The motivating primary text was inspected, but a broader 2025 survey was available only through an indexed excerpt. No external independent audit has been performed.
