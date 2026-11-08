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

# Reproducible checks and boundaries

Execute `python3 verify.py` with Python 3.8 or later; no external packages are required. The script constructs the graph independently of the resistance proof, grounds every unordered pair of candidate leaders for page counts from 2 to 9, inverts the exact integer Laplacian blocks over rational numbers and checks all 708 results against the six closed formulas. It checks 30 effective-resistance identities by a separate single-grounding computation, verifies the minimizer orbits and counts, and samples the sign comparisons through page count 199.

Successful replay on the packaged source gave:

```text
m=2  optimum=opposite  count=2  J=46/21
m=3  optimum=hub-far  count=6  J=95/24
m=4  optimum=hubs  count=1  J=16/3
m=5  optimum=hubs  count=1  J=20/3
m=6  optimum=hubs  count=1  J=8
m=7  optimum=hubs  count=1  J=28/3
m=8  optimum=hubs  count=1  J=32/3
m=9  optimum=hubs  count=1  J=12
VERIFY_OK exact_grounded_pair_comparisons=708; resistance_sample_checks=30; sign_samples=198
```

The infinite assertion is supported by the resistance reductions, exact two-terminal energy minimization, six rational formulas and sign factorizations in `RESULT.md`. Finite checks do not establish the theorem independently. This validation is a self-review; no independent scientific audit has been performed. Possible unindexed equivalent literature remains the principal originality limitation.
