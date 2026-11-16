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

# Verification of the stated determinant and design theorem

The standard-library Python 3 checker in `CHECK.py` compares the closed determinant with independently assembled Cauchy and contrast Gram matrices over several exact rational scale grids, and exhaustively checks spanning trees up to six vertices. It also tests exact rational expressions for the proposed collision constants. All these finite tests pass, but only the incidence/Cauchy proof, strict derivative-cut argument, and controlled finite-product expansion establish the theorem for arbitrary positive distinct scales and every fixed finite rank.

The main normalization is the actual \(L^2((0,\infty),dt)\) energy of each unshifted causal difference: \(W(a,b)=(b-a)^2/(2ab(a+b))\). The determinant is a volume criterion, not the smallest Gram eigenvalue; no independent scientific audit has occurred.
