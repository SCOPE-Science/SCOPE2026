# Sharp diametral rigidity and three contact-entropy scales of Euclidean SIM-bodies

## Finding

For every integer \(n\ge2\) and every strictly decreasing list of positive real numbers \(a_1>\cdots>a_n>0\), let \(P_n(a)\) be the standard-coordinate SIM-body defined below. Put \(S_k=\sum_{j=1}^{k}a_j\), \(Q_k=\sum_{j=1}^{k}a_j^2\), with \(S_0=Q_0=0\).

**Exact diameter and rigidity.** Its squared Euclidean diameter is
\[
D_n^2=Q_{\lfloor n/2\rfloor}+Q_{\lceil n/2\rceil}.
\]
Every diametral pair consists of two vertices with complementary disjoint coordinate supports of sizes \(\lfloor n/2\rfloor\) and \(\lceil n/2\rceil\), each filled with the first that many weights in an arbitrary order. These are the only diametral pairs. Their number is \(n!/2\) for even \(n\) and \(n!\) for odd \(n\).

**Complete minimal enclosing ball.** The unique Euclidean minimum enclosing ball has center \(c_n\mathbf1\) and squared radius
\[
R_n^2=\min_{c\in\mathbb R}\left[nc^2+\max_{0\le k\le n}(Q_k-2cS_k)\right].
\]
This is a finite exact expression: evaluate the bracketed expression on \(\{S_k/n:0\le k\le n\}\cup\{a_j/2:1\le j\le n\}\); the smallest value is \(R_n^2\), with a unique minimizer \(c_n\). The full contact set is precisely the permutations of \((a_1,\ldots,a_k,0,\ldots,0)\) for the maximizing ranks \(k\). There is either one contact rank \(k\), in which case \(c_n=S_k/n\), or two adjacent ranks \(k-1,k\), in which case \(c_n=a_k/2\) and \(S_{k-1}/n\le c_n\le S_k/n\). Each contact rank \(k\) contributes \(n!/(n-k)!\) distinct vertices.

**Three different contact-entropy scales.** Specialize to geometrically decreasing weights \(a_j=t_n^{j-1}\). Write \(N_n\) for the exact number of contacting vertices and \(K_n\) for any contacting rank.

1. If \(t_n=t\in(0,1)\) is fixed, then
\[
K_n=\frac{\log n}{\log(1/t)}+O(1),\quad
R_n^2=\frac1{1-t^2}-\frac1{n(1-t)^2}+O(n^{-2}),\quad
\lim_{n\to\infty}\frac{\log N_n}{(\log n)^2}=\frac1{\log(1/t)},\quad
\lim_{n\to\infty}D_n^2=\frac2{1-t^2}.
\]
2. If \(t_n=\exp(-\lambda/n^\beta)\), where \(\lambda>0\) and \(0<\beta<1\) are fixed, then
\[
\frac{K_n}{n^\beta\log n}\longrightarrow\frac{1-\beta}{\lambda},\qquad
\frac{\log N_n}{n^\beta(\log n)^2}\longrightarrow\frac{1-\beta}{\lambda},\qquad
\frac{R_n^2}{n^\beta}\longrightarrow\frac1{2\lambda},\qquad
\frac{D_n^2}{n^\beta}\longrightarrow\frac1\lambda.
\]
3. If \(t_n=\exp(-\lambda/n)\) with fixed \(\lambda>0\), then, with \(x_\lambda=\lambda^{-1}\log(1+\lambda/2)\),
\[
\frac{K_n}{n}\longrightarrow x_\lambda,\qquad
\frac{\log N_n}{n\log n}\longrightarrow x_\lambda,\qquad
c_n\longrightarrow\frac1{\lambda+2},\qquad
\frac{R_n^2}{n}\longrightarrow\frac1{2(\lambda+2)},\qquad
\frac{D_n^2}{n}\longrightarrow\frac{1-e^{-\lambda}}{\lambda}.
\]
The distinction between \((\log n)^2\), \(n^\beta(\log n)^2\) and \(n\log n\) contact-entropy growth is for a single natural deformation of SIM-bodies, not a change of combinatorial type: all these weights remain strictly decreasing for each finite \(n\).

