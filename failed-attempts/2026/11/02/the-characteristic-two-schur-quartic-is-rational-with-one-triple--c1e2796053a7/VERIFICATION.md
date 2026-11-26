---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The transformed equation zC+N, with C=v³+w³ and N=t(t³+w³), is primitive and linear in z because the forms have no common factor. The equations f_z=f_t=f_v=f_w=0, together with the surface equation, force w=v=t=0; the unique point is P. The cubic initial form in z=1 gives multiplicity three, and the defining equation and partial derivatives in the completed local ring generate (t⁴,v²,w²), since 1+t is a unit. The quotient has length 16. The hypersurface is S2 and regular in codimension one. Projection identifies the open set C≠0 with an open subset of P², and the directions C=N=0 are exactly those with w=1, v³=1 and t=0 or t³=1. This gives twelve geometric lines, two over F₂. Over F_q the rational locus of C=0 has 1+rq points (non-rational components can only contribute their common vertex). The r(r+1) rational base directions give q points each away from P, all other C=0 directions give none, and every C≠0 direction gives exactly one. This proves q²+q+1+r²q and hence the stated singular-surface zeta function. The frozen verifier and recorded output were inspected, not executed; the printed local-algebra statements are not independent computational checks. The proof covers every extension without relying on them.

## originality

FAIL

A distinct earlier Resultary record proves the same literal special fiber's geometry, including the Tjurina length and concurrent lines, and gives an explicit stronger resolution over the base field. Its described fibers and Frobenius action imply the point counts and zeta function with no additional geometric calculation; absence of those formulas in its statement is not a surviving originality claim.

## value

FAIL

The degeneration of this classical quartic is a meaningful object, but its geometric description here duplicates a stronger resolution result. The proposed arithmetic remainder is a direct count of the already-described finite centers and contracted lines. There is no independently valuable surviving claim in this package under the standard for a narrow exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
