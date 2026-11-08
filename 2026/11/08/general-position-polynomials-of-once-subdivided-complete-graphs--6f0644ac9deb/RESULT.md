# General-position polynomials of once-subdivided complete graphs

## Finding
For every integer \(n\ge3\), let \(H_n\) be the graph obtained by subdividing each edge of the complete graph \(K_n\) exactly once. Its original vertices form \([n]\), and \(w_{ab}\) denotes the new vertex on the edge \(ab\). A general-position set contains no three vertices lying on a common shortest path.

Put \(\Psi_n(z)=\sum_{S\subseteq V(H_n)\text{ general-position}}z^{|S|}\). Then
\[
\boxed{\Psi_n(z)=n![t^n]\exp\!\left((1+z)t+t(e^{zt}-1)-\frac{zt^2}{2}+\frac{z^3t^3}{6}\right)+n(n-1)z^2.}
\]
The coefficient notation is formal: \([t^n]\) extracts the coefficient of \(t^n\) in a formal power series in \(t\) with coefficients in \(\mathbb Z[z]\).

In particular the largest general-position set has exactly \(n\) vertices and the number of such maximum sets is
\[
\boxed{\sum_{j=0}^{\lfloor n/3\rfloor}\frac{n!}{6^j j!(n-3j)!}.}
\]
There is a complete set-system description of all general-position sets, including configurations mixing original and subdivision vertices, given below.

## Assumptions and scope
Graphs are finite, undirected, and simple. Define \(E=\binom{[n]}2\). Every subset \(X\subseteq V(H_n)\) has the unique expression
\[
X=A\cup\{w_e:e\in F\},\qquad A\subseteq[n],\quad F\subseteq E.
\]
Write \(U(F)=\bigcup_{e\in F}e\), with \(U(\varnothing)=\varnothing\). Regard \(F\) as a vertex subset of the line graph \(L(K_n)\), in which two edges of \(K_n\) are adjacent precisely when they intersect. The exact criterion is:

* \(F=\varnothing\): every \(A\subseteq[n]\) is admissible;
* \(|F|=1\), say \(F=\{ab\}\): either \(A\cap\{a,b\}=\varnothing\), or \(A=\{a\}\), or \(A=\{b\}\);
* \(|F|\ge2\): the induced line graph \(L(K_n)[F]\) has no induced three-vertex path, and \(A\subseteq[n]\setminus U(F)\).

For \(|F|=1\), the line-graph condition is automatic. For \(|F|\ge2\), it is equivalent to the selected edge family \(F\) being a vertex-disjoint union of edge-stars and triangles in \(K_n\). A single edge counts as a star; a triangle means all three edges on three vertices, rather than a two-edge star on three vertices.

## Proof
**1. All relevant graph distances.** Distinct original vertices \(u,v\) have distance \(2\). An original vertex \(u\) and a subdivision vertex \(w_e\) have distance \(1\) when \(u\in e\) and \(3\) otherwise. Two different subdivision vertices \(w_e,w_f\) have distance \(2\) when their edges share an endpoint, and distance \(4\) when the edges are disjoint. The last assertion follows by moving from either selected edge to an endpoint, crossing to the other edge by a subdivision vertex, and reaching the destination; the graph is bipartite and no shorter route is possible. These distances also apply when \(n=3\).

**2. Three subdivision vertices.** Suppose \(e,f,g\) are distinct. The vertex \(w_g\) lies on a shortest path between \(w_e\) and \(w_f\) precisely when \(e\cap f=\varnothing\), while \(g\) meets both \(e\) and \(f\). This is exactly an induced three-vertex path with middle vertex \(g\) in \(L(K_n)[F]\). Thus the selected subdivision vertices are in general position if and only if \(L(K_n)[F]\) is induced-\(P_3\)-free, equivalently a disjoint union of cliques.

**3. Mixed triples.** Three original vertices never obstruct general position because all distinct original pairs have distance \(2\). For one subdivision vertex \(w_{ab}\) and two distinct originals, an obstruction occurs exactly if one original is in \(\{a,b\}\), with the other original arbitrary: if the other is the second endpoint then \(w_{ab}\) is between the originals, and if the other lies outside that pair then the incident original lies between \(w_{ab}\) and the other original. Thus, with just one selected subdivision vertex, the criterion for \(A\) is exactly that in the statement.

For two selected subdivision vertices \(w_e,w_f\) and a selected original \(u\), any occurrence of \(u\in e\cup f\) makes the triple non-general-position: if \(e\cap f=\{u\}\), then \(u\) is between \(w_e\) and \(w_f\); if \(u\in e\setminus f\), then \(w_e\) is between \(u\) and \(w_f\) when \(e\cap f\ne\varnothing\), while \(u\) is between \(w_e\) and \(w_f\) when \(e\cap f=\varnothing\). The remaining cases are symmetric. Conversely, if \(u\notin e\cup f\), the pairwise distances are \(3,3\) and \(2\) or \(4\), none of which is the sum of the other two. Therefore two or more subdivision vertices require exactly that \(A\cap U(F)=\varnothing\). This proves the claimed full classification.