## Assumptions and scope

Throughout, the ambient metric is the ordinary Euclidean metric of \(\mathbb R^n\), **not** the different induced metric of a homogeneous \((n+1)\)-coordinate lift. The body is
\[
P_n(a)=\left\{z\in\mathbb R_{\ge0}^{n}:\ \sum_{i\in I}z_i\le S_{|I|}\text{ for every nonempty }I\subseteq\{1,\ldots,n\}\right\}.
\]
For strict positive decreasing weights, the complete vertex set is the union, over \(0\le k\le n\), of permutations of \((a_1,\ldots,a_k,0,\ldots,0)\). This vertex description is prior work (Joswig–Klimm–Spitz, Proposition 4), not claimed here. \(D_n\) denotes the maximum distance between two points in \(P_n(a)\); \(R_n\) is the radius of the smallest enclosing Euclidean ball; a contact vertex is a vertex at Euclidean distance \(R_n\) from its unique center. All asymptotics hold as the integer \(n\to\infty\), with the displayed deformation constants fixed.

## Proof

**Diameter.** Fix two vertices \(u,v\). Each coordinate is nonnegative, so
\[
(u_i-v_i)^2\le\max(u_i^2,v_i^2),
\]
with strict inequality whenever both entries are positive. The right-hand side, summed over all \(n\) coordinates, cannot exceed the sum of the \(n\) largest entries in the multiset containing two copies each of \(a_1^2,\ldots,a_n^2\). For \(n=2m\) this sum is \(2Q_m\), and for \(n=2m+1\) it is \(2Q_m+a_{m+1}^2\). Both bounds are realized by assigning the largest \(m\) weights to one support and the largest \(n-m\) to its complementary support, with arbitrary respective within-support permutations. Strict decrease of the weights forces precisely these ranks, and strictness of the coordinate inequality forces disjoint supports. Counting all such pairs gives \(n!/2\) or \(n!\), respectively. The squared norm is strictly convex in either variable, so any nonvertex of the full-dimensional polytope cannot be part of a maximizing pair: express it as a nontrivial convex combination and apply strict convexity of squared distance. Therefore the vertex classification is the complete set of diametral pairs of the entire body.

**Enclosing ball and exact contacts.** The minimizer of \(z\mapsto\max_{v\in P_n(a)}\|v-z\|_2^2\) is unique: the objective is a common \(\|z\|_2^2\) plus a convex maximum of affine functions and hence is strongly convex. Every coordinate permutation preserves the body, so uniqueness forces \(z=c\mathbf1\). A vertex of rank \(k\) has squared distance \(nc^2+Q_k-2cS_k\), proving the one-dimensional minimum formula. Each branch is a convex quadratic with stationary point \(S_k/n\); equality of adjacent branch values occurs exactly when \(c=a_k/2\). The maximum branch changes only at these finitely many breakpoints, so the global minimum lies at one of the listed stationary points or breakpoints. Since every vertex is a permitted rank permutation and the square norm is strictly convex, the only boundary contacts on the entire polytope are the vertices with maximally distant rank. The branch difference from rank \(k-1\) to \(k\) is \(a_k(a_k-2c)\). The strict decrease of the positive weights means that for \(c>0\) the branch values first increase and then decrease; their maximum occurs at a unique rank or at two adjacent tied ranks. The center lies in \(P_n(a)\), and the objective has a strictly negative right derivative at \(c=0\) because all weights are positive, hence \(c>0\). For a unique maximizing rank, first-order optimality yields \(nc=S_k\); for a two-rank tie, \(c=a_k/2\) and the condition that zero belong to the subdifferential gives \(S_{k-1}/n\le c\le S_k/n\). These implications, together with the finite minimum, completely determine all contacts for arbitrary weights. The number of rank-\(k\) vertices is the falling factorial \(n!/(n-k)!\).

