---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For A=[0 I;0 0], commuting B=[X Y;0 X], direct squaring gives X^2=0 and XY+YX=0; rank AB=rank X=s. With X a rank-s square-zero matrix, Y has unconstrained blocks D,P,Q,E,R and lower diagonal -D; the full rank of B is 2s+rank E. Counting image/kernel flags of X and rank-t E gives precisely the claimed Gaussian product. It holds all prime powers, including characteristic two. Independent integer comparison of normalized formulas in 196 parameter cases plus algebraic exponent identity confirms the key enumeration; finite checks are corroborative.

## originality

FAIL

A full prior October 26 result counts rank(AB),rank(B) for square-zero ANTICOMMUTING B with the same fixed maximal square-zero A. The rank fibers are exactly equinumerous: the block sign on the lower diagonal of B changes, but both upper-block linear spaces have identical free dimensions and the same rank formula. Exponent (r-s)^2+s^2-(r-2s)^2=2s(r-s), so the earlier formula literally equals the submitted commuting formula for every q,r,s,b. A still-earlier October 13 theorem covers the maximal-rank-B slice. No surviving independent rank theorem is distinguished.

## value

FAIL

The natural joint rank invariant is interesting but its entire distribution, all feasible strata, and extremal identities are already obtained by the elementary commuting/anticommuting block-sign transfer of a published exact census. Renaming the relation or presenting a second routine block calculation adds no substantive new mathematical information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
