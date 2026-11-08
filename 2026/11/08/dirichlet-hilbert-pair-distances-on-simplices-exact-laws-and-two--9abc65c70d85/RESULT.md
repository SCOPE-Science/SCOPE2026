# Dirichlet–Hilbert pair distances on simplices: exact laws and two-Gumbel extremes

## Finding
Let \(S\) be a nondegenerate Euclidean simplex with \(n\ge2\) labeled vertices. Independently sample \(X,Y\) so that their positive barycentric coordinate vectors have the symmetric \(\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\) distribution, for any fixed \(\alpha>0\). Equip the interior of \(S\) with the **unhalved** logarithmic cross-ratio Hilbert distance \(d_H\), and put \(D_{n,\alpha}=d_H(X,Y)\). All assertions are affine-shape-independent.

Define the beta function \(B\), standard logistic map \(\sigma(t)=e^t/(1+e^t)\), regularized incomplete beta function \(I_u(\alpha,\alpha)\), and
\[
 g_\alpha(t)=\frac{e^{\alpha t}}{B(\alpha,\alpha)(1+e^t)^{2\alpha}},\qquad
 G_\alpha(t)=I_{\sigma(t)}(\alpha,\alpha),\qquad C_\alpha=\frac{1}{\alpha B(\alpha,\alpha)}.
\]
For every integer \(n\ge2\), every \(\alpha>0\), and every \(r\ge0\), the **complete pair-distance distribution** is
\[
 \boxed{\Pr\{D_{n,\alpha}\le r\}=n\int_{-\infty}^{\infty}g_\alpha(t)
 [G_\alpha(t+r)-G_\alpha(t)]^{n-1}\,dt.} \tag{1}
\]
For fixed \(n,\alpha\), the sharp small-radius law is
\[
 \boxed{\Pr\{D_{n,\alpha}\le r\}\sim
 \frac{n B(n\alpha,n\alpha)}{B(\alpha,\alpha)^n}\,r^{n-1}\qquad(r\downarrow0).} \tag{2}
\]
At the Euclidean-volume specialization \(\alpha=1\), the formula admits the exact hypergeometric evaluation, for \(r>0\),
\[
 \boxed{\Pr\{D_{n,1}\le r\}
 =n(e^r-1)^{n-1}B(n,n)\,{}_2F_1(n-1,n;2n;1-e^r),\quad
 \mathbb E D_{n,1}=2\sum_{j=1}^{n-1}\frac1j.} \tag{3}
\]
The CDF equals zero at \(r=0\). In particular, the entire distribution, not merely its expected value, is specified without simulation.

Fix \(\alpha>0\) and let \(n\to\infty\). If \(U,V\) are independent standard Gumbel variables, each with CDF \(\exp(-e^{-s})\), then
\[
 \boxed{\alpha D_{n,\alpha}-2\log(n C_\alpha)\ \Longrightarrow\ U+V.} \tag{4}
\]
Moreover, writing \(\gamma\) for the Euler–Mascheroni constant,
\[
 \boxed{\mathbb E D_{n,\alpha}
 =\frac2\alpha\bigl(\log(n C_\alpha)+\gamma\bigr)+o(1),\qquad
 \operatorname{Var}(D_{n,\alpha})\to\frac{\pi^2}{3\alpha^2}.} \tag{5}
\]
The centering constant depends on the Dirichlet concentration parameter, so formula (4) quantitatively calibrates the distances used in probability-simplex geometry.

## Assumptions and scope
The simplex has \(n\) vertices and affine dimension \(n-1\). Dirichlet sampling is defined in the barycentric coordinates of these vertices; for \(\alpha=1\), it is exactly normalized Euclidean volume. The symmetric Dirichlet distribution for any \(\alpha>0\) is invariant under vertex relabeling, but for \(\alpha\ne1\) it is not uniform Euclidean volume. The Hilbert metric is **unhalved**: multiplying the logarithmic cross-ratio metric by \(1/2\) would multiply the distances, expectations, centering constants and standard deviations by \(1/2\). All finite distribution formulas are valid for every positive \(\alpha\), without assuming an integer or rational concentration parameter. The asymptotic assertions keep \(\alpha\) fixed as \(n\) grows; no uniformity when \(\alpha\) also varies is asserted. No distances to boundary points or claims about intrinsic Hilbert-volume sampling are made.

