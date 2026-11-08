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

# Reproduction and scientific limits

Run `python3 verify.py` in the directory containing `RESULT.md` and `verify.py`. The self-contained checker enumerates all binary words containing exactly three ones at every length from 3 through 26, computes each literal Abelian-cube factor by independently scanning its three equal blocks, and compares the result to the formula. There are exactly 17,550 such words in the tested range. It independently recomputes population sums and exactly integrates the three-piece planar area with rational arithmetic. It also compares the two-inequality continuum feasibility criterion with all pairs of interval bounds on integer meshes of sizes 9, 15, and 21.

Expected output:

```
DIRECT_CUBE_CLASSIFICATION_AND_AGGREGATES_OK 17550
CONTINUUM_FEASIBILITY_AND_EXACT_ATOM_OK 2/9
MEAN_COEFFICIENT_OK 1/270
```

The finite checker does not establish assertions for every length. The infinite claims rely on the exact interval bijection, the binomial and geometric-series identities, Riemann sums on the compact simplex, and the exact probability integral in `RESULT.md`. A separate independent audit has not been performed. The full text of the 2014 unrestricted-average publication was not accessible, so historical priority is qualified.
