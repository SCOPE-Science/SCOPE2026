# Complete graph-metric Vietoris–Rips filtration of the McGee graph

## Finding

Let \(M\) be the twenty-four-vertex McGee cubic graph with unit edge lengths and shortest-path distance \(d\). Its *inclusive* Vietoris–Rips complex at radius \(r\ge0\) is \(K_r=\{\sigma\subseteq V(M):d(x,y)\le r\text{ for all }x,y\in\sigma\}\). The complete integral homotopy filtration is

\[
K_r\simeq\begin{cases}
\text{24 points},&0\le r<1,\\
\bigvee^{13}S^1,&1\le r<3,\\
S^5,&3\le r<4,\\
\ast,&r\ge4.
\end{cases}
\]

The distinctive new structural calculation occurs at radius three: the graph whose edges join vertices at distance exactly four is the disjoint union of six four-cycles. Thus \(K_3\) is *exactly* the independence complex of that disjoint union, a join of six complexes each homotopy equivalent to \(S^0\).

The complete reduced integral persistence module has 23 degree-zero intervals \([0,1)\), 13 degree-one intervals \([1,3)\), and one degree-five interval \([3,4)\), with no others. All stated groups are free abelian.

## Assumptions and scope

The graph is specified independently of an external graph-data package. Vertices are \(i\in\mathbb Z/24\mathbb Z\). Include cycle edges \(\{i,i+1\}\) and chord edges \(\{i,i+s_i\}\), taking all indices modulo 24, where \((s_i)=(-12,7,-7)\) repeated eight times. This is the standard McGee-graph LCF presentation. Distances are unweighted shortest-path distances and threshold inequalities are inclusive; no continuous edge metric is used. Nonempty face counts exclude the empty face. All homotopy types are those of geometric realizations.

## Proof

**Graph distance certificate.** An exhaustive breadth-first search from each vertex, independently corroborated by Floyd–Warshall shortest paths, gives 24 vertices, 36 edges, girth seven, and the common distance histogram \((1,3,6,12,2)\) at distances \(0,1,2,3,4\) from every vertex. Hence the diameter equals four. The code under `mcgee_rips_verifier.py` defines the graph and checks both algorithms, and is short enough to be independently reimplemented from the preceding definition.

**Radii zero and one.** For \(0\le r<1\), no distinct vertices are joined, giving 24 points. For \(1\le r<2\), the clique complex is the original triangle-free connected graph. Its cycle rank is \(36-24+1=13\). Therefore \(K_1\simeq\bigvee^{13}S^1\).

**Radius two, with actual collapse.** The square of this girth-seven graph has 24 vertices, 108 edges, 96 triangles, and 24 tetrahedra. For each original vertex \(v\) with three neighbors \(a,b,c\), first collapse its tetrahedron \(\{v,a,b,c\}\) against its opposite triangle \(\{a,b,c\}\). Then, for each of the three unordered pairs \(\{a,b\}\) of neighbors of \(v\), collapse the triangle \(\{v,a,b\}\) against its distance-two edge \(\{a,b\}\). In the vertex order 0 through 23 this is precisely 96 elementary simplicial collapses. The supplied checker tests each pair is free *at the moment of deletion* against all extant cofaces and confirms that the remaining complex is exactly the original graph. Thus \(K_2\searrow K_1\), preserving the 13 first-homology classes under inclusion. This part also follows from the girth-stability proposition in Adamaszek [2] and is not presented as new.

**Radius three, with the crucial graph decomposition.** Since the diameter is four, two distinct vertices fail to span an edge of the Rips complex \(K_3\) precisely when they lie at graph distance four. Define the distance-four graph \(F\) on the same 24 vertices, with \(uv\in E(F)\) if and only if \(d(u,v)=4\). The exhaustive distance certificate proves that every vertex has precisely two distance-four partners, and that its connected components, as vertex sets, are

