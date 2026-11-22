# Bridge-sensitive homotopy classification of two-cycle matching complexes

## Finding
For integers \(p,q\ge3\), let \(B_{p,q}\) be the graph obtained from disjoint simple cycles \(C_p\) and \(C_q\) by adding one edge joining one vertex of each cycle. Let \(\mathcal M(G)\) denote the ordinary matching complex whose faces are sets of mutually vertex-disjoint edges. Write \(p=3k+r\), \(q=3\ell+s\), where \(k,\ell\ge1\) and \(r,s\in\{0,1,2\}\); swap the cycles to arrange \(r\le s\). Then, integrally,

\[
\mathcal M(B_{p,q})\simeq
\begin{cases}
\bigvee^4 S^{k+\ell-1},&(r,s)=(0,0),\\
\bigvee^2 S^{k+\ell-1},&(r,s)=(0,1),\\
\bigvee^2 S^{k+\ell},&(r,s)=(0,2),\\
\ast,&(r,s)=(1,1),\\
\bigvee^2 S^{k+\ell},&(r,s)=(1,2),\\
S^{k+\ell}\vee S^{k+\ell+1},&(r,s)=(2,2).
\end{cases}
\]

In particular this matching complex is contractible exactly when both cycle lengths are congruent to \(1\pmod3\). It always has torsion-free integral homology. This classification also determines the map induced by deleting the connecting edge: for \((r,s)=(1,1)\) the unique nonzero reduced homology class is killed, while for the other five cases inclusion of the disjoint-cycle matching complex is a split injection on all reduced integral homology.

## Assumptions and scope
All graphs are finite, undirected, simple; each cycle has at least three vertices. A wedge of \(m\) spheres means their one-point wedge; \(\ast\) means a point. The two cycles are disjoint before adding the *one bridge edge* and do not share vertices or other edges. This is different from two cycles identified at a vertex or glued along an edge. The homotopy types and the inclusion assertions are statements over integral homology and arbitrary cycle lengths, not only computations at small sizes. For reduced homology, the spaces here are nonempty.

## Proof
Let \(e\) be the connecting bridge, \(X=\mathcal M(B_{p,q})\), and \(A=\mathcal M(B_{p,q}-e)\). The usual deletion–link decomposition of the matching complex is a homotopy-pushout presentation
\[
X=A\cup_{L}(e\ast L),\qquad A=\mathcal M(C_p)\ast\mathcal M(C_q),\qquad L=\mathcal M(P_{p-1})\ast\mathcal M(P_{q-1}),
\]
where \(P_m\) denotes the path graph with \(m\) vertices. Here the two paths are the cycles after removing the endpoints of \(e\), and \(e\ast L\) is a cone on \(L\). The attaching map \(L\to A\) is the join of the natural inclusions \(\iota_p:\mathcal M(P_{p-1})\hookrightarrow\mathcal M(C_p)\) and \(\iota_q\). Thus \(X\) is the homotopy cofiber of this join map.

The line graph of \(C_m\) is \(C_m\), and that of \(P_{m-1}\) is \(P_{m-2}\). Consequently the classical path/cycle independence-complex formulas [3] give, for \(m=3h+t\) with \(h\ge1\),
\[
\mathcal M(C_m)\simeq\begin{cases}S^{h-1}\vee S^{h-1},&t=0,\\S^{h-1},&t=1,\\S^h,&t=2,\end{cases}
\quad
\mathcal M(P_{m-1})\simeq\begin{cases}\ast,&t=0,\\S^{h-1},&t=1,\\S^{h-1},&t=2.\end{cases}
\]
We also need the homotopy *class* of \(\iota_m\), not just the two homotopy types.

If \(t=0\), its source is contractible. If \(t=1\), identify \(\iota_m\) with the inclusion \(\operatorname{Ind}(P_{m-2})\hookrightarrow\operatorname{Ind}(C_m)\), obtained by deleting two adjacent line-graph vertices. Deleting the first vertex leaves \(P_{m-1}\), and its link is \(\operatorname{Ind}(P_{m-3})\). Deleting the adjacent endpoint of that path leaves \(P_{m-2}\), again with link \(\operatorname{Ind}(P_{m-3})\). Since \(m-3=3(h-1)+1\), the path formula makes both links contractible. A vertex deletion with contractible link induces a homotopy equivalence, so \(\iota_m\) is a homotopy equivalence. If \(t=2\), the source has type \(S^{h-1}\) and the target \(S^h\), hence \(\iota_m\) is nullhomotopic because \(S^h\) is \((h-1)\)-connected (for \(h=1\), every map from \(S^0\) to the path-connected \(S^1\) is freely nullhomotopic).

Now evaluate the join map \(\iota_p\ast\iota_q:L\to A\). If either residue is zero, \(L\) is contractible and \(X\simeq A\). If both residues are one, the join map is a homotopy equivalence and its cofiber is contractible. In all remaining cases, at least one join factor is nullhomotopic and the join map is nullhomotopic; therefore \(X\simeq A\vee\Sigma L\). (The basepoint identification is valid since the relevant connected joins have dimension at least one.) Substituting the displayed path/cycle types and the dimension rule \(S^a\ast S^b\simeq S^{a+b+1}\) gives exactly the six cases above. All homotopy equivalences are integral, so there is no integral torsion.

Finally, inclusion \(A\hookrightarrow X\) becomes a homotopy equivalence when \(L\) is contractible, is a map to a contractible space when both residues are one, and becomes a wedge-summand inclusion when the attaching map is null. This proves the last assertion. \(\square\)

## Verification
The accompanying standard-library-only Python script `verify_barbell.py` constructs all matchings and exact mod-two simplicial boundary matrices for every unordered pair \(3\le p\le q\le9\). Gaussian elimination over \(\mathbb F_2\) matches the theorem's predicted reduced Betti numbers on all \(28\) cases and all \(27,704\) enumerated nonempty simplices. See `verification_output.txt`. The finite computations test signs of errors in the residue table; they do not prove the infinite classification or integral torsion-freeness, which follow from the cofiber argument.

## Relationship to prior work
The path and cycle independence-complex homotopy types due to Kozlov are previously known; the present calculation uses them as inputs, not as a new result [3]. The polygonal-line-tiling study [1] concerns polygons sharing *edges*, not two vertex-disjoint polygons connected by a bridge. The outerplanar-graph theorem [2] already establishes the general qualitative contractible-or-sphere-wedge alternative, which is not reclaimed here; it does not give the six-residue exact homotopy types or the bridge-induced inclusion maps. The cycle-wedge independence-complex study [3] identifies cycle vertices, whereas the line graph here joins two cycle graphs to a new bridge vertex through two pairs of adjacent line-graph vertices; its cycle-wedge formulas do not imply this statement without an additional analysis. The contribution is the complete residue and map-level classification for this natural two-cycle bridge family.

## Limitations
The statement applies only to a single bridge connecting precisely two disjoint simple cycles, with each length at least three; it does not classify cycles connected by longer paths or arbitrary cactus graphs. The computational test is over \(\mathbb F_2\) at bounded sizes, not an independent proof over the integers. The literature comparisons do not establish absolute novelty against all unpublished or unindexed work.

## References
[1] M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, first posted 2022-11-22. https://arxiv.org/abs/2211.12559

[2] M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first posted 2024-11-07. https://arxiv.org/abs/2411.04601

[3] N. Daundkar, S. Panja, S. Prasad, *Independence complexes of wedge of graphs*, arXiv:2303.08798, first posted 2023-03-15; see Theorems 2.12–2.13 for Kozlov's path/cycle formulas. https://arxiv.org/abs/2303.08798
