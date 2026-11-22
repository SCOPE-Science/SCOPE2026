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

# Reproducible checks

The standalone `check.py` constructs exact binomial transition matrices using rational arithmetic. It verifies stochastic row sums, one-step survival, the stated two-sided spectral-rate bounds, survival monotonicity and strict submultiplicativity for degrees \(2\)–\(8\) and powers \(1\)–\(5\). It tests 1,662 random zero-endpoint nodal vectors using a numerical polynomial critical-point method. The final check output is `ALL_ANCHORED_BERNSTEIN_CHECKS_PASS`.

Run with `python3 check.py` (Python standard library and NumPy). No external datasets or downloaded resources are needed. Numerical stress tests can detect counterexamples but cannot certify the universal assertions; those rely on the independent analytical proof in `RESULT.md`. Exact rational checks cover only the explicitly stated finite degrees and powers.
