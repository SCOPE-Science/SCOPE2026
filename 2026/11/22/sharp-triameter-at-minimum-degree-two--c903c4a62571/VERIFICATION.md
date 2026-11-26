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

Reconstructed the canonical projection independently. Write d(ai,aj)=li+lj+e with e the perimeter parity and li nonnegative integers. For e=0, send the positive interiors d(v,ai)<li to levels li−d(v,ai) on arm i and everything else to the tree centre. The interiors are disjoint and cannot share an edge, and across their boundaries the level drops by at most one. For e=1 the closed balls of radii li are disjoint; map each to its arm by the same level formula and send unassigned vertices to a fixed triangle vertex. Any edge between balls or from a ball to unassigned vertices meets the affected ball at level zero. The arms are covered by geodesics to the feet and the odd triangle edges by the consecutive boundary points on each foot-to-foot geodesic. Hence this is a nonexpanding surjection to a model of size ceil(p/2)+1 with edge coverage. At p=2n−2 and, for n≥4, p=2n−3 the map is bijective and the model has a leaf. At p=2n−4 the model is a tree with n−2 edges and there is one doubled fibre z. For each leaf x, singleton fibres at x and its neighbour would force its preimage to have degree at most one, so z lies within distance one of every leaf. A path with ≥4 edges, or a tripod with three positive arms totalling ≥4, has two leaves at distance ≥3. This excludes p=2n−4 for n≥6. Two triangles joined by a path of length n−5 give perimeter 1+2(n−3)=2n−5 by taking two non-attachment vertices in one and one in the other. The small witnesses K3, C4 and K2,3 attain the stated 3,4,6; the n≥4 bijective exclusions give the matching small upper bounds.

## originality

PASS

The canonical projection and the lower-bound shape are not new in themselves. Hak–Kozerenko's Proposition 5.2 already attains 2n−5 by the barbell specialization for n≡0 mod 3, n≥6. It is a witness result, not the extremal upper bound. The distinct claim supported here is the sharp uniform maximum via the new one-double-fibre exclusion, including orders beyond the prior witness subsequence.

## value

PASS

The result settles the first nontrivial fixed-degree slice of an explicit earlier extremal question. It replaces a packing upper bound and a sparse family of lower witnesses with the exact maximum at every order. The method isolates a simple structural obstruction in the near-bijective regime; its value is the sharp upper bound, not novelty of the triangle barbell.

The dated certificate retains the supplied scientific assessment, sources and limitations.
