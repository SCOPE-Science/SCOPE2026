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

This package includes `verify_fermat_quintic.py`, a standalone exact-integer verification script. Run `python3 verify_fermat_quintic.py` in the same directory. Its successful terminal message is `FERMAT_QUINTIC_75_LINE_CRITICAL_GROUP_OK`.

The checker builds the full 75-vertex line-intersection graph, tests all 2,775 unordered pairs independently using projective 4-by-4 determinants over \(\mathbb F_{11}\), proves its integer adjacency annihilator and four trace moments by explicit multiplication, and recovers the reduced-Laplacian Smith valuations over \(\mathbb Z/p^K\mathbb Z\). Three different reduced Laplacians are checked for each of primes 2, 3, and 5. Their valuation sums agree with the known determinant from Kirchhoff's theorem. The product and divisibility chain of the 74 invariant factors are verified.

The infinite-field statement does not follow merely from the finite-field test: the project's proof derives the complex intersection criteria algebraically from the explicitly listed line equations, then applies exact operations to the resulting finite integral graph. The prime-to-2,3,5 exclusion is established by the exact determinant. This certificate is neither a proof of publication priority nor an independent external audit.
