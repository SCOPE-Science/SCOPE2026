# Sharp fundamental groups of cyclic color quotients of clique-path independence complexes

## Finding

Let \(P_m\) be the path on \(m\ge 1\) vertices and \(K_q\) the complete graph on \(q\ge3\) vertices. Set \(X_{m,q}=\operatorname{Ind}(P_m\square K_q)\). The simultaneous cyclic color-rotation group \(C_q\) acts freely on \(|X_{m,q}|\), and the geometric orbit space \(Y_{m,q}=|X_{m,q}|/C_q\) is connected and has the complete fundamental-group classification

\[
\pi_1(Y_{m,q})\cong
\begin{cases}
1,&m=1,\\
F_{q-2},&m=2,\\
\mathbb Z,&(m,q)=(3,3),\\
C_q,&m\ge3,\ q\ge4\ \text{or}\ m\ge4,\ q=3.
\end{cases}
\]

Here \(F_s\) is the free group of rank \(s\), including \(F_0=1\). In the last regime, \(X_{m,q}\) is simply connected and is the universal covering complex of \(Y_{m,q}\). In particular, \(H_1(Y_{m,q};\mathbb Z)\cong\mathbb Z/q\) there, whereas \(Y_{3,3}\simeq S^1\) and \(Y_{2,q}\simeq\bigvee^{q-2}S^1\). This gives a sharp emergence of cyclic integral torsion of unbounded order in the first homology of symmetry quotients of clique-path independence complexes.

## Assumptions and scope

A vertex of \(P_m\square K_q\) is a pair \((i,c)\), with \(1\le i\le m\) and \(c\in\mathbb Z/q\). Two different pairs are adjacent when their first coordinates agree, or when their first coordinates differ by one and their colors agree. An independent set contains at most one vertex in each column, and occupied consecutive columns have distinct colors. The simplicial complex \(X_{m,q}\) contains every such independent set; realization and orbit spaces refer to the actual geometric realization, not a graph on vertex orbits or a naive quotient flag complex. A generator of \(C_q\) adds one to every occupied color.

## Proof

**Freeness.** If a nonidentity color translation fixed a point of the realization, the point's nonempty support face would be invariant under the translation. The orbit of any vertex in that support contains at least two different vertices in the same column; the whole orbit would belong to the support, which cannot be independent. Hence all geometric stabilizers are trivial.

**A simply-connectedness cover.** For every \(c\in\mathbb Z/q\), let \(A_c=\operatorname{st}_{X_{m,q}}(1,c)\) be the closed simplicial star. Each \(A_c\) is a cone. They cover \(X_{m,q}\): a face occupying the first column belongs to the star of its first-column vertex; a face omitting that column can be extended by some first-column color distinct from the at most one color in column two, because \(q\ge3\). For \(a\ne b\), a face of \(A_a\cap A_b\) must omit the entire first column and omit the two colors \(a,b\) from column two. Conversely those two restrictions characterize the intersection.

If \(q\ge4,m\ge3\), the one-skeleton of \(A_a\cap A_b\) is connected: there are at least two allowed vertices in column two; every column-three vertex is linked to at least one allowed column-two vertex, and every allowed column-two vertex is linked to at least two column-three vertices. If \(q=3,m\ge4\), the single permitted column-two vertex is linked to all vertices of column four, every column-three vertex links to some column-four vertex of a different color, and each vertex in columns five and beyond links to the permitted column-two vertex. The same latter argument applies when \(q>3,m\ge4\). Thus each pairwise star intersection is path-connected in the stated regimes. Every intersection of any number of stars contains every column-three vertex, because column one and column three are nonadjacent. Inductively attach the contractible stars, starting from one. The intersection of the next star with the union of previously attached stars is a union of pairwise intersections containing a common column-three vertex, hence connected. Van Kampen now shows \(\pi_1(X_{m,q})=1\). Because the group action is free, \(X_{m,q}\to Y_{m,q}\) is then the universal regular covering with deck group \(C_q\); therefore \(\pi_1(Y_{m,q})\cong C_q\).

