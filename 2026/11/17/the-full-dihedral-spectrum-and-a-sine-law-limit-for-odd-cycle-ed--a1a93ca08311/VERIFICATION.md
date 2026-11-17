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

The source proof gives the unrestricted odd-order statement. The standalone Python 3 checker uses exact rational arithmetic to reconstruct the incidence inverse and the projected facet-normal Gram entries for every odd order from \(3\) through \(39\). Its executed output included:

```
ODD_CYCLE_EDGE_SIMPLEX_PASS odd_orders=3..39 direct_normal_pairs=5130 distribution_orders=101,501,2001,10001
KOLMOGOROV 101 0.01980392
KOLMOGOROV 501 0.00399203
KOLMOGOROV 2001 0.00099950
KOLMOGOROV 10001 0.00019998
```

The distribution comparisons check only four finite large instances; the general convergence and its rate follow from the two parity-class arithmetic meshes in the proof. The basic lattice-volume relation is previously known. There has been no independent audit or external certification.
