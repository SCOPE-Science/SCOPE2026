# Dual shattering of maximal cliques and maximal independent sets in the Shrikhande–rook pair

## Finding
Let \(R=K_4\square K_4\) be the rook graph and \(S\) the Shrikhande graph, with vertex set \(V=(\mathbb Z/4\mathbb Z)^2\). For any graph \(G\), let \(\mathcal I(G)\) denote the family of **inclusion-maximal independent sets**, and \(\mathcal K(G)\) the family of **inclusion-maximal cliques**. A query support \(A\subseteq V\) is shattered by \(\mathcal F\) when \(\{F\cap A:F\in\mathcal F\}=2^A\). Write \(\Delta_{\mathcal F}\) for all such supports and \(\Phi_{\mathcal F}(z)=\sum_{A\in\Delta_{\mathcal F}}z^{|A|}\).

The complete dual classification is
\[
\Delta_{\mathcal I(R)}=\{A:A\text{ is independent in }R,\ |A|\le3\},\qquad
\Delta_{\mathcal I(S)}=\{A:A\text{ is independent in }S,\ |A|\le3\},
\]
\[
\Delta_{\mathcal K(R)}=\{A:A\text{ is a clique in }R,\ |A|\le2\},\qquad
\Delta_{\mathcal K(S)}=\{A:A\text{ is a clique in }S\}.
\]
Consequently, the maximal-independent-set shattering polynomials **coincide**:
\[
\boxed{\Phi_{\mathcal I(R)}(z)=\Phi_{\mathcal I(S)}(z)=1+16z+72z^2+96z^3.}
\]
Both independent-set shattering complexes are pure two-dimensional complexes with \(\widetilde H_2(-;\mathbb F_2)\cong\mathbb F_2^{39}\) and no other reduced homology. But their maximal-clique shattering complexes separate:
\[
\boxed{\Phi_{\mathcal K(R)}(z)=1+16z+48z^2,\qquad
\Phi_{\mathcal K(S)}(z)=1+16z+48z^2+32z^3.}
\]
The first has the homotopy type \(\bigvee^{33}S^1\); the second is homeomorphic to a two-torus \(S^1\times S^1\). In particular, \(\operatorname{VCdim}\mathcal I(R)=\operatorname{VCdim}\mathcal I(S)=3\), whereas \(\operatorname{VCdim}\mathcal K(R)=2\) and \(\operatorname{VCdim}\mathcal K(S)=3\).

## Assumptions and scope
All graphs are finite, simple and loopless. Label \((r,c)\in V\) by \(4r+c\), using representatives \(0,1,2,3\). Distinct \((r,c),(s,t)\) are adjacent in \(R\) exactly when \(r=s\) or \(c=t\). They are adjacent in \(S\) exactly when the difference modulo four belongs to
\[
D=\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}.
\]
The two concept families consist of all inclusion-maximal sets, not merely maximum-cardinality independent sets/cliques or the closed neighborhoods. The homology statements use coefficients in \(\mathbb F_2\); the torus/circle-wedge claims are homotopy or homeomorphism statements, respectively. No assertion covers an arbitrary strongly regular graph.

## Proof
**1. Finite graph presentations and complete concept lists.** For every pair of vertices, determine adjacency by the displayed rules. Each graph has sixteen vertices and forty-eight edges, every vertex has degree six, and every distinct pair of vertices has exactly two common neighbors. An independent subset \(T\) is inclusion-maximal precisely when it is independent and \(\bigcup_{v\in T}N_G[v]=V\). Enumerating the integer masks \(0\le t<2^{16}\) with these two tests gives exactly twenty-four maximal independent sets for \(R\) and forty-eight for \(S\). Apply the same algorithm to \(\overline G\) to obtain all inclusion-maximal cliques: eight for \(R\), thirty-two for \(S\). These two explicit finite loops are independently reproduced by `check_cpp.cpp`; `check_python.py` recovers the concept sets with an independent maximal-clique enumeration algorithm.

**2. Complete Boolean trace certificate.** For a support \(A=\{a_1,\ldots,a_k\}\), encode \(F\cap A\) as \(\sum_{j=1}^k2^{j-1}\mathbf1_{a_j\in F}\). The support is shattered if and only if exactly \(2^k\) distinct codes occur among all concepts. Enumerate each of the \(2^{16}\) supports of size at most four against all concepts. The integer certificate in `check_cpp.cpp` checks for every such support not just face counts but equality of the resulting support collection with each asserted structural description. Specifically, the maximal-independent-set collections shatter exactly the independent supports with cardinality at most three. Every such graph has sixteen independent singleton supports, \(\binom{16}{2}-48=72\) independent pairs, and exactly ninety-six independent triples. Independent four-sets are never shattered. Rook maximal cliques shatter all vertices and all forty-eight edges, but no triples; Shrikhande maximal cliques shatter all vertices, edges and thirty-two triangles, but no four-element support. All supports outside these graph-theoretic classes fail the all-positive trace condition, since a clique/independent concept cannot contain a non-clique/non-independent support. In the finite graphs here no support of size four is shattered; hence no larger support is shattered, by the hereditary property of shattering. This establishes both displayed exact classifications, with exhaustive proof certificates rather than extrapolation from samples.