\[
\begin{aligned}
&\{0,6,12,18\},\quad\{1,5,13,17\},\quad\{2,10,14,22\},\\
&\{3,9,15,21\},\quad\{4,8,16,20\},\quad\{7,11,19,23\}.
\end{aligned}
\]

Each component is a connected simple two-regular graph on four vertices, hence a four-cycle. Therefore \(F\cong\bigsqcup_{j=1}^{6}C_4\), and from the *exact* face condition one obtains the simplicial identity

\[
K_3=\operatorname{Ind}(F)
=\operatorname{Ind}(C_4)^{*6}.
\]

The independence complex of a four-cycle consists of two disjoint edges, so is homotopy equivalent to \(S^0\). Joins preserve homotopy equivalences of nonempty CW complexes, and the six-fold join \((S^0)^{*6}\) is the boundary of a six-dimensional cross-polytope, homeomorphic to \(S^5\). This proves \(K_3\simeq S^5\) integrally, without relying on mod-two Betti numbers. As a separate combinatorial cross-check, the number of radius-three faces of each cardinality is given by the nonconstant coefficients of \((1+4t+2t^2)^6\), totaling 117,648 nonempty faces; the program enumerates and checks every one.

**Radius four and persistence.** For \(r\ge4\), all vertex pairs have distance at most four, so \(K_r\) is a 23-simplex. The radius-one-to-two inclusion is a homotopy equivalence by the explicit collapses. The radius-three stage has no reduced homology in degrees zero or one, and the radius-four stage is contractible. The only fifth homology class is born at three and dies at four. Thus the reduced integral barcode is exactly as claimed. No extension or torsion ambiguity is possible, since the groups in the displayed spaces are free and in distinct positive degrees.

## Verification

Run `python3 mcgee_rips_verifier.py` using the standard library. The checker constructs the graph from the stated 24-term LCF sequence; compares independent all-pairs distance implementations; checks cubicity, girth, common distance histogram, diameter, the exact radius-two face set and its 96 free-face deletions; verifies six four-cycle components in the distance-four graph; and independently enumerates all 117,648 radius-three faces against the join face polynomial. The embedded `mcgee_rips_verifier_output.txt` is the recorded output from this exact program. Reproducibility uses no externally downloaded data or packages.

## Relationship to prior work

McGee's original paper introduced the graph [1]. Adamaszek [2, Proposition 2.2] proves a general collapse theorem for \(\operatorname{Cl}(G^r)\) when the girth is at least \(3r+1\); it supplies the radius-two result for this girth-seven graph but does **not** cover radius three, which would require girth at least ten. The circle-power computations in [2] do not apply to this graph. A reported same-graph calculation of \(\operatorname{Ind}(M)\simeq S^5\) concerns the ordinary independence complex of the original graph, not \(\operatorname{Ind}(F)\) for the distance-four graph \(F\); agreement in dimension is not a covering implication. Similar Rips calculations for the 24-vertex Nauru graph concern a different metric graph. This note claims the exact distance-four decomposition, scale-three homotopy type, and consequent completion of this particular filtration; it does not claim novelty for the already established general girth collapse or the graph definition.

## Limitations

The classification concerns the finite McGee graph with shortest-path vertex metric, not a continuous metric graph, perturbations of edge lengths, or all cubic cages. The geometric identification is a homotopy equivalence, not an assertion of equivariant or simplicial equivalence to a sphere. The radius-three computation is exhaustive for 24 vertices; it is not a general theorem about all girth-seven graphs. The bibliography and indexed comparisons are not a proof that no equivalent unindexed or inaccessible published argument exists. No independent mathematical audit has been performed.

## References

[1] W. F. McGee, *A Minimal Cubic Graph of Girth Seven*, Canadian Mathematical Bulletin 3 (1960), DOI: 10.4153/CMB-1960-018-1. Historic publication year, not a claimed precise first-online date.

[2] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, initial public posting 2011-04-03, especially Proposition 2.2 and Section 6.

[3] *McGee Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/McGeeGraph.html (LCF presentation and basic graph invariants).
