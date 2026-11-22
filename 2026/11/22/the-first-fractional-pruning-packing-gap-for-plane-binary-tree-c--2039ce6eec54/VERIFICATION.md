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

# Reproducibility of the finite pruning-code result

`certificates.json` contains all tree and received-shape strings, the complete exact deletion incidence, a disjoint output-shadow codebook, and exact rational primal and dual LP witnesses for each of the six lengths. No external dataset is required.

Run `python3 verify.py` and `python3 alternate_verify.py` from this directory using Python 3 (standard library only). Both recompute the entire incidence from the defined tree-pruning channel and check it against the data. Both then confirm all disjointness constraints and rational primal-dual inequalities and their equality objectives. Successful runs print `VERIFY_OK` and `ALTERNATE_OK`.

The exact fractional maxima are \(1,1,2,3,7,205/13\); integer codewords are \(1,1,2,3,7,15\). The last LP value has denominator 13, and the integer rounding bound proves a maximum of 15 because \(205/13<16\). These checks cover sizes \(n=1,2,3,4,5,6\) only. The scripts are direct reproducibility checks, not an independent mathematical audit or a general theorem certificate for larger sizes.
