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

# Verification

The included `verify.py` builds every element of each stated finite ring and every invertible upper-triangular matrix. It directly multiplies matrices, constructs every conjugacy orbit by conjugating under every group element, and counts class sizes. Separately it enumerates all additive characters, computes the action of ring units and the associated orbit-stabilizer degree spectrum. Both observed histograms are compared with the six-row and three-row predictions after coincident rows are merged.

From within the directory containing `verify.py`, run `python3 verify.py`. The observed output concludes with `VERIFY_OK` after passing six full enumerations: split square-zero rings with \((q,d)=(2,1),(3,1),(2,2)\); \(\mathbb Z/4\mathbb Z\) and \(\mathbb Z/9\mathbb Z\); and \(\mathbb Z/4\mathbb Z[\epsilon]/(2\epsilon,\epsilon^2)\). The third and sixth have nonprincipal radical dimension two, one split and one mixed-characteristic. Distinct-group-order runs range from 16 to 324 elements. No additional package is needed.

The symbolic proof does not depend on a chosen coefficient-field section. The nonstandard fact needing care is the additive-dual stabilizer calculation: a unit stabilizing an additive character with nonzero restriction \(\beta\) to the radical must be \(1+w\), and stabilization holds exactly when \(\beta(w)=0\). The resulting stabilizer has order \(q^{d-1}\), giving the asserted irreducible degrees by the little-group correspondence.

Independently of enumeration, expansion of the algebraic formulas verifies (i) total class cardinality \(|G|=(q-1)^2q^{3d+1}\), (ii) equality of class and character counts, and (iii) sum of squared irreducible degrees \(|G|\), for every integer \(q>1\) and \(d\ge1\). Computational examples confirm small instances only and are not infinite proofs. Historical equivalence under alternate terminology has not been ruled out. No independent mathematical audit was performed.
