---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

At fixed sum s, the invertible change u=x−y gives 4t=s³+3su². If g=gcd(3s,p^k), a necessary condition is g|4t−s³; after division, there are g lifts of each root mod p^k/g. The singular case g=p^k gives one t and p^k pairs; it occurs once for p≠3 and three times for p=3, even at k=1. For a nonzero reduced target with valuation d, the valuation must be even (d=2h), and a unit root mod p has exactly one lift at each successive step by its derivative 2u; two roots each acquire p^h lifts when restoring the factored p^h. For the zero target the root count is p^floor(j/2). Counting attainable unit squares at the even valuations gives Q_p(j). At fixed nonsingular s the admissible quotient residues c range over all p^j values; only the square residues have nonzero fiber. The sum of their squared root counts equals Σ_{a mod p^j} gcd(a,p^j)=p^j+j(p−1)p^{j−1}, by the invertible (u−v,u+v) change. There are (p−1)p^{j−1} sum coordinates with quotient exponent j for p≠3 and 2·3^j for p=3; multiplying these counts by the square of the lift factor yields the printed energy polynomials. Direct CRT on pair parameters proves all factorizations, and summing additive characters over both dual coordinates introduces q², exactly canceled in the formula. Bounded independent replay check_1.py checked 280221 targets across 13 moduli, comparing all, including zero fibers, by direct x at fixed s and independently counting reduced squares and product-zero pairs. Examples (modulus, support, energy): (3,3,27), (27,87,8019), (243,5703,1436859), (315,4875,3974211).

## originality

PASS

Qualified for the combined exact target census, support and unweighted energy over all odd moduli. The cubic collision identity, square-root arithmetic and prime-field specialization are not new; prior identities motivate but do not state or give the full prime-power fiber census and singular-prime moment.

## value

PASS

The fixed-sum singular strata change both support and energy, including dramatically in characteristic 3 and nonreduced rings. Knowing the exact fibers, not merely a moment estimate, answers every representation query and yields the complete normalized fourth moment uniformly across odd moduli. The unified prime-power and CRT formulas are independently useful in modular additive and restriction calculations even though the ingredients are elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
