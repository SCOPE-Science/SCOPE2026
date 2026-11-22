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

# Reproducibility and verification

Run `python3 verify.py` with Python 3; the script needs no third-party dependencies. A completed run printed:

```
VERIFY_OK raw_lattice_subsets=8183; path_orders=0..11; ring_orders=3..11
path counts: [0, 1, 2, 4, 6, 9, 13, 18, 25, 34, 46, 62]
ring counts: [3, 6, 5, 11, 14, 18, 30, 37, 55]
```

The code independently lists Horn-closed sets, determines meet-irreducibles directly by testing all intersections of pairs of strict closed supersets, compares complete omitted-atom multiplicities to the two rational-series coefficients, and tests the separate Fibonacci closed-set counts. The path orders include the empty case. The ring orders begin at three because smaller cyclic rule systems are outside the theorem's scope. The generating series and growth results for arbitrary length are proved in the accompanying text; exhaustive checks through these finite orders are corroboration, not universal certification. No external independent audit has been performed.
