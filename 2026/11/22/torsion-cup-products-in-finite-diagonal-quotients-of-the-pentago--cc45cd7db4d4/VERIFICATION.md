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

The diagonal circle acts freely since some coordinate lies on S¹ at every point; its finite subgroup preserves orientation. The standard 2-connectivity of X and the homotopy exact sequence imply π₁(B)=0, π₂(B)=Z and a primitive Euler class e for B=X/S¹. I independently checked the 32 induced subgraphs, giving Hochster groups of ranks 1,5,5,1 in degrees 0,3,4,7 with no torsion. By duality H²(B) and H⁴(B) are both Z. If e² were nonzero, the map H²(B)→H⁴(B) would be injective and Gysin would force H³(B) to be Z⁵, impossible for a unimodular alternating pairing in middle degree six. Hence e²=0, H³(B)=Z⁴, and Gysin in degrees five and six gives e:H⁴(B)→H⁶(B) an isomorphism. The finite quotient is the circle bundle with Euler class me: the transition functions are raised to the mth power. Its Gysin sequence now has the two nonzero integral maps given by multiplication by m. It gives degree 2 and 6 torsion Z/m, primitive pullback sublattices in degrees 3 and 4 with free rank-one cokernels, and the other stated groups. The universal cover gives the claimed π₁. Pulling back the base symplectic basis, the primitive degree-four generator and e gives all the claimed products by naturality, with the top class pulling back to a generator of H⁶. No division mod m is used, so composite m works as stated.

## originality

PASS

The strongest inspected prior coverage is Franz's general integral cohomology-ring construction, which applies to the finite subgroup. That supplies a method for the computation, not the evaluated groups or primitive hyperbolic product block. Getting these statements requires actual specialization and product analysis; the parity obstruction and integral Gysin argument provide that analysis. The inspected exact polygon comparisons have materially different actions or compute different invariants.

## value

PASS

The diagonal action is a canonical free scalar action on this seven-manifold. This case gives a rank-four primitive block, exhibiting a product of free classes that generates the full order-m torsion for arbitrary m, a feature invisible to the rational ring or additive integral groups. The useful structural calculation is that middle-degree parity forces the square of the Euler class to vanish, enabling the explicit pairing and mixed product.

The dated certificate retains the supplied scientific assessment, sources and limitations.
