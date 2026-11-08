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

# Verification notes

The accompanying `verify.py` is a standalone Python 3 standard-library checker. Running `python3 verify.py` gives `VERIFY_OK finite_prime_checks=5 head_coefficients=16 disjoint_gaps=15` and exact rational upper-tail and prime-gap coefficients. The exact tests certify the finite-prime tail inequalities for \(p\in\{11,13,17,19,23\}\), the uniform Nagura-tail coefficient, the rational upper bound on \(\log U\), the strict ordering of all sixteen small-prime products, and the least consecutive product ratio \(344/343\).

The mathematical proof, not the program, establishes the universal assertions. Its noncomputational steps are: multiplicativity on squarefree inputs; an infinite-subsums interval lemma; Nagura's 1952 theorem for primes beyond any integer at least 25; the logarithmic inequalities \(\log(1+t)\le t\) and \(\log(1+t)\ge t-t^2/2\) for \(t\ge0\); and the elementary integral comparison for the tail of odd reciprocals. None of these is replaced by a finite experiment.

The closure does not assert that every point is reached by a *finite* squarefree input. The sixteen-component assertion is restricted to the exponent-three squarefree domain, and cannot be extrapolated to all integer inputs, other exponents, or all connected-component parameters. The published priority comparison is not an independently audited novelty certificate.
