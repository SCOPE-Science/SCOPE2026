# Complete higher-independence homotopy types of well-covered cubic polyhedra

## Finding

The four connected well-covered **cubic polyhedral graphs** have distinct integral two-independence homotopy types:

\[
\begin{aligned}
\operatorname{Ind}_2(K_4)&\simeq\bigvee^3 S^1,\\
\operatorname{Ind}_2(C_3\square K_2)&\simeq\bigvee^4 S^1,\\
\operatorname{Ind}_2(C_5\square K_2)&\simeq\bigvee^{11}S^3,\\
\operatorname{Ind}_2(\operatorname{GP}(6,2))&\simeq\bigvee^3 S^3\vee S^4.
\end{aligned}
\]

The last graph is the Dürer graph. In particular, its two-independence complex has nonzero free integral homology in two adjacent dimensions, despite the well-coveredness of the underlying graph. The result is a complete classification for this natural four-graph class, not a statement for all well-covered cubic graphs.

## Assumptions and scope

For a finite simple graph \(G\), define \(\operatorname{Ind}_2(G)\) to be the simplicial complex containing precisely those subsets \(A\subseteq V(G)\) for which every connected component of the induced graph \(G[A]\) has at most two vertices. Equivalently, \(\deg_{G[A]}(v)\leq1\) for all \(v\in A\). The empty face belongs to the complex; homotopy types refer to ordinary geometric realization.

For \(n\ge3\), the generalized Petersen graph \(\operatorname{GP}(n,k)\) has vertices \(u_i,v_i\), \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\). Here \(\operatorname{GP}(3,1)\cong C_3\square K_2\), \(\operatorname{GP}(5,1)\cong C_5\square K_2\), and \(\operatorname{GP}(6,2)\) is the Dürer graph. The classification of well-covered cubic polyhedra used to delimit the class comes from Campbell and Plummer and is explicitly restated in Campbell, Ellingham, and Royle [1,2].

## Proof

All four graphs have at most twelve vertices, making exhaustive face-set enumeration a finite proof. Represent a face by its vertex bit mask. An admissible mask is one for which no selected vertex has two selected neighbors. Independently, construct all forbidden three-vertex paths and reject a mask exactly when it contains one of them. The two constructions return equal face sets in all cases.

Process vertices in order. At stage \(i\), match every currently unmatched face \(\sigma\) not containing vertex \(i\) with \(\sigma\cup\{i\}\), whenever both remain. Delete matched faces before proceeding. This is a sequence of element matchings. The full augmented Hasse diagram, with matched covers reversed relative to unmatched covers, is checked acyclic by an exhaustive topological sort. The empty face is paired, hence a basepoint supplies the zero-cell of the associated Morse CW model.

The face counts (including the empty face), matching counts, and critical dimensions are:

| Graph | Faces | Pairs | Critical cells other than basepoint |
|---|---:|---:|---|
| \(K_4\) | 11 | 4 | three in dimension one |
| \(C_3\square K_2\) | 28 | 12 | four in dimension one |
| \(C_5\square K_2\) | 231 | 110 | eleven in dimension three |
| \(\operatorname{GP}(6,2)\) | 810 | 402 | four in dimension three, two in dimension four |

For the first three graphs the critical cells, aside from a basepoint, are all in one positive dimension, so the discrete-Morse CW theorem directly gives the stated sphere wedges.

For the Dürer graph, orient each simplex increasingly by its vertex labels and use signed face incidences. If a dimension-three simplex \(s\) is the lower member of a matched pair \((s,t)\), its chain projection is obtained recursively from \(\partial t\):

\[
R(s)=-[t:s]^{-1}\sum_{a\in\partial t,\ a\ne s}[t:a]R(a).
\]

Set \(R(s)=0\) for upper matched three-simplices, and \(R(s)=s\) for critical three-simplices. The acyclic matching ensures termination. Applying this reduction to the boundaries of the two critical four-cells gives, with the reproducibly specified ordering in the attached verifier, the signed integral boundary

\[
\partial^{\mathrm M}_4=\begin{pmatrix}-1&-1\\0&0\\0&0\\0&0\end{pmatrix}.
\]

Its nonzero Smith invariant factor is \(1\). The Morse CW complex starts with a point and a wedge of four three-spheres, then attaches two four-cells with equal primitive attaching classes. Since \(\pi_3(\bigvee^4 S^3)\cong\mathbb Z^4\), a change of basis of the three-cells and one four-cell cancellation leaves three three-spheres and one four-sphere. Thus the final statement is an integral **homotopy** equivalence, not merely a computation of homology.

## Verification

The standalone `verification/verify.py` uses only the Python standard library; run `python verification/verify.py` in the extracted package. It independently enumerates the face sets by induced-degree and forbidden-path criteria; checks well-coveredness of all four graphs; reconstructs all matching pairs; checks acyclicity on all oriented Hasse covers; independently computes the mod-two boundary ranks of every original chain complex; computes the full signed Dürer Morse differential by gradient paths, and independently reproduces that differential by direct elementary cancellation in the full integral chain complex. The output is included in `verification/output.txt`. All tests must end with `ALL_CHECKS_PASS`.

The four Hasse-edge counts checked are 16, 54, 720, and 3,192, respectively. The mod-two reduced Betti numbers agree with the integral Morse classifications. The unit Smith invariant rules out integral torsion in the Dürer case.

## Relationship to prior work

The four-graph class comes from the graph-theoretic well-covered cubic/polyhedral classifications of Campbell and Plummer [1] and Campbell, Ellingham, and Royle [2]. Their graph classifications do not supply these two-independence homotopy types. Deshpande and Singh [3] prove broad higher-independence results for complete multipartite graphs, whiskered graphs, paths, cycles, and trees. Their complete-graph formula already covers the simple \(K_4\) entry here; it does not imply the Dürer result or the complete four-polyhedron table.

Earlier work on two-independence complexes of circular ladders gives useful Euler-characteristic information for the prism members, but such values do not imply their full integral homotopy types. The graph-metric Rips complex of the Dürer graph is a different simplicial construction and cannot be substituted for its two-independence complex. Novelty of an exact unindexed equivalent calculation cannot be ruled out by finite search alone.

## Limitations

This is a finite, reproducible homotopy classification for **only** the four well-covered cubic polyhedral graphs. It does not extend to other well-covered cubic graphs, arbitrary convex polyhedral graphs, higher values of the independence parameter, or equivariant homotopy. Formal publication priority has not been conclusively established, and no independent mathematical review is claimed.

## References

[1] S. R. Campbell and M. D. Plummer, *On well-covered 3-polytopes*, Ars Combinatoria 25A (1988), 215–242 (historical classification; full text not independently available during this check).

[2] S. R. Campbell, M. N. Ellingham, and G. F. Royle, *A Characterisation of Well-Covered Cubic Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 13 (1993), 193–212, https://combinatorialpress.com/article/jcmcc/Volume%2013/vol-13-paper%2017.pdf . The official record identifies April 30, 1993 as its publication date.

[3] P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first publicly posted January 2020; later 2021 version), https://arxiv.org/abs/2001.05448 .
