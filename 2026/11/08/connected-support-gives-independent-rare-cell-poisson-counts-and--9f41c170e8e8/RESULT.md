# Connected support gives independent rare-cell Poisson counts and Gaussian bulk fluctuations

## Finding

Theorem (a mixed-scale conditional-Poisson limit). Fix integers \(r,c\ge2\) and a spanning connected bipartite graph \(E\subseteq[r]\times[c]\). Write \(F=([r]\times[c])\setminus E\). Fix positive \(a_{ij}\) for \((i,j)\in E\), positive \(\eta_{ij}\) for \((i,j)\in F\), and positive vertex factors \(h_i,k_j\). Let \(q_{ij}=a_{ij}h_i k_j\) on \(E\), with positive prescribed row and column totals \(R_i=\sum_{j:(i,j)\in E}q_{ij}\) and \(C_j=\sum_{i:(i,j)\in E}q_{ij}\). Suppose \(n\) tends to infinity through integers for which all \(nR_i\) and \(nC_j\) are integers. Independently of any unconditioned sampling interpretation, define a random nonnegative integer table \(X^{(n)}\) with precisely these margins and probability proportional to

\[
\prod_{(i,j)\in E}\frac{a_{ij}^{X_{ij}}}{X_{ij}!}
\prod_{(i,j)\in F}\frac{(\eta_{ij}/n)^{X_{ij}}}{X_{ij}!}.
\]

Set \(\beta_{ij}=\eta_{ij}h_i k_j\) for \((i,j)\in F\). Let \(D\) be the diagonal matrix with entries \(q_{ij}\), \((i,j)\in E\). Let \(B\) be the vertex-edge incidence matrix of \(E\), with one column-vertex row deleted, so its size is \((r+c-1)\times|E|\). Then

\[
\left((X^{(n)}_{ij})_{F},\ \big((X^{(n)}_{ij}-nq_{ij})/\sqrt n\big)_{E}\right)
\ \Longrightarrow\ \big((Z_{ij})_F,\ G\big),
\]

where the \(Z_{ij}\) are mutually independent \(\operatorname{Poisson}(\beta_{ij})\), \(G\) is an independent centered (possibly singular) Gaussian vector with covariance

\[
\Sigma=D-DB^{\mathsf T}(BDB^{\mathsf T})^{-1}BD.
\]

In particular, the rare-cell vector converges in total variation to the independent Poisson law. The statement includes empty \(F\) (the Poisson vector then has zero coordinates) and connected trees (the Gaussian covariance is zero).

**Sharp balanced diagonal example.** Fix \(d\ge3\), row and column margins all equal to \(n\), weights \(a_{ij}=1\) for \(i\ne j\) and \(a_{ii}=\theta_i/n\), where all \(\theta_i>0\). Then

\[
(X_{11},\ldots,X_{dd})\Longrightarrow
\bigotimes_{i=1}^d\operatorname{Poisson}\!\left(\frac{\theta_i}{d-1}\right),
\]

independently of the Gaussian off-diagonal field with center \(n/(d-1)\) per cell. For \(d=3\), the off-diagonal fluctuation of any single cell converges to \(N(0,1/12)\).

**Connectivity boundary.** For \(d=2\) with the same diagonal-suppressed weights, the allowed graph consists of two disjoint edges, the margins force \(X_{11}=X_{22}=K_n\), and the *exact* law is

\[
\Pr(K_n=k)=\frac{(\theta_1\theta_2)^k (n)_k^2}{(k!)^2n^{2k}Z_n},\qquad
Z_n=\sum_{\ell=0}^{n}\frac{(\theta_1\theta_2)^\ell(n)_\ell^2}{(\ell!)^2n^{2\ell}},\quad 0\le k\le n.
\]

Here \((n)_k=n!/(n-k)!\). Consequently \(K_n\) tends in total variation to the discrete Bessel law

\[
\Pr(K=k)=\frac{(\theta_1\theta_2)^k}{(k!)^2I_0(2\sqrt{\theta_1\theta_2})},\qquad
I_0(2\sqrt z)=\sum_{k\ge0}\frac{z^k}{(k!)^2}.
\]

The two diagonal counts are therefore perfectly dependent and not independent Poisson. This explicit disconnected-support example demonstrates why graph connectivity is substantive, not a cosmetic hypothesis.