**Boundary cases.** If \(m=1\), \(X_{1,q}\) consists of \(q\) isolated vertices and its quotient is one point. If \(m=2\), \(X_{2,q}\) is the bipartite graph on two color columns, with an edge between colors \(a\ne b\). Its color-rotation quotient is a connected graph with exactly two vertices and \(q-1\) edges, hence a wedge of \(q-2\) circles. For \((m,q)=(3,3)\), \(X_{3,3}\) has twelve triangles, indexed by triples \((a,b,c)\) with \(a\ne b\), \(b\ne c\). The six triangles with \(a\ne c\) have free opposite edges \(\{(1,a),(3,c)\}\); collapse each together with its unique incident triangle. The six remaining triangles have \(a=c\) and now have free edges \(\{(1,a),(2,b)\}\); collapse those as well. These are whole cyclic orbits of free-face collapses and give an equivariant deformation retraction to a six-cycle on columns two and three, with three pendant first-column vertices. Its geometric quotient is a connected graph with three vertices and three edges, hence a circle. Thus \(\pi_1(Y_{3,3})\cong\mathbb Z\). Since its cover is a connected graph homotopy equivalent to a circle, \(X_{3,3}\) is not simply connected. The two-column complexes have nonzero first Betti number \(q(q-1)-2q+1=q^2-3q+1\), and the one-column complex is disconnected; this also makes the above simply-connectedness threshold sharp.

**Further consequence.** If a finite nontrivial group \(H\) acts freely by permutations on a color set of size \(q\ge3\), then its diagonal action on \(X_{4,q}\) is free by the same support argument, and \(X_{4,q}\) is simply connected. Therefore \(\pi_1(|X_{4,q}|/H)\cong H\). Taking sufficiently many copies of the left-regular color action realizes any finite group in this concrete family; this consequence uses no assertion about higher homotopy or cohomology.

## Verification

The self-contained script `strip_quotient_check.py` independently enumerates all faces, constructs the true signed simplicial orbit chain complex, checks consecutive boundaries compose to zero, and computes first integral homology by a spanning-tree cycle basis and exact Smith normal form. It confirms \(H_1(Y_{2,3})=\mathbb Z\), \(H_1(Y_{3,3})=\mathbb Z\), \(H_1(Y_{4,3})=H_1(Y_{5,3})=\mathbb Z/3\), \(H_1(Y_{2,4})=\mathbb Z^2\), \(H_1(Y_{3,4})=H_1(Y_{4,4})=\mathbb Z/4\), \(H_1(Y_{2,5})=\mathbb Z^3\), and \(H_1(Y_{3,5})=H_1(Y_{4,5})=\mathbb Z/5\). The finite computations verify examples and signed boundary conventions, not the universal assertions. The universal argument is the explicit star cover and van Kampen proof above.

Run `python strip_quotient_check.py` with Python 3 and SymPy installed. It prints the enumerated orbit cell counts and each torsion invariant.

## Relationship to prior work

Bidwan Chakraborty's preprint [1], first publicly submitted 13 November 2026, studies exactly the triangular-column graphs \(P_m\square C_3=P_m\square K_3\) and classifies Cohen–Macaulayness, Buchsbaumness and well-coveredness of Cartesian path–cycle independence complexes. It does not give the cyclic-quotient fundamental groups, sharp van Kampen threshold or arbitrarily high cyclic first-homology torsion. Carnero Bravo's work [2] concerns different graph products and therefore does not imply the present Cartesian-strip classification. General covering-space and van Kampen theory are standard ingredients and are not claimed as new. The statement concerns geometric orbit spaces rather than independence complexes of orbit graphs. Available published-result and literature searches did not reveal equivalent coverage; an unindexed older calculation remains a priority risk.

## Limitations

The quotient is by a **free diagonal color-permutation** action, not arbitrary automorphisms of a strip. The result classifies only fundamental groups and first integral homology, not higher homology, full homotopy type, arbitrary graph products or nonfree symmetry quotients. The illustrative finite Smith reductions are not infinite proofs. No independent mathematical verification has been performed; publication priority beyond inspected accessible sources is not guaranteed.

## References

[1] B. Chakraborty, *Cohen–Macaulayness and Buchsbaumness of Cartesian Products of Paths and Cycles*, arXiv:2611.18495v1, initially submitted 13 November 2026, https://arxiv.org/abs/2611.18495.

[2] A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, https://arxiv.org/abs/2505.06457.

[3] A. Hatcher, *Algebraic Topology*, Chapter 1, covering spaces and van Kampen theorem, https://pi.math.cornell.edu/~hatcher/AT/AT.pdf.
