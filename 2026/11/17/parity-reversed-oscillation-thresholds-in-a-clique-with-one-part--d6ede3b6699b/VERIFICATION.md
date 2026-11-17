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

The proof in `RESULT.md` uses exact local bitwise majority maps, an exhaustive two-phase structural case distinction valid for all indicated integer parameters, and a bounded monotone energy argument excluding longer periods. The orbit classification yields an explicit unique-predecessor argument for every two-cycle.

Reproducible computational corroboration:

```
g++ -O2 -std=c++17 check_direct.cpp -o check_direct
./check_direct
python3 check_symbolic.py
```

Outputs are stored in `check_direct.log` and `check_symbolic.log`. The C++ checker exhausts all labelled states on 117 distinct graphs and verifies fixed points, orbit counts and absence of nonperiodic immediate predecessors. The separate count-weighted Python script reproduces the counts for 1,827 graph parameters. These checks are finite and do not prove the unbounded parameter theorem. The analytical proof supplies that step. Earlier literature not available in full may affect historical priority; no external mathematical audit is represented by these checks.
