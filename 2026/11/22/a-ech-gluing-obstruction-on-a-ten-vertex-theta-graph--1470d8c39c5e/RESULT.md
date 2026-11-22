# A Čech-gluing obstruction on a ten-vertex theta graph

## Finding
Let \(G=\Theta_{3,4,4}\) be the theta graph formed from three internally disjoint paths of edge lengths three, four and four between fixed poles. At Čech scale \(r=4\), its **vertex-centered intrinsic Čech nerve** has reduced mod-two homology
\[
\widetilde H_j(\mathcal N(G,4);\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^2,&j=2,3,\\
0,&\text{otherwise}.
\end{cases}
\]
The union of the intrinsic scale-four Čech nerves of the two seven-cycles sharing the three-edge path is a subcomplex but has reduced mod-two homology only \(\mathbb F_2^2\) in degree three, and zero in every other degree. Consequently its natural inclusion into the full graph's Čech nerve is not a homotopy equivalence. This is a concrete obstruction to extending naïve wedge-type Čech gluing to overlaps longer than a single short path.

## Assumptions and scope
The graph has vertices \(V=\{0,1,\ldots,9\}\), with unit-length undirected edges
\[
\begin{split}
E={}&\{(0,1),(1,2),(2,3),\\
&(3,4),(4,5),(5,6),(6,0),\\
&(3,7),(7,8),(8,9),(9,0)\}.
\end{split}
\]
Thus \(G\) has ten vertices and eleven edges. Each Čech vertex represents a graph vertex. A finite nonempty subset \(\sigma\subset V\) is a face of \(\mathcal N(G,4)\) exactly when the closed balls of metric-graph radius \(2\) centered at its members have a common point in the geometric realization of \(G\). Witnesses may lie in edge interiors; the construction does not restrict witnesses to graph vertices. The coefficient field is \(\mathbb F_2\); no assertion of integral homology or homotopy decomposition is made.

The two constituent seven-cycles have ordered vertices \((0,1,2,3,4,5,6)\) and \((0,1,2,3,7,8,9)\). Their intrinsic Čech nerves are calculated with their own shortest-path metrics and then included on their original vertex labels.

## Proof
For each vertex \(v\), let \(d_v(w)\) be the minimum number of graph edges from \(v\) to \(w\). A graph vertex \(w\) witnesses precisely the face containing all \(v\) with \(d_v(w)\le 2\). For an interior point at fractional position \(0<t<1\) on an edge \((a,b)\),
\[
d_v(t)=\min\{d_v(a)+t,\ d_v(b)+1-t\}.
\]
Since all endpoint distances are integers, at radius two its face is independent of \(t\) throughout the open edge, and consists of all vertices satisfying \(d_v(a)\le1\) **or** \(d_v(b)\le1\). A midpoint therefore represents every possible interior-edge witness set. Enumerating ten vertex witnesses and eleven edge-midpoint witnesses consequently gives **every face**, including all high-dimensional ones, not merely a subset.

Discarding witness faces contained in larger witness faces leaves exactly ten maximal simplices (written as vertex sets):

```
[0,3,4,5,6]
[0,1,2,3,4,7]
[2,3,4,5,6,7]
[1,2,3,4,5,7,8]
[0,1,2,3,6,9]
[0,1,4,5,6,9]
[0,1,2,5,6,8,9]
[0,3,7,8,9]
[2,3,4,7,8,9]
[0,1,6,7,8,9]
```

Taking all nonempty subfaces produces the complete face vector \((10,45,114,134,74,20,2)\), in dimensions zero through six. Exact bit-matrix reductions of the mod-two simplicial boundary maps \(\partial_i\), in dimensions \(i=1,2,\ldots,6\), give ranks \((9,36,76,56,18,2)\). Therefore
\[
\dim \widetilde H_i=f_i-\operatorname{rank}\partial_i-\operatorname{rank}\partial_{i+1}-[i=0],
\]
where the external boundary ranks are zero. This gives precisely two generators in each of degrees two and three and none elsewhere. Both column and row Gaussian elimination return the same exact ranks.

Constructing the two seven-cycle nerves separately and taking their face union on the same ten vertices produces mod-two homology only in degree three, of rank two. Each face of that union is also a face of the theta graph's Čech nerve, checked directly using the ten maximal facets above. Since the source has vanishing degree-two homology whereas the target has degree-two rank two, their canonical inclusion cannot be a homotopy equivalence.

## Verification
Run `python3 verify.py` using only Python's standard library. It regenerates all eleven graph edges, breadth-first shortest-path distances, vertex and midpoint witnesses, the maximal witness faces, every nonempty face and all six exact mod-two boundary ranks. It also runs an independent transposed-matrix rank reduction and computes the separate two-cycle union's reduced homology. The script asserts the face vector, all boundary ranks, all Betti numbers and the inclusion of the two cycle subcomplexes. The complete computation has only \(399\) nonempty faces.

## Relationship to prior work
Adamaszek et al., *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings* (first publicly submitted December 18, 2017), give sufficient gluing criteria primarily for Vietoris–Rips complexes of graphs along short paths. They do not give this intrinsic Čech homology calculation or imply a Čech wedge decomposition for the present three-edge overlap. The metric-graph Čech nerve and its scale convention follow Adams, Shukla and Singh, *Čech complexes of hypercube graphs* (first publicly submitted December 12, 2022), which investigates hypercube graphs rather than this theta example. The overlap has length three, exceeding one third of either seven-edge constituent loop, so the short-overlap guarantee does not cover this configuration. A nearby published calculation of Vietoris–Rips complexes for four-edge-arm theta graphs concerns a different nerve, graph family and scale; its stated third-dimensional homology does not imply the two Čech groups here.

## Limitations
The result is for one specifically labelled ten-vertex metric graph and one scale, with exact mod-two homology. It is not an infinite theta-family classification, an optimal-size obstruction, a proof of integral torsion-freeness, nor a general impossibility theorem for long-path gluing. Literature searches cannot exclude unindexed equivalent calculations; no independent mathematical audit has been performed.

## References
1. M. Adamaszek et al., *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224, first version December 18, 2017. https://arxiv.org/abs/1712.06224
2. H. Adams, S. Shukla and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first version December 12, 2022. https://arxiv.org/abs/2212.05871
3. *Square-growth third homology and full symmetry of four-edge theta Rips filtrations*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-square-growth-third-homology-and-full-symmetry-of-four-edge-thet--5f57307aa768
