# Maximal strong independence in uniform linear edge expansions

## Finding

Let \(G\) be any finite simple graph without isolated vertices, with \(m=|E(G)|\geq1\). Fix an integer \(r\geq3\). For every edge \(e=uv\), take a set \(P_e\) of \(r-2\) new private vertices, disjoint from all other such sets, and form the \(r\)-uniform hypergraph \(\mathcal H_r(G)\) whose hyperedges are exactly \(\{u,v\}\cup P_e\). This hypergraph is linear: two distinct hyperedges meet in at most one vertex.

A strongly independent vertex set meets each hyperedge in at most one vertex. Write \(\mathcal M_{r,G}(z)\) for the cardinality polynomial of **inclusion-maximal** strongly independent sets. The complete polynomial, for every such \(G\) and \(r\), is

\[
\boxed{\mathcal M_{r,G}(z)=\sum_{\substack{X\subseteq V(G)\\G[X]\text{ edgeless}}}(r-2)^{|E(G-X)|}z^{|X|+|E(G-X)|}.}
\]

More precisely, the maximal sets are in bijection with the following decorated independent sets: choose an independent \(X\subseteq V(G)\); then choose **exactly one** private vertex from \(P_e\) for each edge \(e\) with both endpoints outside \(X\); choose no private vertices on other edges. This characterizes every maximal set, not just their sizes.

Since \(X\) is independent, \(|E(G-X)|=m-\sum_{v\in X}\deg_G(v)\). Hence the polynomial is a degree-weighted independence polynomial:

\[
\mathcal M_{r,G}(z)=((r-2)z)^m\sum_{\substack{X\subseteq V(G)\\G[X]\text{ edgeless}}}\prod_{v\in X}\frac{z^{1-\deg_G(v)}}{(r-2)^{\deg_G(v)}}.
\]

The latter is written as a Laurent-polynomial identity; cancellation gives the ordinary polynomial in the first display.

## Assumptions and scope

Graphs are finite, simple, undirected, and have no isolated vertices. The integer \(r\) is fixed and at least three; the expansion may be disconnected if \(G\) is. A *maximal* set means inclusion-maximal, not maximum cardinality. For a finite graph \(Q\), its independence polynomial is \(I(Q;y)=\sum_{X:\,Q[X]\text{ edgeless}}y^{|X|}\). A graph is \(d\)-regular when every vertex has degree \(d\). Let \(\alpha_w(G)\) be the maximum total weight of an independent vertex set in \(G\) when vertex \(v\) is assigned weight \(w(v)=\deg_G(v)-1\).

Additional consequences of the same classification include the following exact statements.

1. The smallest and largest cardinalities of inclusion-maximal strongly independent sets of \(\mathcal H_r(G)\) are, respectively,
\[
\boxed{m-\alpha_w(G)\quad\text{and}\quad m.}
\]
All such sets have the same cardinality if and only if \(G\) is a matching (a disjoint union of copies of \(K_2\)). In that case there are exactly \(r^m\) maximal sets, each of size \(m\).

2. When \(G\) is \(d\)-regular, \(d\geq1\),
\[
\boxed{\mathcal M_{r,G}(z)=(r-2)^m z^m I\!\left(G;\frac{z^{1-d}}{(r-2)^d}\right).}
\]
For the loose \(r\)-uniform cycle \(\mathcal H_r(C_n)\), \(n\geq3\), this becomes
\[
\boxed{\mathcal M_{r,C_n}(z)=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{n}{n-k}\binom{n-k}{k}(r-2)^{n-2k}z^{n-k}.}
\]

3. For \(G=K_n\), \(n\geq3\), and \(m=\binom n2\),
\[
\boxed{\mathcal M_{r,K_n}(z)=(r-2)^m z^m+n(r-2)^{m-n+1}z^{m-n+2}.}
\]
The connected linear hypergraphs \(\mathcal H_r(K_n)\) therefore have no maximal strong independent sets of cardinalities strictly between \(m-n+2\) and \(m\), an interval of \(n-3\) missing integer cardinalities.

