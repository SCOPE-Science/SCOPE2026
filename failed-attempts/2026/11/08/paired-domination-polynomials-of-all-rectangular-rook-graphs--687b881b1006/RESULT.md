# Paired-domination polynomials of all rectangular rook graphs

## Finding

For integers \(m,n\ge 2\), consider the rook graph \(R_{m,n}=K_m\square K_n\): its vertices are the \(mn\) squares of an \(m\)-by-\(n\) board, with adjacency when two distinct squares share a row or a column. A paired-dominating set is a dominating vertex set \(S\) for which \(R_{m,n}[S]\) admits a perfect matching. Define its cardinality polynomial
\[
P_{m,n}(z)=\sum_{S\subseteq V(R_{m,n})\atop S\text{ paired-dominating}} z^{|S|}.
\]

**Theorem (all coefficients).** In the ring of formal power series in \(u,v,z\) with rational coefficients, let
\[
F(u,v;z)=\sum_{a,b\ge0}\frac{u^a v^b}{a!b!}(1+z)^{ab},\qquad
E(u,v;z)=\sqrt{F(u,v;z)F(u,v;-z)},
\]
where the formal square root is uniquely chosen with constant term \(1\). Then, for every \(m,n\ge2\),
\[
\boxed{P_{m,n}(z)=m!n!\,[u^m v^n]\,E(u,v;z)(e^{-u}+e^{-v}-e^{-u-v}).}
\]
Thus every cardinality coefficient for every rectangular rook graph is an explicit finite coefficient extraction. In particular, all odd-cardinality coefficients vanish.

The theorem has a direct structural version. Let \(B_S\) be the spanning bipartite graph on \(m\) named row vertices and \(n\) named column vertices, with edge \(ij\) precisely when square \((i,j)\) is selected. Then \(S\) is paired-dominating **if and only if**:

1. \(B_S\) has no isolated row vertices, or it has no isolated column vertices; and
2. every connected component of \(B_S\) that contains an edge has an even number of edges.

**Minimum size and leading coefficient.** Write \(m\le n\), \(m\ge2\). The minimum cardinality is \(\gamma_{\mathrm{pr}}(R_{m,n})=2\lceil m/2\rceil\). The exact number of minimum sets is given below, with a transparent parity/square-board correction. Define
\[
C_{r,s}=r!\,[t^r]\cosh(t)^s,
\qquad
A_{m,n}=m\binom n2(m-1)!\,[t^{m-1}]\cosh(t)^{n-2}\cosh(2t).
\]
For even \(m\), the number of minimum sets equals \(C_{m,n}\) if \(m<n\), and \(2C_{m,m}\) if \(m=n\). For odd \(m\ge3\), it equals \(A_{m,n}\) if \(n\ge m+2\); it equals \(A_{m,m+1}+C_{m+1,m}\) if \(n=m+1\); and it equals \(2A_{m,m}-9\) if \(n=m=3\), or \(2A_{m,m}\) if \(n=m\ge5\). These are all counts of actual vertex sets, not matchings chosen within them.

Examples of complete polynomials are
\[
P_{2,3}(z)=3z^2+15z^4+z^6,
\]
\[
P_{3,3}(z)=81z^4+84z^6+9z^8,
\]
\[
P_{3,4}(z)=129z^4+840z^6+495z^8+66z^{10}+z^{12},
\]
and
\[
P_{4,4}(z)=80z^4+4464z^6+12150z^8+7992z^{10}+1820z^{12}+120z^{14}+z^{16}.
\]

## Assumptions and scope

All graphs are finite, simple and undirected; \(m,n\) are labelled positive integers with \(m,n\ge2\). Each square is either selected or not; the same selected set is counted once regardless of how many perfect matchings its induced graph possesses. Domination means every unselected vertex has a selected neighbor (selected vertices dominate themselves). Perfect matching means every selected vertex is incident with exactly one edge of the matching in the induced subgraph. No weighting of matched pairs is permitted. The formal generating functions are coefficientwise identities, not analytic convergence statements.

## Proof

**1. Domination translates into full row or column support.** A square \((i,j)\) absent from \(S\) has a selected neighbor exactly when row \(i\) or column \(j\) contains a selected square. Thus an undominated square exists exactly when there are simultaneously an empty row and an empty column. Equivalently, domination means that \(B_S\) has no isolated row vertices or no isolated column vertices.

