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

The geometric closure order is edge contraction of stable labelled trees. A two-edge tree has one four-valent component and all other components trivalent; its three trivalent refinements are precisely the three boundary points on its curve. The argument works in every characteristic; the objects are the geometric strata of the fibers, and over Z the corresponding relative strata. Independently constructed the maximal trees starting with the three-leaf tripod, inserting the next leaf on every edge (deletion and suppression inverts each step), and obtained the curve rows by dropping internal splits. This gives 105 trees and 105 distinct curves, each row and column of weight 3. An exact integer Smith calculation on this matrix gave 81 units, nine 2s and fifteen zeros. A separate replay of all 1,948 supplied operations on the independently generated matrix gave exactly the same diagonal with every off-diagonal entry zero. Transposition does not change the Smith factors.

## originality

PASS

The underlying 25-vertex, 105-edge, 105-triangle complex and its incidence are established. The distinct contribution is the integral Smith form of the unsigned edge–triangle inclusion matrix (or its transpose). The strongest identified primary account treats the same complex but not this unsigned Smith form; neither its simplicial homology nor the cited Chow results imply the rational rank and the exact elementary divisors together.

## value

PASS

This is a full integral invariant of the natural unsigned map taking each boundary curve to its complete three-point boundary. It quantifies the discrepancy between characteristic two and characteristic zero for the first moduli space having a two-dimensional split complex, and shows that the loss of saturation is exactly exponent two, with no odd or higher 2-power obstructions. Those are useful facts for solving integral incidence relations, and not consequences of merely knowing the incidence counts or oriented homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
