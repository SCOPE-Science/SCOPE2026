# Higher-independence homotopy and automorphism modules of double-star trees

## Finding

Let \(T_{a,b}\) be the tree on two adjacent nonleaf vertices \(u,v\), with \(a\geq1\) pendant leaves adjacent to \(u\) and \(b\geq1\) pendant leaves adjacent to \(v\), and no other edges. Put \(N=a+b\). For every integer \(r\geq1\), let \(\operatorname{Ind}_r(T_{a,b})\) be the simplicial complex of vertex subsets whose induced components all have at most \(r\) vertices.

For \(r=1\) and \(r\geq N+2\), the complex is contractible. For every \(2\leq r\leq N+1\), there is an integral homotopy equivalence

\[
\operatorname{Ind}_r(T_{a,b})\simeq\bigvee^{\binom{N-1}{r-2}}S^{r-1}.
\]

This completely determines the homotopy type at all thresholds, including \(r=2\) (one circle) and \(r=N+1\) (one \(N\)-sphere). More precisely, for every \(r\geq2\), there is a homotopy equivalence with the **double suspension of the \((r-3)\)-skeleton of the simplex on the \(N\) leaves**, interpreted as contractible if that skeleton is the full simplex and with the standard augmented convention when \(r=2\).

There is also a canonical integral automorphism-module description. Let \(L\) be the leaf set, \(G=\operatorname{Aut}(T_{a,b})\), \(V=\ker(\mathbb Z[L]\xrightarrow{\sum}\mathbb Z)\), and let \(\varepsilon:G\to\{\pm1\}\) record the sign of the permutation induced on the two hubs. The action on the leaf set defines a \(G\)-action on \(V\). For \(2\leq r\leq N+1\), the only nonzero reduced integral homology module is

\[
\widetilde H_{r-1}(\operatorname{Ind}_r(T_{a,b});\mathbb Z)
\cong \varepsilon\otimes\bigwedge^{r-2}V.
\]

In particular, if \(a\ne b\), then \(G\cong \mathfrak S_a\times\mathfrak S_b\) and \(\varepsilon\) is trivial. If \(a=b\), the group also permits interchange of the hubs and their leaf blocks, and this interchange contributes a minus sign in addition to its induced exterior-power action. For any \(g\in G\), if \(c_j(g)\) is the number of \(j\)-cycles in the permutation of \(L\), the rational homology character is

\[
\operatorname{tr}(g\mid\widetilde H_{r-1})
=\varepsilon(g)\,[t^{r-2}]\frac{\prod_{j\geq1}(1-(-t)^j)^{c_j(g)}}{1+t}.
\]

## Assumptions and scope

The graph is finite, simple, undirected and connected; both hubs have at least one private leaf. Graph-induced components are counted by their numbers of vertices, not their edges. Homology is reduced integral homology unless a rational character is explicitly mentioned. All statements are valid for arbitrary positive integral \(a,b\) and every integral \(r\geq1\). The displayed homotopy equivalence is not asserted to be equivariant; the integral homology-module isomorphism is natural under every graph automorphism. Empty exterior powers have the usual value \(\mathbb Z\).

For a finite vertex set \(L\), write \(\Delta(L)\) for the simplex and \(\mathrm{Skel}_d\Delta(L)\) for its \(d\)-skeleton. When \(d=-1\), the augmented skeleton consists only of the empty face and has reduced homology \(\mathbb Z\) in degree \(-1\); this convention is used only inside joins. When \(d\geq N-1\), the skeleton is the whole simplex and is contractible.

## Proof

**1. Explicit decomposition.** Partition the leaf set as \(L=A\sqcup B\) with \(|A|=a\), \(|B|=b\). Let \(K=\operatorname{Ind}_r(T_{a,b})\). Set \(K_0\) equal to the subcomplex of faces using at most one hub. For \(r\geq2\), every leaf-only face belongs to \(\Delta(L)\); a face using \(u\) but not \(v\) is valid precisely when it uses at most \(r-1\) leaves of \(A\), with arbitrary leaves of \(B\). The analogous statement holds with \(u,A\) and \(v,B\) exchanged. Thus

\[
K_0=\Delta(L)\cup\bigl(u*(\mathrm{Skel}_{r-2}\Delta(A)*\Delta(B))\bigr)
\cup\bigl(v*(\Delta(A)*\mathrm{Skel}_{r-2}\Delta(B))\bigr).
\]

Here \(u*X\) denotes a cone on \(X\), including \(X\) among its faces. Since \(a,b\geq1\), both bases \(\mathrm{Skel}_{r-2}\Delta(A)*\Delta(B)\) and \(\Delta(A)*\mathrm{Skel}_{r-2}\Delta(B)\) are nonempty contractible complexes (they each have a simplex factor on a nonempty set). The first cone attaches to the leaf simplex along the first contractible base; the second attaches to the resulting union along the second contractible base. A union of CW complexes consisting of two contractible subcomplexes with nonempty contractible intersection is contractible, as follows from the homotopy pushout lemma. Therefore \(K_0\) is contractible. For \(r=1\), the same argument applies with bases \(\Delta(B)\) and \(\Delta(A)\); no face can contain both hubs, so \(K=K_0\) is contractible.

