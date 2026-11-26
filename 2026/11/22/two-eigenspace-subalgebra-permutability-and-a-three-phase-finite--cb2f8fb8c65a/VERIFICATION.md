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

The re-audited census partitions subalgebras into all subspaces of V and cosets over split invariant intersections. Mixed closure tests the projected inside subspace for invariance; outside closure tests the quotient coset difference for lying in either eigenspace. Graph-lift and intersection factors give all ordered counts. For fixed a,b Gaussian degrees make the inside population dominate except (2,2) and (2,3)/(3,2). At those exceptions the generic allowed type counts are respectively 1+2+7 out of 25 and 4+2+1 out of 16, with nongeneric intersections lower order. The corrected swap argument uses [x,y]_D+[x,y]_(I−D)=αy−βx, for x=αh+v and y=βh+w; both brackets belong to any subspace containing x,y together or neither does. Zero and one remain distinct in characteristic two. Independently enumerating ambient subspaces by extensions and testing closure directly gave (T,P)=(188,29140),(696,337248),(935,677413) for (a,b,q)=(2,2,2),(2,2,3),(2,3,2), and the separate coordinate-class expansion agreed with the special-case polynomials.

## originality

PASS

The checked finding is the normalized action with both eigenspaces of dimension at least two. The exact catalogue hit is the audited record itself. The best distinct prior comparisons cover rank one, total dimension three, scalar or nilpotent Jordan actions, and general invariance under scalar shifts. These do not cover the exact ordered census or the higher-rank exception classification. The proof correction does not claim the swap or scalar-shift observation as new.

## value

PASS

This is an exact census for a natural next family beyond rank-one and scalar adjoint actions. It explains which higher-rank multiplicities still balance abelian-ideal subalgebras against exterior ones, and separates the two such probability limits from the full-probability range. The ordered pair formula also gives finite-field values before any asymptotic approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
