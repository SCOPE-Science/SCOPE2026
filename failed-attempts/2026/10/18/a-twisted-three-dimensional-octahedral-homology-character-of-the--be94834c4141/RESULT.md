# A twisted three-dimensional octahedral homology character of the cube two-matching complex

## Finding

Let \(Q_3\) be the graph with vertices \((\mathbb F_2)^3\), where two vertices are adjacent exactly when they differ in one coordinate. Let \(X=M_2(Q_3)\), the simplicial complex whose vertices are the twelve edges of \(Q_3\) and whose faces are edge sets in which every graph vertex has selected degree at most two. Then

\[
X\simeq S^5\vee S^5\vee S^5.
\]

The full graph automorphism group is \(B_3=(\mathbb F_2)^3\rtimes S_3\). For \(t\in(\mathbb F_2)^3\), \(\pi\in S_3\), write \(g_{t,\pi}(x)=t+\pi(x)\), with \(\pi\) permuting the three coordinates. The **complete** rational character of the induced action on \(\widetilde H_5(X;\mathbb Q)\) is

\[
\boxed{\operatorname{tr}(g_{t,\pi})=\operatorname{sgn}(\pi)\sum_{i:\pi(i)=i}(-1)^{t_i}.}
\]

Consequently this rational representation is the natural three-dimensional signed-coordinate-permutation module of \(B_3\), tensored with the sign character of its \(S_3\) quotient. It is irreducible over \(\mathbb Q\). Translation by \((1,1,1)\) acts as minus the identity; the fixed subspace under the full group has dimension zero. The statement concerns rational group representations, not a determination of an integral equivariant lattice.

## Assumptions and scope

The graph, simplicial complex and group action above are all finite and unambiguous. An edge set \(F\subseteq E(Q_3)\) is a face if and only if it does **not** contain all three edges of the star of any one cube vertex. In particular there are eight forbidden three-edge stars on the twelve simplicial vertices. Homology uses standard unreduced degree zero and reduced positive-degree conventions, with integral coefficients for the homotopy classification and rational coefficients for character theory.

Every automorphism of the cube has the displayed form: translations act transitively on cube vertices, and any automorphism fixing the zero vertex permutes its three neighbours, thereby determining its action on all vertices by graph distances and intersections of successive spheres. Thus the order is \(8\cdot6=48\).

## Proof

**1. Exact simplicial and Morse certificate.** Number the graph vertices by the three-bit integers from zero to seven, and list its twelve edges lexicographically by the loop

```
(u, u ^ (1 << k)) for u in range(8) for k in range(3)
    if u < (u ^ (1 << k))
```

with zero-based edge indices. Encode an edge subset by its twelve-bit incidence mask. Enumerating all \(2^{12}=4096\) masks and rejecting any mask containing one of the eight full vertex stars gives exactly 1698 nonempty faces, by dimension zero through seven:

\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(12,66,212,423,516,352,108,9).
\]

Here and below each integer count is determined by complete enumeration, not sampling. Pair remaining masks successively by toggling the bits in the order

```
(1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6)
```

whenever both the smaller and larger masks remain available in the augmented face poset. Remove the unique pair containing the empty face. The resulting nonaugmented face-poset matching has 847 pairs and just four critical cells: one vertex and three cells of dimension five. Each matched Hasse arrow is directed upward, all other cover arrows downward. Exhaustive topological sorting of this directed graph on all 1698 faces and all 7980 Hasse incidences visits every face, certifying acyclicity. By discrete Morse theory, the resulting CW complex has exactly one zero-cell and three five-cells; its attaching maps to a point are null, so the integral homotopy type is a wedge of three five-spheres. In particular all reduced homology outside degree five vanishes. The attached standalone checker constructs this matching and verifies every listed condition.

**2. Signed fixed-simplex Lefschetz calculation.** For \(g=g_{t,\pi}\), let \(p_g\) be its induced permutation of the twelve graph edges. If a face \(F\) is fixed setwise by \(p_g\), its contribution to the ordinary simplicial Lefschetz number is \((-1)^{|F|-1}\operatorname{sgn}(p_g|_F)\). All nonfixed faces contribute zero. Because \(X\) has ordinary \(H_0\cong\mathbb Q\) and just one possible nonzero reduced group, in odd degree five,

\[
\operatorname{tr}(g|\widetilde H_5(X;\mathbb Q))
=1-\sum_{\substack{\varnothing\ne F\in X\\gF=F}}
(-1)^{|F|-1}\operatorname{sgn}(p_g|_F).
\]

There is also a useful independent orbit expression. Partition the twelve graph edges into \(p_g\)-orbits \(\mathcal O_g\). Every invariant face is a union of orbits; an orbit of length \(\ell\) has permutation sign \((-1)^{\ell-1}\). The two parity contributions combine to give

