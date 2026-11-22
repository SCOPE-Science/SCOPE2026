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

The twelve cube edges were independently reconstructed by one-bit XOR. A separate vertex-based maximum-matching DP on all 4096 edge masks gives face counts 45, 601, 2665 including the empty face for k=2,3,4. Independently implementing the supplied pivot permutations and all oriented nonempty Hasse covers yields respectively 19/295/1331 matched pairs, 72/2184/13884 cover arrows and complete DAG topological sorting. Removing the augmented empty-face pair leaves exactly (critical d0:1,d1:5), (d0:1,d3:9), (d0:1,d5:1). Each is a legitimate finite acyclic discrete-Morse matching, hence an integral CW model with just one vertex and a single higher-cell dimension, forcing the claimed wedges; mod-2 ranks in the source file provide corroboration but not the integral proof. At k=1 there are only the empty face; a cube perfect matching has size four, so all k>=5 give an 11-simplex. Since positive homology appears only in successive degrees 1,3,5 and transitions are by inclusion, each stage class dies at the next threshold, yielding exactly five [2,3), nine [3,4) and one [4,5) positive-degree integral bars. The result is exact only for Q3; no extrapolation to higher cubes.

## originality

PASS

The complete-bipartite homotopy formula gives K4,4 ranks (9,9,1), while Q3 is K4,4 minus a perfect matching and has first rank 5. Holmsen–Lee proves vanishing bounds for arbitrary bipartite G, and Shan–Lu–Wang prove top-field injectivity and cycle nonvanishing; these do not imply the full cube homotopy classification or exact k=3 rank. A familiar nerve lemma already gives the k=2 stage, and the k=4 top FIELD rank follows from an 8-cycle and injection into K4,4; those partial implications are explicitly credited. The outstanding precise Q3 k=3 integral wedge, k=4 integral homotopy and complete filtration have not been located in the primary results or published record comparisons. This is best-of-knowledge originality with unindexed equivalence risk, not proof of priority.

## value

PASS

The cube is a canonical three-dimensional hypercube and four-crown, naturally just one perfect-matching deletion from the complete bipartite graph where full nonmatching topology is known. The complete threshold-by-threshold INTEGRAL homotopy classification is a natural exact invariant of this particular graph complex, not an arbitrary hand-picked computation. Its nine three-spheres and verified higher-stage sphere distinction, combined with the changed first multiplicity and complete persistence bar pattern, provide a reproducible benchmark for graph-complex topology; a researcher comparing sparse bipartite graphs to the complete case could need this precise answer. The elementary first stage and field-level top rank are prior/standard, so no novelty or value is claimed for those isolated facts, nor for a general family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
