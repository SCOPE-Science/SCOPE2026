# Exact component profiles for power-domination reconfiguration of triangular graphs

## Finding

For every integer \(n\ge4\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph on the two-element subsets of \([n]\). Two vertices of \(T_n\) are adjacent when their underlying two-element subsets intersect. Let \(\mathcal R_{n,k}\) be the token-addition/removal (TAR) graph whose vertices are all power-dominating subsets of \(V(T_n)\) having at most \(k\) members, adjacent precisely when one underlying graph vertex is added or deleted. Let \(c_n(k)\) be its connected-component count, for integer budgets \(k\ge q_n=\lceil(n-2)/2\rceil\).

Put
\[
B_n(t,z)=\exp\left(\frac{zt^2}{2}+\sum_{j\ge3}\frac{z^{j-1}t^j}{(j-1)!}\right),
\qquad
m_{n,k}=\binom n2(n-2)![t^{n-2}z^k]B_n(t,z)
+\mathbf1_{\{n\ \mathrm{odd}\}}\mathbf1_{\{k=(n-1)/2\}}\frac{n!}{2^{(n-1)/2}((n-1)/2)!}.
\]
Then \(m_{n,k}\) counts all inclusion-minimal power-dominating sets of cardinality \(k\), and
\[
\boxed{c_n(k)=\begin{cases}
m_{n,q_n},&k=q_n,\\
1+m_{n,k},&q_n<k\le n-3,\\
1,&k\ge n-2.
\end{cases}}
\]
In the middle range the unique nontrivial component contains every non-isolated reconfiguration vertex; the other \(m_{n,k}\) components are singleton minimal power-dominating sets of cardinality \(k\). Thus the first connected budget and the permanent connectivity threshold coincide and equal \(n-2\). For \(n\ge6\), the last disconnected budget has exactly \(1+\binom n2(n-2)\) components.

An independent all-set count is
\[
\mathcal P(T_n;z)=\sum_{r=0}^{2}\binom nr
\sum_{j=0}^{n-r}(-1)^j\binom{n-r}{j}
(1+z)^{\binom{n-r-j}{2}}.
\]
This polynomial includes every power-dominating set, not just the inclusion-minimal ones.

## Assumptions and scope

All graphs are finite, simple, undirected and labeled. A nonempty set \(S\subseteq V(G)\) is power dominating if the initial observed set \(N_G[S]\), followed by repeatedly observing the unique unobserved neighbor of any observed vertex that has exactly one, eventually covers \(V(G)\). TAR moves add or delete exactly one selected vertex, never exceeding the budget; the graph being reconfigured is \(T_n\), whereas \(n\) is the order of the auxiliary complete graph \(K_n\), not \(|V(T_n)|=\binom n2\). A set is inclusion-minimal if it is power dominating but no proper subset is. The coefficient convention \([t^az^b]\) means extraction of the specified powers from a formal power series.

## Proof

**1. Exact power-domination criterion.** Identify the selected vertices of \(T_n\) with the edge set of a simple auxiliary graph \(H\) on \([n]\). Write \(U\) for the isolated vertices of \(H\), and \(r=|U|\). After the initial closed-neighborhood step in \(T_n\), the only unobserved vertices are the edges of the complete graph induced by \(U\). If \(r\le1\), none remain. If \(r=2\), exactly one remains, say \(uv\). Because \(H\) has an edge, some label \(w\) is incident to a selected edge; the observed vertex \(uw\) of \(T_n\) has \(uv\) as its only unobserved neighbor, so it forces \(uv\). If \(r\ge3\), each initially observed triangular-graph vertex meets \(U\) in at most one label, and whenever it does, it has \(r-1\ge2\) unobserved neighbors; no force can occur. Hence
\[
S\text{ power dominates }T_n\quad\Longleftrightarrow\quad H\text{ has at most two isolated vertices}.
\]
This also proves the all-set inclusion-exclusion formula: choose the exact isolated set of size \(r\le2\), then count nonisolated edge graphs on the remaining \(n-r\) labels by inclusion-exclusion.

**2. Inclusion-minimal configurations.** Removing one selected edge creates at most two new isolated labels. A graph with no isolated labels cannot therefore be minimal. With exactly one isolated label, deletion of *every* edge must create two more isolates. This happens precisely when every edge is an entire two-vertex component, so \(H\) is a perfect matching on \(n-1\) labels and one isolated label (possible only for odd \(n\)). With exactly two isolated labels, deleting every edge must create at least one new isolate. Equivalently every selected edge has a degree-one endpoint, i.e. the nonisolated components of \(H\) are stars \(K_{1,d}\) with \(d\ge1\), and they cover precisely \(n-2\) labels. The converse in both cases follows by checking deletion of each edge and monotonicity of power domination. These families are disjoint and exhaustive.

For a labeled star component on \(j\) labels there is one possibility for \(j=2\) and \(j\) center choices for \(j\ge3\). The labeled exponential formula thus gives \(B_n(t,z)\), with each such component having \(j-1\) selected edges. Choose the two isolates and multiply by \((n-2)!\); for the odd-order matching family choose one isolate and match the other \(n-1\) labels. This proves the formula for \(m_{n,k}\). In particular all inclusion-minimal sizes lie between \(q_n\) and \(n-3\), inclusive, and both extremes occur. The upper endpoint comes from one star on the \(n-2\) covered labels.

**3. Bounded reduction to minimum configurations.** Let an inclusion-minimal configuration have \(s>q_n\) selected edges. It must be a two-isolate spanning star forest. If some star has at least three leaves, add an edge between two leaves, then delete their two star edges successively. All previously covered labels remain covered, the center retains another leaf, and the final edge count decreases by one. If there is no such star but there are two three-vertex stars, add an edge joining one leaf of each, then delete the two leaf-to-center edges. Both centers retain their other leaf and the total edge count again decreases by one. Every intermediate auxiliary edge set covers at least \(n-2\) labels and uses at most \(s+1\) edges. Repeating yields either a matching on \(n-2\) labels (even \(n\)), or a collection of independent edges and one three-vertex star covering \(n-2\) labels (odd \(n\)). In the odd case, add an edge from one leaf of the remaining three-vertex star to one isolated label and delete that leaf-to-center edge. The result is a matching covering \(n-1\) labels, and again only one spare edge is needed. Therefore **every** minimal set of size \(s\) has a TAR path to a minimum set at budget \(s+1\).

**4. Connectivity of minimum configurations with one spare edge.** Minimum configurations in even order are matchings on \(n-2\) labels, with two exposed labels. For odd order, the preceding one-edge exchange also connects every minimum two-isolate star forest to a matching on \(n-1\) labels, with one exposed label. It remains to connect any two fixed-cardinality matchings with at least one exposed label. Given an exposed label \(u\) and a matching edge \(ab\), replace \(ab\) by \(au\); this exchanges the exposed label \(u\) with \(b\). Thus prescribed exposed labels can be attained. With the exposed set fixed, any perfect matching on the remaining labels can be converted to any other using four-label partner switches. Every switch \(ab,cd\mapsto ac,bd\) is realized using an exposed label \(u\) by the three exchanges
\[
ab\mapsto bu,\qquad cd\mapsto ac,\qquad bu\mapsto bd.
\]
The original exposed label is restored. In each exchange, add the new edge before removing the old one; all intermediate states remain power dominating and have at most \(q_n+1\) selected edges. Consequently all minimum configurations lie in one component at budget \(q_n+1\).

**5. Component count.** Fix any \(k>q_n\). A power-dominating set of size at most \(k\) which is not inclusion-minimal at size exactly \(k\) can have edges deleted until it reaches an inclusion-minimal subset of size at most \(k-1\). By Steps 3 and 4, all such subsets are connected to one another at budget \(k\). Conversely an inclusion-minimal set of size \(k\) has no deletion move preserving power domination and no permitted addition move, hence is an isolated reconfiguration vertex. This proves that there is exactly one other component and exactly \(m_{n,k}\) isolated components when \(q_n<k\le n-3\). At \(k=q_n\), all vertices are minimum and isolated, giving \(m_{n,q_n}\) components. For \(k\ge n-2\), no minimal set has size \(k\), so only the connected component remains. When \(n\ge6\), the maximal-size minimal sets are precisely the \(\binom n2(n-2)\) single-star arrangements with two isolated labels, yielding the final numerical claim.

## Verification

A standalone C++17 program `verify.cpp` constructs triangular-graph adjacency independently from label intersection, simulates the power-domination process, checks minimality against all single-edge deletions and the star/matching characterization, counts labeled star partitions independently of the generating function, and computes all connected components of the bounded TAR graphs by breadth-first search. It checks every subset of \(V(T_n)\) for \(4\le n\le7\), and all feasible configurations within budgets through \(n-2\) for \(4\le n\le8\). Run with `c++ -std=c++17 -O2 verify.cpp -o verify && ./verify` in the same directory. Exact integer comparisons pass. The unlimited-order claim is established by the proof, not by the finite tests.

## Relationship to prior work

Bjorkman et al. (2022 preprint, 2026 journal edition) introduced power-domination TAR graphs and general connectedness bounds. Their universal Proposition 2.8 gives a lower bound of upper-minimal-size plus one on permanent connectivity, but does not determine the present triangular-graph feasible-set criterion or all component counts; in the present family the lower bound is attained. Brimkov et al. (2018) introduced the power-domination polynomial, motivating the all-set enumerator. Curtis, Flagg and Hogben (2024 preprint) surveyed the broader TAR framework. The root matching and star-forest structure used here requires family-specific arguments; the general results alone do not imply the component-count formula.

## Limitations

No uniqueness or priority conclusion follows merely from negative searches. The full 2018 polynomial preprint was not obtained in the accessible research environment; only its arXiv record and abstract were examined, and it remains a limited publication-priority risk for the ancillary polynomial. The main TAR component claim is not inferred from that abstract. Selected sections rather than every page of the 2024 survey were read. No assertion is made about other Johnson graphs, other power-domination variants, or token-jumping connectivity. Independent mathematical validation has not been performed.

## References

1. Beth Bjorkman, Chassidy Bozeman, Daniela Ferrero, Mary Flagg, Cheryl Grood, Leslie Hogben, Bonnie Jacob, and Carolyn Reinhart, *Power domination reconfiguration*, arXiv:2201.01798v1 (first publicly posted 2022-01-05); full preprint at https://arxiv.org/pdf/2201.01798 ; 2026 journal version in *La Matematica* at https://doi.org/10.1007/s44007-025-00187-5 .
2. Boris Brimkov, Rutvik Patel, Varun Suriyanarayana, and Alexander Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (first publicly posted 2018-05-28), https://arxiv.org/abs/1805.10984 .
3. Bryan A. Curtis, Mary Flagg, and Leslie Hogben, *TAR reconfiguration for vertex set parameters*, arXiv:2406.05509v1 (first publicly posted 2024-06-08), https://arxiv.org/abs/2406.05509 .
