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

The proof establishes the exact complex rank and right kernel, not just a lower bound on the defect. With m=p−1, take d to be the specified nonzero representative of −k−1 modulo m. The product phase is f(u)=u(1+u^k), so a right character vector maps to the inverse character times its scalar phase sum. Here k is even, k≡1 mod 3, and gcd(k,m)=m/3. The index-three subgroup H=ker(u↦u^k) contains −1 and 2; 3 does not divide |H|. On the three cosets H, ωH, ω²H the multipliers of f are respectively 2, −ω² and −ω. Each is a bijection from its coset onto H, giving exactly {h/2,−ωh,−ω²h} over each h. Factoring these fibers gives the stated bracket and the common period. The period cannot vanish: adjoining ζ_p to Q(ζ_m) gives Q(ζ_pm), of relative degree p−1 by coprimality; its only possible degree-at-most-p−1 polynomial relation is a multiple of Φ_p, but the period polynomial has zero constant term and nonzero coefficients on H. Thus the bracket vanishes exactly for χ(−2)=1 and χ(ω)≠1. Subtracting the annihilator of ⟨−2,ω⟩, of size m/(3t), from that of ⟨−2⟩, of size m/t, proves the count. This also justifies subtracting exactly that many dimensions from m: character inversion permutes a basis.

## originality

PASS

Credit the exact cubic-resonant character kernel and order-dependent count, not character diagonalization, cyclotomic disjointness, or the use of phase fibers. The strongest compared indexed rank theorem has inverse-hyperbola degree d=1 and at most one missing quadratic character in its nondegenerate case; its phase and scope do not give the three-coset result. The compared literature on binomial permutation criteria, distribution of related character sums and prime cyclic Fourier minors does not give this ambient two-dimensional compression's complete character kernel. This is a bounded statement-level priority assessment.

## value

PASS

Square sampling on a single algebraic curve need not permit recovery even at equal numbers of sites and samples. The index-three resonance is motivated by all the phase cosets mapping onto one subgroup, rather than by selecting examples with numerical rank drops. The result quantifies how much information is lost, using an order rather than only the image size, and identifies every unrecoverable character. This is an exact structural invariant for the full stated family; it distinguishes higher-dimensional loss from the inverse-hyperbola obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
