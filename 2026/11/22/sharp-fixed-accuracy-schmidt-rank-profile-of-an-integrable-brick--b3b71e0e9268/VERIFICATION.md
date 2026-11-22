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

# Verification and reproducibility

From the directory containing `RESULT.md` and `verify.py`, run:

```sh
python verify.py
```

The script uses only Python's standard library and directly constructs the finite folded two-site permutation gate, the normalized identity backgrounds, and the inserted one-site matrix unit. It checks the exact count-sector Gram idempotence identity, the nonzero squared singular-value multiplicities, and the prescribed combinatorial block weights at integer times 1, 2 and 3. The observed output was:

```text
t=1 exact folded count-block checks passed: 12
t=2 exact folded count-block checks passed: 140
t=3 exact folded count-block checks passed: 2584
PASS 2736
```

The general theorem uses the initiating paper's analytically proved flat count-block singular spectrum, rank and operator-norm bounds, the Eckart–Young extremal principle and a binomial central-limit theorem. The finite checker is an independent low-time consistency check of its nonstandard input, not an infinite-time proof, a full independent audit, or a proof of optimal global tensor-network bond dimension.
