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

Reconstructed complete all-n proof directly from frozen RESULT.md: a fixed barycentric point has coefficients constant on complete vertex orbits; orbit barycenters produce a PL triangulation, not merely a fixed-vertex subcomplex. For 2<=k<=n-2, a weight-k admissible G orbit would be a clique in Johnson J(n,k) (pairwise k-1 intersection). The star/top dichotomy forces a nonempty proper common intersection of size >=k-1 or a nonempty proper union of size <=k+1<n, respectively, each G invariant; coordinate-transitivity prohibits either. Thus only singleton zero/all-one words and the full weight-one and co-weight-one orbits remain. At n>=4 only (z,E) and (u,Ebar) are compatible; n=3 yields bipartite K2,2=C4; n=2 yields a filled triangle because all Q2 distances <=2; n=1 is one edge. PL types and integral reduced H1(n=3)=Z or H0(n>=4)=Z follow, not only mod-2 Betti. An independent, newly written finite-state orbit enumerator (not imported verifier) directly checked 33 transitive actions for n=1..8, including n=4 regular V4 and n=8 regular elementary abelian 2^3 actions that contain no n-cycle. Exact exhaustive Johnson-clique checks for n=4..7, k=2..n-2 verified the structural dichotomy in those finite cases. All 8 frozen Git blobs were fetched and the Git tree reconstructed byte-exactly from their identities to expected source_tree_sha 2c90808587f5f99c264d0dab3404ba0e436d167b. Finite checks only corroborate analytical infinite proof.

## originality

PASS

Qualified original extension in the quantified group class. Complete original mathematical proofs for long k-cycles (2026-10-25 and 2026-11-01) imply the two-edge PL orbit model when k=n>=4 and explicitly give the n=3 cycle boundary; the all-scale S_n theorem (2026-11-08) also supplies the S_n homotopy and orbit model at radius two. These are substantial constituent prior coverage, not mere title overlap. However neither cyclic-group theorem covers every coordinate-transitive subgroup (e.g. regular V4<=S4 and elementary abelian C2^3<=S8 have no n-cycle), and the full S_n fixed-space theorem is about a single, larger subgroup: fixed spaces for arbitrary subgroups cannot be deduced from it. The new uniform elimination of ALL middle-weight orbits uses the Johnson star/top clique dichotomy plus invariant-coordinate-set argument to prove independence of G. No checked earlier source establishes that same all-transitive quantifier; PASS is best-of-knowledge with material incremental-priority risk, and not a claim that the component cases are first discovered.

## value

PASS

The geometric fixed-point PL type of a natural symmetric metric-family complex under an arbitrary transitive coordinate subgroup is a canonical equivariant-topology invariant, not a curated sample. The result gives a complete transitive-group-independent classification without requiring primitivity or a full cycle: two contractible components after a sharp circle-to-disconnected transition at n=4. It strengthens previously available cyclic-only and S_n-only classifications to groups such as regular V4 and elementary abelian regular groups with no long cycle. The new step is short and uses a classical Johnson clique theorem, so the mathematical advance is limited, but the universal structural subgroup statement is motivated and nontrivial, and it determines PL type rather than only ordinary ambient homology or group-specific homotopy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
