# Complete closed-neighborhood shattering polynomial of triangular Johnson graphs

## Finding
For every integer \(n\ge2\), let \(T_n=J(n,2)\) be the triangular Johnson graph on the unordered pairs of \([n]\). A concept is the closed neighborhood of one vertex. Let \(s_k(n)\) count \(k\)-element shattered supports of the family \(\mathcal B_n=\{N_{T_n}[e]: e\in V(T_n)\}\); in particular \(s_0(n)=1\). Put \(\binom{a}{b}=0\) when \(b<0\) or \(b>a\).

The complete shattering polynomial is
\[
\Phi_n(z)=1+s_1(n)z+s_2(n)z^2+s_3(n)z^3+s_4(n)z^4,
\]
with the coefficients
\[
\begin{aligned}
s_1(n)&=\mathbf 1_{n\ge4}\binom n2,\\
s_2(n)&=\mathbf 1_{n\ge5}n\binom{n-1}{2}+\mathbf 1_{n\ge6}3\binom n4,\\
s_3(n)&=\mathbf 1_{n\ge6}n\binom{n-1}{3}+\mathbf 1_{n\ge7}n\binom{n-1}{2}\binom{n-3}{2},\\
s_4(n)&=\mathbf 1_{n\ge8}\binom n2\binom{n-2}{2}\binom{n-4}{2}.
\end{aligned}
\]
All higher coefficients vanish. Hence the VC dimension is \(0\) for \(n=2,3\), \(1\) for \(n=4\), \(2\) for \(n=5\), \(3\) for \(n=6,7\), and \(4\) for \(n\ge8\).

More precisely, a nonempty support \(S\subseteq\binom{[n]}2\) is shattered **if and only if** its graph \(([n],S)\) has at least two isolated vertices and its nontrivial components have one of these forms: (I) a single star \(K_{1,a}\) with \(1\le a\le3\), or (II) two disjoint stars \(K_{1,a}\sqcup K_{1,b}\) with \(1\le a,b\le2\). The empty support is always shattered.

## Assumptions and scope
Here the vertices of \(T_n\) are the edges of the complete graph \(K_n\). For an edge \(e=\{u,v\}\), its **closed** neighborhood in \(T_n\) is exactly the set of all base edges meeting \(\{u,v\}\), including \(e\) itself. Thus for any query support \(S\), the trace induced by the concept with center \(e\) is
\[
S_e=\{f\in S:f\cap e\ne\varnothing\}.
\]
Shattering means that every one of the \(2^{|S|}\) subsets of \(S\) is equal to \(S_e\) for some base edge \(e\). No additional empty or full concepts are allowed. The statement applies to all \(n\ge2\), including small degenerate graphs.

## Proof
**First, isolated vertices are necessary.** Realizing the empty trace requires an edge \(e=\{u,v\}\) disjoint from every edge of \(S\). Its two endpoints are therefore distinct isolated vertices of the graph \(([n],S)\). Conversely, two such isolated vertices supply an empty-trace center.

**Second, the support is a star forest.** Fix an edge \(f=\{u,v\}\in S\). The singleton trace \(\{f\}\) must be realized by some center edge meeting \(f\) but no other support edge. At least one endpoint of \(f\) belongs to the center; that endpoint cannot be incident with any other edge of \(S\). Hence every support edge has a degree-one endpoint. A connected nontrivial graph in which every edge has a degree-one endpoint must be a star: if it contained a path of three edges, the middle edge would have no leaf endpoint; and if it contained a cycle, each cycle edge would lack a leaf endpoint. Therefore every nontrivial component is a star.

**Third, there are at most two star components.** The trace \(S\) must be realizable. A center with two base endpoints can meet at most two vertex-disjoint nontrivial components, since meeting every component requires at least one endpoint inside each component.

**Fourth, component sizes are bounded.** If \(S\) is a single star of at least four edges, choose any three edges but not a fourth. A center containing the star center includes all star edges, while a center omitting that vertex can cover at most two star edges. Thus this three-edge trace is impossible. If \(S\) has two stars and one has at least three edges, choose exactly two edges from that large star and exactly one from the other. A center containing the large-star center includes all its edges; without that center both endpoint slots are needed for the two selected leaves, leaving none to hit the other component. Thus this trace is also impossible. Necessity of forms (I) and (II) follows.

