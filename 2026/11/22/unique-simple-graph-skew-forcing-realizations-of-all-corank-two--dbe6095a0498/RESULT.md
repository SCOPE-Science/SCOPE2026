# Unique simple-graph skew-forcing realizations of all corank-two matroids

## Finding

**Theorem (existence and uniqueness).** Let \(M\) be any matroid on a finite, specified labelled ground set \(V\), with \(|V|=n\ge2\) and \(r(M)=n-2\). Define skew-zero-forcing closure on a finite simple graph by initially filling \(S\subseteq V\), then repeatedly filling the unique unfilled neighbor of any vertex (including an unfilled vertex) that has exactly one unfilled neighbor. Write \(\operatorname{scl}_G(S)\) for the terminal filled set. There is exactly **one** simple graph \(G\) with vertex set \(V\) satisfying

\[\operatorname{scl}_G(S)=\operatorname{cl}_M(S)\quad\text{for every }S\subseteq V.\]

Explicitly, form the rank-two dual \(P=M^*\). Let \(L\) be the loops of \(P\), and let \(V_1,\ldots,V_r\), where \(r\ge2\), be the parallel classes of its nonloops. Then \(G\) has exactly the edges joining two vertices in different classes \(V_i\), and has no edges incident to \(L\). Equivalently, it is a complete multipartite component together with isolated vertices. Conversely, every graph of this form has a skew-zero-forcing matroid of rank \(|V|-2\), and its dual parallel classes and loops recover its graph uniquely.

**Exact initial-set and matroid invariants.** Put \(m_i=|V_i|\), \(N=\sum_i m_i\), and \(\ell=|L|\). The complete polynomial recording all initial sets that force every vertex, by their cardinality, is

\[\mathcal F_G(z)=z^\ell\left(z^N+Nz^{N-1}+\left(\sum_{i<j}m_i m_j\right)z^{N-2}\right).\]

The minimum sets are **exactly** \(V\setminus\{u,v\}\) with \(u\in V_i\), \(v\in V_j\), \(i\ne j\); their number is the number of edges of \(G\). Their single-vertex-exchange graph is the line graph of the nontrivial multipartite component (with one vertex when that component is a single edge).

The Tutte polynomial of the induced matroid is given, as a polynomial identity with removable apparent denominators, by

\[T_M(x,y)=x^\ell\left((y-1)^2+(y-1)\sum_{i=1}^r\frac{x^{m_i}-1}{x-1}+\frac{x^N-\sum_{i=1}^r x^{m_i}+r-1}{(x-1)^2}\right).\]

## Assumptions and scope

All graphs are finite, undirected, simple, and labelled on exactly the matroid's ground set. Graphs may contain isolated vertices but not loops or multiple edges. Skew forcing permits an unfilled vertex to force. Matroid loops, parallelism, duality, closure, circuits, hyperplanes and the Tutte polynomial have their standard meanings. Rank \(n-2\) is matroid corank two, **not** matroid rank two. The theorem includes the smallest case \(n=2\), in which the unique realizing graph is \(K_2\). No claim is made about uniqueness among multigraphs or graph realizations of matroids of other coranks.

## Proof

**1. Rank-two structure.** A rank-two matroid \(P\) consists of its loop set \(L\) and at least two nonempty parallel classes \(V_1,\ldots,V_r\) of nonloops. Its rank-one hyperplanes are precisely \(L\cup V_i\). Thus the circuits of its dual \(M=P^*\) are exactly the cocircuits of \(P\):

\[C_i=V\setminus(L\cup V_i)=\bigcup_{j\ne i}V_j,\qquad 1\le i\le r.\]

There are no additional circuits: cocircuits of a matroid are exactly complements of its hyperplanes, and these are all the hyperplanes of \(P\). The sets \(C_i\) are nonempty since \(r\ge2\).

**2. Graph realization.** Construct \(G\) by joining vertices in distinct nonloop parallel classes, leaving all vertices of \(L\) isolated. Every vertex in \(V_i\) has open neighborhood \(N_G(v)=C_i\). Every vertex in \(L\) has empty neighborhood. Consequently, a skew forcing step adds precisely the unique currently unfilled element of a circuit \(C_i\). The matroid circuit characterization of closure says that \(e\in\operatorname{cl}_M(S)\setminus S\) exactly when a circuit \(C\) satisfies \(C\setminus S=\{e\}\). At the first step, every such circuit is an actual neighborhood, so the corresponding element can be forced; conversely, each forcing step is a valid circuit-closure step. Repeating this argument gives the identical terminal closures on **every** initial set. (Alternatively, this is the explicit hypothesis of Hall–Pfeil–Taylor, Proposition 2.10; the preceding argument proves the special case directly.)

