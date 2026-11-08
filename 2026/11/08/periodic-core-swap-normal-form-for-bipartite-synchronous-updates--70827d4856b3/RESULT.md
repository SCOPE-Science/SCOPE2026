# Periodic-core swap normal form for bipartite synchronous updates

## Finding
Let \(X\) and \(Y\) be nonempty finite state spaces, \(f:Y\to X\), and \(g:X\to Y\), with synchronous cross-update \(F(x,y)=(f(y),g(x))\). Set \(h=f\circ g:X\to X\), and for each integer \(j\ge1\), write \(A_j=|\operatorname{Fix}(h^j)|\). Then
\[
|\operatorname{Fix}(F^n)|=\begin{cases}
A_n,&n\text{ odd},\\
A_{n/2}^{\,2},&n\text{ even}.
\end{cases}
\]
More structurally, the complete periodic subsystem of \(F\) is conjugate to \(T(u,v)=(h(v),u)\), restricted to two copies of the periodic core of \(h\). If \(Q_n\) denotes the number of configurations whose **least** period is \(n\), then
\[
Q_n=\sum_{d\mid n}\mu(n/d)|\operatorname{Fix}(F^d)|,
\qquad \text{number of orbits of length }n=Q_n/n.
\]
In particular, for \(K=|\operatorname{Fix}(F)|=A_1\), exactly \(K(K-1)\) configurations, or \(K(K-1)/2\) orbits, have primitive period two.

## Assumptions and scope
There is no symmetry, invertibility, uniform alphabet, monotonicity, or graph assumption on \(f\) and \(g\); both state spaces are finite and nonempty. The term *periodic* always means periodic from time zero. The periodic core \(P_h\) is the union of the cycles of \(h\), not its basin. One application is synchronous binary strict-majority updating on any finite simple bipartite graph \(G=(U\sqcup V,E)\) in which all vertices have **odd degree**. Since no vertex retains its state at a tie, the update on \(U\) depends only on the previous state of \(V\), and conversely: it has precisely the cross-update form with \(X=\{0,1\}^{U}\) and \(Y=\{0,1\}^{V}\). Disconnected graphs are allowed. The theorem also applies to any deterministic cross-only rule on a bipartite system, with any finite alphabets.

## Proof
Write \(k=g\circ f:Y\to Y\). Direct composition gives \(F^2(x,y)=(h(x),k(y))\), and hence \(F^{2j}(x,y)=(h^j(x),k^j(y))\). The maps \(g\) and \(f\) intertwine \(h\) and \(k\): \(gh=kg\) and \(fk=hf\). On periodic points, \(g:P_h\to P_k\) is a bijection. Indeed, if \(x\in P_h\) has cycle length \(r\), then \(g(x)\) is periodic under \(k\); the map \(h^{-1}\circ f\), with the inverse taken **only on** \(P_h\), is its inverse because \((h^{-1}f)g(x)=x\). Conversely, if \(y\) is periodic under \(k\), then \(x=h^{-1}f(y)\) is well-defined on \(P_h\), and \(gx=y\), as follows by transporting any full cycle of \(k\) through \(f\), then applying the intertwining identity. Thus the two periodic cores are in bijection, preserving cycle lengths and \(|\operatorname{Fix}(h^j)|=|\operatorname{Fix}(k^j)|=A_j\).

Every \(F\)-periodic point lies in \(P_h\times P_k\), since its even iterates return and are coordinatewise iterates of \(h\) and \(k\). Conversely, the restriction of \(F\) to this product is a permutation because \(f\) and \(g\) restrict to bijections between the cores. Under the coordinate identification \(\Phi(x,z)=(x,g(z))\) from \(P_h\times P_h\) to \(P_h\times P_k\),
\[
F\Phi(x,z)=(h(z),g(x))=\Phi(h(z),x)=\Phi T(x,z).
\]
The normal form is therefore an exact conjugacy of periodic subsystems.

Since \(T^{2j}(x,z)=(h^j(x),h^j(z))\), the number of points fixed by \(F^{2j}\) is \(A_j^2\). For odd iterates, \(T^{2j+1}(x,z)=(h^{j+1}(z),h^j(x))\); the fixed-point equations force \(z=h^j(x)\), then \(h^{2j+1}(x)=x\). There is exactly one such \(z\) for each \(x\in\operatorname{Fix}(h^{2j+1})\), giving \(A_{2j+1}\). The formulas hold for all positive integers, including boundaries \(|X|=1\) or \(|Y|=1\). Möbius inversion on the divisor relation \(|\operatorname{Fix}(F^n)|=\sum_{d\mid n}Q_d\) yields the primitive census. Setting \(n=1,2\) gives \(Q_2=A_1^2-A_1=K(K-1)\), as claimed.

## Verification
Execute the independent Python 3 standard-library scripts `verify_finite_maps.py` and `verify_majority.py` without arguments. The first enumerates all \(900\) pairs of arbitrary functions with \(1\le|X|,|Y|\le3\), checking the formulas against direct dynamics for each of the first twelve iteration lengths (\(10{,}800\) identities). The second checks all \(189\) labelled simple graphs through six vertices that are bipartite and have only odd degrees (\(11{,}700\) initial configurations), plus a ten-vertex ternary tree. On that tree it finds \(K=8\), hence \(56\) primitive period-two configurations and \(28\) temporal two-orbits. The same script gives a sharp failure of the cross-only hypothesis for the four-vertex path with tie-retaining majority: \(K=4\), but only \(2\) states of least period two, versus the hypothetical \(12\). Captured reproducible outputs are in the matching `.out` files. These finite checks corroborate, but do not replace, the universal proof.

## Relationship to prior work
Kuhlman, Mortveit, Murrugarra, and Kumar (2011) study the attractor structure of synchronous threshold and bi-threshold Boolean systems, including the general one/two-period phenomenon in those settings; that result alone does not give the number of *initial* two-cycles or the arbitrary finite-map normal form. Turau (2022) characterizes fixed points, pure period-two trajectories, and mixed trajectories for majority/minority processes on trees; Turau (2023) gives a counting algorithm for fixed points and pure two-cycles on trees. Consequently, on odd-degree bipartite trees, the square identity converts a fixed-point count into a complete primitive-two count, including mixed states. Aledo and coauthors (2020) count periodic states for specified MAX/MIN Boolean graph systems, with different local assumptions and count formulas. The theorem above does not assert that these authors lack implicit corollaries, nor that the general normal form is absent from all unindexed literature; these remain originality risks.

## Limitations
This is a finite deterministic theorem, not a classification of all bipartite cellular automata with self-state dependencies. If local tie-breaking retains a vertex's previous state, the cross-only assumption can fail even on a bipartite graph with an even-degree vertex. No general upper bound of two on periods is claimed: arbitrary \(f,g\) may produce arbitrarily long cycles. On graphs, odd degree is sufficient for the strict-majority application, not necessary for every possible cross-only rule. The prior-literature comparison remains same-author-level research review rather than an independent audit.

## References
1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974v1, first posted 2011-08-15, https://arxiv.org/abs/1108.2974.
2. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1, 2022, https://arxiv.org/abs/2202.01580.
3. V. Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769v1, 2023, https://arxiv.org/abs/2312.13769.
4. J. A. Aledo et al., *Counting Periodic Points in Parallel Graph Dynamical Systems*, *Complexity* 2020, article 9708347, https://doi.org/10.1155/2020/9708347.
