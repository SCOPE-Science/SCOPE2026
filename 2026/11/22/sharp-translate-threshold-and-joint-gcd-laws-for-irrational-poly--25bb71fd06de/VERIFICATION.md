---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For r≤d the first r translate moments form an invertible Vandermonde system, so any nontrivial integer combination has a nonconstant coefficient that is a nonzero rational multiple of α. Its leading nonzero nonconstant term stays irrational on any arithmetic progression after dividing by a fixed modulus. Weyl and the floor-residue boxes therefore give joint uniform residues with n and the claimed lcm denominator. Inclusion–exclusion gives the displayed local factors; for two equal exponents a single increment increases the exponent by 2 and both by 3, while for unequal exponents the two separate increments cost 1 and 2. For tightness, the full-N large-prime estimate quoted from Holdridge is exactly what is needed. The exact statement of Theorem 1.3 was inaccessible, but the required tail can also be derived from the natural-density coprimality result announced in Holdridge’s PDF abstract (its one-polynomial case, with Weyl equidistribution assured by an irrational leading coefficient). In detail, write n=am with a the part supported on primes ≤R. A common prime >R then gives gcd(m,⌊f(am)⌋)>1, while no prime ≤R divides both. For each fixed a this latter superset has density c_R=∏_{p≤R}(1−p⁻²)−1/ζ(2), by fixed-prime Weyl and the one-polynomial coprimality theorem applied to f(a·), which still has irrational leading coefficient. Summing the limsup bound c_R/a over smooth a is justified by the summable majorant 1/a for fixed R. The resulting bound c_R ∏_{p≤R}(1−1/p)⁻¹ is O(R⁻¹/²): c_R=O(1/R) and bounding the reciprocals of odd primes by those of odd integers gives O(√R) for the inverse product. This checks the needed large-prime step without relying on the exact wording of Theorem 1.3. A finite union over shifts and the fixed-p bound p⁻²ᴷ control all tails. CRT gives the same finite-prime laws as the shared Haar model, whose gcd ideals almost surely have finite positive generators since ∑_p r/p² converges. Every specified finite valuation profile has positive probability, and at all other primes the factors are 1−O_r(p⁻²). For d+1 consecutive shifts the integer finite difference of the floor values lies within 2^d of αd!; the choice α>2^d/d! irrational and p>αd!+2^d excludes all simultaneous multiples despite the positive proposed formula. This is existential in α for each d, not failure for every α. The uploaded finite checker was inspected, not executed and not used for the limit.

## originality

PASS

Best-of-knowledge pass only for the joint law of separate dependent GCDs for at least two translates and the sharp universal rank threshold with an explicit obstruction. The fixed-modulus Weyl method, the large-prime control from Holdridge and the r=1 case are not original contributions. The primary abstract directly establishes a strong common-coprimality result, not this separate joint law; unresolved full-text coverage is noted rather than treated as absence.

## value

PASS

Gives a complete law and exact local correlations for the natural shared-coordinate problem, not just the frequency of one common gcd being 1. The finite-difference counterexample identifies precisely the universal degree-controlled number of translates at which the law can fail. The explicit positive factors and the obstruction are useful even though the hard tail estimate is borrowed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
