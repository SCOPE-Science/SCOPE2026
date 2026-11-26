# The seven-cycle quotient of the seven-point matching complex

## Finding

Let \(\mathcal M_7=\mathcal M(K_7)\) be the simplicial matching complex of the complete graph on \(\mathbb Z/7\mathbb Z\): vertices are unordered pairs of distinct labels and simplices are collections of pairwise disjoint pairs. Let \(C_7=\langle\rho\rangle\) act through the simultaneous translation \(\rho\{i,j\}=\{i+1,j+1\}\). Then the **ordinary geometric orbit space** has homotopy type

\[
|\mathcal M_7|/C_7\simeq M(\mathbb Z/21\mathbb Z,1)\vee S^2\vee S^2.
\]

Here \(M(\mathbb Z/21\mathbb Z,1)\) is the two-dimensional Moore complex obtained by attaching a two-cell to a circle with attaching degree 21. In particular, the quotient has \(\pi_1\cong H_1(-;\mathbb Z)\cong\mathbb Z/21\mathbb Z\), \(H_2(-;\mathbb Z)\cong\mathbb Z^2\), and no other positive-degree integral homology.

## Assumptions and scope

The action is the specifically stated seven-cycle on all seven graph vertices. It acts on the *whole* ordinary matching complex, not just maximum matchings, and the quotient is the geometric orbit space, not the abstract complex obtained by identifying vertices nor an arbitrary symmetric-group quotient. No rationalization or localization is used. The conclusion is for this single, canonical seven-point case; it is not a statement for arbitrary odd complete graphs.

## Proof

**1. A free cellular orbit complex.** The matchings of cardinality one, two and three number, respectively, \(21,105,105\). Translation by a nonzero element of \(\mathbb Z/7\mathbb Z\) has order seven on the graph-edge set: no unordered graph edge is invariant under a nontrivial translation (the orbit length divides seven, and a fixed edge would force its two endpoints to form a two-element invariant subset). Every simplex contains at most three edges, so an invariant nonempty simplex would have to contain an entire seven-element edge orbit. This is impossible. Consequently the action is free on the realization. The quotient inherits a two-dimensional \(\Delta\)-CW structure with precisely three vertices, fifteen edges and fifteen triangular cells. Although a quotient triangle may have identified image edges, each source simplex maps homeomorphically onto its open orbit cell, and the attaching loops are determined by the transported vertex orders.

**2. Exact attaching loops.** Number the 21 graph edges lexicographically as \(e_0,\ldots,e_{20}\). For an unordered tuple of disjoint graph edges, select the lexicographically least translate as its canonical orbit representative. Number orbit representatives lexicographically in dimensions zero, one and two. Each triangular representative \((a,b,c)\) attaches along the oriented path \((a,b)(b,c)(c,a)\); transport each oriented edge back to its canonical representative and retain the permutation sign. In the quotient one-skeleton, collapse the spanning tree formed by orbit edges numbered 1 and 2 (zero-based). Label the other thirteen edge orbits in increasing order by generators \(g_1,\ldots,g_{13}\). The fifteen freely reduced attaching words are, in order, with an integer \(j\) denoting \(g_j\) and \(-j\) denoting its inverse:

```text
[1,1,3]       [1,-6]       [7,-4]       [8,-5]       [-2,-3]
[12,-5]       [-9,-6]      [2,-5,-3]    [2,-11,-4]   [4,7,-6]
[7,10,10]     [8,-9,-10]   [8,-13,-11]  [9,13,-11]  [12,12,13]
```

These words and all orbit incidences are independently reconstructed from the graph in `VERIFY_M7_C7.py`; no precomputed cell list is imported.

**3. Homotopy-preserving elimination.** Whenever a relator contains some generator exactly once with exponent \(+1\) or \(-1\), its two-cell and the corresponding one-cell cancel by a standard cellular 1–2 cancellation (equivalently solve the attaching word for that generator and substitute into all remaining attaching words). This is a homotopy equivalence of the CW complex, not merely a change of group presentation. For determinism select the first eligible relator, and within it its first uniquely occurring generator. The twelve successive choices, recorded as (current zero-based relator index, signed generator), are