## Proof
**1. Hilbert distance and normalized gamma variables.** Cross-ratios are invariant under affine bijections, so work in the standard open probability simplex. For barycentric vectors \(x,y\), the Hilbert formula is
\[
 d_H(x,y)=\max_i\log(x_i/y_i)-\min_i\log(x_i/y_i). \tag{6}
\]
Take two independent families of \(n\) independent \(\operatorname{Gamma}(\alpha,1)\) variables \(A_i,B_i\). Then \(X_i=A_i/\sum_jA_j\) and \(Y_i=B_i/\sum_jB_j\) have the prescribed independent symmetric Dirichlet laws. In (6), the common random factor \((\sum_jB_j)/(\sum_jA_j)\) cancels between the largest and smallest coordinate ratios. Consequently,
\[
 D_{n,\alpha}\stackrel{d}{=}\max_{1\le i\le n}Z_i-\min_{1\le i\le n}Z_i,
 \qquad Z_i=\log(A_i/B_i), \tag{7}
\]
with \(Z_1,\ldots,Z_n\) genuinely independent. The quotient \(A_i/B_i\) has beta-prime density \(t^{\alpha-1}(1+t)^{-2\alpha}/B(\alpha,\alpha)\), \(t>0\). A logarithmic change of variables gives the density \(g_\alpha\), CDF \(G_\alpha\) and exact symmetry \(g_\alpha(z)=g_\alpha(-z)\) stated above. This establishes the geometric-to-probabilistic reduction with all normalizations fixed.

**2. Finite distribution and small balls.** Condition on the unique almost-sure index of the minimum \(Z_i=t\). The other \(n-1\) independent observations must lie in \([t,t+r]\), giving (1). As \(r\downarrow0\), \([G_\alpha(t+r)-G_\alpha(t)]/r\to g_\alpha(t)\). The bound \(0\le [G_\alpha(t+r)-G_\alpha(t)]/r\le\sup g_\alpha\), together with integrability of \(g_\alpha\), permits dominated convergence. Under \(u=\sigma(t)\),
\[
 \int_{\mathbb R}g_\alpha(t)^n\,dt
 =\frac{B(n\alpha,n\alpha)}{B(\alpha,\alpha)^n},
\]
which proves (2). This is a probability statement, not an unnormalized Hilbert-volume coefficient.

**3. Exact uniform-volume evaluation.** When \(\alpha=1\), \(G_1(t)=\sigma(t)\), and \(u=\sigma(t)\) is uniform on \([0,1]\). With \(a=e^r-1\),
\[
 G_1(t+r)-G_1(t)=\frac{a u(1-u)}{1+a u}.
\]
Hence (1) becomes \(n a^{n-1}\int_0^1u^{n-1}(1-u)^{n-1}(1+a u)^{-(n-1)}\,du\). Euler's hypergeometric integral yields (3). Also \(Z_i\) are standard logistic; \(\sigma(Z_i)\) are independent uniforms. If \(Z_{(n)}\) is the largest logistic variable, then \(\sigma(Z_{(n)})\) has \(\operatorname{Beta}(n,1)\) law, and elementary beta-logarithm integration yields \(\mathbb EZ_{(n)}=\sum_{j=1}^{n-1}1/j\). Symmetry gives \(\mathbb EZ_{(1)}=-\mathbb EZ_{(n)}\), so the mean range is twice that harmonic sum. Finite expectations follow from exponential tails.

