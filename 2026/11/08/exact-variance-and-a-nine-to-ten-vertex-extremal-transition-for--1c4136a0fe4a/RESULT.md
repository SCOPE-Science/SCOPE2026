# Exact variance and a nine-to-ten-vertex extremal transition for bipartite spanning-tree overlap

## Finding

Let \(a,b\ge1\) be integers, let \(T_1,T_2\) be two independent, uniformly selected spanning trees of the unweighted complete bipartite graph \(K_{a,b}\), and let \(X_{a,b}=|E(T_1)\cap E(T_2)|\). Set \(n=a+b\). Then

\[
\mathbb E X_{a,b}=\frac{(n-1)^2}{ab},\qquad
\operatorname{Var}(X_{a,b})=
\frac{(a-1)(b-1)(n^2-5n+7)}{a^2b^2}.
\]

**Sharp fixed-order extremum.** Among *all* complete bipartite graphs on \(n\ge4\) vertices, the variance of the intersection of two independent uniform spanning trees is maximized uniquely, up to interchanging the two vertex classes, as follows:

\[
\begin{cases}
K_{3,n-3},&6\le n\le9,\\
K_{2,n-2},&n=4,5\text{ or }n\ge10.
\end{cases}
\]

There are no ties between different unordered bipartitions. Thus the maximizing smaller class changes from three vertices to two between \(n=9\) and \(n=10\). For every \(n\ge10\), variance decreases strictly as the smaller class grows from two toward the balanced bipartition. Stars, which have deterministic spanning trees, have variance zero.

The contrast persists asymptotically: for every fixed integer \(a\ge2\),

\[
\operatorname{Var}(X_{a,b})\sim \frac{a-1}{a^2}\,b
\quad(b\to\infty),
\qquad
\lim_{n\to\infty}\operatorname{Var}
\bigl(X_{\lfloor n/2\rfloor,\lceil n/2\rceil}\bigr)=4.
\]

## Assumptions and scope

The graph is simple and unweighted; every labeled spanning tree has equal probability. The two random trees are independent and use the same labeled vertex and edge sets. The intersection counts edges, not vertices. All equalities hold for every pair of positive integers \(a,b\), including stars. Fixed-order maximization ranges over \(K_{a,n-a}\) for every integer \(1\le a\le n-1\), identifying isomorphic choices under \(a\leftrightarrow n-a\). No asymptotic limit or approximate sampling assumption is used in the finite results.

## Proof

**1. One- and two-edge inclusion.** Orient each edge from the class \(A\) of size \(a\) to the class \(B\) of size \(b\); label it \(e=(i,j)\), where \(i\in A\), \(j\in B\). The transfer-current matrix of uniform spanning trees is the orthogonal incidence projection

\[
H_{ef}=d_e^{\mathsf T}L^+d_f,
\]

where \(d_e\) is the signed incidence vector, \(L\) the unweighted graph Laplacian, and \(L^+\) its Moore--Penrose pseudoinverse. On vectors with zero sum on \(A\), \(L\) has eigenvalue \(b\); on those with zero sum on \(B\), eigenvalue \(a\); and on the one-dimensional inter-class contrast, eigenvalue \(a+b\). Orthogonal decomposition of the incidence vectors therefore gives the *explicit* identity

\[
H_{(i,j),(k,l)}
=\frac{\mathbf1_{i=k}}b+\frac{\mathbf1_{j=l}}a-\frac1{ab}.
\]

In particular, every edge has inclusion probability

\[
p=H_{ee}=\frac{a+b-1}{ab}.
\]

For two distinct edges \(e,f\), the transfer-current determinant identity, equivalently the two-edge specialization of the spanning-forest containment count, gives

\[
\Pr(e,f\in T_1)=\det\!\begin{pmatrix}p&H_{ef}\\H_{ef}&p\end{pmatrix}
=p^2-H_{ef}^2.
\]

The three distinct-edge geometries and their numbers of *unordered* edge pairs are

| Geometry | \(H_{ef}\) | Number of pairs |
|---|---:|---:|
| Same \(A\)-endpoint | \((a-1)/(ab)\) | \(ab(b-1)/2\) |
| Same \(B\)-endpoint | \((b-1)/(ab)\) | \(ab(a-1)/2\) |
| Disjoint endpoints | \(-1/(ab)\) | \(ab(a-1)(b-1)/2\) |

**2. Exact first two overlap moments.** For an edge \(e\), let \(J_e=\mathbf1\{e\in T_1\cap T_2\}\). Independence of the sampled trees gives

\[
\mathbb E J_e=p^2,
\qquad
\mathbb E(J_eJ_f)=(p^2-H_{ef}^2)^2\quad(e\ne f).
\]

There are \(ab\) edges, so \(X_{a,b}=\sum_eJ_e\) has mean \(abp^2=(n-1)^2/(ab)\). For the variance, write \(c_A=ab(b-1)/2\), \(c_B=ab(a-1)/2\), and \(c_D=ab(a-1)(b-1)/2\). Summing the three geometries yields the finite exact identity

\[
\begin{split}
\operatorname{Var}(X_{a,b})
={}&abp^2(1-p^2)\\
&+2c_A\left[\left(p^2-\frac{(a-1)^2}{a^2b^2}\right)^2-p^4\right]\\
&+2c_B\left[\left(p^2-\frac{(b-1)^2}{a^2b^2}\right)^2-p^4\right]\\
&+2c_D\left[\left(p^2-\frac1{a^2b^2}\right)^2-p^4\right].
\end{split}
\]

