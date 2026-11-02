---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The standard Minkowski sum has M=2^n-1 and total coordinate sum M. The published proper-tube facet classification gives singleton offsets zero and a hub-containing k-tube offset 2^(k-1)-1. Intrinsic projected singleton normals have squared norm n/(n+1). Summing the n+1 singleton ball constraints yields r<=M/sqrt(n(n+1)) and equality forces c=M/(n+1) times the all-ones vector. For k>=2, the tube-normal squared norm is k(n+1-k)/(n+1), and F(j)=(2^(j-1)-1)/(j(j-1)) is nondecreasing because F(j+1)-F(j)=((j-3)2^(j-1)+2)/(j(j-1)(j+1))>=0. This yields normalized tube slack >=k(N-k)/(N-1)>=sqrt(k(N-k)/(N-1)), proving candidate ball feasible. Equality for a non-singleton requires n=2,k=2. The inspected actual Git tree SHA was independently rebuilt from all seven blob SHAs, and exact rational tube-distance checks n=2..80 confirm the equality pattern as corroboration only.

## originality

FAIL

The final statement is a direct mathematical consequence of the all-positive-integer density monotonicity lemma and full Euclidean inball calculation printed in the separately published complete-bipartite graph-associahedron result. Setting its density parameters to p=1,q=n gives the stellohedron inequality for n>=3. The exceptional n=2 tangency arises from its explicit equality step F(1,1)=F(1,2) and the elementary endpoint k(N-k)=N-1. The printed biclique theorem excludes stars, which is acknowledged, but its proof supplies the general lemma needed for this boundary case; coverage is by implication, not the restricted headline wording. Full comparison and same-day priority limitation are recorded.

## value

FAIL

The standard stellohedron and its intrinsic Euclidean inradius are intrinsically natural, and a uniform incenter with only singleton contacts is geometrically interpretable. But the full all-n radius and contact pattern is an immediate p=1 use of the published general density lemma, singleton upper-bound argument and one elementary low-dimensional equality check. No independently unknown metric invariant, structural obstruction, or new classification remains after this prior mathematical implication. Recomputing the precise formula and a tiny n=2 exception is not an independent research advance under the shared standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
