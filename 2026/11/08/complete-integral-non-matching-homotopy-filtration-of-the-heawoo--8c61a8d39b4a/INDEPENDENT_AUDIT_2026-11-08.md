# Independent mathematical audit

## correctness

PASS

The 21 Fano incidence flags form edges of the Heawood graph, and NM_k consists of masks with maximum matching size < k. The exact k-matching recurrence and independent subset maximum transform enumerate all 2^21 edge masks. Frozen verify_nonmatching_heawood.cpp implements two global acyclic toggle matchings with Hasse directed topological sorts and signed Morse boundary elimination. Critical cells at k2,3,4,7 directly give 8 S1, 36 S3, 92 S5 and S11; k5 has a unit 8-to-7 attachment leaving 113 S7; k6 has a determinant −1 5×5 boundary minor (also independent 6×6 minor in opposite pivot order), leaving 36 S9. Their primitive attaching maps cancel cells integrally by Hurewicz. Independently re-enumerating all 2,097,152 masks reproduced face counts (77,2331,33971,254240,963641,1844248) and alternating reduced Euler values (−8,−36,−92,−113,−36,−1). Full exact integer Hasse checks were inspected in code but not recompilation-rerun. k1 void and k≥8 simplex follow from matching sizes 0 and at most 7.

## originality

PASS

The original non-matching complex of Heawood/Fano incidence graph is a sparse proper subgraph of K_7,7. Linusson–Shareshian–Welker arXiv:math/0410345 Theorem 1.4 computes complete bipartite graphs, not every subgraph, and its ranks (e.g. k2=36 for K_7,7) differ from Heawood k2=8. Holmsen–Lee arXiv:2003.11270 Theorem 1.1 proves high-degree homology vanishing for bipartite graph nonmatching complexes but neither exact ranks nor sphere-wedge homotopy. Previously published Heawood matching, two-matching, ordinary-cut complexes impose different face conditions. Searches under Heawood/Fano/Levi/NM_k did not find prior full exact six-stage homotopy; best-of-knowledge novelty, with indexing risk.

## value

PASS

The Heawood incidence graph is canonical, sparse and highly symmetric; the full family of six natural matching-number thresholds supplies integral homotopy ranks and proves sharpness of the general bipartite vanishing bound at every nontrivial level. This is an independently useful complete classification, not a toy edge case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
