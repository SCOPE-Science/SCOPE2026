# A sharp one-third–one-half isolation peak window for sparse habitat networks

## Finding

**Theorem (sparse-network isolation-peak window).** Let \(G=(V,E)\) be any finite simple undirected graph with \(n=|V|\ge2\), no vertices of degree zero, and \(m=|E|\le n\). Retain each vertex independently with the common probability \(p\in[0,1]\), retain all edges whose endpoints survive, and let \(I_G(p)\) be the number of singleton connected components in this induced surviving graph. Then the expectation \(J_G(p)=\mathbb E[I_G(p)]\) has exactly one maximizer \(p_*\), with strict increase for \(p<p_*\) and strict decrease for \(p>p_*\), and

\[
\frac13\le p_*\le\frac12.
\]

The lower equality holds precisely when \(G\) is \(2\)-regular (a disjoint union of cycles), and the upper equality holds precisely when \(G\) is \(1\)-regular (a disjoint union of edges). All other qualifying graphs have \(1/3<p_*<1/2\). Paths and stars of increasing order approach the lower and upper bounds, respectively, while remaining connected trees.

The edge budget is sharp for the universal lower endpoint: add one chord to a cycle on any \(n\ge4\) vertices, creating \(m=n+1\). This graph has a unique peak at a probability \(p_*<1/3\). Unimodality cannot be extended to arbitrary dense connected networks: attaching one leaf to a vertex of \(K_{13}\) gives two distinct strict local peaks of the expectation.

## Assumptions and scope

The vertices are fixed possible habitat patches, and an edge represents a fixed traversable connection between two patches whenever both survive. Vertex survival indicators are mutually independent and identically distributed. The graph may be disconnected but has no original isolated vertices. The statistic counts *single surviving patches with no surviving neighbor*, not failed patches, isolated edges, all connected components, or the probability of an isolated patch existing. The conclusion concerns the **expectation**, not almost-sure fragmentation or the full distribution.

Write \(d_v\) for vertex degrees and \(a_d=|\{v\in V:d_v=d\}|\) for their degree counts; these counts are nonnegative integers with \(a_0=0\). Let \(q=1-p\) denote failure probability. For each vertex, the event of being a surviving singleton occurs precisely when that vertex survives and all its neighbors fail. Therefore

\[
J_G(p)=p\sum_{v\in V}(1-p)^{d_v},\qquad F_G(q):=J_G(1-q)=(1-q)\sum_{d\ge1}a_dq^d.
\]

## Proof

**1. Degree-budget identity.** The handshaking lemma gives \(\sum_{d\ge1}d a_d=2m\) and \(\sum_{d\ge1}a_d=n\). Subtracting twice the latter yields

\[
a_1=2(n-m)+\sum_{d\ge3}(d-2)a_d.\tag{1}\]

In particular the number of leaves (degree-one vertices) controls the excess degree in the sparse regime.

**2. Derivative signs at the universal endpoints.** Direct differentiation, valid for \(0<q\le1\), gives

\[
F'_G(q)=\sum_{d\ge1}a_d q^{d-1}\bigl(d-(d+1)q\bigr).
\]

