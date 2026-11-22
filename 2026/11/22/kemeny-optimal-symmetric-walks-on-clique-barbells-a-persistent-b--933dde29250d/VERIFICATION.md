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
# Reproduction

Use Python 3.10+ with SymPy 1.10+ installed, in the same directory as `verify.py`, then run:

```sh
python verify.py
```

The checker constructs the entire Laplacian of two cliques linked by one bridge and compares an independently inverted exact rational resolvent with the proposed four-eigenmode formula. It checks 18 rational designs across clique sizes 3–8, six maximum-degree benchmarks, the stationary-point inequalities and asymptotic diagnostics, for 63 assertions in total. This is finite reproducibility evidence, not a proof of infinitely many graph sizes; all-size validity follows from the analytic argument in `RESULT.md`.

The matrix expression uses the zero-at-start version of Kemeny's constant; adding one to use the return-time convention leaves all optimization conclusions unchanged. No external mathematical audit is asserted.