**3. Uniqueness of the simple graph.** Suppose another finite simple graph \(H\) has \(\operatorname{scl}_H=\operatorname{cl}_M\). The smallest spanning set of the matroid has cardinality \(r(M)=n-2\), so the skew-zero-forcing number of \(H\) is \(n-2\). Skew forcing acts independently on connected components, hence its minimum cardinality adds over components. Each isolated vertex contributes one. Every connected component \(D\) with at least two vertices admits a skew forcing set of size at most \(|D|-2\): choose any edge, initially fill all other vertices, and the two endpoints force each other. Therefore \(H\) has exactly one nontrivial component (otherwise its total skew-forcing number is at most \(n-4\)), and that component has skew-forcing number exactly its order minus two. By DeAlba's 2014 Theorem 3.3, every connected graph with that equality is complete multipartite. Writing its partite classes as \(W_j\), Step 2 identifies the dual of its skew-forcing matroid as a rank-two matroid with loops at the isolates and nonloop parallel classes \(W_j\). Since this matroid is \(P=M^*\), its loop set and nonloop parallel classes are necessarily \(L\) and \(V_i\), up to ordering. Thus the edges of \(H\) are uniquely determined, so \(H=G\) as graphs on the labelled set \(V\).

**4. Enumeration and Tutte polynomial.** Every spanning set of a rank-\(n-2\) matroid contains a basis of that size, and the bases of \(M=P^*\) are complements of bases of \(P\). A basis of \(P\) is exactly a pair from different nonloop parallel classes. The successful sets therefore have precisely three sizes: \(n-2\) for each such complementary pair, \(n-1\) for each choice of one omitted nonisolated vertex (\(N\) choices), and \(n\) for the full vertex set. No initial set omitting an isolated vertex succeeds. This gives \(\mathcal F_G(z)\). Two bases of \(M\) exchange one element precisely when their two-vertex complements, which are edges of \(G\), share an endpoint; that is the line-graph assertion.

For the Tutte identity, enumerate subsets of \(P\)'s nonloop ground set \(U=V\setminus L\) by rank. The empty set has rank zero; each nonempty subset lying inside one \(V_i\) has rank one; all remaining subsets have rank two. The rank-generating sum defining \(T_P\) is

\[T_P(a,b)=(a-1)^2+(a-1)\sum_i\frac{b^{m_i}-1}{b-1}+\frac{b^N-\sum_i b^{m_i}+r-1}{(b-1)^2}.\]

The numerator of the last term has a double zero at \(b=1\), so its quotient is a polynomial. Duality gives \(T_{P^*}(x,y)=T_P(y,x)\); the \(\ell\) isolated graph vertices are coloops of \(M\), contributing the factor \(x^\ell\). This proves the formula and completes the theorem.

## Verification

A standalone Python 3 checker implements the skew color-change rule and, independently, computes the dual rank formula

\[r_M(S)=|S|-2+\min\left\{2,\#\{i:V_i\cap(V\setminus S)\ne\varnothing\}\right\}.\]

For every integer-partition multipartite component with \(2\le N\le9\) and each permitted choice of zero, one, or two isolates up to ten total vertices, it exhaustively compares all subset closures, enumerates minimum forcing sets, and evaluates the Tutte polynomial independently at four pairs of integer arguments. The completed run covered 232 graph instances and 101,132 initial subsets, ending in `VERIFY_OK`. Finite enumeration corroborates, but does not substitute for, the unrestricted proof above. Run `python3 verify.py` to reproduce these checks.

## Relationship to prior work

DeAlba (2014), Theorem 3.3, proved the scalar characterization of connected complete multipartite graphs by skew-zero-forcing number equal to order minus two; that theorem is used in Step 3, and its scalar result is not new here. DeAlba also identified matching-matroid bases in certain bipartite graphs. Cooper and Fickes (2023), Proposition 3.16, proved that complete bipartite graphs have a matroidal skew closure and studied the associated kernel matroid. Hall, Pfeil and Taylor (2026), Theorem 2.1 and Proposition 2.10, addressed uniform matroid realizability and provided a general circuit-neighborhood sufficient condition, respectively. In particular, the realizability of uniform corank-two matroids was already known.

The present result identifies the precise dual parallel-class matroid for **every** multipartite graph, including nonbipartite cases and isolates, and deduces a unique *simple-graph* realization for **every** corank-two matroid, not just the uniform subclass. Searches of accessible mathematical records and related work did not reveal that complete realization-and-uniqueness classification; this is a priority assessment, not a proof of historical uniqueness.

## Limitations

No result is claimed for non-simple graph realizations, matroid corank greater than two, or arbitrary graph closure operators. The uniqueness proof uses a published characterization by DeAlba; it is not independent of that literature. The Tutte identity and enumerators are formal polynomial identities, not claims about a new general algorithm. A historical-priority search cannot exclude all unindexed or inaccessible publications. Independent mathematical validation has not been performed.

## References

1. L. M. DeAlba, *Some results on minimum skew zero forcing sets, and skew zero forcing number* (2014), Theorem 3.3 and Section 4. https://arxiv.org/html/1404.1618v2
2. J. Cooper and G. Fickes, *Zero loci of nullvectors and skew zero forcing in graphs and hypergraphs* (2023), Section 3, Proposition 3.16. https://arxiv.org/abs/2303.17419
3. D. Hall, S. Pfeil and J. Taylor, *Skew Zero Forcing Matroids* (first public 2026-11-11), Theorem 2.1 and Proposition 2.10. https://arxiv.org/html/2611.15741v1
