# Poisson extremal-edge geometry and an independent endpoint-split law for uniform Cayley trees

## Finding

For every integer \(n\ge2\), choose uniformly among the \(n^{n-2}\) unrooted trees on the labelled vertices \([n]=\{1,\ldots,n\}\). For every tree edge \(\{i,j\}\) with \(i<j\), place an atom at
\[
  \left(\frac{i}{\sqrt n},\frac{n+1-j}{\sqrt n}\right).
\]
The resulting locally finite point measure \(\Xi_n\) converges in distribution, in the vague topology on \([0,\infty)^2\), to a homogeneous Poisson point process of intensity \(2\,du\,dv\).

Let \(L_n=\max_{\{i,j\}\in E(T_n)}|j-i|\). Among edges attaining \(L_n\), choose the one with lexicographically least ordered endpoints \(I_n<J_n\), and set
\[
 D_n=\frac{n-L_n}{\sqrt n},\qquad
 U_n=\frac{I_n}{I_n+n+1-J_n}.
\]
Then \((D_n,U_n)\) converges jointly to independent variables \((D,U)\), where \(U\) is uniform on \((0,1)\), and
\[
 \Pr(D>t)=e^{-t^2}\quad(t\ge0).
\]
Equivalently, the two scaled distances of the endpoints of the longest-span edge from opposite ends of the label order converge jointly to a pair \((X,Y)\) with density
\[
 f_{X,Y}(x,y)=2e^{-(x+y)^2}\,\mathbf1_{\{x>0,y>0\}}.
\]
Thus the deficit of the maximum fixed-order edge span is of square-root order with a Rayleigh-type law, and its allocation between the two ends is asymptotically an independent uniform fraction.

## Assumptions and scope

The distribution is uniform over *all labelled Cayley trees*, not uniform over unlabelled tree shapes and not the minimum-spanning-tree distribution. The linear vertex ordering is the fixed order \(1<\cdots<n\); no optimization over orderings is performed. An edge is undirected and is counted once at its increasing pair of endpoints. The process statement concerns bounded subsets of the closed first quadrant whose boundaries have zero planar Lebesgue measure. All limits concern \(n\to\infty\) through positive integers. Finite-size ties for the largest edge are resolved as specified; the limit does not depend on this tie rule.

## Proof

**1. Exact forest inclusion.** For a deterministic forest \(F\) on \([n]\) with \(k\) edges, let the sizes of its connected components, including isolated vertices, be \(s_1,\ldots,s_{n-k}\). The number of trees containing every edge of \(F\) is
\[
 n^{n-k-2}\prod_{a=1}^{n-k}s_a,
\]
and hence
\[
 \Pr(F\subseteq T_n)=n^{-k}\prod_{a=1}^{n-k}s_a.\tag{1}
\]
To reconstruct this classical identity, contract the components of \(F\). The resulting complete multigraph has \(s_as_b\) edges between contracted vertices \(a,b\). Its Laplacian is \(n\operatorname{diag}(s)-ss^{\mathsf T}\). Deleting one row and column and applying the matrix determinant lemma yields \(n^{n-k-2}\prod_a s_a\) (the one-component case follows directly). Dividing by Cayley's \(n^{n-2}\) gives (1). In particular, \(k\) pairwise vertex-disjoint designated edges have inclusion probability \((2/n)^k\). A designated cyclic set has inclusion probability zero.

**2. Rare edges form a Poisson process.** Let \(B_1,\ldots,B_r\) be disjoint bounded planar Borel sets with null-area boundaries. Write \(H_{n,a}\) for candidate edges with their scaled endpoint pair in \(B_a\), and \(N_{n,a}\) for how many such edges actually occur in \(T_n\). Lattice counting gives
\[
 |H_{n,a}|/n\longrightarrow |B_a|,
\]
where \(|B_a|\) is planar area. All candidates in the bounded union \(H_n\) have their low endpoints in the first \(O(\sqrt n)\) labels and their high endpoints in the last \(O(\sqrt n)\) labels. Therefore \(|H_n|=O(n)\), the maximum vertex degree in the candidate graph is \(O(\sqrt n)\), and
\[
 \sum_v\deg_{H_n}(v)^2=O(n^{3/2}).\tag{2}
\]

Fix nonnegative integers \(m_1,\ldots,m_r\), put \(k=\sum_a m_a\), and expand the mixed falling factorial moment \(\mathbb E\prod_a (N_{n,a})_{\underline{m_a}}\) into ordered choices of \(k\) distinct candidate edges. Those choices whose edges share a vertex number at most
\[
 O_k\left(|H_n|^{k-2}\sum_v\deg_{H_n}(v)^2\right)=O_k(n^{k-1/2})
\]
for \(k\ge2\). By (1), each such selection has probability at most \((k+1)^k/n^k\) if acyclic, and zero if cyclic; their total contribution is \(O_k(n^{-1/2})\). The remaining choices are matchings, each of inclusion probability \((2/n)^k\). Hence
\[
 \mathbb E\prod_{a=1}^{r}(N_{n,a})_{\underline{m_a}}
 \longrightarrow \prod_{a=1}^{r}(2|B_a|)^{m_a}.\tag{3}
\]
For bounded axis-aligned rectangles the convergence in (3) is \(O_k(n^{-1/2})\), because the lattice-count error is \(O(\sqrt n)\). The joint factorial moments identify independent Poisson limits with respective means \(2|B_a|\). These count limits, together with uniform local first-moment bounds, imply vague convergence of \(\Xi_n\) to a Poisson point process of intensity \(2\,du\,dv\). This does not assume independence of tree-edge indicators; their actual dependence was controlled by (1) and (2).

