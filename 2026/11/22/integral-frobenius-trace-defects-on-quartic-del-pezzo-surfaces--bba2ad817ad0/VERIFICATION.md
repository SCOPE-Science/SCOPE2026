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

# Reproducible exact verification

The attached `verify_quartic_trace_lattice.py` is standalone Python 3 requiring only the standard library. From its directory run:

```sh
python3 verify_quartic_trace_lattice.py > calculated.csv
cmp calculated.csv quartic_trace_lattice_classes.csv
```

The certificate includes the conjugacy-class size, Frobenius element order, fixed Picard rank, line-orbit partition, orbit-trace index, and a reflection word for each of eighteen conjugacy classes. It checks the group order \(1920\), all eighteen conjugacy classes, the agreement of two independently computed ranks for each element representative, the complete distribution \(1^{12},2^3,4^2,16\), and the four indices for orbit pattern \(4^4\).

Integer matrices, exact rational row reduction, and fraction-free determinants are used throughout. Every rank-size minor required by the determinantal-divisor theorem is examined unless an index of one is already proved by a unit minor. This program does not establish that the source geometry and its standard \(W(D_5)\)-representation are previously unknown; those facts are cited as prior work. The arithmetic calculation has received self-review, not independent validation.