**2. Matching translates into even-sized edge components.** The induced rook graph \(R_{m,n}[S]\) is the line graph \(L(B_S')\), where \(B_S'\) is \(B_S\) after discarding isolated row/column vertices. Necessity: a perfect matching cannot pair vertices lying in different connected components, so the number of edges of each nontrivial component of \(B_S\) must be even.

For sufficiency, take a connected graph \(H\) with an even number of edges, and show that its edges can be partitioned into pairs sharing an endpoint. Choose any spanning tree, root it, and orient non-tree edges arbitrarily. Traverse tree edges from the leaves to the root, orienting each tree edge so that each non-root vertex has even indegree. The root also receives even indegree because the total indegree is the even number \(|E(H)|\), and all other indegrees are even. Pair the edges entering each vertex arbitrarily. The resulting pairs cover all edges and each pair shares the vertex it enters; they are a perfect matching of \(L(H)\). Apply this separately to the nontrivial components of \(B_S\). Together with step 1, this proves the structural iff.

**3. Connected-component parity gives the square-root series.** Let \(F(u,v;z)\) be the exponential generating function for all bipartite graphs on two disjoint, separately labelled vertex classes, weighted by \(z\) per edge. Fixing class sizes \(a,b\), there are \(ab\) optional edges, giving the factor \((1+z)^{ab}\) above. Write \(C(u,v;z)=\log F(u,v;z)\); the labelled exponential formula identifies \(C\) as the generating function for connected bipartite graphs (including isolated single vertices). Replacing \(z\) by \(-z\) flips the sign of each connected object with an odd number of edges. Thus
\[
C_{\mathrm{even}}(u,v;z)=\tfrac12(C(u,v;z)+C(u,v;-z))
\]
retains exactly connected components having even edge counts. Taking arbitrary sets of these components gives
\[
\exp C_{\mathrm{even}}(u,v;z)=\sqrt{F(u,v;z)F(u,v;-z)}=E(u,v;z).
\]
The connected components consisting of one isolated row or column are among the retained even-edge components. Removing them from the component species multiplies \(E\) by \(e^{-u}\) or \(e^{-v}\), respectively. Inclusion-exclusion for no isolated rows **or** no isolated columns therefore multiplies \(E\) by \(e^{-u}+e^{-v}-e^{-u-v}\). Extracting the coefficient for \(m\) row labels and \(n\) column labels proves the claimed polynomial identity. Every retained nontrivial component has an even number of edges, so the total \(|S|\) is even.

**4. Minimum and leading counts.** Any dominating placement uses at least \(m=\min(m,n)\) squares: a set of fewer squares touches fewer than \(m\) rows and fewer than \(n\) columns, leaving an undominated intersection. Paired-dominating sets have even cardinality, so the lower bound is \(2\lceil m/2\rceil\). It is attained by a complete column when \(m\) is even. When \(m\) is odd, take a complete column and one additional square outside it in any row: the selected clique on \(m\) vertices and the new square admit a perfect matching, using the edge between the new square and its selected row partner and pairing the remaining \(m-1\) selected column vertices inside their clique. Thus the lower bound is exact.

For even \(m<n\), exactly \(m\) squares must touch all \(m\) rows, one in each row. For a given column its selected squares form a clique; distinct columns are disconnected from one another in the induced rook graph. The perfect matching condition is that the number of selections in every column be even. These are precisely the functions from the \(m\) row labels to the \(n\) column labels with all fiber sizes even, counted by \(C_{m,n}\). When \(m=n\), one may instead cover all columns, producing an equal additional count. The two types cannot overlap: one per row and one per column would be an independent set, not paired-dominating.

For odd \(m\), a minimum set has \(m+1\) squares. If it covers all \(m\) rows, exactly one row holds two squares, necessarily in two distinct columns \(a,b\); the other \(m-1\) rows each hold one. Let \(q_j\) count those single selections in column \(j\). The selected rook graph is a union of column cliques with one additional edge joining the two selections in the doubled row. A perfect matching either uses that row edge, when \(q_a\) and \(q_b\) are even and all other \(q_j\) even, or does not use it, when \(q_a,q_b\) are odd and the other \(q_j\) even. Since \(\sum_j q_j=m-1\) is even, these cases together are equivalent to requiring every \(q_j\) for \(j\notin\{a,b\}\) to be even. Choose the doubled row, the two distinguished columns, and distribute the remaining labelled rows. Their count is exactly \(A_{m,n}\), since the distinguished-column generating factor is \(\cosh(t)^2+\sinh(t)^2=\cosh(2t)\).

The only other possible minimum sets cover every column. If \(n\ge m+2\), this requires more than \(m+1\) selections and contributes nothing. If \(n=m+1\), they have exactly one square in every column, with each row occupied an even number of times so that the induced union of row cliques has a perfect matching. They contribute \(C_{m+1,m}\) sets, disjoint from the row-covering sets: a set covering all rows and all columns would have only the doubled-row edge available and other selected vertices isolated. If \(n=m\), the column-covering families contribute another \(A_{m,m}\). A set counted in both families has exactly one doubled row and one doubled column, so the selected rook graph has at most two edges. For \(m\ge5\) it cannot have a perfect matching; for \(m=3\), both edges must be disjoint, which is achieved in exactly \(3\cdot3=9\) sets, one for each doubled-row/doubled-column choice with their crossing square unselected. Subtract those nine duplicated configurations. This completes every leading-coefficient case.

## Verification

The self-contained programs `verify_direct.py`, `verify_series.py`, and `verify_minima.py` require only Python 3.9 or newer and the standard library. Run each in a directory containing the three programs, with `python verify_direct.py`, `python verify_series.py`, and `python verify_minima.py`. Their exact tested outputs are included in the correspondingly named `.out` files. The first program enumerates all placements and directly tests induced-graph perfect matchings without using the component parity theorem; the second implements integer polynomial arithmetic from \(E^2=F(z)F(-z)\), followed by inclusion-exclusion; the third independently counts the minimum patterns from column-fiber parities. Each program reports `PASS` after checking its expected values.

The direct and series programs agree on every coefficient for boards of sizes \((2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4)\); the exact minimum counts additionally agree for \((4,5),(5,5),(5,6)\). These finite checks are not used as a proof for unbounded \(m,n\): that proof is the four-step argument above.

## Relationship to prior work

The paired-domination predicate was introduced by Haynes and Slater (1998), who studied general bounds; the exact rook-graph polynomial is not asserted there in the accessible abstract. Brešar, Henning, and Rall (2005/2007) studied paired-domination inequalities on Cartesian products; their accessible descriptions concern bounds, not cardinality enumeration. Choudhary, Margulies, and Hicks (2011 arXiv / 2013 journal) prove general inequalities for total and paired domination of Cartesian products; their available full preprint contains no rook-graph polynomial. The ordinary domination polynomial of the rook graph was computed by Mertens (2024). It counts all dominating selections, irrespective of induced perfect matchings, and is a strictly different polynomial: on the \(2\)-by-\(2\) graph its coefficient of \(z^2\) is \(6\), while the paired polynomial's coefficient is \(4\). The even-edge component test and the specific square-root exponential generating function above are the additional pairing-filter structure.

The general fact that connected even-order claw-free graphs admit perfect matchings is older; the line-graph matching lemma is not claimed as an independent novelty. The new claim is the complete two-class labelled rook-family enumeration and its minimum-count phase distinctions, not the domination rule alone or the standard labelled exponential formula.

## Limitations

The polynomial is a formal coefficient-extraction formula, not a claimed closed single-binomial sum or complexity-optimal evaluation method. No analytic asymptotic estimate and no result for other chess-move graphs is asserted. The directly checked finite boards do not prove the theorem for larger parameters. The accessible texts do not establish absolute historical priority; complete earlier publisher texts and unindexed calculations could conceivably contain the same coefficient formula or an equivalent stronger result. There has been no independent scholarly audit.

## References

1. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206, DOI `10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F` (publisher's first online date: 1998-12-07).
2. B. Brešar, M. A. Henning, and D. F. Rall, *Paired-domination of Cartesian products of graphs and rainbow domination*, Electronic Notes in Discrete Mathematics 22 (2005), 233–237, DOI `10.1016/j.endm.2005.06.059`; see also *Paired-domination of Cartesian products of graphs*, Utilitas Mathematica 73 (2007), 255–265.
3. K. Choudhary, S. Margulies, and I. V. Hicks, *A Note on Total and Paired Domination of Cartesian Product Graphs*, Electronic Journal of Combinatorics 20 (2013), P25; arXiv `1109.2174` (first posted 2011-09-09), DOI `10.37236/2535`.
4. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv `2401.00716` (first posted 2024-01-01; revised 2024-03-10), ordinary rather than paired domination.
5. The labelled exponential formula (standard combinatorial species theory) and the connected even-edge line-graph pairing lemma used in the proof, both explicitly derived above for the needed case.
