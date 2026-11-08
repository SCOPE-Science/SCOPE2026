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

Extract the attached `check_formula.py`, `check_direct.py`, `formula_run.txt` and `direct_run.txt` files into the same directory. With Python 3.10 or newer, run:

```
python check_formula.py
python check_direct.py
```

The first program independently builds the graph by enumerating all valid slides, breadth-first searches from the standard diagonal state for orders 2 through 8 and compares exact distances and invariants with the claimed expression. The second program enumerates edge subsets and tests slide adjacency directly for orders 2 through 5, then performs an independent breadth-first search; it imports only the mathematical metric function from the first program.

The first run explored 322,560 states at order eight and found diameter eleven. The direct matching enumeration found 600 states and 2,400 undirected edges at order five, with diameter six. All tests completed successfully and the output logs reflect those executions. These finite tests support but do not replace the general proof. The article contains the noncomputational all-order argument.
