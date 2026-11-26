---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independently enumerated all 32767 nonzero forms under all 168 invertible binary matrices, rather than using the supplied orbit generators. For each representative, tested the quartic and its three partials for a common zero on each of three affine charts using SymPy Gröbner bases over F2 and the weak Nullstellensatz. Including the equation itself is essential in characteristic two. Geometric smoothness is invariant under the action; in particular a smooth quartic cannot contain a line component by Bézout together with smoothness. For each smooth equation, computed tangent restrictions F(P+tQ) by binomial coefficient parity, with Q a distinct rational vector on the tangent. The initial nonzero degree is the local contact order and is unchanged by a change of tangent parameter. All eleven rows agree exactly; totals are 78 classes and 10920 equations. Mask 4418 lies in the sole (4,0) orbit of size 168 and gives the displayed polynomial. Its tangent lines at the three coordinate points and [1:1:1] have cubic leading contact terms, as claimed. Canonical embeddings identify projective equivalence with isomorphism here.

## originality

PASS

Credit the 78-class total and complete normal forms to Nart and Ritzenthaler and the three-hyperflex orbit to the earlier indexed Resultary result. The supported distinct finding is the eleven-stratum split by rational ordinary-flex and hyperflex counts, including the unique four-ordinary-flex orbit. The strongest inspected classification table enumerates by Newton polygon and does not calculate this tangency invariant. Its catalogue of curves allows a further exact computation, but neither that table nor the compared theta-contact descriptions mechanically supply the two contact counts.

## value

PASS

The smallest finite field is a natural test for arithmetic inflection in characteristic two. Separating rational third- and fourth-order contacts rather than merely tallying curves or inflection lines gives a usable distribution by equation and by class, and resolves a sharp extremum with an explicit unique projective witness. The known class total is a cross-check, not the new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
