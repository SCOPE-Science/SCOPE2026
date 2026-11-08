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

# Verification

The standalone `verify.py` computes the exact finite-sample terminal-minimum count distribution by two independent methods: a rational gamma-integral coefficient formula and absorption recursion for the original count-vector process. It tests every pair of integers with `2 <= n <= 5` and `1 <= m <= 3`, checks nonnegativity and unit total mass, and recovers the harmonic-number identity for singletons when `m=1`. It prints `PASS: 143 exact-rational assertions across n=2..5, m=1..3` on success. Run `python verify.py` with the Python 3 standard library. The tests are finite checks and do not replace the asymptotic proof, including the compact-uniform quantile and marked mixture arguments.
