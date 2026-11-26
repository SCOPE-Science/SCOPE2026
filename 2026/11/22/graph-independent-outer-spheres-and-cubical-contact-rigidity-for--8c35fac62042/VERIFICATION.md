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

The support is the sum of the norms of the projections of the unit normal onto the edge planes. In squared coordinates, for fixed hub square a and mean rim square b, Jensen on the spokes gives n sqrt(a+b), with equality only at a flat rim; Jensen on the rim uses the degree sum dnb and gives (nd/2)sqrt(2b). Both bounds attain equality simultaneously at flat rims whether or not H is connected. Putting t=sqrt((n-1)b), Cauchy–Schwarz gives the unique optimum t=c/sqrt(1+c^2) with c=d/sqrt(2(n-1)). It lies in the interior because 0<d^2<2(n-1)^2. Thus precisely the independent sign choices of (sqrt(a_*),sqrt(b_*),...,sqrt(b_*)) maximize support. Every maximizing unit u exposes the point R u by the equality case in u·z<=||z||<=R, and every norm-maximizing point supplies such a normal. Multiplying the squared rim and hub entries by R^2 yields n^2 d^2/[2(n-1)^2] and n^2(1-d^2/[2(n-1)^2]) respectively, proving the exact constellation without residual faces or arcs. Any enclosing ball must contain an antipodal contact pair, which attains the radius lower bound only with center zero. Equality in the diameter bound identifies exactly the antipodal contact pairs. For arbitrary H and under the stated positive flat-rim and nonzero-hub condition, varying one rim square up and another down at fixed hub gives equality of rim derivatives, namely 1/(2 sqrt(a+b))+deg_H(i)/(2 sqrt(2b)); therefore H must be regular.

## originality

PASS

The support function and norm maximization are standard, and prior catalogue results substantially overlap in question and method. The supported distinct result is the exact graph-independent circumsphere, every coordinate contact and the flat-rim degree converse for all regular rims in the stated nonregular cone family. None of the compared whole-graph regular, bipartite or weighted split results gives that conclusion under these assumptions.

## value

PASS

The full coordinate-level contact constellation, not just its radius or abstract isometry type, can fail to distinguish regular rims with different edges, even when the rim may be disconnected. This is a meaningful boundary on what outer Euclidean geometry encodes for nonregular graphical discotopes. The converse recovers exactly the degree condition from the positive flat-rim maximizing pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