**3. The extremal edge and its endpoint mark.** In the limit process, let \((X,Y)\) be the atom with the smallest value of \(x+y\). Such an atom exists and is almost surely unique, because the triangle \(\{(x,y):x,y\ge0,\ x+y<t\}\) has area \(t^2/2\), and the intensity is diffuse. The probability that this triangle is empty is \(e^{-t^2}\). For a small area element at \((x,y)\), the density of the minimizing atom equals the local intensity \(2\,dx\,dy\) times the probability \(e^{-(x+y)^2}\) of no atom with smaller coordinate sum, establishing the displayed joint density.

Put \(S=X+Y\) and \(U=X/(X+Y)\). The change of variables \((x,y)=(s u,s(1-u))\) has Jacobian \(s\); thus their joint density is \(2s e^{-s^2}\) for \(s>0\) and \(0<u<1\), the product of a Rayleigh-type density and a unit-uniform density. For a finite tree edge, the point-process coordinate sum equals \((n+1-(j-i))/\sqrt n\), which differs from its span deficit by just \(1/\sqrt n\). Restriction first to \(\{x+y\le K\}\), then letting \(K\to\infty\), makes the argmin functional continuous at the almost-surely unique limit atom. The continuous-mapping theorem proves both joint limits and makes the tie-break immaterial.

## Verification

The accompanying standalone \(\texttt{check.py}\) uses only Python's standard library. Running \(\texttt{python check.py}\) enumerates every Prüfer sequence for each \(2\le n\le8\), totaling 280,392 labelled trees, and checks 906 exact assertions. They include all one- and two-edge forest inclusion probabilities and all first-through-third falling factorial moments of several longest-span edge-count events. In particular, the 262,144 labelled trees of order eight are enumerated exhaustively. These computations check finite combinatorial inputs to the argument, not the infinite-dimensional point-process limit; that limit follows from the analytic proof above.

## Relationship to prior work

The forest containment identity (1), and Cayley's tree enumeration, are established antecedents, not claimed new. Pitman's forest enumerator and Cameron–Kagan's forest-extension count provide primary published treatments. Esteban, Ferrer-i-Cancho and Gómez-Rodríguez study sums of edge lengths in random tree linear arrangements and the *optimized* minimum-sum arrangement. Their random-order total-length expectation does not determine the extreme fixed-order span or its endpoint locations. Kuba and Wagner study **exactly the same label-difference edge weight** and its maximum, but exclusively in increasing-tree models (including plane-oriented recursive and binary increasing trees). Their Theorem 7 and section 6.2 use growth-restricted trees, rather than the uniform distribution over all Cayley trees; their theorem does not give the two-dimensional opposite-endpoint Poisson process or endpoint-split law here. Hackl, Panholzer and Wagner study ordered vertex uncovering, especially induced-prefix edge counts and component sizes. Their prefix-edge process is different from the rare edges connecting opposite ends of the order. Bóna, Burghart and Wagner analyze common edges of *two* independent trees, not long edges in one tree. The present claim is the two-dimensional rare-edge limit and the induced joint longest-edge/endpoint-split law. The exact underlying forest counts alone do not state this limiting geometry.

## Limitations

The convergence is asymptotic; no uniform finite-\(n\) total-variation estimate for the full point process is claimed. Its endpoint locations use the prescribed uniform Cayley model and a fixed vertex order. The factorial-moment rate mentioned above applies to fixed orders and bounded rectangles, not arbitrary growing collections of test sets. There may be older results with an equivalent general sparse-edge Poisson process interpretation; novelty is assessed relative to the specifically inspected literature, not asserted as a priority guarantee. No independent mathematical validation has been performed.

## References

1. J. Pitman, *Forest Volume Decompositions and Abel–Cayley–Hurwitz Multinomial Expansions*, Berkeley Statistics Technical Report 591 (public report listed April 1, 2001); J. Combin. Theory A 98 (2002), 175–191. https://statistics.berkeley.edu/tech-reports/591
2. P. J. Cameron and M. Kagan, *Counting spanning trees containing a forest: a short proof*, arXiv:2210.09009 (first submitted 2022-10-14). https://arxiv.org/html/2210.09009v1
3. J. L. Esteban, R. Ferrer-i-Cancho and C. Gómez-Rodríguez, *The scaling of the minimum sum of edge lengths in uniformly random trees*, arXiv:1602.07940 (first submitted 2016-02-25). https://arxiv.org/html/1602.07940v2
4. B. Hackl, A. Panholzer and S. Wagner, *The Uncover Process for Random Labeled Trees*, arXiv:2301.00664 (first submitted 2023-01-02). https://arxiv.org/abs/2301.00664
5. M. Kuba and S. Wagner, *Deterministic Edge Weights in Increasing Tree Families*, author manuscript dated 2008-04-02, published online 2009-06-22; *Combinatorics, Probability and Computing* 19 (2010), 99–119, section 6.2 and Theorem 7. https://www.dmg.tuwien.ac.at/kuba/incew2st.pdf
6. M. Bóna, F. Burghart and S. Wagner, *On the Intersection of Pairs of Trees*, arXiv:2501.18570 (first submitted 2025-01-30). https://arxiv.org/abs/2501.18570
