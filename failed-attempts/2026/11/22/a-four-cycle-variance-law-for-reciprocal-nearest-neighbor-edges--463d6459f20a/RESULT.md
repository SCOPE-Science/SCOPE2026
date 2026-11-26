# A four-cycle variance law for reciprocal nearest-neighbor edges in randomly weighted graphs

## Finding
Let \(G=(V,E)\) be any finite loopless simple graph. Assign its edges independent identically distributed atomless real weights. A reciprocal nearest-neighbor edge \(e=uv\) is the minimum-weight incident edge at **both** \(u\) and \(v\). Let \(X_e\) indicate this event and \(M_G=\sum_{e\in E}X_e\).

For each edge \(e=uv\), put \(a_e=d(u)+d(v)-1\). For distinct vertex-disjoint edges \(e,f\), put \(h_{ef}\) equal to the number of host-graph edges joining one endpoint of \(e\) to one endpoint of \(f\). Then the **complete pairwise covariance law** is
\[
\mathbb E X_e=\frac1{a_e},\qquad
\operatorname{Cov}(X_e,X_f)=
\begin{cases}
-1/(a_e a_f),&e,f\text{ share an endpoint},\\[2pt]
h_{ef}/\{a_ea_f(a_e+a_f-h_{ef})\},&e,f\text{ are disjoint}.
\end{cases}
\]
In particular, distinct reciprocal-edge events have strictly negative covariance when their edges touch, strictly positive covariance when their edges are vertex-disjoint but joined by at least one host edge, and covariance zero otherwise. A family of these indicators is mutually independent **if and only if** its underlying edge set is an induced matching.

For a second structural conclusion, suppose \(G\) is \(d\)-regular and triangle-free, with \(d\ge2\) and \(m=|E|\). Write \(c_4(G)\) for its number of unoriented simple four-cycles. Then
\[
\boxed{\mathbb E M_G=\frac{m}{2d-1},\quad
\operatorname{Var}(M_G)=
\frac{2m(d-1)^2}{(2d-1)^2(4d-3)}
+\frac{2c_4(G)}{(d-1)(2d-1)^2(4d-3)}.}
\]
Consequently the variance attains its exact girth-five baseline if and only if \(c_4(G)=0\); each four-cycle adds precisely the positive coefficient shown. Hence the four-cycle count is exactly recoverable from the variance when \(m,d\) are known. As an example, for \(K_{d,d}\), \(\operatorname{Var}(M_G)=d^2(d-1)/[2(2d-1)^2]\).

## Assumptions and scope
All graphs are finite, undirected, simple, with no loops or parallel edges; isolated vertices may be present but contribute no reciprocal edge. Every weight has the same atomless distribution, independently across different unordered host edges. The random weights are **shared** by the two ends of each edge, unlike independently sampled directed preferences. Ties have probability zero. Distinct edge pairs and all finite graphs are covered by the covariance formula. Regularity, triangle-freeness, and \(d\ge2\) are required **only** for the four-cycle variance identity. Counts of four-cycles are unoriented and unrooted, each cycle counted once.

## Proof
**Distribution-free reduction.** Applying the common continuous distribution function to the edge weights preserves their strict ordering almost surely. We may therefore take every edge weight to be independent uniform on \((0,1)\). The event \(X_e=1\) says that the weight of \(e\) is smallest among its closed edge-neighborhood: the \(a_e\) edges incident to either endpoint, counting \(e\) once. Symmetry yields \(\mathbb E X_e=1/a_e\).

**Joint law of two edges.** If \(e\) and \(f\) touch, they cannot both be minimal at their shared vertex, so their joint probability is zero. Suppose instead their endpoints are disjoint. Write \(a=a_e\), \(b=a_f\), \(h=h_{ef}\). The respective closed edge-neighborhoods intersect in exactly the \(h\) edges running between their endpoint pairs. In particular \(0\le h\le\min(a-1,b-1)\). Conditional on the weights \(x,y\) of \(e,f\), the joint event has probability
\[
(1-x)^{a-h-1}(1-y)^{b-h-1}(1-\max(x,y))^h.
\]
Split the unit square at \(x=y\). In the half \(x>y\), integrating first over \(y\) gives
\[
\int_0^1 (1-x)^{a-1}\left(\int_0^x(1-y)^{b-h-1}\,dy\right)dx
=\frac1{a(a+b-h)}.
\]
The half \(y>x\) contributes \(1/[b(a+b-h)]\). Consequently
\[
\Pr(X_e=X_f=1)=\frac{a+b}{ab(a+b-h)},
\]
whose difference from \(1/(ab)\) is exactly \(h/[ab(a+b-h)]\). The three covariance signs follow, with no asymptotic assumption.

**Independence.** If a set of edges forms an induced matching, their closed edge-neighborhoods are disjoint, so their indicator events depend on disjoint collections of weights and are jointly independent. Conversely, if the set is not an induced matching, it has a touching pair or a disjoint pair connected by a cross edge. The preceding strictly nonzero covariance rules out even pairwise independence, hence rules out mutual independence.

