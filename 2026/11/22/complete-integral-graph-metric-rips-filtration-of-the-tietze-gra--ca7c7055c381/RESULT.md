# Complete integral graph-metric Rips filtration of the Tietze graph

## Finding

Let \(T\) be the twelve-vertex, eighteen-edge Tietze cubic graph, with the shortest-path distance on its vertices. Write \(\operatorname{VR}(T;r)\) for the *inclusive* Vietoris–Rips complex whose simplices are vertex subsets of diameter at most \(r\). For all real \(r\geq0\),

\[
\operatorname{VR}(T;r)\simeq
\begin{cases}
\bigvee^{11} S^0, & 0\leq r<1,\\
\bigvee^{6} S^1, & 1\leq r<2,\\
\bigvee^{4} S^2, & 2\leq r<3,\\
*, & r\geq3.
\end{cases}
\]

The full reduced *integral* persistent-homology barcode therefore consists of eleven degree-zero intervals \([0,1)\), six degree-one intervals \([1,2)\), and four degree-two intervals \([2,3)\); no other intervals occur. The homotopy claims, particularly at radius two, are integral statements, not consequences inferred from a finite-field Betti calculation.

## Assumptions and scope

The graph is fixed up to isomorphism by the following labeled model. Vertices are the integers from zero through eleven, and the undirected edges are

```
(0,1) (0,5) (0,9) (1,2) (1,6) (2,3)
(2,7) (3,8) (3,10) (4,6) (4,7) (4,11)
(5,7) (5,8) (6,8) (9,10) (9,11) (10,11)
```

This is the familiar operation of replacing a Petersen-graph vertex with a triangle: vertices nine, ten and eleven form the unique triangle, each attached to a distinct former neighbor. The graph is connected and three-regular, has graph-theoretic diameter three, and every distance is integral. We use the vertex-set shortest-path metric, *not* the continuum geodesic metric on its geometric realization. Simplices of diameter exactly the threshold are included. Homology is reduced and has coefficients \(\mathbb Z\) unless explicitly noted.

## Proof

**Radius zero and one.** At radius zero there are twelve isolated vertices. At radius one the complex is the graph together with its unique filled triangle. Its filled triangle is a contractible CW subcomplex; quotienting by it is a homotopy equivalence. The quotient is a connected graph with ten vertices and fifteen edges, hence is homotopy equivalent to a wedge of \(15-10+1=6\) circles. Equivalently, the unique two-cell kills one primitive generator of the seven-dimensional first homology of the underlying graph.

**Radius two: complete finite combinatorial certificate.** Encode a nonempty simplex by its twelve-bit vertex mask. The simplices are exactly those masks for which every pair of selected vertices has shortest-path distance at most two. Exhaustive enumeration, reproduced from the graph in the standalone verification code, gives the counts by dimension zero through six

\[
(12,51,96,87,51,19,3),
\]

or 319 nonempty simplices. The supplied `collapse_certificate.json` specifies 119 ordered pairs \((\sigma,\tau)\) of masks. At each step of the specified order, the verifier reconstructs the surviving face set and checks that \(\tau\) is the **unique codimension-one coface** of \(\sigma\), then removes both. This is an elementary simplicial collapse, not merely an abstract Morse matching whose acyclicity has been assumed. After all 119 verified collapses the residual complex has exactly 12 vertices, 38 edges and 31 triangles, and no higher-dimensional simplices.

The certificate also supplies eleven edges forming a spanning tree in the residual one-skeleton. Collapsing that contractible tree gives a homotopy-equivalent CW complex with one zero-cell, 27 one-cells and 31 two-cells. Orient every surviving edge by increasing vertex label, and orient each triangle \((a,b,c)\) with \(a<b<c\) by the boundary walk \((a,b),(b,c),(c,a)\). Edges of the tree become trivial; all other edges are named free-group generators. Accordingly, each triangular attaching loop becomes a word containing at most three signed generators, computed explicitly by the verifier.