**4. Two independent extrema.** Since \(g_\alpha(z)\sim e^{-\alpha z}/B(\alpha,\alpha)\) as \(z\to+\infty\),
\[
 \Pr\{Z_i>z\}\sim C_\alpha e^{-\alpha z},\qquad
 \Pr\{Z_i<-z\}\sim C_\alpha e^{-\alpha z} \quad(z\to+\infty).
\]
Set \(a_n=\log(nC_\alpha)/\alpha\), \(M_n=\max_iZ_i\), \(m_n=\min_iZ_i\). For real \(s,t\), independence of the \(Z_i\) gives the **joint** limit
\[
 \begin{aligned}
 &\Pr\{\alpha(M_n-a_n)\le s,\ \alpha(-m_n-a_n)\le t\}\\
 &=\bigl[G_\alpha(a_n+s/\alpha)-G_\alpha(-a_n-t/\alpha)\bigr]^n
 \longrightarrow \exp(-e^{-s}-e^{-t}).
 \end{aligned}
\]
The limit factors, establishing *independence* of the two Gumbel extremes; the continuous mapping theorem gives (4). The right and left centered tails of each extreme obey exponential and double-exponential bounds, respectively: the upper bound follows from the exponential survival tail and a union bound; the lower bound follows from \((1-p)^n\le e^{-np}\) until the central region, and the remaining far tail from the opposite exponential tail of \(Z_i\). Splitting the tail integrals at the fixed central region yields uniform integrability of every fixed positive power of the centered extremes. Thus the first two moments converge. Since a standard Gumbel has mean \(\gamma\) and variance \(\pi^2/6\), and the limiting extremes are independent, (5) follows. This uses a joint extreme-value limit, not an unjustified assumption that finite-sample maxima and minima are independent.

## Verification
The standalone `check_hilbert_dirichlet.py` calculates (1) using incomplete beta functions and independent quadrature, compares it with direct Hilbert distances computed from two independently normalized gamma samples, tests the \(\alpha=1\) hypergeometric identity and harmonic mean, and checks the small-radius and large-dimension normalizations. It successfully completed five finite-dimensional configurations with 100,000 pairs each, three large-dimensional configurations with 6,000 pairs each, and six small-radius checks. Its final output was `HILBERT_DIRICHLET_RANGE_VERIFIED_FINITE_CDF_AND_LIMIT_SANITY`. These finite numerical checks are corroboration; the all-dimensional claims rest on the preceding proof. Run `OPENBLAS_NUM_THREADS=1 python check_hilbert_dirichlet.py` with versions listed in `requirements.txt`.

## Relationship to prior work
Foertsch and Karlsson (2004) establish the metric characterization of simplices as the Hilbert geometries isometric to finite-dimensional normed spaces, without a random-distance law. Nielsen and Sun (2017) describe computation and statistical uses of the Hilbert simplex metric. Nielsen and Sun (2023, Section 2 and Figure 7) give the coordinatewise distance and show simulated distance histograms for pairs of uniform points, but not an exact law, beta-prime reduction, or joint extreme-value asymptotics. A prior fixed-center Euclidean Hilbert-ball-mass identity yields an implicit integrated two-point law at \(\alpha=1\); it neither treats both points under arbitrary symmetric Dirichlet sampling nor gives the sharp two-extreme concentration-dependent limit. Equations (1)–(5) state the quantitative contribution beyond that background. Standard order-statistic and beta-prime facts are used as proof ingredients, not claimed as independent discoveries.

## Limitations
The research concerns the Hilbert metric on simplices with symmetric Dirichlet sampling. Nothing is asserted for nonsimplicial domains, asymmetric Dirichlet parameters, intrinsic Hilbert volumes, or concentration parameters varying with dimension. The full literature cannot be exhaustively searched; an equivalent unpublished or unindexed calculation remains a historical-priority risk. The formula (1) specializes to generic order-statistic range calculus after the nontrivial geometric identification; the value lies in its explicit induced simplex law, small-ball normalization, exact uniform-volume evaluation, and sharp two-sided limiting calibration. Numerical checks cannot certify the infinite-dimensional asymptotics. No independent mathematical audit is claimed.

## References
- T. Foertsch and A. Karlsson, *Hilbert metrics and Minkowski norms*, arXiv:math/0407197v1 (first public arXiv posting 2004-07-12), https://arxiv.org/abs/math/0407197.
- F. Nielsen and K. Sun, *Clustering in Hilbert simplex geometry*, arXiv:1704.00454 (2017), https://arxiv.org/abs/1704.00454.
- F. Nielsen and K. Sun, *Non-linear Embeddings in Hilbert Simplex Geometry*, Proceedings of Machine Learning Research **221** (2023), https://proceedings.mlr.press/v221/nielsen23a/nielsen23a.pdf.