**Rank bounds used in all three regimes.** For any active rank \(K\), the adjacent branch differences give \(a_K\ge 2c_n\ge a_{K+1}\), with \(a_0=+\infty\) and \(a_{n+1}=0\). Also \(nc_n\) lies in the interval spanned by the \(S_k\) of the active ranks. In particular,
\[
 S_{\max(0,K-1)}\le nc_n\le S_{\min(n,K+1)},\qquad |nc_n-S_K|\le a_1.
\]
For \(K\ge1\) the last bound improves to \(a_K\), since a tie with its predecessor uses the increment \(a_K\) and a tie with its successor uses \(a_{K+1}\le a_K\). These bounds apply to the lower rank of a tie as well as the upper rank. Always \(c_n\le S_n/n\), and rank zero cannot be active for \(n>2\): it would either give \(c_n=0\), or tie with rank one at \(c_n=a_1/2\le a_1/n\).

**Fixed geometric discount.** Since \(c_n\le S_n/n=O(n^{-1})\), the inequality \(2c_n\ge t^K\) for \(K<n\) forces \(K\to\infty\) (and \(K=n\) already tends to infinity). The two-sided prefix bounds then give \(c_n\sim 1/[n(1-t)]\). The inequality \(t^{K-1}\ge 2c_n\) excludes \(K=n\) for large \(n\), and together the adjacent-weight bounds give \(t^K\asymp1/n\). Thus \(K=\log n/\log(1/t)+O(1)\). At this rank, \(Q_K=1/(1-t^2)+O(n^{-2})\), \(S_K=1/(1-t)+O(n^{-1})\), and \(nc_n-S_K=O(n^{-1})\). The identity \(R_n^2=Q_K-S_K^2/n+n(c_n-S_K/n)^2\) gives the claimed radius expansion. The diameter formula gives its limit. Finally, \(\log(n!/(n-k)!)=k\log n+O(k^2/n)\) uniformly for \(k=o(n)\), while at most two ranks are active. This proves the contact-entropy limit for either choice of \(K\).

**Intermediate discount.** Write \(h_n=\lambda/n^\beta\). Geometric sums give \(S_n\sim n^\beta/\lambda\), \(Q_n\sim n^\beta/(2\lambda)\), and \(c_n\le S_n/n\to0\). For \(K<n\), \(e^{-h_nK}\le 2c_n\), while for \(K=n\), \(h_nK=\lambda n^{1-\beta}\). Thus \(h_nK\to\infty\) and \(S_K\sim n^\beta/\lambda\). By the prefix-sum bound \(|nc_n-S_K|\le1\), this gives \(c_n\sim n^{\beta-1}/\lambda\). Since \(e^{-h_n(n-1)}=o(n^{\beta-1})\), the lower bound \(a_K\ge2c_n\) rules out \(K=n\) eventually. The adjacent weights differ by the ratio \(e^{-h_n}\to1\), giving \(e^{-h_nK}\sim2c_n\), and hence \(K\sim(1-\beta)n^\beta\log n/\lambda=o(n)\). The geometric tail \(Q_n-Q_K\) and both center-dependent terms \(nc_n^2\) and \(2c_nS_K\) are \(o(n^\beta)\), yielding the radius limit. The exact diameter yields its limit. The falling-factorial entropy estimate and the at-most-two-ranks bound give the limit for \(N_n\).