**4. Structure of the selected edges.** An induced-\(P_3\)-free finite graph has complete connected components. A family of at least two pairwise intersecting edges of a complete graph is either a star centered at one original vertex or exactly the three edges of a triangle (the latter when no common center exists). If two distinct complete components of the line graph shared an original vertex, edges from those components would be adjacent, impossible. Thus their supports are disjoint.

**5. Enumeration.** Apart from the singleton-edge cases with \(A\) equal to one endpoint, each allowable configuration corresponds bijectively to a set partition of \([n]\) into independent blocks of the following types:

* an uncovered singleton, with weight \(1+z\) (original vertex unselected or selected);
* a two-element block representing its unique selected edge, with weight \(z\);
* a three-element block representing one of its three two-edge stars, with total weight \(3z^2\), or its triangle, with weight \(z^3\);
* a \(k\)-element block, for \(k\ge4\), representing one of the \(k\) stars with \(k-1\) selected edges, with weight \(kz^{k-1}\).

The labelled exponential formula for these unordered disjoint blocks gives the exponential generating series
\[
\exp\!\left((1+z)t+\frac{zt^2}{2}+\frac{(3z^2+z^3)t^3}{6}+\sum_{k\ge4}\frac{kz^{k-1}t^k}{k!}\right).
\]
The exponent simplifies to \((1+z)t+t(e^{zt}-1)-zt^2/2+z^3t^3/6\). The omitted exceptional configurations consist of a choice of edge \(ab\) and either selected endpoint \(a\) or \(b\), so add exactly \(2\binom n2z^2=n(n-1)z^2\). This proves the polynomial identity.

**6. Maximum cardinality.** A star block of size \(k\) contributes \(k-1\) selected vertices, while a triangle block of size three contributes three. An uncovered singleton contributes at most one, and a singleton-edge exception contributes two vertices on a support of two, but leaves all other original vertices unselected. Hence the total is at most \(n\), attained by the set of all \(n\) original vertices. For equality, no star block can occur, every uncovered singleton must be selected, and all nonsingleton blocks must be triangles. Each partition of \([n]\) into singleton blocks and \(j\) unordered triples gives exactly one maximum set. The number of these partitions is \(n!/(6^j j!(n-3j)!)\), and summing over \(j\) proves the second formula.

## Verification
The standalone file `verify.py` uses only the Python standard library. It builds \(H_n\) directly, computes all-pairs shortest-path distances by breadth-first search and detects forbidden selected triples without assuming the structural characterization. For \(n=3,4,5\), every vertex subset is checked against the characterization and the polynomial recurrence: \(64\), \(1024\), and \(32768\) subsets respectively. For \(n=6\), \(40000\) reproducibly sampled subsets are checked directly and the complete polynomial is separately checked by enumerating every possible selected subdivision-edge family. Top coefficients and degree are compared to the partition formula for every \(3\le n\le20\).

The verified outputs are \(\Psi_3(z)=1+6z+15z^2+2z^3\), \(\Psi_4(z)=1+10z+45z^2+30z^3+5z^4\), and \(\Psi_5(z)=1+15z+105z^2+175z^3+100z^4+11z^5\). All checks passed. These finite tests independently corroborate the formula but do not establish the unrestricted theorem; that follows from Steps 1–6.

## Relationship to prior work
Iršič, Klavžar, Rus and Tuite introduced general-position polynomials and computed them for several graph families and operations; their accessible complete article does not state this subdivision-of-complete-graphs polynomial. Ghorbani, Klavžar, Maimani, Momeni, Rahimi Mahid and Rus established the general-position number of \(L(K_n)\) and used its clique-component decomposition. That work covers the selected-edge-only structure and its maximum; neither this known fact nor the general induced-clique partition characterization of Anand and collaborators is claimed as new. The contribution here is the **joint original/subdivision-vertex classification** and the exact full-size enumerator, including the exceptional two-vertex configurations, with its maximum-set count.

## Limitations
The result applies to one subdivision per edge of a complete graph, not to arbitrary subdivisions, arbitrary host graphs or other geodesic invariants. Its originality is provisional pending independent literature and mathematical assessment. The selected-edge-only structural condition is a natural specialization of prior line-graph general-position work; the novelty claim is restricted to the mixed-vertex enumeration and resulting formulas. A matching formula might appear under incidence graphs, line-graph duality or geodesic irredundance terminology. Computations on small orders do not prove the general statement.

## References
1. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696, first posted January 11, 2024; *Results in Mathematics* 79 (2024), article 110. https://arxiv.org/abs/2401.05696
2. M. Ghorbani, S. Klavžar, H. R. Maimani, M. Momeni, F. Rahimi Mahid and G. Rus, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286; *Discussiones Mathematicae Graph Theory* 41 (2021), 1199–1213. https://arxiv.org/abs/1903.04286
3. B. S. Anand, S. V. Ullas Chandran, M. Changat, S. Klavžar and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460. https://arxiv.org/abs/1812.08460
