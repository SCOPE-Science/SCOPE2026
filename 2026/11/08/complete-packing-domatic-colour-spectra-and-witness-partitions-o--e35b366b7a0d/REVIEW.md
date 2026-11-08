# Review of the packing–domatic multipartite classification

**Correctness — PASS.** In a connected complete multipartite graph, colour \(1\) occurs within at most one part, and every higher colour is a singleton whose broadcast radius covers the graph. This yields the complete obstruction to creating a block without higher colours. The stated Stirling partition factors, falling-factorial injection counts, exact minimum palette, and equality cases follow directly. A separate exhaustive graph-distance/partition checker covers 116 graph/palette instances, 67,470 admissible colourings and 96 graph/target optimum cases. The infinite proof is the structural argument, not finite extrapolation.

**Originality — PASS, qualified.** Brešar–Ferme–Hu [1] introduced packing \(k\)-domatic colouring and establish general \(k=3\) and selected path/cycle cases. These scalar portions are not claimed as new. The full multipartite capacity distribution, Stirling witness-partition counts, all-\(k\) chromatic spectrum and exact optimal-colouring multiplicities are mathematically stronger information than that stated baseline. Related packing-total criticality, limited subset packing, and list/correspondence colouring results concern different invariants. The full 26-page originating manuscript was inaccessible; priority remains provisional and its unadvertised special cases are a residual risk.

**Mathematical value — PASS.** The theorem gives the whole infinite multipartite family in one closed normalisation, for all palette and target partition sizes. In particular, whether a part of an exact prescribed size exists determines one-unit versus two-unit jumps in the chromatic spectrum. The partition-witness enumerator records meaningful multiplicity beyond the existence threshold, relevant to robustness under random broadcast-colouring assignments.

**Scientific limits.** These statements are for ordinary packing colours on finite connected complete multipartite graphs. Counting uses named vertex/colour labels and unordered witnessing partitions; no other distance-sequence generalisation or independent mathematical audit is asserted.

Self-review: passed. Independent audit: not yet performed.

## References

1. B. Brešar, J. Ferme, W. Hu, *Partitioning an \(S\)-packing coloring into broadcast dominating sets*, arXiv:2610.03477 (2026).
2. J. Ferme et al., *On \(S\)-packing total colorings*, arXiv:2609.10107 (2026).
3. S. Cambie, R. Hämäläinen, *Packing colourings in complete bipartite graphs and the inverse problem for correspondence packing*, arXiv:2303.01944 (2023).
