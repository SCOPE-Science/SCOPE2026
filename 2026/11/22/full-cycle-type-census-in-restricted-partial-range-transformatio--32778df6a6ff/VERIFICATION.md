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

The objects are total maps on X, restricted only by f(Y) being contained in Z. Once a path enters Y it enters Z and never leaves, so cycles are wholly in Z or wholly outside Y. For specified cyclic vertices and permutations, delete their outgoing cycle edges. The noncyclic vertices in Z form a forest rooted at the a cyclic Z vertices and vertices in Y outside Z have k independent target choices each. Outside Y the forest roots are the m vertices of Y together with the b designated cyclic vertices outside Y, since no path can return to the exterior after entering Y. The rooted complete-graph forest minor is NI-J on the nonroots, giving r N^(N-r-1), with the empty minor equal to 1. These choices are independent and recover the map uniquely. Choosing the root sets and the two permutations yields (1); partition summation yields (2). Normalizing the product gives independence and the two probabilities, including the all-root case w=0. The stable image supports a permutation, so eventual period is the lcm, with divisor Möbius inversion valid. Bidegrees recover k and w; for fixed k,w the coefficient sum k^m(m+w)^w is strictly increasing in m except for the stated singleton family.

## originality

PASS

The supported distinction is explicit joint arbitrary cycle-type enumeration and the resulting independent stable-rank factors for this nested restricted partial range. The one-zone rooted-forest calculation and the permutation/lcm identification are prior mechanisms; total cardinality and generating rank are already known. Inspected related theorems and indexed records do not imply the two-zone result without the new separation at Y.

## value

PASS

The periodic part is the canonical eventual action of each transformation. Resolving the two cycle profiles goes beyond an unrestricted rooted-forest exercise: it gives the full distribution of stable-image sizes and exact periods under a natural semigroup restriction, makes the two rank counts independent despite exterior attachments into Y, and retains enough information to distinguish cardinality triples with precisely one exception family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
