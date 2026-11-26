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

The Euclidean parametrization counts each unordered primitive positive triangle once and gives J=mn(m−n)(m+n)/6. In the odd-m branch, F(m,n)−F(m,n′) for even n,n′ is (n−n′) times a unit at 2; this bijects even inputs with even outputs at all levels. The swapped parity branch has the same count. At 3 every nonzero residue pair gives F≡0, and its gradient reduces to (−n³,m³), so exactly three of nine lifts hit each prescribed next digit. The local counts at moduli 2^{a+1} and 3^{b+1} give 16Q pairs per target mod 6Q for Q=2^a3^b, including Q=1. In the sector of area πX/8, Möbius inversion uses only d coprime to 6. For each d, the parameter classes for the rescaled variables are the inverse-scaled preimages of the target classes (F is degree four), preserving the number of classes rather than fixing each class. The absolutely convergent factor is 9/π² and the summed boundary errors are O_Q(√X log(2X)), yielding X/(2πQ). At p≥5 the same primitive lattice argument makes nonzero pairs equally weighted; four lines contribute 4(p−1) of p²−1 pairs. Hence uniformity modulo any multiple of p is impossible. Independent enumeration agreed on all fibers for 14 smooth moduli through Q=72 and on the zero counts for p=5,7,11,13,17,19.

## originality

PASS

The supported distinct result is exact flatness of the normalized area on all dyadic and ternary depths and the consequent classification of all uniform fixed moduli in the full primitive triangle family. The normalized area, its factorization and the odd-prime zero-locus obstruction have substantial antecedents and are not independent grounds for novelty.

## value

PASS

Normalization by the compulsory area factor gives a natural statistic. The exact all-target local law distinguishes full equidistribution from mere support and explains why precisely the primes removed by normalization permit uniformity at every depth. It yields a complete modulus classification and fixed-modulus counts rather than a list of congruences at a few small levels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
