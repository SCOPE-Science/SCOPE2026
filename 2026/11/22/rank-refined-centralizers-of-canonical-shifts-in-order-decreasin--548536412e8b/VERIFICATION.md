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

Distances to the two extreme domain points force every other image point between the two endpoint images, hence the map is x-d or c-x as stated; rank one has a unique offset and rank zero is counted once. For x-d both compositions have the same x-d-k output wherever defined; in the only possible input range x>=d+k+1 their domain tests are x in D and x-k in D. Equality forces complete residue chains, so independently selecting them gives the product. For c-x any common domain input gives values differing by 2k, so equality requires both domains empty. This is equivalent to D in the top k positions and its image in the bottom k positions. Positive images and order decrease then give q+1<=c<=p+min(k,p); every interior point is independently optional. This proves the endpoint sum even when n<2k-1. When n>=2k-1 a gap w allows k-w choices of p and k-w centers, giving the square. The stable reversing sum at z=1 satisfies S(k+1)=2S(k)+k^2, S(1)=0, confirming the closed count. At k=1 there are no reversals and the one full chain for each offset gives the powers, including the empty map and identity.

## originality

PASS

Pass for the exact order-decreasing, isometric all-power centralizer spectrum, including ambient-dependent reversals and their stable range. The unrestricted nilpotent centralizer, the monoids/generators and the k=1 single-chain case are not new.

## value

PASS

This exact invariant addresses centralizers of every nonzero power of the canonical nilpotent generator in both natural metric monoids. It separates translation-chain freedom from reversed maps permitted only by annihilation, gives a genuine stable regime for the latter and still covers the nonstable range. The filtered counts cannot be read from the unrestricted centralizer rank spectrum. Value is the complete enumeration and classification, not the familiar k=1 count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
