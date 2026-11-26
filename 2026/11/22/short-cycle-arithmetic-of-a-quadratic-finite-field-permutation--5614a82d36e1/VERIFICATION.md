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

In the coordinate u=x+β^(−1)y with β²=δ, the fiber map is multiplication by α_z=1+βz. Its norm cannot vanish because δ is nonsquare; the multipliers are all q distinct roots of X^q+X−2 since β^q=−β and the derivative is one. On z=0 all q² points are fixed, and elsewhere only u=0 is fixed. On nonzero points, every orbit of a multiplier has its multiplicative order. Counting trace roots with order dividing m subtracts the identity root exactly once; Möbius inversion and division by d give the displayed count for d>1. For an exact order d, p does not divide d, q²≡1 mod d, and q cannot be ±1 mod d: trace two would then force α=1, including in the reciprocal case. Independent /workspace/review_checks.py argument 4 verified the unit residues at d=2 to 15, all 12 integer resultants using determinants of multiplication in the cyclotomic quotient rather than the source's Sylvester matrix, and all four exact monic modular gcds, not just their degrees. The nontrivial residue entries isolate (d,p,r)=(8,3,3),(12,5,5),(15,19,4),(15,11,11); each p has order two modulo the corresponding d and gives the right residue for odd f. The cyclotomic polynomials are separable in these characteristics and their gcd roots are exactly two trace-line multipliers of primitive order d. Each contributes (q²−1)/d cycles. Finally, the sign of the fiber permutation is the quadratic character of the determinant (odd-order transvections and a diagonal scalar check); the product of determinants is 4 because each product of 1±βz over z is 1−β^(q−1)=2. This proves evenness for every odd q and shows independence from δ. The archived verifier was inspected, not executed.

## originality

PASS

Credit the explicit uniform initial resonance table and counts for the known map. The map, linear-fiber cycle mechanism and character parity method are not new constructions or general techniques. No separate source was found establishing the particular arithmetic classification; the highly relevant uninspected primary material remains an explicit access limitation.

## value

PASS

The window includes precisely the first three moduli whose unit groups admit a q involution other than ±1; it is not a list of arbitrary finite-field tests. The arithmetic resolves the first genuine period possibilities of an existing quadratic map, including four specific resonant characteristics, extension parity and multiplicities. The gcd formula covers higher periods algorithmically, not by a further uniform evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
