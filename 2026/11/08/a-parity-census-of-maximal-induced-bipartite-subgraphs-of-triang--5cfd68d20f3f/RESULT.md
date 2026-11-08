# A parity census of maximal induced bipartite subgraphs of triangular graphs

## Finding
For every integer \(n\ge 3\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph: its vertices are the two-element subsets of \([n]\), and two are adjacent when they meet. Let \(I_n(z)\) count *all* vertex subsets inducing bipartite graphs, including the empty subset, by number of selected vertices. Let \(M_n(z)\) similarly count only inclusion-maximal such subsets. With formal power series interpretation,
\[
\sum_{n\ge0}I_n(z)\frac{x^n}{n!}
=\frac{\exp\!\left(x+\frac{zx^2}{2(1-zx)}-\frac{z^2x^2}{4}\right)}{(1-z^2x^2)^{1/4}},
\]
\[
\sum_{n\ge0}M_n(z)\frac{x^n}{n!}
=\frac{\exp(-z^2x^2/4)}{(1-z^2x^2)^{1/4}}
\left(1+x+\frac{zx^2}{2}+\frac{z^2x^3}{2(1-z^2x^2)}\right).
\]
Define the rational coefficients \(c_j\) by
\[
\sum_{j\ge0}c_ju^j=(1-u)^{-1/4}e^{-u/4},\qquad
c_0=1,\quad c_1=0,\quad
4jc_j=\sum_{i=0}^{j-2}c_i\quad(j\ge2).
\]
The maximal polynomial, for every integer \(m\ge1\), is
\[
M_{2m}(z)=(2m)!\left(c_mz^{2m}+\tfrac12c_{m-1}z^{2m-1}\right),
\]
\[
M_{2m+1}(z)=(2m+1)!\left(c_m+\tfrac12\sum_{j=0}^{m-1}c_j\right)z^{2m}.
\]
Consequently \(T_n\) is *well-bicovered* (all inclusion-maximal induced bipartite subgraphs have the same order) precisely when \(n\) is odd or \(n\in\{2,4\}\), for integers \(n\ge2\). For every even \(n\ge6\), the only maximal cardinalities are \(n-1\) and \(n\); the probability that a uniformly sampled inclusion-maximal bipartite vertex subset has cardinality \(n\) converges to \(2/3\) as \(n\) tends to infinity through even values. Complements of these subsets enumerate all inclusion-minimal odd-cycle transversal sets via \(z^{\binom n2}M_n(z^{-1})\).

## Assumptions and scope
All graphs are finite, undirected, simple, and labeled. Inclusion-maximal refers to adding vertices of \(T_n\), not maximizing their number. An induced bipartite subgraph may be disconnected. The notation \(T_2\) is used only for the exact small-order exception; the theorem's principal family has \(n\ge3\). The two generating functions also make sense at \(n=0\) and \(n=1\), with the unique empty induced graph counted as maximal. All generating-function identities are formal identities with rational coefficients; no analytic convergence is assumed for their combinatorial interpretations.

## Proof
**1. Line-graph reduction.** A selected vertex subset \(S\subseteq V(T_n)\) is uniquely the edge set of a spanning simple graph \(H=([n],S)\). The induced graph \(T_n[S]\) equals the line graph \(L(H)\). The latter is bipartite if and only if every component of \(H\) is an isolated vertex, a simple path, or an even cycle of length at least four. Indeed, three edges incident to one base vertex would form a triangle in \(L(H)\), forcing maximum base degree at most two. With this degree bound, all connected base components are paths, isolated vertices, or cycles. A cycle of odd length induces the corresponding odd cycle in the line graph, while the line graph of any path is a path and that of any even cycle is an even cycle. This proves both directions.

**2. Maximality.** In such an \(H\), call an isolated vertex a path on one vertex. If there are at least two path components, choose an endpoint from each (the unique vertex in the singleton case) and add their edge. This joins the paths into a larger path, so \(S\) was not maximal. If there is exactly one path on \(r\) vertices with even \(r\ge4\), its two endpoints may be joined to make a cycle of even length \(r\), also contradicting maximality. Conversely, if there are no path components then every base vertex has degree two, so no new edge can be added without creating a vertex of degree three. If there is a single path, and it has odd order \(r\) or order \(r=2\), every new edge incident to a cycle vertex or an internal path vertex creates degree three. When \(r\ge3\), the sole missing edge between the two endpoints closes a cycle of length \(r\), which is odd when \(r\) is odd and therefore prohibited. When \(r=1\), no pair of endpoints exists; when \(r=2\), the two endpoints are already adjacent, so there is no missing closing edge. Every other possible new edge touches a degree-two vertex. Hence these and only these configurations are inclusion-maximal.

**3. Labeled component enumeration.** A simple path on exactly one labeled base vertex has one structure and no selected edges. A simple path on \(r\ge2\) specified labels has \(r!/2\) structures, carrying \(r-1\) selected edges. A simple even cycle on \(2j\ge4\) specified labels has \((2j-1)!/2\) structures and \(2j\) selected edges. In the labeled exponential formula the even-cycle components contribute
\[
C(zx)=\exp\left(\sum_{j\ge2}\frac{(zx)^{2j}}{4j}\right)
=(1-z^2x^2)^{-1/4}\exp(-z^2x^2/4).
\]
Every path contributes the exponential series
\[
P(x,z)=x+\sum_{r\ge2}\frac{z^{r-1}x^r}{2}
=x+\frac{zx^2}{2(1-zx)}.
\]
Arbitrary sets of path and even-cycle components therefore give \(\exp(P(x,z))C(zx)\), proving the expression for \(I_n(z)\).

By Step 2, a maximal configuration has no path or a single permissible path. The permissible path exponential series is
\[
Q(x,z)=x+\frac{zx^2}{2}+\sum_{j\ge1}\frac{z^{2j}x^{2j+1}}{2}
=x+\frac{zx^2}{2}+\frac{z^2x^3}{2(1-z^2x^2)}.
\]
Thus the maximal exponential generating function is \(C(zx)(1+Q(x,z))\), proving the displayed identity.

**4. Coefficient extraction and boundaries.** Set \(C(\sqrt u)=\sum_{j\ge0}c_ju^j\). Logarithmic differentiation yields
\[
\frac{d}{du}\log\left((1-u)^{-1/4}e^{-u/4}\right)
=\frac{u}{4(1-u)},
\]
which gives \(4jc_j=\sum_{i=0}^{j-2}c_i\) and the stated initial values. In even base order \(n=2m\), the only possible terms of the maximal generating function are the cycle-only coefficient \(c_m z^{2m}\) and the one-two-vertex-path coefficient \(c_{m-1}z^{2m-1}/2\). In odd base order \(n=2m+1\), there are no cycle-only terms, and the contributions from a singleton path and all odd paths sum to \((c_m+\tfrac12\sum_{j=0}^{m-1}c_j)z^{2m}\). Multiplication by \(n!\) completes the polynomial formulas. The recurrence makes \(c_j>0\) for every \(j\ge2\), whereas \(c_1=0\). It follows that all odd orders have one maximal cardinality, the even orders \(n=2\) and \(n=4\) have one each, and every even order at least six has exactly two. Concrete small cases are
\[
M_3(z)=3z^2,\quad M_4(z)=3z^4,\quad
M_5(z)=75z^4,\quad M_6(z)=45z^5+60z^6.
\]

**5. Asymptotics.** Singularity analysis (or the standard binomial-coefficient asymptotic applied to the analytic factor \(e^{-u/4}\)) gives
\[
c_m\sim \frac{e^{-1/4}}{\Gamma(1/4)}m^{-3/4}.
\]
In particular \(c_{m-1}/c_m\to1\). For even \(n=2m\ge6\), the exact probability of maximal cardinality \(n\) is
\[
\frac{c_m}{c_m+\frac12c_{m-1}},
\]
so its limit is \(2/3\).

**6. Complementation.** A set of vertices is an inclusion-minimal odd-cycle transversal if and only if its complement is an inclusion-maximal vertex set inducing a bipartite graph. Since \(T_n\) has \(\binom n2\) vertices, cardinalities are transformed by \(z^{\binom n2}M_n(z^{-1})\). This is an equality of ordinary polynomials after cancellation of negative powers.

## Verification
The included independent adjacency-based verifier `verify_bipartite_triangular.cpp` constructs \(T_n\) from edge incidences, checks every selected vertex subset for bipartiteness using two-color breadth-first search, and tests maximality by adding each omitted graph vertex. It independently enumerates base-component configurations and compares *all* coefficients for \(2\le n\le7\), examining \(2{,}131{,}018\) candidate subsets in total. It reports `VERIFY_OK graph_orders=2..7 candidate_subsets=2131018 bipartite_subsets=15470 maximal_subsets=3442 graph_level_and_base_structure=PASS`.

The separate exact-arithmetic verifier `verify_bipartite_triangular_series.py` counts labeled sets of even cycles by a recurrence over the cycle containing the smallest label. It then adds each allowed single path and verifies its coefficients against the rational generating-function recurrence through \(n=30\), including small graph-level counts. It reports `VERIFY_OK exact_component_recurrence_and_series n=2..30 odd_well_bicovered=PASS even_two_sizes=PASS`.

Both programs are standalone; instructions are in their leading comments. These finite checks corroborate the proof but do not establish the unrestricted formulas by themselves.

## Relationship to prior work
Goddard, Kuenzel, and Melville introduced well-bicovered graphs and studied graph classes and operations, but their inspected treatment does not give the parity classification or complete cardinality polynomials of triangular graphs. Madsen, Nielsen, and Skjernaa studied general upper and lower bounds on numbers of maximal induced bipartite subgraphs and an enumeration algorithm, rather than this exact family census. Cao developed general algorithms for enumerating maximal induced subgraphs of hereditary classes; those algorithmic guarantees do not supply these coefficients. The line-graph reduction is elementary and not claimed as new: the contribution is the exact characterization and labeled enumeration of *inclusion-maximal* configurations together with its parity and asymptotic consequences.

## Limitations
This result concerns precisely the triangular graphs \(L(K_n)\), not all line graphs. The asymptotic proportion uses the uniform distribution over distinct labeled inclusion-maximal selected vertex sets. Public-literature comparison is not a proof of global publication priority; an unindexed equivalent enumeration could exist. The computational checks are finite and do not independently validate the general proof.

## References
1. Wayne Goddard, Kirsti Kuenzel, and Eileen Melville, “Graphs in which all maximal bipartite subgraphs have the same order,” arXiv:1909.07503, first posted 2019-09-16. https://arxiv.org/abs/1909.07503
2. Bolette Ammitzbøll Madsen, Jesper Makholm Nielsen, and Bjarke Skjernaa, “On the Number of Maximal Bipartite Subgraphs of a Graph,” BRICS Report Series RS-02-17, 2002. https://www.brics.dk/RS/02/17/BRICS-RS-02-17.pdf
3. Yixin Cao, “Enumerating Maximal Induced Subgraphs,” arXiv:2004.09885, first posted 2020-04-21. https://arxiv.org/abs/2004.09885
4. Giacomo Paesani, Daniël Paulusma, and Paweł Rzążewski, “Feedback Vertex Set and Even Cycle Transversal for H-Free Graphs,” arXiv:2105.02736, first posted 2021-05-06. https://arxiv.org/abs/2105.02736
