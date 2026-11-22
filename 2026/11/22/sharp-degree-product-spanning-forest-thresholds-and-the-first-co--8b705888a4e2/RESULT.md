# Sharp degree-product spanning-forest thresholds and the first complete-bipartite obstruction

## Finding

Let \(K_{a,b}\) be a labelled complete bipartite graph, \(3\le a\le b\), and let \(F_{a,b}\) denote the number of all spanning forests, allowing isolated vertices and counting distinct edge sets. Write \(D_{a,b}=a^b b^a\) for the product of vertex degrees. The following strict threshold law holds for every integer \(b\ge a\):

\[
F_{a,b}>D_{a,b}\quad\Longleftrightarrow\quad b\ge t_a,
\qquad (t_3,t_4,t_5)=(14,22,31),\qquad a\in\{3,4,5\}.
\]

For all smaller admissible \(b\), one has the strict reverse inequality. Among **all** complete bipartite graphs with minimum degree at least three and at most seventeen vertices, the unique graph violating \(F\le\prod_v\deg(v)\), up to isomorphism, is \(K_{3,14}\). The witness value \(F_{3,14}=13\,186\,891\,776\) was already reported by Wu–Lu–Dong; the sharp cutoff and minimality across the entire biclique class are the claims here.

## Assumptions and scope

Graphs are finite, simple, undirected, and labelled for counting. A spanning forest retains every graph vertex, and may contain singleton components. The cutoff statement covers *all* integer larger-side sizes without a finite upper limit, for smaller-side size exactly three, four or five. The seventeen-vertex minimality assertion ranges over all complete bipartite graphs of minimum degree at least three, **not** over all simple graphs.

## Proof

**1. A finite-coefficient all-depth formula.** Fix the shore of \(a\) vertices, and designate a vertex of the other shore as a *connector* precisely when it has at least two forest edges. An acyclic forest can have at most \(a-1\) connectors: adding a connector to the previously processed incidence graph can only avoid a cycle when all its neighbours occupy distinct connected components, so it decreases the number of components containing the \(a\) left vertices by at least one. Equivalently, an acyclic incidence graph with \(j\) connector vertices and connector degrees at least two has at least \(2j\) edges and at most \(a+j-1\), forcing \(j\le a-1\).

For \(0\le j\le a-1\), let \(c_{a,j}\) be the number of **ordered** \(j\)-tuples of subsets of the \(a\) left vertices, each of size at least two, whose bipartite incidence graph is acyclic. An ordered tuple specifies the neighbour sets for \(j\) selected, individually labelled right-shore vertices in increasing label order. Every remaining right-shore vertex has either degree zero or degree one, independently giving \(a+1\) options. These choices do not create a cycle. Conversely, every forest has a unique connector set and such a tuple, so

\[
F_{a,b}=\sum_{j=0}^{a-1}\binom bj\,c_{a,j}\,(a+1)^{b-j}.\tag{1}
\]

Direct exact enumeration of all connector subset tuples by the explicit union–find criterion in the included executable certificate gives

\[
(c_{3,j})_{j=0}^{2}=(1,4,6),\quad
(c_{4,j})_{j=0}^{3}=(1,11,54,96),\quad
(c_{5,j})_{j=0}^{4}=(1,26,300,1560,3000).
\tag{2}
\]

The computation is finite: for each \(a\le5\) it visits every possible sequence of length at most \(a-1\) from all \(2^a-a-1\) eligible subsets. Insertion of a connector is accepted exactly when its distinct left neighbours lie in distinct current union–find classes. This criterion is necessary and sufficient for no cycle; merging all such classes proves its sufficiency. The certificate also independently enumerates every edge subset for five small bicliques, detecting cycles from scratch, and agrees with (1).

**2. Strict monotonicity in the eventual range.** Set

\[
P_a(b)=\sum_{j=0}^{a-1}c_{a,j}\binom bj(a+1)^{-j},\qquad
R_a(b)=\frac{F_{a,b}}{a^b b^a}=\frac{(a+1)^bP_a(b)}{a^b b^a}.
\]

Since every coefficient is nonnegative, \(P_a(b+1)\ge P_a(b)>0\) for all integers \(b\ge a-1\). Consequently,

\[
\frac{R_a(b+1)}{R_a(b)}\ge\frac{a+1}{a}\left(\frac b{b+1}\right)^a.
\]

The right-hand side is strictly increasing in \(b\), and exceeds one already at \(b=10,18,27\), respectively for \(a=3,4,5\); these checks reduce to \((a+1)b^a>a(b+1)^a\) and are exact integer inequalities. Thus each ratio \(R_a\) is strictly increasing at every integer \(b\ge10,18,27\), respectively.

