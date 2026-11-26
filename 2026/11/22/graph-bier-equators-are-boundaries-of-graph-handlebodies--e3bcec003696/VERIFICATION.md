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

In the (N−2)-dimensional Bier PL sphere, the full red subcomplex is the unfilled graph. Each mixed simplex intersects the half-height hyperplane in the affine product obtained by giving each color half the mass; these identifications agree on all common faces. To check the regular-neighborhood step, take a derived subdivision by coning each original face from an interior point, at height 1/2 for each mixed face. Its simplices represent nested nonempty faces. A chain cannot contain pure faces of both colors. A chain of all mixed faces extends by a nonempty pure-red subface of its smallest face, and likewise by a pure-blue subface. Thus the half-height superlevel is exactly the closed derived star of the derived full red subcomplex and the color level is its frontier, by the full-subcomplex PL regular-neighborhood theorem. The connected graph neighborhood has a ball per vertex and a 1-handle per edge. Amalgamating along a spanning tree leaves one ball and g=|E|−N+1 orientable 1-handles, since the ambient sphere is orientable. The boundary is the asserted connected sum, with a sphere at g=0; for N=5 this is the usual surface case. For K_(q+4) the dual is precisely the q-skeleton, and the cycle rank is binomial(q+3,2), for q≥1 only.

## originality

PASS

The evaluated PL frontier for every graph–dual pair, and in particular the complementary simplex-skeleton cases with p=1 and q≥3, are not supplied by the compared statements. Prior work already covers mixed-skeleton manifoldness, closed orientation, the genus-six surface, the free fundamental group for q≥2, and the q=2 TOP classification (which also determines its PL type by three-dimensional PL uniqueness). No distinct novelty is assigned to those consequences.

## value

PASS

This is a structural PL classification of an infinite family, including different noncomplete graphs with the same cycle rank. It explains that only the graph rank controls the frontier and settles the positive-q, p=1 instances in PL type, rather than only checking low case homology or computing another invariant of them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
