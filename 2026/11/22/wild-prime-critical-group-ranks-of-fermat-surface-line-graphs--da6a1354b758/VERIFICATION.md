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

The exact standard-library verifier `verify_fermat_wild_rank.py` was executed from the accompanying package. Its generated output is `verification_output.txt` and terminates `FERMAT_WILD_CRITICAL_RANK_OK`. It tests prime degrees 3, 5, 7, 11, and 13; confirms every finite graph matrix entry against the stated congruences and an independent projective-determinant construction; checks the factorization \(L=-EHE^T\), explicit evaluation kernel and Gram ranks; and computes modular Laplacian ranks directly.

For prime 3 the modular Laplacian rank is 7 and graph-critical-group 3-rank is 19; prime 5 gives 26 and 48. Primes 7, 11, 13 yield Laplacian ranks 48, 96, 120, and corresponding critical-group ranks 98, 266, 386. Auxiliary projective-determinant checks cover all 351, 2,775, 10,731, 65,703, and 128,271 distinct pairs of lines at these degrees. No floating-point computation enters the certificate.

The all-prime assertion does not follow from the five test cases. Its infinite step uses the displayed degree-at-most-two spanning set of the evaluation kernel and vanishing of sums of polynomials of degree at most four over \(\mathbb F_p\) for all primes \(p\ge7\). The proof is limited to the critical-group \(p\)-rank, not the entire critical group; independent mathematical audit has not been performed.
