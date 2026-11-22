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

The proof applies to every pair of positive exponents and every pair of distinct primes. The standalone Python 3 checker `verify.py` builds ordered-factorization length histograms recursively from the first factor, without using the finite-sum formula, then compares with the claimed exact binomial/Jacobi expression over all 144 exponent pairs \(1\le a,b\le12\). Four sample vectors are independently asserted.

Run `python3 verify.py` in the directory containing this document and that script. Expected result: `PASS: 144 pairs of exponents, 4 illustrative coefficient vectors` followed by a note that infinite claims rely on analytic proof.

The root classification follows from the classical Jacobi orthogonality theorem and the explicitly nonzero endpoint evaluations. The independent Bernoulli representation follows by factorization of the normalized probability generating polynomial. The Gaussian limit follows from bounded summands and diverging variance. The finite checks are not certificates for all exponents and do not establish the novelty of this result.