**3. Exact sign at the boundaries.** Substituting (2) in (1), exact integer arithmetic checks \(F_{a,b}<D_{a,b}\) for every integer \(a\le b<t_a\), and \(F_{a,t_a}>D_{a,t_a}\). The boundary differences \(F-D\) at consecutive sizes are:

| \(a\) | \(b=t_a-1\) | \(F-D\) there | \(b=t_a\) | \(F-D\) there |
|---|---:|---:|---:|---:|
| 3 | 13 | -600269263 | 14 | 62424840 |
| 4 | 21 | -129475887822892024 | 22 | 6141205090613629 |
| 5 | 30 | -1294029536811971806787691744 | 31 | 11678495949781668291893243437 |

The exhaustive finite comparisons include all smaller \(b\), not only the displayed boundary pairs. Since each threshold lies beyond its corresponding monotonicity start, strict increase of \(R_a\) proves the positive sign for **all** larger \(b\). This proves the three iff statements and rules out equality anywhere in their stated domains.

**4. The first biclique obstruction.** Suppose \(3\le a\le b\) and \(a+b\le17\). If \(3\le a\le5\), the just-proved thresholds leave precisely \((a,b)=(3,14)\) as a positive case. If \(a\ge6\), then \(b\le17-a\le11\le2a\), so the minimum degree \(a\) of \(K_{a,b}\) is at least \((a+b)/3\). Since \(a+b\ge12\), the strict inequality \(F_{a,b}<D_{a,b}\) follows from Wu–Lu–Dong, Theorem 1.3 (arXiv:2611.18076v1). This excludes every other biclique on at most seventeen vertices. Finally \(K_{3,14}\) has seventeen vertices and the positive difference displayed above, proving sharpness. \(\square\)

## Verification

Run `python3 verify_forests.py` with a standard Python 3 installation; it imports no external packages. The script (i) directly enumerates all eligible connector neighbour tuples for each \(a=3,4,5\), (ii) independently exhausts all edge subsets of five small complete bipartite graphs and tests acyclicity, (iii) verifies every finite sign required for the sharp thresholds, (iv) checks the exact integer inequality that makes the ratio increasing thereafter, and (v) checks the at-most-seventeen-vertex cases of smaller-side width three to five. The published minimum-degree theorem supplies the width-at-least-six implication; the executable does not purport to reprove that published theorem. The exact combinatorial bijection and monotonicity argument above establish the infinite ranges.

## Relationship to prior work

Wu, Lu and Dong [1], first public November 13, 2026, proposed the degree-product setting, proved the positive result at minimum degree at least one third of graph order, demonstrated that *some* sufficiently unbalanced bicliques violate the bound, and already reported the numerical counterexample \(K_{3,14}\). Their paper does not assert the three exact all-size thresholds or the unique minimum-order classification among bicliques. Stones [2] gives general exact algorithms for enumerating \(h\)-edge forests of bicliques, and reports calculations for parameter ranges containing all three finite boundaries; those **finite forest counts are not claimed novel**. The further comparison of these counts against the degree product, the eventual ratio monotonicity, and the all-biclique first-failure result are the added statements. Stark [3] provides prior asymptotic methods for balanced growing shores, not the thin-shore cutoff proof here.

## Limitations

This is an exact result only for smaller-side widths three, four and five, together with a seventeen-vertex optimality result within **complete bipartite graphs**. It neither locates the minimum violating graph among *all* graphs nor supplies thresholds for arbitrary fixed widths. Existing general forest enumeration algorithms can reproduce the finite coefficients; the claimed contribution is the sharp infinite classification and extremal minimality. Literature priority remains provisional pending independent assessment. The numerical components are exhaustively reproducible but are not substitutes for the infinite proof.

## References

1. T. Wu, S. Lu, X. Dong, *Upper bounds for the number of spanning forests of a graph*, arXiv:2611.18076v1 (posted 2026-11-13), https://arxiv.org/html/2611.18076v1 .
2. R. J. Stones, *Computing the number of h-edge spanning forests in complete bipartite graphs*, Discrete Mathematics and Theoretical Computer Science 16 (2014), 313–326, https://doi.org/10.46298/dmtcs.1248 ; https://dmtcs.episciences.org/1248/pdf .
3. D. Stark, *The asymptotic number of spanning forests of complete bipartite labelled graphs*, Discrete Mathematics 313 (2013), 1256–1261, https://doi.org/10.1016/j.disc.2012.10.026 .
