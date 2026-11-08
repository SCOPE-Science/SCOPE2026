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

From this package's root, run `python3 checks/verify.py`. It uses only Python's standard library. It explicitly constructs the unit hyperbolic shell in small finite rings and computes every Fourier coefficient as an exact cyclotomic coefficient-count vector, testing the predicted zero pattern against the actual cyclotomic relation. Cyclic prime-square and equal-characteristic split square-zero rings are both included. The extension-field test \(\mathbb F_4[t]/(t^2)\) uses its exact four-element-field arithmetic and exact sign character; the chosen frequencies in the higher-dimensional instance are a reproducible pseudorandom sample.

The tested \(n=2\) frequency universes have \(256\) frequencies for \(q=2\) and \(6561\) frequencies for \(q=3\) in each of the cyclic and split variants. They produce convolution ranks 112 and 2025, respectively. Additional tests include \(n=1\) as a boundary sanity check (not a claim of its novelty), \(q=5\) cyclic, and \(q=4\) split. No tolerance-based zero test is used. Code execution is a finite check, **not** an exhaustive test of all rings or a proof of the universal result.

# Mathematical scope and limits

The theorem is proven by exact character orthogonality, square-zero stationary phase, and cyclotomic noncancellation; those proof steps stand independently of the checker. The statement is restricted to finite commutative length-two chain rings, unit level and \(n\ge2\). Broader local-ring Fourier results could duplicate the statement after specialization; the bounded comparison does not certify independent priority. Independent mathematical audit is not performed.
