# Sharp stabilization and complete homotopy classification of leaf-symmetry multipath quotients

## Finding

Let \(D_n\), for each integer \(n\ge 1\), be the bidirected complete bipartite digraph on the two hubs \(u,v\) and \(n\) leaves: every hub–leaf edge occurs with both possible orientations. Let \(X_n\) be its multipath complex, whose vertices are directed arcs and whose simplices are collections of arcs forming a disjoint union of directed paths (isolated vertices being allowed). The symmetric group \(\mathfrak S_n\) acts on \(X_n\) by permuting the leaves and fixing the hubs. The **actual geometric orbit space**, not a naïve vertex-orbit complex, has homotopy type

\[
|X_n|/\mathfrak S_n\simeq
\begin{cases}
S^0,&n=1,\\
S^2\vee S^1\vee S^1,&n=2,\\
S^2,&n=3,\\
\{\mathrm{pt}\},&n\ge4.
\end{cases}
\]

For every \(n\ge4\), the orbit spaces have **isomorphic regular CW face posets**, with exactly four vertices, eight edges, eight two-cells and three three-cells, and admit a uniform eleven-pair elementary collapse to a point. Thus \(n=4\) is the exact homotopy-transition and combinatorial-stabilization threshold.

## Assumptions and scope

All graphs are finite. Use four distinct arc colors: \(0\) for \(u\to i\), \(1\) for \(i\to u\), \(2\) for \(v\to i\), and \(3\) for \(i\to v\), for any leaf \(i\). The group \(\mathfrak S_n\) permutes the leaf labels, while leaving every color and each hub fixed. A directed path is simple, so any collection containing a directed cycle is prohibited.

A cell signature \((S,\pi)\) consists of a nonempty subset \(S\subseteq\{0,1,2,3\}\) and a partition \(\pi\) of \(S\) such that (i) every block is a singleton or one of \(\{0,3\},\{1,2\}\); (ii) it is not the two-block partition \(\{\{0,3\},\{1,2\}\}\); and (iii) \(|\pi|\le n\). A signature has dimension \(|S|-1\). The restriction of a signature to \(T\subseteq S\) intersects every block with \(T\), discarding empty intersections. A face is represented by its color set and the equal-leaf equivalence partition on its arcs.

## Proof

**1. Faces and orbit signatures.** Every directed multipath has indegree and outdegree at most one at either hub; hence it contains at most one arc of each of the four colors. Two arcs assigned to the same leaf cannot have the same orientation (both entering or both leaving that leaf), nor be opposite orientations on the same hub–leaf edge (that would form a directed two-cycle). The only permitted double-occupancy leaf blocks are consequently \(\{0,3\}\), producing the path \(u\to i\to v\), and \(\{1,2\}\), producing the path \(v\to i\to u\). Triple occupancy is impossible. The two double blocks together would form a directed four-cycle across the two hubs and are forbidden. Conversely, each partition satisfying the stated restrictions, using at most \(n\) blocks, can be realized with distinct leaves for distinct blocks; it has at most one incoming and outgoing arc at each hub and leaf and no directed cycle. Thus these signatures classify all multipath faces up to leaf relabelling.

The permutation group acts transitively on faces of any given signature. Moreover, a group element stabilizing a face must fix every arc of that face individually, because there is only one arc of each color. Hence the action has **no inversions**, and the geometric quotient inherits a regular CW structure with one open \((|S|-1)\)-cell per signature. Distinct restrictions of a fixed signature to distinct proper color subsets have distinct color sets, so the characteristic maps are embedded and attaching boundaries have exactly the claimed face incidences. In particular, this is genuinely the quotient of the geometric realization; it is not the simplicial complex obtained by forgetting all leaf labels before realization.

**2. Stabilization.** Every admissible signature has at most four blocks. For all \(n\ge4\), condition \(|\pi|\le n\) is automatic. The identical signatures and face-incidence relations show that the quotient regular CW structures are combinatorially isomorphic for every \(n\ge4\). Direct partition enumeration gives the numbers of cells by dimension:

\[
\begin{array}{c|rrrr}
 n&0&1&2&3\\\hline
 1&4&2&0&0\\
 2&4&8&4&0\\
 3&4&8&8&2\\
 n\ge4&4&8&8&3
\end{array}.
\]

