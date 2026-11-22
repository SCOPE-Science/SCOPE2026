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

Run `python3 verify_stern_prime_threshold.py` with Python 3 and SymPy in the same folder as this document. The program directly constructs the \(p^2-1\)-state transition matrices for primes \(2,3,5,7,11\) and recomputes, over the exact integers, each stated characteristic factorization. It separately checks all dyadic initial-prefix residue counts for exponents \(0\) through \(12\), proving that the implementation matches the definition in these test ranges.

For prime \(11\), the same script computes the rational polynomial \(P(X)\) and reproduces the nonzero matrix-polynomial coefficient \(573530441763580574433280\) on the pair \((1,2)\). It checks the cubic's irreducibility and the exact inequalities for the reciprocal-quartic radial bounds. The exact matrix certificates support the algebraic proof of all-depth root-growth; finite prefix comparison by itself does not prove any all-depth assertion.

No external or independent audit was performed.
