# Mixed-dimensional homotopy and symmetry of the bidirected theta multipath complex

## Finding

Let \(D=\overleftrightarrow{K}_{2,3}\) be the directed graph on the two hubs \(A=\{a_0,a_1\}\) and the three branch vertices \(B=\{b_0,b_1,b_2\}\), with both directed arcs between every hub and branch. Let \(X(D)\) be its multipath simplicial complex. There is an integral homotopy equivalence

\[
X(D)\simeq S^1\vee\bigvee^{6}S^2.
\]

In particular, \(\widetilde H_1(X(D);\mathbb Z)\cong\mathbb Z\), \(\widetilde H_2(X(D);\mathbb Z)\cong\mathbb Z^6\), and all other reduced integral homology groups vanish.

The natural group \(\Gamma=S_2\times S_3\times C_2^{\mathrm{rev}}\) acts simplicially: its first factor permutes hubs, its second permutes branch vertices, and the last reverses every directed arc. These operations commute. Let \(\varepsilon\in\{0,1\}\) indicate hub interchange, let \(r\in\{0,1\}\) indicate global arc reversal, and let \(\sigma\in S_3\) permute branches. With \(\eta=(-1)^{\varepsilon+r}\), the complete rational homology characters are

\[
\begin{aligned}
\operatorname{tr}\bigl((\varepsilon,\sigma,r)_*\mid H_1(X(D);\mathbb Q)\bigr)&=\operatorname{sgn}(\sigma),\\
\operatorname{tr}\bigl((\varepsilon,\sigma,r)_*\mid H_2(X(D);\mathbb Q)\bigr)&=1+\chi_{\mathrm{Std}}(\sigma)+\eta\bigl(\operatorname{sgn}(\sigma)+\chi_{\mathrm{Std}}(\sigma)\bigr),
\end{aligned}
\]

where \(\mathrm{Std}\) denotes the two-dimensional standard representation of \(S_3\). Equivalently, as rational \(\Gamma\)-modules, the first homology is the inflated sign representation of \(S_3\), while the second is

\[
\bigl((\mathbf 1\oplus\mathrm{Std})\otimes\mathbf1\bigr)\oplus
\bigl((\operatorname{sgn}\oplus\mathrm{Std})\otimes\eta\bigr).
\]

Here \(\eta\) is the one-dimensional sign character of the quotient of the two order-two factors given by their parity sum; the two indicated \(S_3\)-modules are inflated across the remaining factors. No equivariant homotopy equivalence is asserted.

| Branch permutation class | Trace in degree one | Trace in degree two when \(\eta=1\) | Trace in degree two when \(\eta=-1\) |
|---|---:|---:|---:|
| Identity | 1 | 6 | 0 |
| Transposition | -1 | 0 | 2 |
| Three-cycle | 1 | 0 | 0 |

## Assumptions and scope

A *multipath* is a spanning directed subgraph whose connected components are isolated vertices or simple directed paths. Therefore a face of \(X(D)\) is an arc set in which every vertex has indegree and outdegree at most one, and which contains no directed cycle. The twelve distinct arcs are indexed in this fixed order: for each \(i=0,1\) and \(j=0,1,2\), first \(a_i\to b_j\), then \(b_j\to a_i\), in lexicographic order of \((i,j)\). A face is encoded by the twelve-bit integer recording its arc subset. The statement concerns precisely this five-vertex fully bidirected theta graph, not all complete bipartite digraphs.

## Proof

**Face-poset reconstruction.** A twelve-bit subset is a multipath if and only if its selected arcs have no repeated source or target and contain no directed cycle. One complete enumerator checks these conditions directly; a second checks distinct sources and targets together with acyclicity of the underlying undirected edge multigraph using union-find. Both enumerate the same face set. Its numbers of faces in dimensions \(-1,0,1,2,3\), respectively, are \((1,12,42,48,12)\). No faces of higher dimension exist because a directed path forest on five vertices has at most four arcs.

**Acyclic matching.** On the nonempty face poset, repeatedly process the twelve arc coordinates in their fixed order. At coordinate \(i\), pair every as-yet-unpaired face \(F\) not containing that coordinate with \(F\cup\{i\}\) whenever both faces remain unpaired. Delete each such pair before advancing to the next coordinate. The rule yields 53 matched pairs and precisely the critical faces encoded by \(1,392,514,580,1060,1156,2072,2120\). Their dimensions are one zero-cell (mask \(1\)), one one-cell (mask \(514\)), and six two-cells (the remaining masks). Direct the covering relations in the face Hasse diagram downward, except for the matched relations, which are directed upward. An exhaustive topological sort visits all 114 nonempty faces and proves that this directed graph, with all 276 nonempty covering incidences, is acyclic. Thus the matching is an acyclic discrete-Morse matching, not merely an enumerative heuristic.

