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

# Verification of the higher toric-hexagon weights

The package contains standalone `verify_hexagon_higher.py` and its actual output `verify_output.txt`. The exact integer Newton check enumerates all \(127\) nonempty subsets of the seven lattice exponents, computes translation-normalized convex hulls, tests the complete finite translation box, and verifies that only three primitive segment and two unimodular triangle shapes admit at least three residual monomials. Every segment case has a four-point unit-square residual and every triangle case has a three-point unit-triangle residual. These are exactly the cases needed for a common gcd of three or four independent sections.

For the field of five elements the checker forms the complete \(16\)-row, seven-column evaluation matrix. Every one of its \(8,008\) choices of six rows has rank at least five, and every one of its \(4,368\) choices of five rows has rank at least four. Modular Gaussian elimination is performed exactly, without floating-point computations. It also verifies the fiber-plus-one and fiber-only sharp constructions for fields of sizes five, seven, and eleven. The checker completed and printed `HEXAGON_HIGHER_WEIGHTS_VERIFIED`.

The infinite-family proof does **not** rest on finite-field sampling: it uses the exact Newton classification, the degree-six intersection bound when the linear system has no fixed curve, the Segre residual geometry when it has a fixed ruling fiber, and linear independence of any three distinct torus evaluation rows. The only separate finite characteristic check needed in the stated domain is \(q=5\); no impossibility claim is inferred from a timeout or partial enumeration. Independent audit is not performed.