**Fifth, every listed shape is shattered.** For a single star of one, two or three edges, a requested subset of three or fewer edges is covered by choosing its leaf endpoints when it has two edges, its unique leaf plus one isolated vertex when it has one edge, or the star center plus one isolated vertex when it has all three edges; for the empty subset use two distinct isolated vertices. (For a star of one or two edges the same constructions apply, with the star center covering the complete support.) For two stars each with one or two edges, each star independently has a representative base vertex: its center for both edges, its corresponding leaf for one edge, and an isolated base vertex for none. Take the two representatives as the center edge. When both requested component subsets are empty, use the two distinct isolated vertices. Every subset is therefore a trace. This proves the classification, including the upper bound of four.

**Finally, count the shapes.** A single edge yields \(\binom n2\). A two-edge star has a unique center, giving \(n\binom{n-1}{2}\), while two disjoint edges can be selected in \(3\binom n4\) ways. A three-edge star gives \(n\binom{n-1}{3}\). A two-edge star plus a disjoint edge is specified by its center, its two leaves, and the other edge, giving \(n\binom{n-1}{2}\binom{n-3}{2}\). Two disjoint two-edge stars have two uniquely identifiable degree-two centers, an unordered pair of which is chosen in \(\binom n2\) ways, with two leaves for the first center and two for the second, giving \(\binom n2\binom{n-2}{2}\binom{n-4}{2}\). Each shape is eligible only if it leaves two additional isolated base vertices; these are exactly the displayed cutoff conditions. The shapes are disjoint and exhaustive, completing the polynomial and dimension formulas.

## Verification
The independent Python 3 script `verify_triangular_graph.py` builds all closed-neighborhood trace masks from the pair-intersection rule, enumerates every support of sizes one through four for each \(2\le n\le10\), and compares the resulting coefficients against the formulas. It checks 265,023 nonempty supports across nine graphs and reports `ALL_TRIANGULAR_CLOSED_NEIGHBORHOOD_CHECKS_PASS 9 graphs 265023 supports`. The \(n=8\) polynomial is \(1+28z+378z^2+1960z^3+2520z^4\). The universal exclusion of all higher sizes is proved structurally above; finite testing does not establish that infinite statement.

## Relationship to prior work
Adler, Benediktsson and Macpherson study the **open** neighborhoods of Johnson and Hamming graphs. Their Theorem 3.7 establishes VC dimension four for \(J(7,2)\) using open neighborhoods and their abstract notes boundedness for closed neighborhoods; neither supplies the closed-neighborhood coefficientwise census here. The difference between open and closed concepts matters: the closed family first has dimension four at \(J(8,2)\). Coudert, Csikós, Ducoffe and Viennot study algorithms for computing **closed** graph VC dimension in arbitrary graphs; their general algorithms do not supply the specialized exact all-size support counts or star-forest criterion. The bounded-dimension conclusions of earlier work do not imply these coefficient formulas. Searches also considered the equivalent names triangular graphs, line graphs of complete graphs, and edge-intersection ranges; no exact equivalent enumeration was located in accessible sources.

## Limitations
The theorem only concerns the \(k=2\) Johnson family and inclusive radius-one neighborhoods. It does not assert all-\(k\) formulas, an arbitrary-line-graph theorem, or any independent verification of historical priority. Mathematical originality was assessed through accessible papers and indexed records, not exhaustive world literature. The finite test covers \(n\le10\), with the proof supplying universal correctness. No independent external audit has been conducted.

## References
1. Isolde Adler, Bjarki Geir Benediktsson, Dugald Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first public version 2020-07-31); *Discrete Applied Mathematics* 312 (2022), 29–44, doi:10.1016/j.dam.2021.09.017. Primary full text: https://eprints.whiterose.ac.uk/178584/1/Adler_Benediktsson_Macpherson.pdf.
2. David Coudert, Mónika Csikós, Guillaume Ducoffe, Laurent Viennot, *Practical Computation of Graph VC-Dimension*, *Proceedings of SEA 2024*, LIPIcs 301 (2024), article 8; https://drops.dagstuhl.de/storage/00lipics/lipics-vol301-sea2024/LIPIcs.SEA.2024.8/LIPIcs.SEA.2024.8.pdf, arXiv:2405.07588.
