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

The result is proved mathematically for all positive graph orders in `RESULT.md`. Two executable, standard-library-only Python checks are supplied. `python3 verify_direct.py` enumerates all normalized integer states in \([0,2n]^n\) for graph orders \(1\) through \(5\), compares direct second iterates with the block-gap characterization, counts fixed points, and matches the finite composition count; it ends with `DIRECT_OK`. The proof bounds the spread of every initially periodic normalized state by \(2n-3\) when \(n\ge2\), so the tested boxes contain all such states in these dimensions. `python3 verify_egf.py` compares independent composition counts against coefficients of the rational-exponential generating function with exact fractions through graph order \(13\); it ends with `EGF_OK`.

These checks do not enumerate states of every graph order, prove analytic pole uniqueness, or constitute independent expert certification. They are reproducibility checks supplementary to the all-size algebraic and analytic arguments. Captured outputs are in `verify_direct.out` and `verify_egf.out`.
