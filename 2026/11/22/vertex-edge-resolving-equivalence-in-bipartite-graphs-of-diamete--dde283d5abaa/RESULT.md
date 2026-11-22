# Vertex–edge resolving equivalence in bipartite graphs of diameter three

## Finding

Let \(G\) be any finite, connected, simple bipartite graph with at least three vertices and diameter at most three. For distinct vertices \(u,v\), define the vertex-separation set
\[
D_V(u,v)=\{s\in V(G):d(s,u)\ne d(s,v)\}.
\]
For distinct edges \(e,f\), define
\[
D_E(e,f)=\{s\in V(G):d(s,e)\ne d(s,f)\},\qquad d(s,xy)=\min\{d(s,x),d(s,y)\}.
\]
For every selection \(S\subseteq V(G)\) and every positive integer \(k\), the following are equivalent:

1. \(|S\cap D_V(u,v)|\ge k\) for every pair of distinct vertices;
2. \(|S\cap D_E(e,f)|\ge k\) for every pair of distinct edges.

Moreover, for every nonnegative weight vector \(w=(w_s)_{s\in V(G)}\), the conditions \(\sum_{s\in D_V(u,v)}w_s\ge1\) for all vertex pairs and \(\sum_{s\in D_E(e,f)}w_s\ge1\) for all edge pairs are equivalent. Thus the ordinary vertex- and edge-resolving families, their generating polynomials, all \(k\)-resolving families, and their fractional resolving feasible polyhedra are identical. In particular \(\operatorname{dim}(G)=\operatorname{edim}(G)\) and their fractional analogues agree, with exactly the same minimizers.

The graph obtained by attaching one pendant vertex to a six-cycle has diameter four and admits an edge-resolving two-vertex set that is not vertex-resolving; hence the universal diameter bound cannot be increased to four.

## Assumptions and scope

Graphs are finite, connected, simple, undirected and bipartite. Distance is ordinary unweighted shortest-path distance. A vertex landmark measures distance to vertices; an edge landmark measures the minimum distance to either endpoint. A \(k\)-resolving set requires at least \(k\) landmarks distinguishing **each pair**, not the unrelated convention in which \(k\) counts induced edges within a resolving set. No assertion is made for graphs on only two vertices, where edge resolution is vacuous, nor for arbitrary graphs of diameter four. Nonnegative fractional landmark weights may additionally be bounded above by one without changing equivalence of the feasible regions.

## Proof

Write the bipartition as \(A\sqcup B\). Distinct vertices on the same shore have distance exactly two, since their distance is even, positive and at most three. Consequently they have a common neighbor. Every pair on opposite shores has distances of opposite parity from any landmark, and hence is distinguished by **every** vertex. Because \(|V(G)|\ge3\), at least one shore contains a pair; thus every same-shore separation requirement also implies any opposite-shore separation requirement with the same threshold, whether for sets or nonnegative weights.

**First separation-mask lemma.** If \(u,v\) are distinct vertices on the same shore and \(w\) is a common neighbor, then
\[
\boxed{D_V(u,v)=D_E(uw,vw).}
\]
Indeed, for a sensor \(s\) on the same shore as \(u,v\), vertex distances to the two endpoints are zero if \(s\) is that endpoint and two otherwise. The corresponding distances to incident edges are zero for the endpoint itself; for every other same-shore sensor both edges have the identical distance \(\min\{2,d(s,w)\}\). For \(s\) on the opposite shore, \(d(s,u),d(s,v)\) each lie in \(\{1,3\}\). If \(s=w\), both edge distances vanish and both vertex distances equal one. Otherwise \(d(s,w)=2\), so each edge distance is one if \(s\) is adjacent to its other endpoint, and two if it is not. Thus unequal vertex distances correspond exactly to unequal edge distances for every sensor.

