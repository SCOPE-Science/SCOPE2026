---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Tree edge root generators b_e are linearly independent by leaf elimination, making its centered zonotope a linear image of the (n−1)-cube. The intrinsic facet dual normals for the two chosen cuts are u_e=1_A−(a/n)1 and u_f=1_C−(c/n)1 with A,C disjoint outer components of T minus two edges. Their normalized inner product is −sqrt(ac/((a+b)(b+c))). Each edge pair produces four parallelotope ridges with outward signs split evenly, giving two acute arccos(q) and two obtuse pi−arccos(q), count 2(n−1)(n−2), mean pi/2, never right. Maximizing q²=(a/(n−a))(c/(n−c)) under positive a,b,c yields b=1 and balanced a,c, iff a degree-two balanced vertex; q>=1/(n−1) universally with star iff all maximizing pairs give a=c=1. Tested independent exact cut normal q for path and star trees at n=3,4,5,10, reproducing equality extrema, plus fully inspected exact finite checker. Infinite result follows from algebra/graph structure, not sampled trees.

## originality

PASS

Best-of-knowledge PASS for all ridges of canonical tree graphical zonotopes and both sharp extremal tree equality characterizations. A same-date cycle-zonotope theorem uses the very same cut-size cosine q but only obtuse cycle ridges; it neither implies supplementary four-ridge multiplicities for tree parallelotopes nor the star/balanced-degree-two tree classification. The dual-normal computation is classical and not alone asserted original.

## value

PASS

A canonical tree zonotope is combinatorially a cube regardless of tree, but its Euclidean ridge angles retain cut-size information. The four-ridge decomposition and exact sharp extremizers identify geometric structure invisible to the common face lattice, a natural complete metric classification rather than an arbitrary angle table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