For \(0<q<1/2\) every summand is nonnegative and at least one is strictly positive, hence \(F'_G(q)>0\). At the two relevant endpoints,

\[
F'_G(1/2)=\sum_{d\ge2}\frac{(d-1)a_d}{2^d}\ge0,\tag{2}
\]
\[
3F'_G(2/3)=-a_1+\sum_{d\ge3}(d-2)a_d(2/3)^{d-1}
=-2(n-m)-\sum_{d\ge3}(d-2)a_d\bigl(1-(2/3)^{d-1}\bigr)\le0.\tag{3}
\]

Equation (2) vanishes exactly when every vertex has degree one. Equation (3) vanishes exactly when \(m=n\) and no vertex has degree at least three; (1) then gives \(a_1=0\), so all vertices have degree two.

**3. Strict concavity on the decisive interval.** For \(q\ge1/2\), differentiate once more to obtain

\[
F''_G(q)=-2a_1+2a_2(1-3q)
+\sum_{d\ge3}a_d\,d q^{d-2}\bigl((d-1)-(d+1)q\bigr).\tag{4}
\]

The degree-two coefficient satisfies \(2(1-3q)\le-1\). For each integer \(d\ge3\), the maximum of the degree-\(d\) coefficient over \(0\le q\le1\) occurs at \(q=(d-2)/(d+1)\) and equals

\[
d\left(\frac{d-2}{d+1}\right)^{d-2}<2(d-2).\tag{5}\]

For \(d=3\) the left side is \(3/4<2\); for \(d\ge4\) it is strictly smaller than \(d\le2(d-2)\). Combining (1), (4), and (5), for \(1/2\le q\le1\) we obtain

\[
F''_G(q)\le-2a_1-a_2+2\sum_{d\ge3}(d-2)a_d=-4(n-m)-a_2\le0.\tag{6}
\]

If some vertex has degree at least three, inequality (5) makes the first comparison strict; otherwise \(F''_G(q)=-2a_1+2a_2(1-3q)<0\), since \(n\ge2\) and there are no isolated vertices. Thus \(F''_G(q)<0\) throughout \([1/2,1]\).

Since \(F'_G(1/2)\ge0\), \(F'_G(2/3)\le0\), and \(F'_G\) is strictly decreasing on \([1/2,1]\), it has exactly one zero \(q_*\in[1/2,2/3]\). By positivity for \(q<1/2\) and strict decrease to \(F'_G(1)=-n<0\), this is the unique global maximum of \(F_G\). Reversing the parameter gives \(p_*=1-q_*\), the stated interval, monotonicities, and equality cases.

**4. Sharpness within connected trees.** For a path on \(n\ge3\) vertices the degree counts are \(a_1=2\), \(a_2=n-2\), so its stationarity equation is

\[
2(1-2q)+(n-2)(2q-3q^2)=0.
\]

As \(n\to\infty\), its unique root in \([1/2,2/3]\) tends to \(q=2/3\), hence \(p_*\to1/3\). For a star on \(n\ge3\) vertices, \(a_1=n-1\), \(a_{n-1}=1\), and the equation is

\[
(n-1)(1-2q)+q^{n-2}\bigl((n-1)-nq\bigr)=0.
\]

Its unique root tends to \(1/2\), so \(p_*\to1/2\). Neither connected-tree endpoint is attained for orders at least three.

**5. One excess edge breaks the lower bound.** Adding a chord to \(C_n\) for \(n\ge4\) yields two vertices of degree three and \(n-2\) vertices of degree two. Its expectation is

\[
F(q)=(1-q)\bigl((n-2)q^2+2q^3\bigr),\qquad F'(2/3)=\frac8{27}>0.
\]

Every degree-two and degree-three term in \(F''(q)\) is strictly negative for \(q\ge2/3\). Together with \(F'(1)=-n<0\), this proves a unique root above \(2/3\), or equivalently a unique peak below \(1/3\). For \(q<2/3\), the degree-two term in \(F'\) is nonnegative and the degree-three term is positive, so no additional root occurs.

**6. Dense connected nonunimodality witness.** Let \(G\) consist of a clique on thirteen vertices with one pendant leaf attached to one clique vertex. Its degree counts are \(a_1=1\), \(a_{12}=12\), \(a_{13}=1\), giving

\[
F(q)=(1-q)(q+12q^{12}+q^{13}).
\]

Exact evaluations yield \(F'(1/2)>0\), \(F'(3/5)<0\), \(F'(9/10)>0\), and \(F'(1)<0\). Continuity and polynomial analyticity give two distinct strict local maxima separated by a local minimum. This shows that the sparse hypothesis prevents genuinely possible nonunimodal behavior, rather than merely furnishing numerical convenience.

## Verification

Run \(\texttt{python3 check.py}\) with an ordinary Python 3 interpreter; the checker uses only the standard library and exact rational arithmetic. It independently enumerates all vertex-survival configurations for several finite graphs, verifies the closed degree formula, exhaustively tests 914 realizable tree degree multisets through 18 vertices at three rational failure probabilities, and checks the chorded-cycle and dense connected counterexamples. Exact finite checks corroborate examples; equations (1)–(6), not computation, prove the all-size statement and global uniqueness.

## Relationship to prior work

Callaway, Newman, Strogatz, and Watts (first public 18 July 2000) developed degree-distribution generating functions for network site percolation; the elementary singleton expectation is compatible with their general framework and is not claimed as new. Bunn, Urban, and Keitt (2000) used habitat-patch graphs and vertex/edge removal in conservation. Gastner and colleagues (2009) studied vegetation fragmentation through gradient percolation. Diskin and Krivelevich (2023) analyze isolated small tree components under site percolation on high-degree pseudorandom graphs; this is a different asymptotic setting. Brown, Kolokolnikov, and Kooij (2024) approximate *bond*-failure reliability using isolated-vertex heuristics; it does not imply the finite homogeneous site-survival peak window. None of the inspected source passages states the exact universal interval, its two equality classifications, or sharp edge-budget and dense-network boundaries. That comparison is based on examined primary material, not a claim of exhaustive priority or formal uniqueness.

## Limitations

The statement applies to independent homogeneous site failures, simple undirected graphs, and expected singleton-component count; it does not extend to bond failures, heterogeneous correlated patch persistence, all fragmentation measures, or realized connected-component numbers. The graph may be disconnected; connectedness is not necessary. Although exact proofs establish the mathematical identities, originality remains provisional pending independent literature assessment, including any historical rephrasing in reliability or degree-polynomial language. The result does not assert ecological model calibration or policy effectiveness.

## References

1. Callaway, D. S., Newman, M. E. J., Strogatz, S. H., and Watts, D. J. (2000), *Network robustness and fragility: Percolation on random graphs*. First publicly posted 18 July 2000. https://arxiv.org/abs/cond-mat/0007300.
2. Bunn, A. G., Urban, D. L., and Keitt, T. H. (2000), *Landscape connectivity: A conservation application of graph theory*. Journal of Environmental Management 59, 265–278. https://doi.org/10.1006/jema.2000.0373.
3. Gastner, M. T., Oborny, B., Zimmermann, D. K., and Pruessner, G. (2009), *Transition from Connected to Fragmented Vegetation across an Environmental Gradient: Scaling Laws in Ecotone Geometry*. The American Naturalist 174. https://doi.org/10.1086/599292.
4. Diskin, S., and Krivelevich, M. (2023), *Site percolation on pseudo-random graphs*. Random Structures & Algorithms 63, 406–441. https://doi.org/10.1002/rsa.21141.
5. Brown, J. I., Kolokolnikov, T., and Kooij, R. E. (2024), *New approximations for network reliability*. Networks 84, 51–63. https://doi.org/10.1002/net.22215.
