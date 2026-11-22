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

# Exact internal verification and limits

Run `python verify.py` with Python 3 and SymPy (tested with 1.14). The checker constructs the matrix directly from the finite type-gap criterion and obtains Smith normal forms independently with SymPy over the integers for parameter lengths \(1\) through \(9\). It also enumerates all ways of inserting two distinct new points in both linear orders for each of the 33 distinct parameter permutations of lengths \(1\) through \(4\), comparing 16,714 feasibility entries to the proposed formula.

Observed output:

```
{"base_permutations": 33, "feasibility_cells_checked": 16714, "smith_parameters_checked": [1, 2, 3, 4, 5, 6, 7, 8, 9], "status": "VERIFY_OK"}
```

No finite computation is treated as proving the theorem for all parameter lengths. The all-length argument instead consists of exact finite-difference transformations of the integer cokernel presentation. The finite tests do not settle historical priority or supply independent validation. The review status is same-model only; no independent audit evidence is supplied.
