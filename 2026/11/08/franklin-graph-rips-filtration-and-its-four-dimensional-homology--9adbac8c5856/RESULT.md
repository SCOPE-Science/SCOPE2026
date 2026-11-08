# Franklin graph Rips filtration and its four-dimensional homology character

## Finding

For the Franklin graph \(F\), with its vertex shortest-path distance, the **inclusive graph-metric Vietoris--Rips filtration** \(R_r\) has the complete homotopy classification

\[
R_r\simeq\begin{cases}
\bigvee^{11}S^0,&0\le r<1,\\
\bigvee^7S^1,&1\le r<2,\\
\bigvee^4S^2,&2\le r<3,\\
*,&r\ge3.
\end{cases}
\]

Write \(G=\operatorname{Aut}(F)\), and let \(z(i)=i+6\pmod {12}\). The action on second rational homology satisfies

\[
\widetilde H_2(R_2;\mathbb Q)\cong \mathbf1\oplus W,
\qquad \dim W=3,
\]

where \(W\) is absolutely irreducible over \(\mathbb C\), and the central order-two automorphism \(z\) acts by \(-1\) on \(W\). Thus the \(G\)-invariant subspace is one-dimensional. An equivalent formulation is that \(R_2\) is an independence complex of a graph isomorphic to \(F\).

## Assumptions and scope

Let \(V(F)=\mathbb Z/12\mathbb Z\). The undirected edges are the twelve cycle edges \(\{i,i+1\}\), with indices reduced modulo twelve, and the six chords \(\{2j,2j+5\}\) for \(j=0,\ldots,5\). This is the standard \([5,-5]^6\) LCF presentation of the Franklin graph. Let \(d_F\) denote the ordinary shortest-path distance in this graph, **not** a Euclidean or continuous-graph metric. For every real \(r\ge0\) define

\[
R_r=\{\sigma\subseteq V(F):d_F(u,v)\le r\text{ for all }u,v\in\sigma\}.
\]

We include the empty face in finite face-poset computations. Homotopy types refer to geometric realizations, and all non-equivariant homotopy statements are integral. The representation statement is over \(\mathbb Q\) only.

## Proof

**Graph and easy scales.** The graph has twelve vertices, eighteen edges, is connected, and its graph-metric diameter is three. Thus \(R_0\) consists of twelve points; \(R_1\) is the triangle-free connected graph \(F\) of cycle rank \(18-12+1=7\); and \(R_r\) is the full simplex once \(r\ge3\). These descriptions extend over the indicated half-open intervals because distances are integral.

**Scale-two finite homotopy certificate.** The executable `verify_franklin.py` constructs the graph from the explicit edges, computes all twelve breadth-first-search distance rows, and enumerates all \(2^{12}=4096\) vertex subsets. Independently it obtains maximal cliques by a recursive clique search and checks that their downward closure agrees with the exhaustive face set. Exactly \(196\) faces (including the empty face) occur, with nonempty face vector \((12,48,76,45,12,2)\) in dimensions zero through five and exactly \(17\) maximal faces.

For each of the two vertex orders \(0,1,\ldots,11\) and \(11,10,\ldots,0\), start with the full face set and the empty matching. At a vertex \(v\), consider currently remaining faces \(\sigma\) in increasing order of pair \((|\sigma|,\operatorname{mask}(\sigma))\). Whenever \(v\notin\sigma\) and both \(\sigma\) and \(\sigma\cup\{v\}\) remain, match these two faces and remove both. This completely specifies the matching without a search heuristic. Each order yields exactly \(96\) disjoint matched pairs, one of which matches the empty face to a vertex, and exactly four unmatched two-dimensional faces.

The program **constructs all** \(588\) cover incidences of the face poset (including those from the empty face), reverses the matched incidences and orients every other incidence downward. It then runs a full topological sort, confirming that all \(196\) faces are visited: the directed matching has no cycles. By the finite acyclic-matching theorem of discrete Morse theory, the geometric realization has a CW model with just one zero-cell and four two-cells, with no one-cells. Every two-cell therefore attaches to a point, proving \(R_2\simeq\bigvee^4S^2\). This is a complete homotopy proof rather than an inference from mod-two Betti numbers. Separately, direct mod-two boundary elimination on the unreduced simplicial complex gives ranks \((11,37,35,10,2)\) in positive chain degrees one through five and confirms the four-dimensional second homology.

**Automorphism representation.** All graph automorphisms are obtained by a recursive partial-bijection enumeration that tests adjacency and nonadjacency against assigned vertices at every extension. There are \(48\) such permutations. The involution \(z(i)=i+6\) commutes with all of them and is the unique nonidentity central element. The second homology is the only positive reduced rational homology group. Hence for every \(g\in G\), its trace equals the reduced simplicial Lefschetz number

