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

The theorem is established by the cell-presentation proof, not by experiments. The two scripts below test independently specified finite instances; they are not an infinite certificate.

Run `python3 check_nerve.py` with Python 3. This script uses only its standard library, constructs every ordered nondegenerate cell at total length at most two, verifies signed boundary composition and computes exact finite-field ranks over four primes for six Hamming profiles and a five-cycle negative control. Expected stdout is `verification_output.txt`.

Run `python3 check_quotients.py` with Python 3 and SymPy installed (the exact Smith normal form routine in `sympy.matrices.normalforms`). This independent implementation builds the integral translation-orbit chain complex from the first-vertex-normalized ordered simplices. It tests seven profiles, verifying that all nonzero Smith factors are either units or exactly \(d\) copies of \(q\). Expected stdout is `quotient_output.txt`.

For the smallest nontrivial higher-dimensional examples, the cover on \((d,q)=(2,2)\) has \(\widetilde H_2\cong\mathbb Z^7\), and its quotient has \(H_1\cong(\mathbb Z/2)^2\), \(H_2\cong\mathbb Z\); the cover for \((3,3)\) has \(\widetilde H_2\cong\mathbb Z^{512}\), while the quotient has \(H_1\cong(\mathbb Z/3)^3\), \(H_2\cong\mathbb Z^{18}\).

Boundary of the claim: dimension and alphabet-size parameters are arbitrary positive integers with \(q\ge2\), but only inclusive length two and the whole translation group are classified. There is no standalone integer Smith calculation for every parameter and no claimed knowledge of the quotient's higher homotopy, cup products, or the integral second-homology deck module. Independent mathematical audit has not been performed.