4. At \(r=3\), counting all inclusion-maximal strongly independent sets of connected linear \(3\)-uniform hypergraphs is \(\#P\)-complete under polynomial-time counting reductions. In fact, \(\mathcal M_{3,G}(1)=I(G;1)\) for every isolate-free \(G\). This complexity statement uses the classical \(\#P\)-completeness of counting graph independent sets, not a new complexity assumption.

## Proof

**Necessity of the decorated form.** Let \(S\) be maximal strongly independent in \(\mathcal H_r(G)\), and put \(X=S\cap V(G)\). If \(X\) contained both endpoints of an edge \(e\), then \(S\) would meet the corresponding hyperedge in two vertices, contradicting strong independence. Thus \(X\) is independent.

For each edge \(e=uv\) with an endpoint in \(X\), its hyperedge already meets \(S\), so no private vertex of \(P_e\) can be in \(S\). If both endpoints of \(e\) lie outside \(X\), at most one private vertex of \(P_e\) can belong to \(S\). If none did, adjoining any private vertex of \(P_e\) would preserve strong independence, since that vertex occurs in no other hyperedge. This contradicts maximality. Thus exactly one is selected.

**Sufficiency.** Start with any independent \(X\), and pick exactly one private vertex on each edge with neither endpoint in \(X\), choosing none on the other edges. Each hyperedge now contains precisely one selected vertex, hence the constructed set is strongly independent. Any omitted private vertex is forbidden by its hyperedge's already selected representative. Consider an omitted original vertex \(v\). Because \(G\) has no isolated vertices, \(v\) lies on some edge \(e\); the hyperedge of \(e\) already contains a selected representative (an original endpoint in \(X\), or a chosen private vertex). Adjoining \(v\) violates strong independence. No single omitted vertex can be added. Strong independence is hereditary under deletion, so absence of a one-vertex extension is equivalent to inclusion-maximality. This proves the bijection.

**Weight and extremal cardinalities.** For fixed \(X\), each of the \(|E(G-X)|\) remaining edges independently offers \(r-2\) possible selected private vertices. The cardinality is \(|X|+|E(G-X)|\). Since \(X\) is independent, the edges incident to distinct vertices of \(X\) are disjoint, giving \(|E(G-X)|=m-\sum_{v\in X}\deg_G(v)\). Therefore the size equals \(m-\sum_{v\in X}(\deg_G(v)-1)\). With no isolates, all these vertex weights are nonnegative. Choosing \(X=\varnothing\) gives the maximum \(m\); maximizing the weighted independent-set sum gives the minimum \(m-\alpha_w(G)\).

If every maximal set has the same cardinality, comparing \(X=\varnothing\) with each singleton \(X=\{v\}\) gives \(m=m+1-\deg_G(v)\), hence \(\deg_G(v)=1\) for every vertex. This says \(G\) is a matching. Conversely a matching has \(m-\sum_{v\in X}(\deg_G(v)-1)=m\) for every independent \(X\), and the hyperedges are disjoint; one of their \(r\) vertices must be selected per hyperedge, giving \(r^m\) maximal sets.

**Regular graphs and cycles.** If \(\deg_G(v)=d\), the displayed Laurent-polynomial formula reduces to the independence polynomial substitution in the statement. For a labelled cycle, the independent \(k\)-subsets are counted by \(\frac{n}{n-k}\binom{n-k}{k}\): distribute \(n-2k\) unchosen vertices into the \(k\) nonempty cyclic gaps between successive chosen vertices, accounting for the \(n/k\) choices of a distinguished chosen starting vertex, and include the empty set separately. Substitution with \(m=n\) and \(d=2\) gives the cycle formula.

**Complete graphs and gaps.** Independent sets of \(K_n\) are only the empty set and \(n\) singletons. Substitution yields the two-term polynomial. For \(n\geq3\), the difference between its two exponents is \(n-2\), giving \(n-3\) strictly intermediate absent cardinalities.

**Counting complexity.** Membership in \(\#P\) is immediate: one checks a candidate vertex subset against every hyperedge and every possible single-vertex addition in polynomial time. Counting independent sets of a finite simple graph is \(\#P\)-complete (equivalently counting vertex covers). Given any nonempty graph \(Q\), let \(G=Q\vee K_1\) be its join with one universal vertex. Then \(G\) is connected without isolates and \(I(G;1)=I(Q;1)+1\). Our bijection for \(r=3\) gives \(\mathcal M_{3,G}(1)=I(Q;1)+1\). A single oracle count followed by subtracting one counts independent sets of \(Q\). The expansion \(\mathcal H_3(G)\) is connected, linear, and \(3\)-uniform. Therefore the restricted counting problem is \(\#P\)-complete under polynomial-time counting (metric) reductions. This argument does **not** claim parsimonious \(\#P\)-completeness.

## Verification

The standalone `verify.py` reconstructs the hyperedges, exhaustively tests the defining strong-independence condition for every subset, and tests maximality by every one-vertex addition. It independently builds the predicted family from base-graph independent sets and private-vertex choices, then compares the families themselves and the cardinality polynomials. It checks every labelled simple graph of orders one through four (including isolated vertices under a slightly more general checker version that forces isolated originals to be selected) for \(r=3,4\), and loose cycles on four, five, and six base vertices at both uniformities. The isolated-vertex checker extension is used only for finite testing; the theorem above assumes no isolates.

Command: `python3 verify.py`

Observed output:

`VERIFY_OK instances=156 vertex_subsets=567300 maximal_sets=2498 full_families=PASS loose_cycle_coefficients=PASS`

These finite tests do not establish the unrestricted result; its proof is the preceding bijection and deductions.

## Relationship to prior work

Barát, Gerbner and Halfpap (first publicly available as arXiv:2211.14101 on 2022-11-25) studied maximal strongly independent sets and maximal \(A\)-transversals, including sharp global upper bounds. Their accessible full paper establishes general extremal counting rather than this exact edge-expansion classification and weighted degree formula. The new claim is the complete, explicitly reconstructible count for the canonical edge-expansion family, together with the connected-linear counting reduction and strong well-covered boundary. The proof uses only the definitions of strong independence and graph independence.

The \(3\)-uniform case is the maximal-independent-set problem of the two-section graph of an edge corona with a single private vertex per edge. Related work on **independent domination numbers** of edge-corona graphs (Cabrera-Martínez et al., 2026) is a significant priority risk: its accessible abstract discusses minimum sizes, but its subscription-only full theorem was not available for comparison. The current statement does not claim novelty for any independently known minimum-size formulas. Work on independent semitotal domination in edge coronas (Susada and Eballe, 2023) adds a distance-two requirement not present here.

## Limitations

The theorem concerns specifically uniform linear hypergraphs in which each hyperedge contains two original graph vertices and a disjoint set of private vertices. It does not characterize maximal strongly independent sets of arbitrary linear hypergraphs. The complexity corollary uses counting reductions, not a parsimonious reduction. The cycle and clique formulas are consequences of the general theorem, not separate discoveries. Priority remains provisional, particularly because the complete text of the 2026 edge-corona independent-domination paper was inaccessible; an equivalent classification or stronger theorem there would supersede the present originality claim. No independent mathematical audit has been performed.

## References

1. J. Barát, D. Gerbner and A. Halfpap, *On the number of A-transversals in hypergraphs*, arXiv:2211.14101 (first version 2022-11-25), later *Periodica Mathematica Hungarica* 89 (2024), 107–115. https://arxiv.org/html/2211.14101 ; https://doi.org/10.1007/s10998-024-00586-1
2. J. S. Provan and M. O. Ball, *The complexity of counting cuts and of computing the probability that a graph is connected*, *SIAM J. Comput.* 12 (1983), 777–788. https://doi.org/10.1137/0212053
3. B. L. Susada and R. G. Eballe, *Independent semitotal domination in the corona of graphs*, *Adv. Appl. Discrete Math.* 39 (2023), 89–98. https://doi.org/10.17654/0974165823038
4. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar and A. Serrano-Díaz, *Independent Domination and k-Tuple (Total) Domination in Edge Corona Graphs*, *Bull. Iran. Math. Soc.* 52 (2026), article 48. https://doi.org/10.1007/s41980-026-01067-6 (abstract available; full text not inspected).