**3. Eleven free-face collapses in the stabilized quotient.** Write \(012[0|12]\) for the cell whose colors are \(\{0,1,2\}\), with equal-leaf blocks \(\{0\}\) and \(\{1,2\}\); analogous notation applies to all signatures. In the following list each left-hand cell is a free codimension-one face of its right-hand cell *in the complex remaining after all earlier pairs are removed*:

```
012[0|12]    < 0123[0|12|3]
013[0|1|3]   < 0123[0|1|2|3]
012[0|1|2]   < 0123[03|1|2]
01[0|1]      < 013[03|1]
03[0|3]      < 023[0|2|3]
02[0|2]      < 023[03|2]
12[1|2]      < 123[1|2|3]
12[12]       < 123[12|3]
0[0]         < 03[03]
1[1]         < 13[1|3]
2[2]         < 23[2|3]
```

For each pair, checking all surviving higher-dimensional signatures that restrict to its left-hand signature gives precisely the listed right-hand cell. Therefore all are legitimate elementary collapses of a regular CW complex, not merely algebraic boundary cancellations. Exactly one cell remains, the vertex \(3[3]\). This proves contractibility for every \(n\ge4\).

**4. The cases with fewer leaves.** For \(n=1\), only two edges survive among four vertices, and they are disjoint; the quotient is two intervals, thus homotopy equivalent to \(S^0\). For \(n=2\), the four triangular cells are the four distinct triangles on the four colors. Their six boundary edges assemble into the tetrahedral boundary, a two-sphere. The other two one-cells are additional edges joining pairs of vertices already lying in this sphere; attaching each adds one free circular summand. Hence the quotient is \(S^2\vee S^1\vee S^1\).

For \(n=3\) there are exactly two three-cells. The following four successive elementary collapses remove both three-cells and two further two-cells:

```
012[0|1|2]   < 0123[03|1|2]
012[0|12]    < 0123[0|12|3]
12[1|2]      < 123[1|2|3]
12[12]       < 123[12|3]
```

The remaining regular CW complex has four vertices, six edges and four triangular two-cells; every edge belongs to two distinct triangles, and the link of each vertex is a connected circle. Thus it is a connected closed surface with Euler characteristic \(4-6+4=2\), hence homeomorphic to \(S^2\). This proves the stated classification and the sharpness of the stabilization threshold.

## Verification

The standalone `verify.py` enumerates every allowed partition signature and checks face restrictions. It independently builds ordinary labeled digraph multipath faces for \(1\le n\le5\), determines their orbit signatures, and compares them with the symbolic construction. It verifies all eleven stabilized free-face pairs and all four \(n=3\) pairs against **every** surviving coface. It also tests the tetrahedral sphere with two extra edges for \(n=2\), the four-triangle closed surface for \(n=3\), and the two-interval case for \(n=1\). Running `python3 verify.py` produces `ALL_VERIFY_OK` with exact counts; `verification_output.txt` contains its complete output.

The infinite-parameter part follows from the color/partition classification and the fact that there are only four colors. The finite direct-face enumeration is a check of this proof, not a substitute for it.

## Relationship to prior work

Caputi, Collari and Smith's 2026 study analyzes the multipath complexes of bidirected polygonal digraphs, not leaf-permutation orbit spaces of complete bipartite bidigraphs. Deshpande and Sawant study directed-forest / multipath complexes and vertex decomposability, not this geometric quotient. Caputi, Collari, Di Trani and Smith earlier considered multipath complexes for complete bipartite **one-way** orientations; the bidirected graph and the orbit quotient in the present theorem are different. Other related findings determine homotopy or symmetry characters for the **unquotiented** bidirected \(K_{2,6}\) multipath complex, not its orbit space; those results do not imply a regular-CW quotient collapse. The present theorem addresses the actual orbit spaces for all leaf counts, with their sharp transition at four.

## Limitations

The theorem is restricted to exactly two fixed hubs and the full permutation action on the opposite shore. It does not classify quotients by proper subgroups, hub swaps, graphs with three or more hubs, or equivariant homotopy types before passage to the orbit space. Mathematically equivalent prior work outside the inspected sources remains possible.

## References

1. L. Caputi, L. Collari, and P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, publicly posted 2026-01-09. https://arxiv.org/abs/2601.05670
2. D. Deshpande and S. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936, publicly posted 2026-02-16. https://arxiv.org/abs/2602.14936
3. L. Caputi, L. Collari, G. Di Trani, and P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, publicly posted 2022-08-09. https://arxiv.org/abs/2208.04656