```text
(0,3), (0,1), (0,7), (0,8), (0,-2), (0,12),
(0,-9), (0,-5), (0,-11), (0,-6), (0,4), (1,-13).
```

There remains one one-cell, labeled \(g_{10}\), and three two-cells with attaching words

\[
g_{10}^{-21},\qquad 1,\qquad g_{10}^{-42}.
\]

The first two-cell creates the Moore complex \(M(\mathbb Z/21\mathbb Z,1)\). Because \(g_{10}^{21}\) is nullhomotopic after that attachment, \(g_{10}^{42}\) is also nullhomotopic, so attaching the last two-cell wedges on \(S^2\). The middle trivial attaching word wedges on another \(S^2\). This proves the stated **homotopy equivalence**, including its fundamental group and all integral homology. No inference from homology alone is used.

## Verification

With Python 3, execute `python3 VERIFY_M7_C7.py` in the directory containing this document. The standard-library-only checker constructs all matchings, checks that every nonempty face orbit has size seven, generates the oriented quotient attaching loops, verifies the boundary-of-boundary identity, replays all twelve reversible cancellations, and checks that the final relators have degrees 21, 0 and 42. It finishes with `M7_C7_HOMOTOPY_OK`.

As a methodologically separate check, install the pinned dependency in `requirements.txt`, then execute `python3 CHECK_BARYCENTRIC.py`. This constructs the quotient of the **barycentric subdivision**, with 33, 120 and 90 cells, and computes the integral Smith form of the boundary in a cycle basis. It finds the unique nonunit invariant factor 21 and free second-homology rank two, printing `BARYCENTRIC_INDEPENDENT_CHECK_OK`. The latter is an independent *homology* check and is not substituted for the attaching-word proof of the homotopy type.

## Relationship to prior work

Bouc's 1992 calculation, restated by Shareshian and Wachs (2004), establishes three-torsion in \(H_1(\mathcal M_7;\mathbb Z)\); the exact covering-space homotopy type above is different information. Jonsson's work develops exact sequences for the integral homology of matching complexes, while Mondal–Mukherjee–Saha (2023/2024, with a 2025 corrigendum) computes the unquotiented complex's homology and optimal Morse matching. Their stated results do not identify the degree-21 fundamental-group relator or the geometric \(C_7\) orbit-space homotopy type. Published related cyclic Moore-space examples for different complexes do not imply this result by a change of graph or a relabeling. The proof here instead uses the actual fifteen two-cell orbit attachments.

## Limitations

The statement is a single finite, natural symmetry quotient, not a classification of all cyclic subgroups of symmetric groups. The exhaustive finite computation is valid because the input complex is exactly finite and the verifier enumerates **all** its cells; it is not being used as proof of any infinite-family assertion. The secondary barycentric computation alone would not determine homotopy type. Publication-priority uncertainty remains for unindexed equivalents and for the inaccessible full text of the 2026 Wang–Li manuscript on integral matching-complex homology lattices; its available abstract treats lattice saturation and does not expressly claim this geometric quotient equivalence. No independent external validation has been performed.

## References

1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1 (first public preprint 2004-09-03), especially Introduction and Section 4. https://arxiv.org/abs/math/0409054
2. J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, arXiv:1203.5641v1 (2012-03-26), preprint of J. Combin. Theory Ser. A 115 (2008), 1504–1526. https://arxiv.org/abs/1203.5641
3. A. Mondal, S. Mukherjee and K. Saha, *Topology of Matching Complexes of Complete Graphs via Discrete Morse Theory*, arXiv:2305.02973, Discrete Math. Theor. Comput. Sci. 26:3 (2024), particularly Section 4. https://arxiv.org/abs/2305.02973
4. A. Mondal, S. Mukherjee and K. Saha, *Corrigendum to “Topology of Matching Complexes of Complete Graphs via Discrete Morse Theory”*, arXiv:2505.01477v1 (2025-05-02), Theorem 2.1. https://arxiv.org/abs/2505.01477
5. Q. Wang and W. Li, *Integral Homology Lattices of Matching and Circulant Complexes*, arXiv:2610.22082v1 (2026-10-15); abstract inspected, full text not retrieved. https://arxiv.org/abs/2610.22082
