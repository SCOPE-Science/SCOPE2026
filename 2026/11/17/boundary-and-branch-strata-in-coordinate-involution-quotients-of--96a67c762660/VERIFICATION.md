---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For M_n=(D^1,S^0)^{C_n} with C_3=boundary triangle, cells count V=2^n, E=n2^{n-1}, squares=n2^{n-2}; every vertex link is C_n, making a closed connected orientable surface of chi=(4-n)2^{n-2}. Coordinate sign flip on S has fixed points iff every flipped coordinate can be interior simultaneously, i.e. S is a vertex (2^{n-3} fixed circles) or an adjacent pair (2^{n-2} isolated fixed points); all other actions free. Its orientation degree is (-1)^|S|, and local fixed-point actions are respectively a boundary reflection and orientation-preserving half-turn branch. The formula chi(quotient)=(chi(M)+chi(Fix))/2, connectedness of quotients, and the compact surface classification give the four stated genus/crosscap formulas and equal nonfree genus. Direct integer Euler/genus identities verified for n=3..12. The inspected sign-equivariant subdivision program enumerates all 243 nontrivial sign involutions n=3..7; this finite check supplements rather than proves the general cell/fixed-locus argument. Boundary examples n=3 give disk/S2/RP2 and n=4 give annulus/S2/T2/Klein bottle.

## originality

PASS

PASS best-of-knowledge with material risk. Ambient real moment-angle polygon genus and free sign quotients follow established vector-colouring formulas and are explicitly not claimed new. Published Erokhovets 2024 general non-free subgroup quotient manifold criteria do not in the relevant inspected mathematical statements provide the complete four-case, nonfree explicit boundary-circle/isolated branch-point homeomorphism types and equality of genus. A very plausible Liu 2015 paper specifically entitled partial quotients of moment-angle manifolds over a polygon remained inaccessible in full (arXiv/OA search failed; authorized institutional download returned VPN disconnected), so overlap cannot be excluded. Its available abstract suggests a different higher-dimensional toric/partial quotient setting, not a decisive mathematical implication to the present 2D coordinate involution classification. Inaccessibility alone does not defeat best-of-knowledge originality; retain as a high-priority residual risk.

## value

PASS

PASS: an all-n and all-nontrivial-coordinate-involutions complete topological homeomorphism classification, especially the nonfree fixed-circle versus isolated branch loci, is a natural structural question in moment-angle and equivariant topology. The identical genus formula for distinct branch types is mathematically explanatory, while boundary and branch counts distinguish them. It is not merely Euler-characteristic arithmetic on an arbitrarily selected small case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
