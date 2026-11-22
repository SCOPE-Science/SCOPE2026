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

# Computational and mathematical verification

`verify.py` is a self-contained Python 3 checker using only the standard library. It independently constructs the vertices from the cited vertex theorem, exhaustively checks every unordered squared distance, and tests the largest and second distinct values and second-shell multiplicity against the formulas. Run `python verify.py` with the files in this directory. The exact output is:

```
GENERALIZED_PARKING_SECOND_SHELL_EXACT_PASS cases=9
```

The cases cover dimensions four, five and six, distinct positive parking increments, missing/imbalance/overlap winners, and multiway ties. All arithmetic is exact integer arithmetic; no tolerance is used.

The infinite-domain proof is mathematical rather than computational: it uses the exact source vertex theorem, rearrangement inequalities for oppositely aligned coordinate lists, discrete strict concavity for rank selection, overlap-deletion improvements, and a separate exclusion of defective balanced rank configurations. Computer checks do not establish untested parameters or historical priority.
