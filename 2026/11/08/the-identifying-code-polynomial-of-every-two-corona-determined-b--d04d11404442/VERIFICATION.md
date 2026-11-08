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

# Reproducibility and limits

Run `python3 verify.py` with an ordinary Python 3 interpreter. The standalone code uses the standard library only and is independent of the theorem in its definition of an identifying code: it forms every graph's closed neighborhoods, enumerates every selected vertex subset, and requires the resulting nonempty traces to be pairwise distinct.

The script exhaustively tests all connected labeled core graphs of orders 2, 3, and 4; it additionally tests a path, a cycle, a star, a complete graph, and a tailed cycle on five core vertices, as well as a six-vertex path. It compares graph-level eligibility with the claimed local three-state classification and compares every cardinality coefficient with an independently multiplied class-factor polynomial. It also checks the predicted count of minimum-size codes and the total number of codes.

Expected successful line from an actual execution:

`VERIFY_OK base_graphs=49 direct_subsets=583744 identifying_codes=4805 characterization=PASS full_polynomial=PASS minimum_multiplicities=PASS`

This is an exhaustive verification only for the stated finite collection of cores. It is not an exhaustive enumeration of all graphs of larger order. The unrestricted result is proved directly in `RESULT.md` by comparing all trace types and counting the independent choices inside each closed-twin class. A separate external mathematical audit has not been performed.
