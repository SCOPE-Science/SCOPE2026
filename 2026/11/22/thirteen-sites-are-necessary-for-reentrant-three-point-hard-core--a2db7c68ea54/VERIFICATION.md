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

# Reproducibility

Use Python 3.10 or later, from the package directory:

```sh
python verify.py
```

The completed run printed `TREE_CERTIFICATE_OK` and the rooted-tree counts `1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766`. It covered exactly 4765 marked rooted types whose root can be the median of three distinct vertices. All but two had fewer than two descending coefficient sign changes in the root-conditioned occupancy-difference polynomial. Both exceptional order-eleven cases had zero positive roots by exact rational Sturm sequences. The independent witness enumeration verified root-empty and root-occupied coefficient arrays and tested all 8192 occupancy masks for three-point cumulants at fugacity values 1, 4 and 15, giving signs positive, negative, positive.

All computations are exact integer or rational arithmetic; approximate root values in the result are informative only. The finite census requires the stated rooted-tree multiset enumeration, does not cover arbitrary trees beyond twelve vertices for the minimum argument, and does not establish priority of the theorem in the literature.