**Integral attaching degrees.** The Morse differential is reconstructed with exact signed simplicial incidence numbers. For each matched lower-dimensional face \(F\) paired with \(U\), project \(F\) to critical cells of its dimension by the recursion

\[
P(F)=-[U:F]\sum_{E\subset U,\ |E|=|F|,\ E\ne F}[U:E]\,P(E),
\]

with \(P(F)=F\) on critical faces and \(P(F)=0\) on upper members of matched pairs. The coefficients \([U:E]\in\{\pm1\}\) are ordinary oriented face incidences. Acyclicity ensures termination. For every critical two-cell \(C\), sum the projected oriented codimension-one facets of \(C\) to compute its integral Morse boundary. All six coefficients in the single-row degree-two-to-degree-one Morse boundary matrix are exactly zero; the degree-one-to-degree-zero Morse boundary is zero because there is only one critical vertex. The associated Morse CW complex consequently has one vertex, one loop, and six attached two-cells, each attached to the loop with degree zero. Every degree-zero map \(S^1\to S^1\) is null-homotopic, so this CW complex is \(S^1\vee\bigvee^{6}S^2\), proving the claimed integral homotopy equivalence.

**Symmetry action.** The matched vertex–edge pairs form a spanning tree on the twelve vertices of the simplicial complex. Combining its unique additional critical one-cell with the unique tree path joining that edge's endpoints gives an integral one-cycle of support four, pairing to \(1\) with the critical-one-cell projection cocycle. For each of the 24 symmetries, act on this cycle by permuting arcs, including the sign induced on oriented simplices. Evaluation against that integral cocycle yields the degree-one trace \(\operatorname{sgn}(\sigma)\). Independently calculate the signed simplicial Lefschetz number from all faces fixed setwise by each symmetry. Since the only nonzero reduced homology degrees are one and two, subtracting the contribution of the unique \(H_0\)-class gives

\[
\operatorname{tr}(g_*\mid H_2)=L(g)-1+\operatorname{tr}(g_*\mid H_1).
\]

The resulting twelve conjugacy-class pairs of traces are exactly those in the table above. Applying the standard \(S_3\) character table identifies the stated rational direct-sum decomposition.

## Verification

Run `python3 CHECK.py` using Python 3 with no external packages. The program checks all \(2^{12}=4096\) arc subsets using two different validity criteria, the full discrete-Morse matching, acyclicity of the directed Hasse graph, signed integer Morse boundaries, mod-two boundary ranks \((11,30,12)\), a primitive integral one-cycle and cocycle, and all 24 signed symmetry actions. Successful execution emits the human-readable `CHECK_OUTPUT.json` data and the terminal status `ALL_EXACT_CHECKS_PASSED`; the included output file records a completed run. The Euler characteristic independently agrees: \(12-42+48-12=6=1-1+6\).

## Relationship to prior work

Caputi, Collari, Di Trani and Smith introduce and investigate multipath complexes systematically. Their section 3.2 treats an *alternatingly oriented* complete bipartite digraph (every arc goes from one part to the other), identifies a chessboard/matching complex, and computes its Euler characteristic. This does not give the homotopy or equivariant homology of the *fully bidirected* five-vertex theta graph considered here. Vrećica and Živaljević introduce general cycle-free chessboard complexes associated with directed graphs, but their principal homological results concern complete digraphs and connectivity bounds, without an exact computation for this theta case. The later study by Caputi, Collari and Smith treats bidirectional paths and polygons; the theta graph has three internally disjoint two-edge paths between its hubs, so it is neither of those families.

## Limitations

This is an exact five-vertex result and a rational symmetry-character calculation, not an all-parameter classification of \(\overleftrightarrow{K}_{2,n}\) and not a statement about integral splitting of the equivariant representation. Computations exhaust the stated finite complex and cannot alone prove arbitrary-parameter phenomena. The existence of an equivalent result in unindexed literature cannot be excluded from the searches performed.

## References

1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first publicly available 2022-08-09), especially Definitions 2.1–2.2 and Section 3.2. https://arxiv.org/abs/2208.04656
2. S. T. Vrećica, R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252 (2007), Sections 2–3 and 7–8. https://arxiv.org/abs/0710.5252
3. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (2026), Introduction and Sections 1–2. https://arxiv.org/abs/2601.05670
