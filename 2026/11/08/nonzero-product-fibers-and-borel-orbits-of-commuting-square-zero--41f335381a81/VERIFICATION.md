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

Run `python3 verify_borel_product.py` with Python 3 standard library. The independent direct enumeration checks every square-zero strictly upper-triangular matrix and every commuting ordered pair for fields of orders 2, 3, 4 and 5, tabulating all products. The order-four implementation uses polynomial arithmetic over the extension field defined by \(z^2+z+1\), rather than integer arithmetic modulo four.

For fields of orders 2, 3 and 4, the checker independently generates simultaneous conjugacy orbits under the invertible upper-triangular group, using elementary adjacent transvections and diagonal generators. It compares the disjoint orbit sizes and their union with the closed formulas.

`checks.txt` records the exact output reproduced from the enclosed checker. Exhaustion of finite samples does not prove identities over all fields. The unrestricted proof instead uses invertible block coordinates and stable ideals in the four-dimensional regular module of \(k[s,t]/(s^2,t^2)\). This is a self-review only; no independent mathematical audit, priority certification, or nonreduced-scheme calculation has been performed.