\[
\operatorname{tr}(g|\widetilde H_5)
=\sum_{\substack{J\subseteq\mathcal O_g\\\bigcup J\in X}}(-1)^{|J|}.
\]

Thus the character can be computed in two ways: oriented fixed faces or signed admissible orbit selections. Both calculations are run independently for all 48 automorphisms and agree with the closed formula in the Finding. They are exact integer evaluations, each requiring at most 4096 subsets, and the complete finite check is implemented in the accompanying standalone Python program.

For a compact independently readable certificate, let \(\lambda_+\) and \(\lambda_-\) be the partitions of the lengths of coordinate cycles of \(\pi\) on which the total translation-bit parity is respectively even and odd. These positive/negative signed-cycle types give all ten conjugacy classes. The exact computations give:

| \(\lambda_+\) | \(\lambda_-\) | Class size | Trace |
|---|---|---:|---:|
| \((1,1,1)\) | \(\varnothing\) | 1 | 3 |
| \((1,1)\) | \((1)\) | 3 | 1 |
| \((1)\) | \((1,1)\) | 3 | -1 |
| \(\varnothing\) | \((1,1,1)\) | 1 | -3 |
| \((2,1)\) | \(\varnothing\) | 6 | -1 |
| \((2)\) | \((1)\) | 6 | 1 |
| \((1)\) | \((2)\) | 6 | -1 |
| \(\varnothing\) | \((2,1)\) | 6 | 1 |
| \((3)\) | \(\varnothing\) | 8 | 0 |
| \(\varnothing\) | \((3)\) | 8 | 0 |

The class sizes sum to 48; all traces equal \(\operatorname{sgn}(\pi)\sum_{i:\pi(i)=i}(-1)^{t_i}\) because every fixed coordinate corresponds to a signed one-cycle and coordinate cycles of larger length contribute zero. The character therefore determines the rational representation by semisimplicity of \(\mathbb Q[B_3]\). Its restriction to the normal translation subgroup has three distinct coordinate-sign characters, each with multiplicity one. The quotient \(S_3\) permutes these three characters transitively, so a nonzero group-invariant proper rational submodule cannot exist: the representation is irreducible. Averaging the displayed character over the group yields zero invariants.

## Verification

Run `python3 verify_cube_two_matching.py` using only the Python standard library. The program checks two independent face predicates on every mask, the entire face vector, all 847 pairings, every Hasse arrow and directed acyclicity, and independent mod-two boundary ranks in every degree. It then constructs all 48 induced permutations, computes the oriented fixed-face Lefschetz trace, computes the signed orbit-union trace separately, and checks both against the stated formula. The script asserts the antipodal value \(-3\), the character histogram and the absence of group invariants.

The mod-two Betti vector in ordinary degrees zero through seven is \((1,0,0,0,0,3,0,0)\). This second computation corroborates the Morse certificate, but the integral homotopy equivalence follows from the complete acyclic matching rather than from mod-two Betti numbers alone.

## Relationship to prior work

Vega introduced and systematically studied two-matching complexes using matching trees, classifying several families including wheels and caterpillars. The inspected paper does not state a homotopy or full symmetry-character classification for the three-cube. Kawamura proved general homological relationships between independence and edge-covering complexes using Alexander duality; Tsukuda developed corresponding incidence-graph and homotopy formulations. Their general duality is acknowledged as prior work: its ordinary homology implications are not claimed as new here. The present claim is the **explicit complete full-automorphism rational representation** of this specific bounded-degree complex, determined by 48 signed fixed-face Lefschetz calculations.

Published computations for the ordinary matching complex of the cube concern a different degree bound. Symmetry results for the cube's cut complexes and for the *octahedral graph's* matching complex concern other simplicial complexes or other graphs; a common abstract symmetry group does not transfer their representations. These comparisons do not establish universal novelty. An unindexed equivalent treatment, or a more general equivariant duality specialized with further computation, remains possible.

## Limitations

This is a single finite graph, not an infinite-family result. The nonequivariant homotopy type is integral; the symmetry description is over \(\mathbb Q\), and no integral lattice-isomorphism, equivariant homotopy splitting, geometric basis or independence from previous literature is asserted. The discrete-Morse matching itself need not be equivariant. Reproducibility uses a finite exhaustive proof certificate that must be executed or inspected rather than an unsupported computational log. Independent external mathematical audit is not asserted.

## References

1. J. Vega, *2-Matching Complexes*, arXiv:1909.10406 (first posted 2019-09-23), https://arxiv.org/abs/1909.10406.
2. K. Kawamura, *Independence Complexes and Edge Covering Complexes via Alexander Duality*, Electronic Journal of Combinatorics 18(1), P39 (2011), doi:10.37236/526.
3. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12(1), 28–46 (2017), doi:10.55016/ojs/cdm.v12i1.62277.
