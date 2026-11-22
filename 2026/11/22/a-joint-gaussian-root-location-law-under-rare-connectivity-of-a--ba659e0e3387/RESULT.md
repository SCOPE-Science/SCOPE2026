# A joint Gaussian root-location law under rare connectivity of a one-dimensional nearest-neighbor graph

## Finding

For each integer \(n\ge2\), sample independent \(\operatorname{Uniform}(0,1)\) points and write their order statistics as \(X_{(1)}<\cdots<X_{(n)}\). Direct one edge from each sample point to its (almost surely unique) nearest other sample point, and let \(\mathcal C_n\) be the event that the resulting directed graph is weakly connected. Write \(J_n\in\{1,\ldots,n-1\}\) for the index of the unique reciprocal-nearest-neighbor pair \((X_{(J_n)},X_{(J_n+1)})\), and \(M_n=(X_{(J_n)}+X_{(J_n+1)})/2\) for its spatial midpoint. All conditional assertions below refer to \(\mathcal C_n\).

**Single structural and distributional theorem.** The graph is connected precisely when the sequence of its \(n-1\) interior spacings first strictly decreases and then strictly increases. For all \(n\ge2\),
\[
\Pr(\mathcal C_n)=\frac{2^{n-2}}{(n-1)!},\qquad
J_n\mid\mathcal C_n\ \stackrel d=\ 1+\operatorname{Bin}(n-2,1/2).
\]
The conditional rank \(J_n\) is independent of the unordered multiset of interior spacings and of the two exterior spacings. The finite conditional moments are exactly
\[
\begin{aligned}
&\mathbb E[J_n]=\frac n2,\quad \mathbb E[M_n]=\frac12,\quad
\operatorname{Var}(J_n)=\frac{n-2}{4},\\
&\operatorname{Cov}(J_n,M_n)=\frac{(n-1)-(n-1)^{-1}}{4(n+1)},\\
&\operatorname{Var}(M_n)=\frac{n-(n-1)^{-2}}{2(n+1)(n+2)}.
\end{aligned}
\]
Consequently, as \(n\to\infty\),
\[
\boxed{
\left(\frac{J_n-n/2}{\sqrt n},\ \sqrt n(M_n-1/2)\right)\ \Bigm|\ \mathcal C_n
\ \xrightarrow{d}\ \mathcal N_2\!\left(0,
\begin{pmatrix}1/4&1/4\\1/4&1/2\end{pmatrix}\right).}
\]
In particular, the asymptotic correlation between the root-pair rank and its position equals \(1/\sqrt2\), while the conditional spatial-midpoint variance is asymptotic to \(1/(2n)\).

## Assumptions and scope

The sample size \(n\) is an integer at least two; the observations are independent, absolutely continuous and uniformly distributed on the **fixed unit interval**. Edge directions use the ordinary Euclidean distance, with the undirected connectivity interpreted in the weak sense. Ties have probability zero. There are no extra random graph edges or distance thresholds. Finite-moment statements refer to the stated connectivity conditioning, not the unconditional sample.

## Proof

**1. Characterize connectivity and its rare-event probability.** Set \(m=n-1\), \(G_i=X_{(i+1)}-X_{(i)}\) for \(1\le i\le m\), and set \(G_0=X_{(1)}\), \(G_{m+1}=1-X_{(n)}\). Every directed edge joins consecutive sample points. An interior edge across gap \(G_i\) is missing from the underlying undirected graph exactly when \(G_i>G_{i-1}\) and \(G_i>G_{i+1}\), for \(2\le i\le m-1\); the two extreme interior edges are necessarily present. Thus connectivity is equivalent to having no strict local maximum in the finite list \(G_1,\ldots,G_m\), which for distinct entries is equivalent to a strictly decreasing segment followed by a strictly increasing segment. The minimum interior gap is the unique reciprocal two-cycle.

The \(m\) interior gaps, together with the two exterior gaps, have the symmetric \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Their interior rank permutation is uniform among \(m!\) permutations, independent of all ordered interior magnitudes and both exterior spacings. Exactly \(2^{m-1}\) of these permutations are valley-shaped: reading the \(m-1\) nonminimal gaps in decreasing order, place each, independently, at the left or the right end, then leave the minimum in the center. Conditioning on connectivity therefore produces \(m-1=n-2\) independent fair placement bits. Their number of left placements is \(J_n-1\), proving the event probability, binomial law and stated independence.

