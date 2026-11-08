# Integral Weyl-group persistence of the 24-cell graph

## Finding
Let \(V=\{\pm e_i\pm e_j:1\le i<j\le4\}\subset\mathbb R^4\), comprising the \(24\) long \(D_4\) roots. Join two distinct roots by an edge exactly when their Euclidean inner product is \(1\); this is the graph \(G\) of the regular \(24\)-cell. Give \(G\) unit-edge shortest-path metric and let \(K_r=\operatorname{VR}_{\le r}(V(G))\) be the inclusive Vietoris–Rips complex for each real \(r\ge0\).

Write \(W=\operatorname{Aut}(G)=W(F_4)\), of order \(1152\), and \(\epsilon(g)=\det_{\mathbb R^4}(g)\). The natural \(W\)-action preserves the filtration. Let \(\mathcal F\) be the \(W\)-set of \(24\) octahedral facets of the \(24\)-cell. The complete **integral equivariant persistence** is

\[
\widetilde H_k(K_r;\mathbb Z)\cong
\begin{cases}
\ker\bigl(\mathbb Z[V]\xrightarrow{\mathrm{sum}}\mathbb Z\bigr), & k=0,\quad0\le r<1,\\
\mathbb Z_\epsilon\otimes\bigl(\mathbb Z[\mathcal F]/\mathbb Z\sum_{F\in\mathcal F}[F]\bigr), & k=2,\quad1\le r<2,\\
\mathbb Z_\epsilon, & k=11,\quad2\le r<3,\\
0, &\text{otherwise}.
\end{cases}
\]

Here \(\mathbb Z_\epsilon\) denotes the rank-one sign lattice on which \(g\) acts by \(\epsilon(g)\); the group acts on permutation lattices by permuting their indicated bases. There are no nonzero positive-degree structure maps across different integer-scale stages. Non-equivariantly, \(K_1\simeq\bigvee^{23}S^2\) and \(K_2\cong S^{11}\), and \(K_3\) is a simplex. The reduced barcode over \(\mathbb Z\) comprises \(23\) intervals \([0,1)\) in degree zero, \(23\) intervals \([1,2)\) in degree two, and a single interval \([2,3)\) in degree eleven.

