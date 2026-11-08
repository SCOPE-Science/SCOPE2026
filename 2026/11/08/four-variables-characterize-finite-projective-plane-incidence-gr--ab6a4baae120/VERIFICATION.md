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

# Reproducible finite checks

Run the supplied three Python programs with a standard Python 3 interpreter:

```
python3 recognition_check.py
python3 formula_check.py
python3 pebble_check.py
```

Exact standard output from those runs is provided in the three corresponding `_output.txt` files. `recognition_check.py` constructs the Fano and ternary projective-plane incidence graphs, tests all six semantic axioms and all 91 one-edge perturbations of the Fano graph, and rejects the complementary Fano biplane. `formula_check.py` independently constructs the *actual closed first-order formula syntax trees*, checks that no name beyond \(x,y,z,w\) occurs, and evaluates all six clauses on the two projective planes and the complement. `pebble_check.py` independently enumerates all ordered two-pebble atomic types and their possible one-vertex extensions in these three graphs, confirming matching response supports.

These are finite sanity checks and not an exhaustive search of all graphs or a formal proof of any infinite statement. The unrestricted recognition and three-pebble equivalence are established by the mathematical argument in `RESULT.md`. No independent mathematical audit has been performed.
