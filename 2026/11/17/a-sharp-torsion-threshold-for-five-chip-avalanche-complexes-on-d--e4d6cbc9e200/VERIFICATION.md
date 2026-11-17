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

# Integral verification

Execute `python verify.py` in the same directory as `census.csv`, using `sympy>=1.13,<2` (see `requirements.txt`). The program independently regenerates and overwrites the entire census from graph dynamics' exact cyclic-translate description; it does not take the CSV as an input.

The command was executed successfully. Its exact result was:

```
dihedral_classes=747; length15_five_chip_classes=111
torsion_cases=14; each has H1_torsion=(Z/2)^2
ten cases: H1_free=2,H2_free=1; four cases: H1_free=1,H2_free=0
all other listed integral groups torsion-free
uncollapsed_witness_matrix_checks=2 passed
census.csv bytes=28044 sha256=7b680b2b1242115d43cdf44c974c40e515e5335043e9cc3eb549615b963e231b
```

For each representative, exact integer Smith forms are taken for all boundary maps surviving the elementary collapses; homology free ranks follow by rank–nullity and torsion by the Smith factors. Two witnesses are separately checked using the original uncollapsed complexes. The verifier explicitly asserts the fourteen canonical supports and both free-rank signatures. Its loops are exhaustive only over the finite domain \(3\le n\le15\), \(|S|\le5\); no conclusion about longer cycles or larger chip budgets is computed or claimed. The integer Smith routine is a library implementation and no independent external validation is claimed.