**Macroscopic discount.** Put \(t_n=e^{-\lambda/n}\). The scaled sums converge uniformly to
\[
\frac{S_{\lfloor nx\rfloor}}n\longrightarrow A(x)=\frac{1-e^{-\lambda x}}\lambda,\qquad
\frac{Q_{\lfloor nx\rfloor}}n\longrightarrow B(x)=\frac{1-e^{-2\lambda x}}{2\lambda}.
\]
Take any subsequence on which \(K/n\to x\). The prefix-sum bound gives \(c_n\to A(x)\). If \(x=0\), then \(a_{K+1}\to1\) but \(2c_n\to0\), a contradiction; if \(x=1\), then \(a_K\to e^{-\lambda}<2A(1)\) since \(2(e^\lambda-1)>\lambda\), also a contradiction. Thus \(K\) is eventually interior on the subsequence and the adjacent-weight bounds yield \(e^{-\lambda x}=2A(x)\). This equation has the unique solution \(x=x_\lambda=\lambda^{-1}\log(1+\lambda/2)\), with \(A(x)=(\lambda+2)^{-1}\). All subsequences have these limits. Evaluating \(c^2+B(x)-2cA(x)\) gives \(1/[2(\lambda+2)]\). The contact-entropy limit follows from Stirling's formula \(\log(n!/(n-K)!)=K\log n+O(n)\) and the at-most-two-ranks bound. The exact diameter formula and a Riemann sum give \(\lim D_n^2/n=(1-e^{-\lambda})/\lambda\).

## Verification

The standalone standard-library program `check_sim.py` implements exact rational rank-distance and enclosing-ball calculations. Run `python3 check_sim.py` from the directory containing this file. The recorded successful report is `SIM_METRIC_PASS exact_vertex_cases=12 pairs=165555 exact_rank_cases=41644 generic_weight_cases=495 asymptotic_cases=8`. It exhausts all vertices and vertex pairs for twelve small geometric profiles, checks 41,644 rank-pair inequalities, and checks 495 strictly decreasing rational sequences. Its large-dimensional floating-point tests probe rank, center or metric quantities in the fixed and macroscopic discount regimes, not the intermediate regime or the entropy limits. The all-dimensional assertions are proved above and do not rely on finite enumeration or floating-point accuracy.

## Relationship to prior work

Joswig, Klimm and Spitz give the SIM-body definition, generalized-permutahedron structure and rank-orbit vertex description used here. Doker and Giannakopoulos–Koutsoupias provide antecedent families and their auction/volume setting. For a partial permutohedron \(\mathcal P(m,N)\) with \(m\le N\), the increment sequence is \(a_j=N-j+1\), \(1\le j\le m\), up to the ambient dimension convention. The earlier *Exact circumball and contact-rank transitions of partial permutohedra* gives the exact radius and one- or two-rank contact classification in this standard Euclidean specialization, including the same rank intervals with clipped stationary points. Its displayed result is for consecutive labels, not arbitrary real decrements or the three geometric-discount contact-entropy laws. The present result does not claim the rank-orbit vertex description, the consecutive-label circumball, or general convex optimality principles as new.

## Limitations

The classification assumes strictly decreasing positive weights. Equal weights change the vertex-orbit structure and can create many additional contact ranks, as in the cube limit. The formulas use the projected standard Euclidean metric and cannot be silently transferred to the homogeneous lift. The earlier partial-permutohedron circumball statement was compared on its stated consecutive-label scope. There is no claim of exhaustive priority or exclusion of a stronger result for wider symmetric polymatroid families. The exact diameter is a short general inequality, while the geometric content of the combined finding includes the full sphere/contact classification and three distinct asymptotic contact regimes.

## References

- M. Joswig, M. Klimm, S. Spitz, *Generalized permutahedra and optimal auctions*, arXiv:2108.00979, first public posting 2021-08-02, https://arxiv.org/abs/2108.00979 . See Section 2, Propositions 3–4, Corollary 6.
- J. Doker, *Geometry of Generalized Permutohedra*, master's thesis, 2011, Section 2.4, https://matthbeck.github.io/teach/masters/jeff.pdf .
- Y. Giannakopoulos, E. Koutsoupias, *Duality and Optimality of Auctions for Uniform Distributions*, 2018, https://doi.org/10.1137/17M1136480 .
- F. Behrend et al., *Partial permutohedra*, arXiv:2207.14253, 2022, https://arxiv.org/abs/2207.14253 .
- *Exact circumball and contact-rank transitions of partial permutohedra*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-circumball-and-contact-rank-transitions-of-partial-permuto--5aee45e4fbff .
