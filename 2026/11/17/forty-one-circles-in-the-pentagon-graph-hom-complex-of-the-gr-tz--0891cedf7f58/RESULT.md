# Forty-one circles in the pentagon graph-Hom complex of the Grötzsch graph

## Finding
Let \(C_5\) be the simple five-cycle and let \(\mu(C_5)\) be its eleven-vertex Mycielskian (the Grötzsch graph). The standard regular polyhedral Hom complex satisfies
\[
\operatorname{Hom}(C_5,\mu(C_5))\simeq\bigvee^{41}S^1.
\]
More strongly, the complex has exactly 310 vertices, 500 one-cells and 150 square two-cells, and admits a sequence of 150 elementary polyhedral collapses to a connected graph with 310 vertices and 350 edges. Consequently its integral fundamental group is free of rank 41 and \(H_1\cong\mathbb Z^{41}\), with no higher positive-degree homology.

## Assumptions and scope
All graphs are finite, simple, undirected and loopless. Write the target vertices as \(v_i,u_i\), for \(i\in\mathbb Z/5\mathbb Z\), and \(w\). Its edges are \(v_iv_{i+1}\), \(u_iv_{i-1}\), \(u_iv_{i+1}\) and \(u_iw\), for all cyclic indices. This graph has 11 vertices, 20 edges, no triangles and contains the four-cycle \(v_0u_1wu_4v_0\). The source has the edges \(i(i+1)\) for the five cyclic indices.

A cell of the polyhedral graph-Hom complex is a tuple of nonempty sets \((A_0,\ldots,A_4)\), each \(A_i\subseteq V(\mu(C_5))\), with \(A_i\times A_{i+1}\subseteq E(\mu(C_5))\) for all cyclic indices. Its cell is the product \(\prod_i\Delta(A_i)\), of dimension \(\sum_i(|A_i|-1)\). Elementary polyhedral collapses remove an open maximal cell and a unique free codimension-one face; they preserve homotopy type. This is the standard non-looped graph-Hom convention.

## Proof
First enumerate all singleton assignments \((\{x_0\},\ldots,\{x_4\})\) with \(x_ix_{i+1}\) an edge of the target for every cyclic index. The standalone verifier computes this independently as length-five closed walks in the 11-vertex adjacency matrix and confirms 310 choices.

The full face poset can be enumerated without missing cells: starting at every singleton assignment, repeatedly add one target vertex to one coordinate, retaining exactly those resulting tuples for which all five cross-coordinate edge conditions hold. Every valid multi-homomorphism contains a singleton assignment and can be reached by adding its other coordinate elements one at a time, because the required edge conditions are hereditary under taking subsets. Therefore this enumeration is exhaustive, not a truncation. It produces 960 cells of dimension at most two: 310 zero-cells, 500 one-cells, and 150 two-cells. Each two-cell is a product of exactly two intervals and has four codimension-one edges.

The companion `collapse_pairs.json` specifies an ordered list of 150 pairs, each comprising one one-cell and one two-cell, encoded by the five integer bitmasks of their coordinate sets. `verify_hom.py` reconstructs the entire face poset from the target adjacency rule and, for every pair in order, independently verifies (i) both cells remain, (ii) the edge is a codimension-one face of the proposed square, and (iii) among all remaining squares it is incident to that square alone. Thus each pair is a legal elementary free-face collapse. After all 150 pairs no two-cells remain and there are precisely 350 one-cells.

For each remaining one-cell the verifier computes both distinct singleton endpoints, constructs the residual adjacency graph and traverses it completely. All 310 vertices are visited: the collapsed graph is connected. A connected finite graph with 310 vertices and 350 edges has a spanning tree of 309 edges and is homotopy equivalent to a wedge of \(350-309=41\) circles. The sequence of legal collapses proves the claimed homotopy equivalence, including its integral fundamental group and homology assertions.

## Verification
Run the dependency-free command `python3 verify_hom.py collapse_pairs.json` from a directory containing the two accompanying files. The program checks the target graph, the independent adjacency-walk count, exhaustive multi-homomorphism enumeration, the complete cell vector, all 150 successive free-face claims, and residual graph connectedness. The verified output is provided as `verification_output.txt`; the last line is `STATUS: PASS`. The actual files and complete certificate are supplied with this result; no unproved asymptotic assertion or numerical approximation is used.

## Relationship to prior work
Graph-Hom complexes and their multi-homomorphism description are standard; see Dochtermann and the earlier work of Lovász and Babson–Kozlov. In papers first released on 2024-12-26, Matsushita and, independently, Fujii–Kimura–Nozaki classified graph-Hom components for **square-free** codomains. Those theorems do not directly apply to the specified Grötzsch target because it has a four-cycle. This calculation supplies the exact cell structure, elementary collapse and homotopy type for this natural non-square-free codomain and odd-cycle source; it does not extend their theorems to arbitrary codomains.

## Limitations
Only the indicated graph pair and standard polyhedral graph-Hom model are classified. The computation does not classify other Mycielskian graphs, other source cycles, or equivariant actions on homology. The exhaustive certificate is finite and exact, but potential equivalent unindexed earlier calculations remain a bibliographic limitation.

## References
1. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144 (first public version 2024-12-26), https://arxiv.org/abs/2412.19144.
2. S. Fujii, K. Kimura and Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039 (first public version 2024-12-26), https://arxiv.org/abs/2412.19039.
3. A. Dochtermann, *Hom complexes and homotopy theory in the category of graphs*, European Journal of Combinatorics, https://doi.org/10.1016/j.ejc.2008.04.009.
4. E. Weisstein, *Grötzsch Graph*, MathWorld, https://mathworld.wolfram.com/GroetzschGraph.html.
