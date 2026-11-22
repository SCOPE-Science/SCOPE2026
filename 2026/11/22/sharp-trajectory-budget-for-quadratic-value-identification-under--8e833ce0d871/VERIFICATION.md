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

# Verification of the quadratic-regression trajectory theorem

The characteristic-zero proof is the temporal/product-class factorization followed by a simultaneous rank-one Vandermonde witness; it does not use a computer or finite search to establish the all-dimensional statement.

A standalone supplementary checker `CHECKER.py` was run on the packaged source. It reported: `PASS: 63 exact-rational-spectrum families, 643 finite-field rank comparisons; all matched the proven formula`.

The checker explicitly constructs the modal start vectors, the observations at all required times, and the resulting quadratic design. It checks rank over a large prime field for geometric, equal, zero, signed, and partially repeated spectra. Modular tests support the algebra but do not certify arbitrary real spectra, all matrix dimensions, the genericity argument, or independence from literature. No randomized numeric solver or finite test replaces the written proof.

Reproduce with `python3 CHECKER.py` from the package directory. This requires only the Python standard library. Independent mathematical audit has not been performed.
