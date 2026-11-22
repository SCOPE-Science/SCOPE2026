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

# Reproducibility

Run `python verify.py` in a directory containing only the extracted standalone checker. The script requires the standard Python library, no downloads and no other artifact files. It computes direct permutation orbits from the polynomial definition, independently constructs the predicted exact cycle vector using quadratic congruence roots, and compares the two. It also enumerates all parameters in smaller prime-power ensembles and checks the rational covariance matrix and exact distinct-type frequencies.

The checked odd primes were 3, 5, 7 and 11. Moduli and parameter ranges are explicitly bounded inside the code. Successful local replay returned `PASS: 2606 direct permutation-cycle checks;  14 exact parameter moment/type checks`. This tests finite samples, **not** the infinitely many primes, levels or limiting probabilities. Those require the proof in `RESULT.md`, including the p-adic period-growth lemma, the root-count martingale, and the Haar-measure argument.

The self-review checked the proof hypotheses and formal output; independent audit and external scientific validation have not been performed.