**2. The faces using both hubs.** For \(r\geq2\), once both hubs are selected, every selected leaf joins their connected component. Thus exactly those faces with at most \(r-2\) selected leaves can accompany the two hubs. Let \(S=\mathrm{Skel}_{r-3}\Delta(L)\). The union of all faces containing both hubs with their subfaces is the join \(B_0=\Delta(\{u,v\})*S\), which is contractible. Its intersection with \(K_0\) is precisely

\[
J=\partial\Delta(\{u,v\})*S\cong S^0*S.
\]

This identity includes the leaf-only faces. The Mayer--Vietoris homotopy-pushout principle for cofibrations gives \(K=K_0\cup_J B_0\simeq\Sigma J\simeq\Sigma^2 S\), because both \(K_0\) and \(B_0\) are contractible. The same argument covers \(r=N+2\) when \(S=\Delta(L)\), giving contractibility. For larger \(r\), every vertex subset is valid and \(K\) is a simplex.

**3. Sphere count.** For \(2\leq r\leq N+1\), \(S\) is the \((r-3)\)-skeleton of an \((N-1)\)-simplex. The standard elementary relative-cell argument (or exact augmented chain complex of the full simplex) gives \(S\simeq\bigvee^{\binom{N-1}{r-2}}S^{r-3}\), using the augmented \((-1)\)-sphere convention at \(r=2\). Double suspension yields the claimed wedge of \((r-1)\)-spheres, with the exact integral multiplicity. No finite computation is used to pass from finite \(N\) to general \(N\).

**4. Integral automorphism action.** Every automorphism preserves the unordered pair of hubs, the leaf set, \(K_0\), \(B_0\) and \(J\). Natural Mayer--Vietoris connecting homomorphisms give a \(G\)-equivariant isomorphism \(\widetilde H_{r-1}(K;\mathbb Z)\cong\widetilde H_{r-2}(J;\mathbb Z)\). The join Künneth isomorphism identifies the latter with \(\widetilde H_0(\partial\Delta(\{u,v\});\mathbb Z)\otimes\widetilde H_{r-3}(S;\mathbb Z)\). The first factor is the one-dimensional sign module \(\varepsilon\) for hub interchange. The second factor is \(\bigwedge^{r-2}V\), since the augmented simplicial boundary on \(\bigwedge^{r-2}\mathbb Z[L]\) is contraction by the summation functional and its kernel is \(\bigwedge^{r-2}\ker(\sum)\). There is no higher boundary within the skeleton. All isomorphisms are integral and natural under leaf permutations. Taking determinants gives \(\det(1+tg\mid V)=\prod_j(1-(-t)^j)^{c_j(g)}/(1+t)\), proving the character formula.

## Verification

`check_double_star.py` reconstructs all admissible vertex subsets from the actual induced-graph connected components, independently checks the four hub-status formula, computes all reduced mod-two Betti numbers, and calculates signed Lefschetz traces for every leaf-block permutation and, when applicable, every hub-exchange coset element. It exhaustively tests every \(1\leq a,b\leq3\) and every \(1\leq r\leq a+b+2\): 54 graph/threshold combinations, 4,174 enumerated nonempty faces across tests, 576 hub-fixing symmetry tests, and 316 hub-exchange tests. Output is `check_output.json`. This finite confirmation checks examples and signs but the unrestricted conclusion follows from the decomposition and natural homology argument above.

## Relationship to prior work

Sawant (2026) proves vertex decomposability of higher-independence complexes of all trees, but this qualitative result does not specify the wedge dimensions, binomial multiplicities, or automorphism modules for the double-star family. Deshpande, Shukla and Singh (2020) prove a general wedge-of-spheres property for chordal graphs, also without this exact quantitative and equivariant classification. Deshpande and Singh (2020/2021) compute families including complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect regular rooted trees; the general two-centre, independently varied private-leaf family is not one of those stated classes. Abdelmalek and collaborators (2021/2023) establish structural vertex-decomposability results for caterpillars, but not the present uniform integral module description. The path-on-four-vertices endpoint \(a=b=1\) is covered by known path classifications and is not proposed as a new special case.

## Limitations

The homotopy classification is for diameter-three trees only; it does not give an explicit homotopy formula for arbitrary caterpillars or trees with three or more nonleaf vertices. The integral module is for the actual graph automorphism group and does not assert an equivariant homotopy splitting into spheres. The source comparison cannot exclude an unpublished or unindexed equivalent double-star formula. In particular, this is not a new proof that all tree higher-independence complexes are vertex decomposable.

## References

- R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, first posted 2026-05-24, https://arxiv.org/abs/2605.25150.
- P. Deshpande, S. Shukla, A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775, https://arxiv.org/abs/2001.06775.
- P. Deshpande, A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, https://arxiv.org/abs/2001.05448.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, https://arxiv.org/abs/2106.10863.
