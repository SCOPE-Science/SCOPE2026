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

Run `python3 verify.py` in the directory containing the six research files and this standalone checker. The checker requires only the Python standard library and performs 38 deterministic assertions: positive scaling-profile checks, independent finite-persistence mode-space and transformed-integral quadrature comparisons, convergence under increasing persistence, and short-/long-time diagnostic ratios for the exact dimension-five profile. It prints the dimension-five value at unit scaled lag.

The mathematical argument in `RESULT.md` is self-contained in the stationary continuum Debye model. No finite quadrature validates the infinite-dimensional limit or proves the asymptotic constants; those are supplied by a positive-kernel dominated-convergence argument and two asymptotic integral reductions. The checks also do not address excluded boundary dimensions, finite-system zero-mode effects, or literature priority.