Substituting \(p=(n-1)/(ab)\), expanding and factoring gives exactly

\[
\operatorname{Var}(X_{a,b})
=\frac{(a-1)(b-1)(n^2-5n+7)}{a^2b^2}.
\]

The formula is also valid when one part has size one: the factor \(a-1\) or \(b-1\) vanishes, consistently with the unique spanning tree of a star.

**3. All-size extremal classification.** Fix \(n\ge4\). The positive factor \(n^2-5n+7\) is constant across bipartitions. Stars give zero, and all nonstar bipartitions give positive variance. It is enough to maximize

\[
h_n(x)=\frac{(x-1)(n-x-1)}{x^2(n-x)^2}
\quad\text{for integers }2\le x\le\lfloor n/2\rfloor.
\]

For real \(2\le x\le n/2\), direct logarithmic differentiation gives

\[
\frac{h_n'(x)}{h_n(x)}
=\frac{(n-2x)\,[2n-2-x(n-x)]}
{x(n-x)(x-1)(n-x-1)}.
\]

For \(n\ge8\) and \(3\le x\le n/2\), the factor \(x(n-x)\) is at least \(3(n-3)>2n-2\), and hence \(h_n\) strictly decreases for \(x\ge3\). It follows that the only possible integer maximizers are \(x=2\) and \(x=3\). Their exact comparison is

\[
\begin{split}
&36(n-2)^2(n-3)^2\,[h_n(3)-h_n(2)]\\
&\qquad=8(n-4)(n-2)^2-9(n-3)^3\\
&\qquad=-(n-5)(n^2-12n+23).
\end{split}
\]

This is strictly positive for integers \(6\le n\le9\) and strictly negative for every integer \(n\ge10\). For \(n=6,7\), the only nonstar possibilities are \(x=2,3\), and the same comparison applies. For \(n=4,5\), only \(x=2\) is possible. This proves every case, strict uniqueness, and the claimed transition.

**4. Asymptotics.** Substitute fixed \(a\ge2\) and \(b\to\infty\) into the exact formula to obtain \(\operatorname{Var}(X_{a,b})/b\to(a-1)/a^2\). Substituting \(a=\lfloor n/2\rfloor\), \(b=\lceil n/2\rceil\) gives variance converging to \(4\).

## Verification

The accompanying standalone standard-library checker enumerates all candidate edge subsets of the appropriate size and tests for spanning-tree connectivity and acyclicity for each \(1\le a,b\le4\). From these independent tree lists it computes exact one- and two-edge inclusion probabilities and the exact first and second overlap moments, testing them against the formulas above. It also tests the claimed unique fixed-order maximizers through \(n=150\). It performs 836 exact integer/rational assertions without Monte Carlo sampling or floating-point tolerances. The computations serve as reproducibility checks; the all-size theorem is proved by the preceding identities and inequalities, not by a finite range of experiments.

To run: `python3 checker.py` in the directory containing the two files. No external packages or additional data are required.

## Relationship to prior work

London and Pluhár (2023) motivate studying the number of shared edges of two independent uniform spanning trees as a network-overlap statistic, but their principal quantitative analysis concerns its expectation. Albin and collaborators (2021) analyze minimum *expected* overlap and edge-usage fairness; the variance of the random overlap is a different statistic. Dong and Ge (2021) derive general complete-bipartite spanning-tree counts with prescribed forest edges: these support the two-edge input, but the present exact overlap-variance factorization and the all-orders maximizing-bipartition transition require the further two-tree computation and optimization given here. Bóna, Burghart and Wagner (2025, revised later) study the intersection distribution, including Poisson behavior for dense complete multipartite graphs and a binomial approximation for unbalanced bicliques. Their accessible June 2025 version does not state the finite exact variance or the fixed-order \(n=10\) extremal transition. These results are not claimed as a new transfer-current formula, forest count, mean-overlap formula, or general distributional limit theorem.

## Limitations

The result is confined to two *independent*, *uniform* spanning trees of a simple complete bipartite graph. It does not describe the full finite overlap distribution, arbitrary networks, nonuniform edge weights, or intersections of three or more trees. The variance and extremal transition are explicit consequences of known forest-counting and transfer-current principles, not an independent replacement for those general principles. Historical priority remains qualified because the full September 2026 revision of the highly related Bóna--Burghart--Wagner paper could not be examined; the directly relevant 2025 text was examined. Neither the finite checker nor unsuccessful searches establish novelty.

## References

1. A. London and A. Pluhár, *Intersection of random spanning trees in complex networks*, Applied Network Science **8**, article 72 (published 13 October 2023), https://doi.org/10.1007/s41109-023-00600-4 .
2. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, 2021 preprint, https://arxiv.org/abs/2103.05294 .
3. N. Albin, J. Clemens, D. Hoare, P. Poggi-Corradini, B. Sit, and S. Tymochko, *Fairest edge usage and minimum expected overlap for random spanning trees*, Discrete Mathematics **344** (2021), 112282, https://doi.org/10.1016/j.disc.2020.112282 .
4. M. Bóna, F. Burghart, and S. Wagner, *On the intersection of pairs of trees*, https://arxiv.org/abs/2501.18570 , especially accessible v2 dated 6 June 2025; a later v4 revision was recorded in September 2026.
5. R. Burton and R. Pemantle, *Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impedances*, Annals of Probability **21** (1993), 1329–1371 (transfer-current determinant identity).
