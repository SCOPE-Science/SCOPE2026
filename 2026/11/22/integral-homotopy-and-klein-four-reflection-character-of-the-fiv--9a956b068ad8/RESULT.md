# Reflection character of the five-robust clique complex of the four-by-five grid

## Finding

Let \(G=P_4\square P_5\) and \(K=\{S\subseteq V(G):\alpha(G[S])<5\}\). Write \(\rho_r\) and \(\rho_c\) for reversal of rows and columns, respectively. With entries ordered by \(1,\rho_r,\rho_c,\rho_r\rho_c\), the character of their action on \(\widetilde H_7(K;\mathbb Q)\) is
\[
(489,31,13,15).
\]
The simultaneous eigenspaces of signs \((+,+),(+,-),(-,+),(-,-)\) have dimensions \(137,123,114,115\), respectively. In particular the ordinary geometric quotients by the row, column, and half-turn involutions have rational seventh Betti ranks \(260,251,252\), and the quotient by the full reflection group has rank \(137\). The result identifies a rational homology representation, not an integral lattice or an equivariant wedge equivalence.

## Proof

**The support of homology.** The Alexander dual \(\Delta=K^*\) is the total five-cut complex: its facets are exactly the complements of independent five-subsets of the 20 grid vertices. Bayer et al., [*Total Cut Complexes of Graphs*](https://arxiv.org/pdf/2209.13503), §5, Table 3, give \(\beta_{10}(\Delta)=489\) and specify successive lexicographic element matchings as their computational method. For clarity, the companion `check_grid_reflections.py` reproduces the matching by including the empty face and successively toggling each vertex in row-major order wherever both faces are unmatched. Exact enumeration gives 976,007 faces including the empty face and 489 unpaired faces all of cardinality 11. The empty face is matched to a vertex; omitting that pair gives one critical vertex in the nonempty face poset. Theorem 7.5 of Bayer et al. gives acyclicity of this element matching; Theorem 7.2 gives the resulting wedge of 489 ten-spheres for \(\Delta\). Thus integral combinatorial Alexander duality gives \(\widetilde H_i(K;\mathbb Z)\cong\widetilde H^{20-i-3}(\Delta;\mathbb Z)\), supported in degree seven, free of rank 489. In fact \(K\) is simply connected since it contains the full three-skeleton. Hurewicz and the homology version of Whitehead's theorem give the ordinary wedge of 489 seven-spheres. The size and homotopy type are background here: the rank is tabulated and the homotopy conclusion is a consequence of the published matching procedure and the duality argument. No originality is claimed for them.

**Reflection traces.** Use vertex labels \(5r+c\) for \(0\le r<4\), \(0\le c<5\), with adjacency given by Manhattan distance one. Each reflection and their product permute these labels and preserve \(K\). A fixed nonempty simplex is a union of vertex orbits of the symmetry. If it uses \(b\) orbits and has cardinality \(a\), the sign of the permutation on its orientation is \((-1)^{a-b}\). Its contribution in simplicial degree \(a-1\) to the Lefschetz sum is therefore \((-1)^{b-1}\). There are exactly 1,998 independent five-sets, found by testing every five-subset against grid adjacency. All complements of sets containing an independent five-set are marked as dual faces, by downward closure from the complemented five-sets. Enumerating all nonempty unions of the vertex orbits of each symmetry and keeping those with unmarked complement gives these exact sums:

| Symmetry | Fixed nonempty simplices | Lefschetz number |
|---|---:|---:|
| Identity | 72,568 | −488 |
| Row reflection | 252 | −30 |
| Column reflection | 444 | −12 |
| Product | 212 | −14 |

Since the action on \(H_0\) is trivial and the only positive-degree homology is in odd degree seven, the desired traces are one minus these Lefschetz numbers. The four character multiplicities are the inner products with the four sign characters, namely \((489+31\epsilon_r+13\epsilon_c+15\epsilon_r\epsilon_c)/4\). For a finite group acting simplicially, barycentric subdivision gives a quotient chain complex identified with the chain coinvariants. Over \(\mathbb Q\) coinvariants are exact and identified by averaging with invariants. This yields the claimed quotient ranks by taking the invariant subspace under each subgroup.

## Scope and comparison

The claim is only for the indicated graph, independence threshold, and rational reflection action. Filakovský, [*The Topology of k-Robust Clique Complexes in Grid-like Graphs*](https://arxiv.org/html/2602.11365), Theorems 1–2 and Corollary 3, does not treat this higher-threshold rectangular case in its proved families; Conjecture 5 predicts the wedge shape, not the action. Bayer et al., §5 and Appendix §7, give the cited dual rank and matching framework, not the four reflection traces. Chandrakar et al., [arXiv:2408.07646v3](https://arxiv.org/html/2408.07646v3), Theorem 1.1, treat other grid dimensions or cut thresholds. Nearby finite classifications for the four-robust version of this grid and the five-robust four-by-four grid concern different complexes. The distinction is an exact invariant of the existing symmetry, not a claim to a new Betti number or to the priority of the ordinary wedge computation.