## Assumptions and scope

All dimensions and weights except the suppressed weights' factor \(1/n\) are fixed; the graph \(E\) must contain all row/column vertices and be connected. Positive \(q\) with the displayed margins are assumed as data, so there is no unproved existence claim for scaling factors. All convergence takes place along the integer subsequence of admissible margins; when no unbounded such sequence exists, the theorem does not assert one. The matrix \(B\) has full row rank because \(E\) is connected. Each original table has exactly the displayed margins; the unconditioned independent-Poisson model below is a proof device.

## Proof

**Step 1 (exact conditional representation).** Let \(U_{ij}\) on \(E\) be independent \(\operatorname{Poisson}(nq_{ij})\), and \(V_{ij}\) on \(F\) independent \(\operatorname{Poisson}(\beta_{ij})\), independent of all \(U\)'s. Condition their combined row and column sums to be \((nR,nC)\). The factor relating their unconditioned joint probability at a table to the displayed Gibbs weight equals

\[
\prod_{ij}(nh_i k_j)^{X_{ij}}
=n^{\sum_i nR_i}\prod_i h_i^{nR_i}\prod_j k_j^{nC_j},
\]

which depends only on the fixed margins. Hence the conditional law is exactly that of \(X^{(n)}\). In particular its conditioning event has positive probability, since the allowed mean has integral margins for large admissible \(n\), and the connected incidence lattice has all integer offsets compatible with total balance; for the zero-offset conditioning event a feasible integral allowed table is guaranteed for all sufficiently large \(n\) by positivity of \(q\) and lattice approximation inside its affine fiber (or equivalently by the local limit below).

**Step 2 (the needed lattice local limit).** Delete one redundant column-sum constraint. With \(s=r+c-1\), the allowed margins vector is \(BU\) and its mean is \(nBq=nm\). The \(s\times|E|\) integer matrix \(B\) has full rank and spans the full lattice \(\mathbb Z^s\). Indeed, after multiplying column-vertex rows by \(-1\), the incidence submatrix of a spanning tree is square unimodular when one vertex row is removed. Put \(M=BDB^{\mathsf T}\), which is positive definite. For each fixed \(z\in\mathbb Z^s\), Fourier inversion of the independent Poisson characteristic function gives

\[
\Pr\{BU=nm-z\}
=(2\pi n)^{-s/2}(\det M)^{-1/2}(1+o(1)).
\]

The sole unit-modulus point on the Fourier torus is zero modulo \(2\pi\), by the full-lattice span. On a fixed small neighborhood, the logarithm expands as \(-\tfrac n2t^{\mathsf T}Mt+O(n|t|^3)\). Off that neighborhood its modulus is exponentially smaller. In particular the corresponding Fourier integral gives the **uniform** bound \(\sup_{z\in\mathbb Z^s}\Pr\{BU=nm-z\}\le Cn^{-s/2}\) for all sufficiently large \(n\), using the triangle inequality before integration. These estimates also hold after finitely many \(O(1)\) shifts of margins.

**Step 3 (rare Poisson vector).** Let \(H\) be the analogous deleted-row incidence matrix over \(F\). For each fixed nonnegative rare vector \(v\), the exact conditioning formula is

\[
\Pr\{V=v\mid BU+HV=nm\}
=\frac{\Pr\{V=v\}\Pr\{BU=nm-Hv\}}{\mathbb E[\Pr\{BU=nm-HV\}] }.
\]

The local-limit ratio at fixed \(v\) tends to one. The uniform bound in Step 2, together with dominated convergence against the summable mass function of \(V\), shows that the denominator is asymptotic to \(\Pr\{BU=nm\}\). Therefore the conditional mass converges to the unconditioned product-Poisson mass for each \(v\). Since the limit masses sum to one, total-variation convergence follows.

**Step 4 (Gaussian bulk, jointly and independently).** For any fixed \(v\) and \(t\in\mathbb R^{|E|}\), use the same Fourier integral with the extra factor \(\exp(i t^{\mathsf T}(U-nq)/\sqrt n)\). After setting the integration variable equal to \(z/\sqrt n\), the exponent in the numerator has quadratic form