**Second moment on an arbitrary host.** By expanding the variance of \(M_G\),
\[
\operatorname{Var}(M_G)=\sum_{e\in E}\frac{a_e-1}{a_e^2}
-2\sum_{\{e,f\}:e\cap f\ne\varnothing}\frac1{a_ea_f}
+2\sum_{\{e,f\}:e\cap f=\varnothing}
\frac{h_{ef}}{a_ea_f(a_e+a_f-h_{ef})},
\]
where the sums over edge pairs are unordered and distinct. This exact formula works for every finite host.

**Triangle-free regular specialization.** In a \(d\)-regular host each \(a_e=2d-1=:a\). There are exactly \(m(d-1)\) unordered touching pairs of edges. For every edge \(g=uv\), choosing another edge at \(u\) and another at \(v\) produces \((d-1)^2\) disjoint-edge pairs because a common third endpoint would create a triangle. Each choice witnesses one crossing edge between the two selected edge pairs. Thus
\[
\sum_{\{e,f\}\text{ disjoint}}h_{ef}=m(d-1)^2.
\]
Triangle-freeness also forces \(h_{ef}\in\{0,1,2\}\), because the cross edges must themselves form a matching between the two endpoint pairs. The \(h_{ef}=2\) cases are precisely opposite-edge pairs of four-cycles, with exactly two such pairs for each four-cycle. Hence \(N_2=2c_4(G)\) and \(N_1=m(d-1)^2-4c_4(G)\). The diagonal variance \(m(a-1)/a^2=2m(d-1)/a^2\) exactly cancels the negative touching-pair contribution \(-2m(d-1)/a^2\). The surviving variance is
\[
\frac2{a^2}\left(\frac{N_1}{2a-1}+\frac{2N_2}{2a-2}\right)
=\frac{2m(d-1)^2}{a^2(2a-1)}
+\frac{4c_4(G)}{a^2(a-1)(2a-1)},
\]
which is the displayed identity after substituting \(a=2d-1\). The coefficient of \(c_4(G)\) is strictly positive. Finally \(K_{d,d}\) has \(m=d^2\) and \(c_4=\binom d2^2\); substitution and simplification give the example.

## Verification
Run `python VERIFY.py` using the Python standard library. The independent exhaustive finite check enumerates **every ranking** of the edges for every simple graph on at most four vertices, together with a deterministic selection of larger sparse graphs, and compares exact event probabilities with the formulas. Further rational checks cover paths, cycles, complete bipartite hosts, the Petersen graph and the Heawood graph. The delivered script prints `VERIFY_OK 11732 assertions` and `REGULAR_FORMULA_OK 13598 assertions total`. These finite checks do not establish the all-graph statements: the integral and graph-counting arguments above do.

## Relationship to prior work
The random-nearest-neighbor construction on weighted lattices originates in work of Nanda and Newman (1999), while Pittel and Weishaar (1999) study a bipartite nearest-neighbor construction and its matching behavior. Bock, Damron and Hanson (2020 preprint; 2023 journal) investigate translation-invariant nearest-neighbor structures. These works motivate the probability model but do not, in their inspected accessible material, assert the present finite arbitrary-host pairwise formula or its four-cycle variance identity. The publicly available *Exact mutual-nearest-neighbor component law in symmetric random-link graphs* proves stronger **all-order** matching probabilities for the **complete graph**, and already contains the positive covariance of two disjoint candidate edges in that model; that special case is expressly credited and not claimed here. The previously known mean and variance of mutual nearest-neighbor counts on a uniform circle also coincide with our cycle-host example, so those marginal numbers are not claimed original. The assessed contribution is the arbitrary-host covariance geometry and its exact four-cycle rigidity in regular triangle-free networks.

## Limitations
Independent identically distributed atomless **undirected** edge weights are essential; dependence, heterogeneous distributions, directed independent priorities or geometric metric constraints can change the law. The variance identity does not apply as stated to graphs containing triangles or to irregular graphs, though the pairwise formula and general variance expansion still do. It neither identifies the full distribution of \(M_G\) nor proves a central limit theorem. An inaccessible historical nearest-neighbor paper and possible general published local-minimum formulas leave some priority uncertainty. These qualifications do not affect the elementary finite exact proof. Independent audit has not been performed.

## References
1. S. Nanda and C. M. Newman, *Random nearest neighbor and influence graphs on \(\mathbb Z^d\)*, Random Structures & Algorithms 15 (1999), 262–278. https://doi.org/10.1002/(SICI)1098-2418(199910/12)15:3/4%3C262::AID-RSA5%3E3.0.CO;2-7
2. B. Pittel and R. S. Weishaar, *The random bipartite nearest neighbor graphs*, Random Structures & Algorithms 15 (1999), 279–310. First publicly dated October 20, 1999. https://doi.org/10.1002/(SICI)1098-2418(199910/12)15:3/4%3C279::AID-RSA6%3E3.0.CO;2-J
3. B. Bock, M. Damron and J. Hanson, *Random nearest neighbor graphs: The translation invariant case*, arXiv preprint first submitted June 29, 2020. https://arxiv.org/abs/2006.16347
4. *Exact mutual-nearest-neighbor component law in symmetric random-link graphs*, publicly accessible mathematical note, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-mutual-nearest-neighbor-component-law-in-symmetric-random--f51047a8a8b8/RESULT.md