**Second separation-mask lemma.** Given two distinct edges \(e=ab\) and \(f=a'b'\), with \(a,a'\in A\), \(b,b'\in B\), there exist two distinct vertices \(x,y\) in the same shore with
\[
\boxed{D_V(x,y)\subseteq D_E(e,f).}
\]
If \(b=b'\), then \(a\ne a'\), and the first lemma gives equality with \((x,y)=(a,a')\). If \(b\ne b'\), choose \((x,y)=(b,b')\). A sensor in \(B\) distinguishes \(b,b'\) only when it equals one of them; it then has distance zero to the edge containing it and positive distance to the other edge. A sensor \(s\in A\) distinguishes \(b,b'\) precisely when it is adjacent to one but not the other, as the two respective distances are one and three. The edge incident to its adjacent vertex then has distance zero or one from \(s\), whereas the other edge has distance two: it cannot share an endpoint with \(s\), since its opposite-shore endpoint is nonadjacent to \(s\). This gives the asserted inclusion.

Every same-shore vertex-pair inequality is therefore **exactly** some edge-pair inequality by the first lemma. Conversely every edge-pair inequality is implied by a same-shore vertex-pair inequality using the second lemma and nonnegativity. Opposite-shore vertex-pair inequalities are redundant, as noted initially. This is an equality of nonnegative separation-constraint systems, simultaneously for integer landmark counts at every positive threshold and for nonnegative fractional weights with threshold one. Every stated equality of optimizers and enumerators follows immediately.

**Sharpness.** Label the vertices of a six-cycle consecutively \(0,4,2,3,1,5,0\) and add the pendant edge \(0,6\). The resulting connected bipartite graph has diameter four. The landmark set \(S=\{4,5\}\) distinguishes its seven edges: for the edges \(04,05,06,13,15,23,24\), the respective ordered edge-distance signatures are \((0,1),(1,0),(1,1),(2,1),(2,0),(1,2),(0,2)\), all different. However, vertices \(3\) and \(6\) both have vertex-distance signature \((2,2)\), so \(S\) is not vertex-resolving. The diameter-three restriction is therefore sharp for this universal all-sets claim.

## Verification

Run `python3 artifacts/verify.py` with Python 3 and its standard library. The checker constructs all connected labelled bipartite graphs of diameter at most three in bipartition sizes \((2,2),(2,3),(3,3),(3,4),(4,4)\), for a total of 8,701 graphs. By shortest-path distances it checks the two mask lemmas for every eligible vertex pair and edge pair. It separately builds the stated seven-vertex diameter-four counterexample and checks all its relevant signatures. Observed output:

```
PASS: 8701 connected labelled bipartite graphs of diameter <=3,
      all same-shore separator equalities and edge-mask inclusions
PASS: diameter-four sharpness witness C6 with pendant leaf
```

These finite experiments support, but do not replace, the unrestricted argument above. The counterexample is directly checkable from the displayed edge list.

## Relationship to prior work

Kelenc, Tratnik and Yero introduced edge metric dimension (arXiv:1602.00291v1, publicly submitted 31 January 2016) and proved scalar dimension equalities on families including complete bipartite graphs. Their examined article does not state the present equality of all vertex- and edge-separation constraint systems across every connected bipartite graph of diameter at most three, nor its fractional and multi-separation implications. Bailey's work on incidence graphs (arXiv:1707.02899) treats vertex metric dimension for finite designs and supplies a natural family to which the theorem applies; it does not supply the edge-constraint equivalence. The published crown-graph edge-basis classification and the complete ordinary resolving polynomial of matching-deleted bicliques yield specialized calculations; the new theorem transfers such results between vertex and edge settings whenever the diameter hypothesis holds. The examined Pappus-graph edge census exhibits a bipartite graph of diameter four with more edge bases than vertex bases, a related boundary phenomenon independent of the present seven-vertex witness. A 2023 paper on metric dimension of bipartite graphs addresses projections and ordinary vertex resolution, not the universal vertex-to-edge transfer. These comparisons are by implications of actual mathematical claims rather than by titles alone.

## Limitations

The argument yields no closed formula for the common dimension or resolving polynomial for a particular graph without additional structural information; it transfers **all** such information across the two definitions. The diameter-four example disproves an unrestricted extension of the all-sets equality, not every possible scalar equality for diameter-four graphs. Bibliographic novelty remains provisional given possible equivalent results under unsearched terminology or in inaccessible older material. No independent mathematical audit has been carried out.

## References

1. A. Kelenc, N. Tratnik and I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291v1, 2016-01-31. https://arxiv.org/abs/1602.00291
2. R. F. Bailey, *On the metric dimension of incidence graphs*, arXiv:1707.02899, 2017. https://arxiv.org/abs/1707.02899
3. *On the metric dimension of bipartite graphs*, 2023, DOI:10.1080/09728600.2023.2223248. https://doi.org/10.1080/09728600.2023.2223248
4. *Edge metric bases of crown graphs*, research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-edge-metric-bases-of-crown-graphs--b5b3c45f23e8
5. *Resolving polynomials and the upper dimension transition in matching-deleted bicliques*, research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-resolving-polynomials-and-the-upper-dimension-transition-in-matc--01c06d3fb257
6. *Geometric edge-metric bases and the complete edge-resolving polynomial of the Pappus graph*, research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-geometric-edge-metric-bases-and-the-complete-edge-resolving-poly--4aa71f8104c8
