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

The proof gives a uniform exact formula for every odd prime, with no reliance on numerical extrapolation. Its critical steps are the finite-field character-correlation identity, the exact \(t\)-adic leading coefficient of the prime-level group-algebra polynomial, the two-root Hensel lift on units, and the integral block reduction at prime-square modulus. The localized pivot is justified by proving that the square-residue adjacency block is invertible modulo the characteristic prime; the determinant calculation then rules out other torsion primes.

Exact checker invocation: `python checker.py`, requiring Python 3 and SymPy. The actual standalone checker passed 46,351 exact assertions, including direct Smith forms at prime squares \(9\) and \(25\), prime-level Smith forms for seven primes, and elementwise prime-square congruence-lift checks for five primes. It does not directly compute Smith forms at all prime squares, and a numerical test is not an infinite proof.

The scientific novelty comparison covers prime-field Paley Smith groups, selected integral circulants, polynomial circulants, prime-power Gauss sums, and indexed semantic searches. A previously unlocated general theorem on integral Cayley convolutions could still subsume this explicit formula. There has been no independent audit.
