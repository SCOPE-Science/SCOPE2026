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

# Verification of the stated polynomial-value Smith-form theorem

The proof in `RESULT.md` establishes every modulus by unimodular fiber reductions, exact minor ideals, and a Chinese remainder tensor product. The standalone `CHECKER.py` carries out exact integer matrix reductions in Python 3 with no third-party packages. It checked five polynomials, nineteen different moduli, and independently computed square-value cardinalities for five primes and multiple powers. It passed 126 grouped assertions, including the claimed \(N=15\) and \(N=4\) examples.

These finite tests verify displayed examples and support the calculation; the all-modulus correctness follows from the written proof, not the tests. Originality remains qualified by incomplete historical coverage, and no independent mathematical audit has been conducted.
