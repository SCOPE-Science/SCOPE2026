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

# Reproduction and verification

Run `python3 verify.py` from the directory containing the standalone script; it uses the Python 3 standard library only. It prints `PASS: 849 standalone arithmetic/numerical assertions` when all tests succeed. The tests cover exact rational three-level stationarity at 149 reset probabilities, independent complex-matrix calculations, derivative signs, four-measurement rational interpolation and residue recovery, and the six-point homometric obstruction at 99 reset values.

The rigorous infinite and all-parameter statements depend on the renewal sum, positive pole decomposition, polynomial uniqueness bound, and the explicit pairwise difference identity in `RESULT.md`. The checker is supporting evidence and not exhaustive verification over continuous reset probabilities, unknown dimensions, or all spectra. The spectral gap number is assumed known and no finite-precision error bars are proved. Independent audit has not been performed.