\[
\chi(g)=-1+\sum_{\substack{\varnothing\ne\sigma\in R_2\\g\sigma=\sigma}}
 (-1)^{|\sigma|-1}\,\operatorname{sgn}(g|_\sigma).
\]

Here \(\operatorname{sgn}(g|_\sigma)\) is the orientation sign of the induced permutation of the increasingly ordered vertices of \(\sigma\). Enumerating the \(48\) permutations yields \(\chi(1)=4\), \(\chi(z)=-2\). The joint histogram `(order, trace): multiplicity` is `(1,4):1; (2,-2):1; (2,0):9; (2,2):9; (3,1):8; (4,0):6; (4,2):6; (6,1):8`.

For any \(g\), the character of the plus and minus eigenspaces of \(z\) is respectively \(\chi_+(g)=(\chi(g)+\chi(zg))/2\) and \(\chi_-(g)=(\chi(g)-\chi(zg))/2\). The finite check gives \(\chi_+(g)=1\) for every \(g\) and \(\chi_-(1)=3\); moreover

\[
\frac{1}{48}\sum_{g\in G}\chi_-(g)^2=1.
\]

Thus the plus eigenspace is the trivial one-dimensional module; the minus eigenspace has irreducible complex character (character inner product one) and is therefore absolutely irreducible. This proves the stated rational decomposition. The total fixed-space dimension equals \(48^{-1}\sum_g\chi(g)=1\).

**Equivalent independence-complex model.** Every pair of distinct vertices is separated by distance one, two or three. Therefore \(R_2\) contains precisely those sets with no pair at distance three, so it equals \(\operatorname{Ind}(F_{d=3})\) where the graph \(F_{d=3}\) joins distance-three pairs. A complete backtracking graph-isomorphism check identifies \(F_{d=3}\cong F\). This equivalence is included in the prior-work comparison, not treated as a novelty-preserving change of terminology.

## Verification

Run `python3 verify_franklin.py` from the directory containing the accompanying script. It uses only the Python standard library. `verification_output.txt` is the recorded output. Checks include exhaustive simplicial membership, maximal-clique closure, two complete acyclic Morse matchings, graph isomorphism, full automorphism enumeration, and every homology-character evaluation. The script's deterministic output is compared with the embedded record. The stand-alone mod-two boundary ranks are an additional calculation, not a substitute for the acyclic matching proof.

## Relationship to prior work

Adamaszek and Adams (2021), Theorem 1, classify graph-metric scale-two Rips complexes of hypercubes, which are different metric graphs. Feng and Nukala (2023), Theorems 11--16, address specific symmetric-difference finite-subset metrics, again not the graph metric on the Franklin graph. A recorded hexagon-packing result for scale-two Rips complexes requires graph girth at least six, whereas the Franklin graph has girth four. A recorded classification of five asymmetric cubic graphs on twelve vertices excludes the Franklin graph, which has an automorphism group of order \(48\). Matching-complex results for Franklin concern simplices made from graph edges rather than the vertex-based complexes here.

The distance-three graph is isomorphic to Franklin itself, so the claim also provides a homotopy type for its ordinary independence complex; this equivalence was searched explicitly rather than presumed novel. The literature and searchable records consulted did not imply either the four-two-sphere homotopy type or its rational automorphism character, but incomplete indexing remains a risk.

## Limitations

The proof concerns this exact twelve-vertex graph with its combinatorial vertex metric. No general classification of crossed prisms or cubic graphs is proved. The module decomposition is over \(\mathbb Q\), not a splitting of an integral automorphism lattice. No canonical \(G\)-equivariant CW wedge equivalence is asserted. An independently discovered unindexed equivalent statement cannot be excluded.

## References

1. M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040, first public version 2021-03-01, Theorem 1, https://arxiv.org/html/2103.01040v3 .
2. Z. Feng and N. C. P. Nukala, *On Vietoris--Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664, first public version 2023-02-28, Theorems 11--16, https://arxiv.org/html/2302.14664v3 .
3. *Franklin graph*, reference descriptions of the named graph and standard LCF presentation, https://mathworld.wolfram.com/FranklinGraph.html and https://en.wikipedia.org/wiki/LCF_notation .
4. Relevant indexed records: `2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb`; `2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtrations-of-the-five-asym--417fbc0c618b`; and `2026/10/11/SCOPE-edge-orbit-matching-complex-splitting-for-the-franklin-graph--be4888fadcca` (identified as non-covering by differing hypotheses or complexes).