The full rational degree-two character is
\[\chi_2(g)=\epsilon(g)\bigl(\#\operatorname{Fix}_{\mathcal F}(g)-1\bigr).\]
Its value distribution is: \(-11\) on \(12\) elements, \(-5\) on \(12\), \(-1\) on \(597\), \(1\) on \(444\), \(3\) on \(54\), \(5\) on \(32\), and \(23\) on the identity. The degree-eleven character is exactly \(\epsilon\), taking each sign on \(576\) elements. In particular neither positive-degree rational homology group has a \(W\)-fixed class.

## Assumptions and scope
The theorem concerns the **graph shortest-path** metric, not the Euclidean distance inherited from \(\mathbb R^4\); this choice matters because Euclidean distance has four positive values on this vertex set, whereas graph distance has three. Only the four discrete stages \(0,1,2,3\) matter for real nonnegative \(r\). All homology is reduced and integral unless indicated. No orientation of individual sphere-wedge summands is asserted to be invariant under the group.

## Proof
**1. Geometry and distances.** By direct inspection of the \(24\) root vectors, the graph has \(96\) edges. For any two distinct roots, graph distance is \(1\) on \(96\) unordered pairs, \(2\) on \(168\), and \(3\) on exactly \(12\), the antipodal pairs \(\{v,-v\}\). These counts and the stronger pairwise statements follow from the four-coordinate criterion for a common neighbor; the supplied exact finite checker also enumerates all \(276\) pairs. Thus \(K_0\) consists of \(24\) points, and \(K_2\) is the clique complex with the \(12\) antipodal edges deleted from a complete graph. It is the join of \(12\) copies of \(S^0\), namely the boundary of the \(12\)-dimensional cross-polytope, homeomorphic to \(S^{11}\). At radius \(3\), it becomes the full simplex.

**2. The radius-one skeleton.** The convex regular \(24\)-cell \(P=\operatorname{conv}(V)\) has \(24\) octahedral facets. Their supporting normals can be chosen as the \(8\) vectors \(\pm e_i\) and all \(16\) vectors \((\pm1/2,\pm1/2,\pm1/2,\pm1/2)\). A facet with normal \(n\) contains exactly the six vertices for which \(v\cdot n=1\). Its edge graph is octahedral and has eight triangular faces. Exhaustive checking of the \(\binom{24}{3}\) vertex triples proves that the \(96\) graph triangles are **exactly** the \(96\) triangular two-faces of \(P\): every such triangle belongs to two of the enumerated octahedral facets, and no other triple is pairwise adjacent. Since the graph has no four-cliques, \(K_1\) is precisely the two-skeleton of \(\partial P\cong S^3\). Removing a small open three-ball from the interior of each of the \(24\) octahedral facets and radially retracting the remaining shell onto the two-skeleton identifies \(K_1\) with the homotopy type of a three-sphere with \(24\) disjoint open three-balls removed. This is \(\bigvee^{23}S^2\), proving that its homology is torsion-free and concentrated in dimension two.

**3. Exact integral group lattice in degree two.** Orient \(\partial P\) using the ambient orientation of \(\mathbb R^4\), and orient each octahedral facet consistently as a piece of its boundary. The cellular top boundary is
\[\partial_3:\mathbb Z[\mathcal F]\longrightarrow C_2(K_1;\mathbb Z).\]
Because the full boundary is a three-sphere, \(\ker(\partial_3)=\mathbb Z\sum_{F\in\mathcal F}[F]\), and \(\operatorname{im}(\partial_3)=\widetilde H_2(K_1;\mathbb Z)\), as there are no \(3\)-cells in \(K_1\) and the full sphere has vanishing second homology. Every orthogonal symmetry \(g\in W\) permutes the facets and changes **all** their induced orientations by the same sign \(\epsilon(g)\). The exact \(W\)-module quotient asserted above follows; note that it is a quotient lattice, not an unqualified identification with the integral augmentation kernel. Its rational trace is \(\epsilon(g)(\#\operatorname{Fix}_{\mathcal F}(g)-1)\).

**4. The degree-eleven orientation character.** Order the \(12\) antipodal pairs and orient each by a chosen representative. Any graph automorphism permutes these pairs and possibly swaps their representatives; its degree on the cross-polytope boundary is the sign of the pair permutation times \((-1)\) raised to the number of within-pair swaps. The four simple \(F_4\) reflections with normals \((0,1,-1,0)\), \((0,0,1,-1)\), \((0,0,0,1)\), and \((1,-1,-1,-1)/2\) act on this orientation by \(-1\), just as they act on the ambient orientation. They generate \(W\), so the orientation character on \(\widetilde H_{11}(K_2;\mathbb Z)\) is \(\epsilon\) for every element. The finite checker separately enumerates all \(1152\) automorphisms, computes both signs, and verifies equality.

**5. Full characters and persistence.** Enumeration of all automorphisms and their fixed facets gives the stated seven-value distribution of \(\chi_2\). The average of \(\chi_2\) over \(W\) is zero, as is the average of \(\epsilon\), establishing the rational invariant assertions. Since nonzero homology occurs in different degrees in the successive positive-scale stages, all nontrivial persistent groups die at the next indicated stage, and no additional positive-degree intervals can occur. In degree zero the connected radius-one complex kills precisely the \(23\) initial reduced components.

## Verification
The complete standalone checker `verify.py` generates the \(24\) roots, computes graph distances, facets and all clique triangles, checks the complete facet-incidence identity, and independently computes rank \(73\) of the \(96\times96\) simplicial triangle boundary over \(\mathbb F_2\). It generates \(W(F_4)\) from the four exact rational reflections and independently enumerates all graph automorphisms; both have order \(1152\). It computes the complete fixed-facet character distribution and antipodal orientation signs. The recorded run used Python 3.13.5, NetworkX 3.6.1, and SymPy 1.14.0; run `python3 verify.py` to reproduce it. Expected final output: `TWENTYFOUR_CELL_EQUIVARIANT_RIPS_PASS`. The structural geometry and cellular-exact-sequence proof establish the integral and homotopy conclusions; mod-two computation alone would not.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers*, first public April 3, 2011, provides the general graph-power/Vietoris–Rips framework and the definition of these complexes. Its inspected text treats graph-power stability, universality, line graphs, subdivisions and cycles, not the present equivariant \(24\)-cell calculation. Nada Saleh's 2023 thesis *On Vietoris-Rips Complexes of the 2-Sphere*, Chapter 4 §4.2 p.73, already reports \(23\) second-homology classes and one eleventh-homology class in a **different four-distance filtration** of the Euclidean \(24\)-cell. Those dimensions and the corresponding numerical phenomena are acknowledged as previous work; they are **not** presented as novel. In particular, that table does not determine the integral \(W(F_4)\)-module, fixed-facet character, group action on the eleventh-dimensional generator, or the graph-shortest-path filtration with diameter three. Standard \(24\)-cell face counts and the \(1152\)-element geometric symmetry group are also known geometric data. The contribution is the explicit full integral equivariant persistence and character distribution, not rediscovery of face counts or Betti numbers.

## Limitations
This is one canonical graph rather than a uniform result for all root polytopes. The rational trace distribution uniquely determines the complexified character but is not presented as a decomposition into named irreducible \(F_4\) characters; the stronger exact integral quotient lattice is supplied directly. General equivariant cellular-homology principles provide much of the mechanism, so the priority risk concerns whether an unindexed calculation has already instantiated these mechanisms for this specific polytope and metric. Independent mathematical review and definitive publication-priority assessment remain outstanding.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first submitted 2011-04-03. https://arxiv.org/abs/1104.0433
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral thesis, Justus-Liebig-Universität Gießen, September 2023, especially Chapter 4 §4.2 p.73. https://d-nb.info/1375949942/34
3. *24-cell*, geometric coordinates, octahedral face counts and Weyl-group order. https://en.wikipedia.org/wiki/24-cell
4. *24-Cell*, Wolfram MathWorld, regular polychoron coordinates and combinatorial data. https://mathworld.wolfram.com/24-Cell.html
