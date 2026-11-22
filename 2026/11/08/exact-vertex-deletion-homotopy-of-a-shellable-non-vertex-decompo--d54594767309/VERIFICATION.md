---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For G=C16(1,4,8) on Z/16Z, checked every one of 2^16 vertex subsets and reconstructed the exact face vectors K=(1,16,80,144,80), D=(1,15,70,117,60), L=(1,10,27,20,0). An independent Python matching implementation found for D 129 nonempty matched pairs, critical cells (one 0, two 2, one 3), all 731 directed nonempty cover relations acyclic, and exact signed Morse boundary (-1,0)^T. Hence D≃S² by integral CW cancellation. For L: 26 matched pairs, one 0, one 1, three 2, 114 acyclic directed covers, signed Morse boundary (1,0,1), giving L≃S²∨S². Existing Earl et al. full-complex shelling and computed Euler characteristic imply K≃S³; Mayer–Vietoris for K=D∪(v*L) gives a split primitive surjection H2(L)=Z²→H2(D)=Z. The rotations cover all 16 vertices. Verified the earlier primitive top cycle: 80 tetrahedra, 64 unit and 16 double coefficients, with 16 unit and 4 double tetrahedra incident at each vertex. No leap from mod-two ranks to integral homotopy was made.

## originality

PASS

Qualified historical-priority PASS. The original assigned source was publicly committed 2026-11-08 at 17:29:40 UTC. Earlier 2015/2023 primary papers established shellability, deletion face/h vectors and non-Cohen–Macaulayness, not D≃S² or its primitive link map. The published October 25 local-homology theorem already implies L≃S²∨S² and that portion receives priority credit. Importantly, the now-published Resultary primitive-top-cycle and nonorientable-core theorems, when combined with the local-homology theorem, DO mathematically imply the entire audited finding via the primitive coefficient and Mayer–Vietoris/van Kampen/Whitehead. However their public Git commits were 2026-11-08 at 20:01:35 UTC, after the audited public source at 17:29:40 UTC, and cannot retroactively be counted as earlier published priority. An unindexed prior theorem remains possible; this is not novelty proof by negative search.

## value

PASS

The exact vertex deletion of the canonical minimal shellable but nonvertexdecomposable circulant is a natural local-topology test, not an arbitrary small slice. Its integral S² homotopy type and primitive Z²→Z map explain more than the known non-Cohen–Macaulay h-vector: one vertex-link generator survives deletion and one accounts for the ambient 3-sphere attaching class. At original public priority it was an independently motivated exact topological invariant beyond the earlier partial local-link classification. It is finite but complete and mathematically meaningful; it does not pretend to classify other circulants or offer new novelty over later overlapping top-cycle findings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
