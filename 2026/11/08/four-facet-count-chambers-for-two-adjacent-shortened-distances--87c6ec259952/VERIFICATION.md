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

The claimed formula follows from a connected-tight-graph characterization of Lipschitz-polytope vertices, an exhaustive 16-state distinguished-triple classification, and a limit argument on the two parameter walls. The supplied `check_facets.py` executes exact rational comparisons for all four regimes, checks 54 outsider assignments families, and independently enumerates all four-point vertices from active inequalities for nine rational parameter pairs. Universal correctness is a mathematical claim based on the written proof; finite checker cases are not used as exhaustive proof over the real parameter domain or all dimensions.

Run `python3 check_facets.py` and `python3 check5_extra.py` from the directory containing the standalone programs. The second program independently enumerates all active four-constraint intersections for four five-point examples without using the 16-state templates. Python standard library only. No external verification or independent audit has been performed.