**3. Independent shattering homology.** In each common independence-query shattering complex the reduced boundary ranks over \(\mathbb F_2\) are \(\operatorname{rank}\partial_1=15\) and \(\operatorname{rank}\partial_2=57\), obtained by exact binary pivot reduction of the incidence columns of all faces. With \(16\) vertices, \(72\) edges and \(96\) triangles, this gives
\[
\widetilde\beta_1=(72-15)-57=0,\qquad
\widetilde\beta_2=96-57=39.
\]
The same boundary calculations prove there are no other reduced Betti numbers. Both complexes are pure, because each independent singleton or pair extends to a shattered independent triple; the assertions on all faces are checked in the complete certificate.

**4. Clique shattering topology.** In the rook graph, the shattered supports are the vertices and edges of the connected one-dimensional rook graph. Thus its realization is a connected graph of cycle rank \(48-16+1=33\), homotopy equivalent to a wedge of thirty-three circles.

In the Shrikhande graph, the thirty-two shattered triangles are exactly
\[
\{(r,c),(r+1,c),(r+1,c+1)\},\qquad
\{(r,c),(r,c+1),(r+1,c+1)\},
\]
for every \((r,c)\in(\mathbb Z/4\mathbb Z)^2\), with indices read modulo four. These are the two triangles in each diagonalized square of the periodic four-by-four grid; `check_cpp.cpp` verifies their equality to the entire shattered triangle set, and no higher-dimensional face occurs. The geometric realization of this periodic triangulation is the ordinary quotient of the plane by translations through four units in either coordinate, hence a two-torus. An exact independent binary boundary calculation additionally yields ranks \(15\) and \(31\) in dimensions one and two, giving \((\widetilde\beta_1,\widetilde\beta_2)=(2,1)\) as expected.

## Verification
Compile and run the standard C++17 program from the same directory: `g++ -O2 -std=c++17 check_cpp.cpp -o check_cpp && ./check_cpp`. Its terminal marker is `SHRIKHANDE_ROOK_DUAL_SHATTER_PASS`. It generates all sixty-five-thousand-five-hundred-thirty-six labeled supports, enumerates independent dominating sets and maximal cliques directly, compares the complete face sets and their characteristic tests, computes the exact binary boundary ranks and verifies the thirty-two toroidal triangles.

An independently implemented program uses `networkx` maximal-clique enumeration, the complement graph, Boolean trace sets and a separate binary-rank routine: `python3 check_python.py`. Its terminal marker is `INDEPENDENT_GRAPH_CLIQUE_SHATTER_PASS`. Both programs were executed on files extracted from the delivered package. Their finite exhaustive loops cover every support (large supports excluded using downward-closure after all size-four supports have failed), not random observations. No theorem for larger graphs is inferred.

## Relationship to prior work
The two strongly regular graph presentations and the distinction between their ordinary clique complexes are classical. Bodnar and coauthors (2021) explicitly use the pair in topological graph-learning examples; therefore the toroidal Shrikhande triangulation is **not claimed as a new discovery**. Existing full-result comparisons of the two ordinary *independence* complexes prove different homotopy types (respectively wedges of twenty-three and fifteen two-spheres); those results concern every independent face, whereas the present maximal-independent-*membership shattering* systems agree in their entire face enumerators and reduced mod-two homology. Ordinary independence homology and known face counts can imply some low-dimensional truncated homology, so the rank thirty-nine alone is not an asserted priority claim. The novel candidate is the combined exact four-family Boolean trace classification and its opposing equivalence/separation phenomena.

Coudert–Csikós–Ducoffe–Viennot study graph VC dimension through **closed-neighborhood** concepts; these sixteen-element graph-neighborhood families are distinct from the eight, twenty-four, thirty-two and forty-eight concepts used here. A related published finite computation of neighborhood shattering for the Shrikhande–rook pair distinguishes closed-neighborhood triple coefficients, but it does not determine maximal-set membership traces. Classical graph-theoretic triangle and independent-face counts by themselves do not imply that every eligible support has *all* Boolean traces, nor the failure for four-point independent supports and rook triangles.

## Limitations
The result is finite and concerns only these two explicitly specified graphs, with a computationally exhaustive proof of the novel shattering classifications. It does not claim an all-graph theorem, a new topological identification of the classical toroidal clique complex, or a new computation of the ordinary independence complexes. Priority is uncertain for any equivalent maximal-clique or maximal-independent-set Boolean trace enumerations hidden under other terminology or unpublished tables. Independent human review has not been performed.

## References
1. C. Bodnar et al., *Weisfeiler and Lehman Go Topological: Message Passing Simplicial Networks*, arXiv:2103.03212v1, public March 4, 2021, https://arxiv.org/abs/2103.03212.
2. D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1, May 13, 2024, https://arxiv.org/abs/2405.07588.
3. S. Shrikhande, R. Pawale and P. Yadav, *Designs over regular graphs with least eigenvalue −2*, 2021, https://doi.org/10.1007/s10801-021-01036-8.
4. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187.
5. *A closed-neighborhood shattering-polynomial separation of the Shrikhande and rook graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-closed-neighborhood-shattering-polynomial-separation-of-the-sh--670b6697d463.