**2. Exact conditional moments.** Write \(a_1>\cdots>a_m\) for the interior gaps in decreasing order and let \(B_1,\ldots,B_{m-1}\) be the independent fair placement bits, with \(B_r=1\) for the left end. Under connectivity, the midpoint is represented exactly by
\[
J_n=1+\sum_{r=1}^{m-1}B_r,\qquad
M_n=\frac{1+G_0-G_{m+1}}2
+\sum_{r=1}^{m-1}(B_r-1/2)a_r.
\]
These bits are independent of all spacing magnitudes. Dirichlet moments give
\[
\mathbb E G_i=\frac1{n+1},\quad
\mathbb E G_i^2=\frac2{(n+1)(n+2)},\quad
\operatorname{Var}(G_0-G_{m+1})=\frac2{(n+1)(n+2)}.
\]
For \(T=\min_{1\le i\le m}G_i=a_m\), translating the \(m\) constrained simplex coordinates yields, for \(0\le t\le1/m\),
\[
\Pr(T>t)=(1-mt)^n,\quad
\mathbb ET=\frac1{m(n+1)},\quad
\mathbb ET^2=\frac2{m^2(n+1)(n+2)}.
\]
The conditional variance of the bit-sum in \(M_n\) is \(\frac14\sum_{r<m}a_r^2\), and its covariance with \(J_n\) is \(\frac14\sum_{r<m}a_r\). The bit-sum has conditional mean zero, so it has zero covariance with the exterior-spacing contribution. Substituting the Dirichlet and minimum-gap moments into the law of total variance gives precisely the three asserted second-moment formulas. The cases \(n=2,3\) are included without empty-sum ambiguity.

**3. Joint conditional Gaussian limit.** Use the exponential representation of the Dirichlet vector: if \(E_0,\ldots,E_{m+1}\) are independent \(\operatorname{Exp}(1)\), then \(G_i=E_i/\sum_{j=0}^{m+1}E_j\). The law of large numbers gives, under the conditioning as well (which concerns only the independent interior permutation),
\[
\sum_{r<m}a_r\xrightarrow{\Pr}1,\qquad
n\sum_{r<m}a_r^2\xrightarrow{\Pr}2,\qquad
\sqrt n\max_{r<m}a_r\xrightarrow{\Pr}0.
\]
For the second limit, apply the law of large numbers to the squared exponentials; for the third, their maximum is \(O_{\Pr}(\log n)\), while the sum is \(n+O_{\Pr}(\sqrt n)\). Removing the minimal gap does not change any of these limits. Also \(\sqrt n(G_0-G_{m+1})\to0\) in probability. The centered, rescaled vector is therefore the sum of independent (given the spacing magnitudes) symmetric two-point vectors
\[
\sum_{r=1}^{m-1}(B_r-1/2)
\begin{pmatrix}n^{-1/2}\\\sqrt n\,a_r\end{pmatrix}
+\begin{pmatrix}0\\\sqrt n(G_0-G_{m+1})/2\end{pmatrix}.
\]
Its conditional covariance matrix tends in probability to \(\bigl(\begin{smallmatrix}1/4&1/4\\1/4&1/2\end{smallmatrix}\bigr)\), while the largest summand norm tends to zero in probability. The triangular-array Lindeberg central limit theorem, first conditional on the spacing magnitudes and then unconditionally, proves the stated joint Gaussian limit. The limiting covariance matrix has determinant \(1/16>0\).

## Verification

The accompanying `checker.py` enumerates every relative ordering of the interior spacings for each \(2\le n\le9\), independently counts all connected rank patterns, and checks the full binomial law of the reciprocal-pair index. It then integrates the conditional first and second moments by an independent exact-rational representation of the ordered interior exponential gaps as independent exponential increments. All eight sample sizes passed. This finite verification confirms the formulas only at the checked sizes; the probability, finite moments at all \(n\), and limit theorem rest on the analytic arguments above. Run with `python checker.py` using Python's standard library.

## Relationship to prior work

Penrose and Wade's March 23, 2006 arXiv preprint primarily studies the on-line nearest-neighbor graph and, as an ancillary result, computes weighted-length moments for the standard directed one-dimensional nearest-neighbor graph using Dirichlet spacings; its theorems do not state the rare **connected-graph conditional joint root-rank/spatial-location law** given here. Eppstein, Paterson and Yao describe nearest-neighbor components and reciprocal-pair roots, and treat expected component counts in two dimensions, not this conditional bivariate law. Later work on random near-neighbor graphs addresses typical component counts and giant-component constructions. Published adjacent results on nearest-neighbor count–length covariances or circular samples do not imply the conditional spatial midpoint fluctuations under interval connectivity. Historical priority remains provisional because some adjacent published records were accessible only as summaries.

## Limitations

The normal limit is for the unique reciprocal-pair midpoint and its index *conditional on the extremely rare event* \(\mathcal C_n\). It is not an unconditional central limit theorem, an estimate for higher-dimensional geometric graphs, or a universal result for nonuniform sampling densities. The exact \(n\)-dependent formulas do not assert finite-sample Gaussianity. No optimal convergence rate or independent external audit is claimed. A search of available mathematical literature and records did not establish a broader equivalent theorem; this absence is not a proof of historical priority.

## References

1. M. D. Penrose and A. R. Wade, *Limit theory for the random on-line nearest-neighbour graph*, first arXiv version, March 23, 2006, [arXiv:math/0603561v1](https://arxiv.org/abs/math/0603561).
2. D. Eppstein, M. S. Paterson and F. F. Yao, *On Nearest-Neighbor Graphs*, Discrete & Computational Geometry 17 (1997), 263–282; [accessible author's manuscript](https://www.ics.uci.edu/~eppstein/pubs/EppPatYao-DCG-97.pdf), doi:10.1007/PL00009293.
3. G. C. Linderman et al., *Randomized near-neighbor graphs, giant components and applications in data science*, Journal of Applied Probability 57 (2020), 458–476; [open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7480951/).