The certificate provides an ordered list of 27 one-cell generator labels. For each, the verifier checks that one *remaining* two-cell has attaching word consisting of precisely that one generator or its inverse. This one-cell together with its two-cell forms a contractible subcomplex of the current based CW complex. Contracting the pair is a homotopy equivalence (the pair is a contractible CW subcomplex), and in the other attaching words it simply deletes that generator. After these 27 individually verified reductions, exactly four two-cells remain and **each has empty attaching word**. There are no one-cells. Thus the final based CW model consists of one zero-cell and four two-cells attached by constant maps, which is exactly \(\bigvee^4S^2\). All cell cancellations and their order are witnessed by the accompanying finite certificate rather than postulated from Betti ranks.

**Radius three and larger.** Since the graph diameter is three, every subset of vertices has diameter at most three, so the complex is the full eleven-simplex and is contractible at every radius at least three.

**Persistence.** Every distinct filtration stage is separated by an integer distance. The radius-zero to radius-one inclusion merges all twelve connected components, producing eleven finite reduced degree-zero intervals. The radius-one to radius-two map is zero on first homology because the latter vanishes; the rank-six circle module therefore dies at radius two. The radius-two four-dimensional free second-homology module dies at radius three because the latter complex is contractible. Since there are no other nontrivial homology groups at any stage, the stated integral barcode is complete. There are no extension or torsion ambiguities because the homotopy types are integral sphere wedges.

## Verification

Run the standalone script and witness in the same directory with

```sh
python3 verify_tietze.py collapse_certificate.json
```

Only the Python standard library is used. The verifier does not accept precomputed face sets, boundary matrices or homology values as evidence: it recomputes distances from the explicit graph and enumerates all faces. It checks all 119 elementary simplicial collapse pairs against the current face poset, all eleven spanning-tree edges, and all 27 generator–relation cancellations. It separately computes mod-two boundary ranks for radii one and two as a cross-check, but this finite-field test is not substituted for the integral homotopy proof. The verifier output is included in `verification_output.txt`, and the exact certificate is included in `collapse_certificate.json`.

## Relationship to prior work

M. Adamaszek and H. Adams (first publicly posted March 1, 2021, arXiv:2103.01040) investigate Vietoris–Rips complexes of graph vertices in their shortest-path metric and prove a radius-two sphere-wedge result for **hypercube graphs**. That family is bipartite with a different metric and is not the nonbipartite Tietze graph. The present result follows the same natural finite-graph metric filtration question for a canonical, smallest almost-Hamiltonian cubic graph with a triangle, and determines *all* its scales rather than extracting only finite-field Betti numbers.

Adamaszek's earlier *Clique complexes and graph powers* (arXiv:1104.0433, 2011) identifies graph-power clique complexes with graph-metric Rips complexes and proves several general stability criteria, including a girth-at-least-seven criterion at radius two. The Tietze graph has girth three, so that theorem does not determine its radius-two homotopy. The paper classifies powers of cycles, not this graph. Additional inspected hypercube work by Shukla and by Adams–Virk likewise studies other graph families.

The ordinary independence, ordinary matching and perfect-matching complexes of the Tietze graph appearing in published research records have different face definitions: their known homotopy groups and symmetry characters do **not** imply the result for the graph-power clique complex. For context, contracting the Tietze triangle back to one vertex recovers the Petersen graph, whose shortest-path diameter is two; its radius-two Rips complex is therefore a simplex, unlike the four-sphere wedge found here. This contrast motivates studying the structural effect of the triangle expansion; it is not a general vertex-expansion theorem.

## Limitations

The computation and homotopy classification concern this *single labeled finite graph* up to graph isomorphism. They do not classify all cubic graphs, all single-vertex triangle expansions, or any continuum geodesic version of the graph. Neither automorphism representations nor higher refinements of persistent homotopy are asserted. Bibliographic searches and inspections cannot exclude every unindexed equivalent calculation. The classification is exact because the finite face poset and each allowed homotopy-preserving cancellation are checked exhaustively.

## References

1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first posted 2021-03-01). https://arxiv.org/abs/2103.01040
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011). https://arxiv.org/abs/1104.0433
3. S. Shukla, *On Vietoris–Rips complexes (with scale 3) of hypercube graphs*, arXiv:2202.02756 (2022). https://arxiv.org/abs/2202.02756
4. H. Adams and Ž. Virk, *Lower bounds on the homology of Vietoris–Rips complexes of hypercube graphs*, arXiv:2309.06222 (2023). https://arxiv.org/abs/2309.06222
5. *Tietze Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/TietzeGraph.html (graph identification and standard parameters).
