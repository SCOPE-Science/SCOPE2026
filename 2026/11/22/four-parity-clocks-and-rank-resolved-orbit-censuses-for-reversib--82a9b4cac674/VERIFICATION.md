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

## Reproducible verification
Run `python3 check_matrix.py` and `python3 verify_orbits.py` in the directory containing these files. Both require only Python 3 standard libraries. The matrix program independently constructs incidence matrices for six symmetric designs and verifies incidence parameters, global wave orders, and every time-\(t\) fixed-space nullity for \(1\leq t\leq12\). The direct-state program independently enumerates every two-row binary state for the \(3\)-point and \(4\)-point symmetric designs, comparing exact primitive periods and fixed-space populations.

The tests passed. In the direct-state runs, primitive-period state counts are \(\{1:4,2:12,3:60,6:4020\}\) for \((v,k,\lambda)=(3,2,1)\), and \(\{1:1,3:255,6:65280\}\) for \((4,3,2)\). Matrix checks also cover the Fano plane, its complementary design, an eleven-point biplane, and the point-hyperplane design of \(\mathrm{PG}(3,2)\).

No finite testing is asserted to prove the universal claim. The incidence Gram identity and the three Jordan-to-temporal module transfers provide the all-design argument; no independent external mathematical audit has occurred.