\[
-\tfrac12(t+B^{\mathsf T}z)^{\mathsf T}D(t+B^{\mathsf T}z)
\]

plus an offset phase tending to one. Dividing by the scalar local limit and completing the Gaussian square yields

\[
\lim_{n\to\infty}\mathbb E\left[e^{it^{\mathsf T}(U-nq)/\sqrt n}\mid BU=nm-Hv\right]
=\exp(-\tfrac12t^{\mathsf T}\Sigma t).
\]

The same Fourier magnitude bound controls the numerator by \(Cn^{-s/2}\), uniformly in fixed \(t\) and all rare vectors \(v\). Applying dominated convergence to the countable Poisson mixing law proves that the joint characteristic function factors into the product-Poisson factor and the centered-Gaussian factor. This proves the mixed-scale limit, including a singular \(\Sigma\).

**Step 5 (balanced examples).** For \(d\ge3\), the bipartite graph excluding diagonal edges is connected. Set \(h_i=1\), \(k_j=1/(d-1)\). Then \(q_{ij}=1/(d-1)\) for \(i\ne j\) and \(\beta_{ii}=\theta_i/(d-1)\). The Gaussian diagonal-entry exclusion variance for \(d=3\) follows from the rank-one cycle kernel or directly from \(\Sigma\). When \(d=2\), the margins force the displayed single parameter \(K_n\). Dividing its Gibbs weight by that of \(K_n=0\) gives the falling-factorial ratio above. Since \((n)_k/n^k\le1\), dominated convergence of the series proves both the Bessel normalizer and total-variation convergence.

## Verification

The standalone standard-library `verify.py` reconstructs all small fixed-margin tables (including the exact suppressed-cell reweighting), checks the conditioning identity against the original Gibbs probabilities, verifies the \(2\times2\) Bessel formula and its finite-size convergence, and computes the Gaussian projected covariance and incidence ranks. It executes **831 finite checks**. These are exact finite tests or consistency checks of asymptotics, not a computational proof of the general Fourier local limit; that infinite argument is given above. Reproduce with `python3 verify.py`.

## Relationship to prior work

Duan, Lyu and Powell (2026) introduce weighted Poisson contingency tables and their equivalence to Gibbs permutations, with entropic-transport limits. Their dimension-growing bounded-cost results do not directly address fixed dimensions with weights decaying as \(1/n\), a singular support graph, or a joint finite-Poisson / Gaussian fluctuation law. Their finite-dimension transference bounds motivate but do not directly imply the asserted conditional rare-cell distribution. Zhou (2017/2018) analyzes marginally constrained occupancy-type arrays and individual cell limits for different, non-Gibbs weights; its array law does not yield the connected-support multivariate singular-weight theorem. Chen (2007) develops exact and sequential sampling for tables with structural zeros, including diagonal restrictions, without the present weakly permitted-cell crossover or limiting independence. Fisher's noncentral hypergeometric distributions already account for the elementary exact \(2\times2\) fiber; no novelty is claimed for the Bessel series in isolation. The new contribution assessed here is the connected-support joint mixed-scale theorem and the explicit connectivity boundary.

## Limitations

The result does not treat dimension growing with \(n\), disconnected support in general, weights that vanish at other rates, or support graphs without an interior positive transportation flow. It gives convergence without quantitative error rates. The hypothesis allowing an unbounded integer-margin subsequence is essential; no unproved rounding-based extension is asserted. Independent historical-priority review may identify a more general previously published conditional local-limit theorem implying this result; the searches cannot establish uniqueness. All validations here are mathematical and computational checks, not independent certification.

## References

1. D. Duan, H. Lyu and W. Powell, *Poisson contingency tables, Gibbs permutations, and entropic optimal transport*, arXiv:2610.14616, first public October 10, 2026. https://arxiv.org/abs/2610.14616
2. Q. Zhou, *Asymptotics of multivariate contingency tables with fixed marginals*, arXiv:1710.08903, first public October 24, 2017. https://arxiv.org/abs/1710.08903
3. Y. Chen, *Conditional Inference on Tables With Structural Zeros*, Journal of Computational and Graphical Statistics 16 (2007), 445–467, DOI:10.1198/106186007X209226. https://publish.illinois.edu/yuguo/files/2012/12/final.pdf
